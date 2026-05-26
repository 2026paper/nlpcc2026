from __future__ import annotations

import argparse
import concurrent.futures
import csv
import importlib.util
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Any

import pandas as pd


HERE = Path(__file__).resolve().parent
PAPER_ROOT = HERE.parent
API_ROOT = Path(os.environ.get("API_REPLICATION_ROOT", "."))
API_SCRIPT = API_ROOT / "scripts" / "run_api_judge_replication.py"
PAIRS_PATH = HERE / "controlled_ab_pairs_for_llm_judge.json"

RUN_PREFIX = "official_ab_judge_run"
DIMENSIONS = ["fa", "cc", "lc", "tf", "mq", "risk"]
QUALITY_DIMS = ["fa", "cc", "lc", "tf", "mq"]


def load_api_module() -> Any:
    spec = importlib.util.spec_from_file_location("api_judge_replication", API_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import API replication script: {API_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["api_judge_replication"] = module
    spec.loader.exec_module(module)
    return module


def now_stamp() -> str:
    import datetime as dt

    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def build_items() -> pd.DataFrame:
    pairs = json.loads(PAIRS_PATH.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for pair in pairs:
        for version in ["A", "B"]:
            rows.append(
                {
                    "item_id": f"{pair['case_id']}_{version}",
                    "case_id": pair["case_id"],
                    "version": version,
                    "domain": pair["domain"],
                    "concept": pair["concept"],
                    "hidden_intervention": pair["hidden_intervention"],
                    "question": pair["question"],
                    "task_type": "controlled_ab_science_explanation",
                    "generated_text": pair[f"version_{version}"],
                    "expected_quality_preference": pair["expected_quality_preference"],
                    "expected_riskier_version": pair["expected_riskier_version"],
                }
            )
    return pd.DataFrame(rows)


def write_items(run_dir: Path, items: pd.DataFrame) -> None:
    items.to_csv(run_dir / "controlled_ab_judge_inputs.csv", index=False, encoding="utf-8-sig")
    anonymized = items[["item_id", "case_id", "version", "domain", "concept", "task_type", "generated_text"]].copy()
    anonymized.to_csv(run_dir / "controlled_ab_judge_inputs_anonymized.csv", index=False, encoding="utf-8-sig")


def append_score_row(api: Any, scores_path: Path, row: dict[str, Any]) -> None:
    needs_header = (not scores_path.exists()) or scores_path.stat().st_size <= 3
    with scores_path.open("a", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=api.SCORE_FIELDNAMES, extrasaction="ignore")
        if needs_header:
            writer.writeheader()
        writer.writerow(row)


def completed_pairs(scores_path: Path) -> set[tuple[str, str]]:
    if not scores_path.exists() or scores_path.stat().st_size == 0:
        return set()
    scores = pd.read_csv(scores_path, encoding="utf-8-sig")
    if scores.empty or "parse_success" not in scores.columns:
        return set()
    ok = scores[scores["parse_success"].astype(str).str.lower().isin(["true", "1"])]
    return set(zip(ok["item_id"].astype(str), ok["judge_provider"].astype(str)))


def load_env_values(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        env[name.strip()] = value.strip().strip('"').strip("'")
    return env


def resolve_providers(api: Any, providers_filter: list[str] | None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    config = api.read_config()
    providers = config["providers"]
    if providers_filter:
        wanted = set(providers_filter)
        providers = [p for p in providers if p["provider"] in wanted]
        missing = wanted - {p["provider"] for p in providers}
        if missing:
            raise ValueError(f"Unknown providers: {sorted(missing)}")

    availability_rows: list[dict[str, Any]] = []
    resolved: list[dict[str, Any]] = []
    for provider in providers:
        api_key = os.environ.get(provider["api_key_env"], "").strip()
        if not api_key:
            availability_rows.append(api.missing_key_availability(provider))
            continue
        provider_resolved, model_list_row = api.resolve_actual_model_id(provider, api_key)
        if model_list_row and model_list_row.get("available") is False:
            availability_rows.append({**model_list_row, "available": False, "successful_calls": 0, "failed_calls": 0})
            continue
        if model_list_row and model_list_row.get("model_list_status", 200) not in (None, 200):
            availability_rows.append({**model_list_row, "available": False, "successful_calls": 0, "failed_calls": 0})
            continue
        resolved.append(provider_resolved)
        if model_list_row:
            availability_rows.append({**model_list_row, "available": True})
    return resolved, availability_rows


def score_items(api: Any, run_dir: Path, providers_filter: list[str] | None, sleep_seconds: float, concurrency: int) -> None:
    api.load_dotenv(API_ROOT / ".env")
    config = api.read_config()
    schema = api.score_schema()
    system_prompt, user_template = api.read_prompts()

    # Keep the diagnostic compact while preserving the original scoring protocol.
    config = {**config, "max_output_tokens": 800, "retry_parse_failures": 2}

    items_df = build_items()
    write_items(run_dir, items_df)
    items = items_df.to_dict("records")

    raw_log_path = run_dir / api.RAW_LOG_NAME
    scores_path = run_dir / api.SCORES_NAME
    completed = completed_pairs(scores_path)

    providers, availability_rows = resolve_providers(api, providers_filter)
    status_rows: list[dict[str, Any]] = []

    for provider in providers:
        api_key = os.environ.get(provider["api_key_env"], "").strip()
        provider_success = 0
        provider_fail = 0

        pending_items = [item for item in items if (str(item["item_id"]), provider["provider"]) not in completed]

        def run_one(item: dict[str, Any]) -> dict[str, Any]:
            row = api.call_with_retries(provider, api_key, item, system_prompt, user_template, schema, config, raw_log_path)
            if sleep_seconds:
                time.sleep(sleep_seconds)
            return row

        executor = None
        if concurrency <= 1 or len(pending_items) <= 1:
            row_iter = (run_one(item) for item in pending_items)
        else:
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=max(1, concurrency))
            futures = [executor.submit(run_one, item) for item in pending_items]
            row_iter = (future.result() for future in concurrent.futures.as_completed(futures))

        try:
            for row in row_iter:
                key = (str(row["item_id"]), provider["provider"])
                append_score_row(api, scores_path, row)
                completed.add(key)
                if row.get("parse_success"):
                    provider_success += 1
                else:
                    provider_fail += 1
        finally:
            if executor is not None:
                executor.shutdown(wait=True, cancel_futures=True)

        status_rows.append(
            {
                "judge_provider": provider["provider"],
                "paper_model_label": provider["paper_model_label"],
                "judge_model_requested": provider["model"],
                "actual_api_model": api.actual_api_model(provider),
                "api_endpoint": provider["endpoint"],
                "available": provider_success > 0,
                "reason": "ok" if provider_success > 0 else "no_successful_calls",
                "successful_calls": provider_success,
                "failed_calls": provider_fail,
                "checked_at": api.now_utc(),
            }
        )

    pd.DataFrame(availability_rows + status_rows).to_csv(
        run_dir / "api_model_availability_log.csv", index=False, encoding="utf-8-sig"
    )


def choice_from_pair(a_value: float, b_value: float, higher_is_better: bool = True) -> str:
    if math.isclose(a_value, b_value, abs_tol=1e-9):
        return "tie"
    if higher_is_better:
        return "A" if a_value > b_value else "B"
    return "A" if a_value < b_value else "B"


def analyze_run(run_dir: Path) -> None:
    items = pd.read_csv(run_dir / "controlled_ab_judge_inputs.csv", encoding="utf-8-sig")
    scores_path = run_dir / "api_judge_scores_long.csv"
    scores = pd.read_csv(scores_path, encoding="utf-8-sig") if scores_path.exists() and scores_path.stat().st_size else pd.DataFrame()
    if scores.empty:
        raise RuntimeError("No scores available for analysis.")

    scores["parse_success"] = scores["parse_success"].astype(str).str.lower().isin(["true", "1"])
    scores = scores[scores["parse_success"]].copy()
    for dim in DIMENSIONS:
        scores[dim] = pd.to_numeric(scores[dim], errors="coerce")
    scores["judge_quality"] = scores[QUALITY_DIMS].mean(axis=1)

    long = scores.merge(items, on="item_id", how="left")
    long.to_csv(run_dir / "official_ab_judge_scores_long_with_metadata.csv", index=False, encoding="utf-8-sig")

    pair_rows: list[dict[str, Any]] = []
    for (provider, case_id), part in long.groupby(["judge_provider", "case_id"]):
        by_version = {row["version"]: row for _, row in part.iterrows()}
        if "A" not in by_version or "B" not in by_version:
            continue
        a = by_version["A"]
        b = by_version["B"]
        expected_quality = str(a["expected_quality_preference"])
        expected_risk = str(a["expected_riskier_version"])
        q_choice = choice_from_pair(float(a["judge_quality"]), float(b["judge_quality"]))
        r_choice = choice_from_pair(float(a["risk"]), float(b["risk"]))
        q_expected_value = float(a["judge_quality"] if expected_quality == "A" else b["judge_quality"])
        q_other_value = float(b["judge_quality"] if expected_quality == "A" else a["judge_quality"])
        r_expected_value = float(a["risk"] if expected_risk == "A" else b["risk"])
        r_other_value = float(b["risk"] if expected_risk == "A" else a["risk"])
        pair_rows.append(
            {
                "judge_provider": provider,
                "paper_model_label": a["paper_model_label"],
                "case_id": case_id,
                "domain": a["domain"],
                "concept": a["concept"],
                "hidden_intervention": a["hidden_intervention"],
                "expected_quality_preference": expected_quality,
                "expected_riskier_version": expected_risk,
                "quality_choice": q_choice,
                "risk_choice": r_choice,
                "quality_aligned": q_choice == expected_quality,
                "risk_aligned": r_choice == expected_risk,
                "both_aligned": q_choice == expected_quality and r_choice == expected_risk,
                "quality_gap_expected_minus_other": q_expected_value - q_other_value,
                "risk_gap_expected_minus_other": r_expected_value - r_other_value,
                "quality_A": float(a["judge_quality"]),
                "quality_B": float(b["judge_quality"]),
                "risk_A": float(a["risk"]),
                "risk_B": float(b["risk"]),
            }
        )

    pair_df = pd.DataFrame(pair_rows)
    pair_df.to_csv(run_dir / "official_ab_pair_level_judge_diagnostic.csv", index=False, encoding="utf-8-sig")

    summary_rows: list[dict[str, Any]] = []

    def add_summary(name: str, frame: pd.DataFrame) -> None:
        summary_rows.append(
            {
                "group": name,
                "n_judge_case_pairs": int(len(frame)),
                "n_judges": int(frame["judge_provider"].nunique()) if len(frame) else 0,
                "quality_expected_direction_rate": float(frame["quality_aligned"].mean()) if len(frame) else math.nan,
                "risk_expected_direction_rate": float(frame["risk_aligned"].mean()) if len(frame) else math.nan,
                "both_expected_direction_rate": float(frame["both_aligned"].mean()) if len(frame) else math.nan,
                "quality_tie_rate": float((frame["quality_choice"] == "tie").mean()) if len(frame) else math.nan,
                "risk_tie_rate": float((frame["risk_choice"] == "tie").mean()) if len(frame) else math.nan,
                "mean_quality_gap_expected_minus_other": float(frame["quality_gap_expected_minus_other"].mean()) if len(frame) else math.nan,
                "mean_risk_gap_expected_minus_other": float(frame["risk_gap_expected_minus_other"].mean()) if len(frame) else math.nan,
            }
        )

    add_summary("all_available_official_api_judges", pair_df)
    for provider, part in pair_df.groupby("judge_provider"):
        add_summary(f"judge:{provider}", part)
    for case_id, part in pair_df.groupby("case_id"):
        add_summary(f"case:{case_id}", part)

    summary = pd.DataFrame(summary_rows)
    summary.to_csv(run_dir / "official_ab_judge_summary.csv", index=False, encoding="utf-8-sig")

    by_case = (
        pair_df.groupby(["case_id", "domain", "concept", "hidden_intervention"], as_index=False)
        .agg(
            n_judges=("judge_provider", "nunique"),
            quality_expected_direction_rate=("quality_aligned", "mean"),
            risk_expected_direction_rate=("risk_aligned", "mean"),
            both_expected_direction_rate=("both_aligned", "mean"),
            mean_quality_gap_expected_minus_other=("quality_gap_expected_minus_other", "mean"),
            mean_risk_gap_expected_minus_other=("risk_gap_expected_minus_other", "mean"),
        )
        .sort_values("case_id")
    )
    by_case.to_csv(run_dir / "official_ab_judge_case_summary.csv", index=False, encoding="utf-8-sig")

    overall = summary.iloc[0].to_dict()
    lines = [
        "# Official API LLM-Judge Sensitivity on Controlled A/B Pairs",
        "",
        f"Run directory: `{run_dir}`",
        "",
        "## Overall",
        "",
        f"- Successful judge-case pairs: {int(overall['n_judge_case_pairs'])}",
        f"- Available official API judges: {int(overall['n_judges'])}",
        f"- Expected quality direction: {overall['quality_expected_direction_rate']:.3f}",
        f"- Expected risk direction: {overall['risk_expected_direction_rate']:.3f}",
        f"- Both directions correct: {overall['both_expected_direction_rate']:.3f}",
        f"- Mean expected quality gap: {overall['mean_quality_gap_expected_minus_other']:.3f}",
        f"- Mean expected risk gap: {overall['mean_risk_gap_expected_minus_other']:.3f}",
        "",
        "## Case-Level Summary",
        "",
        "| Case | Mechanism | Quality dir. | Risk dir. | Both dir. | Q gap | Risk gap |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for _, row in by_case.iterrows():
        lines.append(
            f"| {row['case_id']} | {row['hidden_intervention']} | "
            f"{row['quality_expected_direction_rate']:.2f} | {row['risk_expected_direction_rate']:.2f} | "
            f"{row['both_expected_direction_rate']:.2f} | {row['mean_quality_gap_expected_minus_other']:.2f} | "
            f"{row['mean_risk_gap_expected_minus_other']:.2f} |"
        )
    (run_dir / "official_ab_judge_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--providers", nargs="*", default=None)
    parser.add_argument("--sleep-seconds", type=float, default=0.2)
    parser.add_argument("--concurrency", type=int, default=1)
    parser.add_argument("--analyze-only", action="store_true")
    args = parser.parse_args()

    run_dir = args.run_dir or HERE / f"{RUN_PREFIX}_{now_stamp()}"
    run_dir.mkdir(parents=True, exist_ok=True)

    api = load_api_module()
    if not args.analyze_only:
        score_items(api, run_dir, args.providers, args.sleep_seconds, args.concurrency)
    analyze_run(run_dir)

    latest_file = HERE / "latest_official_ab_run.txt"
    latest_file.write_text(str(run_dir), encoding="utf-8")
    print(f"AB_DIAGNOSTIC_RUN_DIR={run_dir}")


if __name__ == "__main__":
    main()
