import csv
import json
import re
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAIRS_JSON = ROOT / "controlled_ab_pairs_for_llm_judge.json"
RAW_OUTPUT = ROOT / "kimi_controlled_ab_judge_raw_output.txt"
LONG_CSV = ROOT / "kimi_controlled_ab_judge_scores.csv"
SUMMARY_CSV = ROOT / "kimi_controlled_ab_judge_summary.csv"
SUMMARY_MD = ROOT / "kimi_controlled_ab_judge_summary.md"

POSITIVE_DIMS = [
    "factual_accuracy",
    "concept_completeness",
    "language_clarity",
    "task_fit",
    "misconception_handling",
]


def load_scores():
    text = RAW_OUTPUT.read_text(encoding="utf-8")
    match = re.search(r"(\[\s*\{.*?\}\s*\])", text, flags=re.S)
    if not match:
        raise RuntimeError("Could not find JSON array in Kimi output")
    data = json.loads(match.group(1))
    for row in data:
        row["quality_mean"] = round(statistics.mean(float(row[d]) for d in POSITIVE_DIMS), 3)
    return data


def main():
    pairs = {p["case_id"]: p for p in json.loads(PAIRS_JSON.read_text(encoding="utf-8"))}
    scores = load_scores()
    by_case = {}
    for row in scores:
        by_case.setdefault(row["case_id"], {})[row["version"]] = row

    summary = []
    for case_id in sorted(pairs):
        pair = pairs[case_id]
        a = by_case[case_id]["A"]
        b = by_case[case_id]["B"]
        expected_quality = pair["expected_quality_preference"]
        expected_risk = pair["expected_riskier_version"]
        quality_winner = "A" if a["quality_mean"] > b["quality_mean"] else "B" if b["quality_mean"] > a["quality_mean"] else "Tie"
        risk_winner = "A" if float(a["misleading_risk"]) > float(b["misleading_risk"]) else "B" if float(b["misleading_risk"]) > float(a["misleading_risk"]) else "Tie"
        summary.append(
            {
                "case_id": case_id,
                "domain": pair["domain"],
                "concept": pair["concept"],
                "intervention": pair["hidden_intervention"],
                "expected_quality": expected_quality,
                "judge_quality_winner": quality_winner,
                "quality_aligns": quality_winner == expected_quality,
                "quality_A": a["quality_mean"],
                "quality_B": b["quality_mean"],
                "expected_riskier": expected_risk,
                "judge_riskier": risk_winner,
                "risk_aligns": risk_winner == expected_risk,
                "risk_A": a["misleading_risk"],
                "risk_B": b["misleading_risk"],
            }
        )

    with LONG_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = [
            "case_id",
            "version",
            *POSITIVE_DIMS,
            "misleading_risk",
            "quality_mean",
            "reason",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in scores:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    with SUMMARY_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)

    q_align = sum(1 for r in summary if r["quality_aligns"])
    r_align = sum(1 for r in summary if r["risk_aligns"])
    both = sum(1 for r in summary if r["quality_aligns"] and r["risk_aligns"])
    q_gap = statistics.mean(
        (r["quality_A"] - r["quality_B"]) if r["expected_quality"] == "A" else (r["quality_B"] - r["quality_A"])
        for r in summary
    )
    risk_gap = statistics.mean(
        (float(r["risk_A"]) - float(r["risk_B"])) if r["expected_riskier"] == "A" else (float(r["risk_B"]) - float(r["risk_A"]))
        for r in summary
    )

    lines = [
        "# Kimi Controlled A/B Judge Diagnostic",
        "",
        "Model route: local Kimi CLI, configured as Kimi-k2.6 in the local Kimi config.",
        "This is a small diagnostic over the eight existing controlled A/B pairs, not a new corpus-scale experiment.",
        "",
        f"- Cases: {len(summary)} pairs, {len(scores)} independently scored versions.",
        f"- Quality preference aligned with expected safer/better version: {q_align}/{len(summary)} ({q_align/len(summary):.1%}).",
        f"- Risk preference aligned with expected riskier version: {r_align}/{len(summary)} ({r_align/len(summary):.1%}).",
        f"- Both quality and risk directions aligned: {both}/{len(summary)} ({both/len(summary):.1%}).",
        f"- Mean expected-direction quality gap: {q_gap:.3f} points on the 1-5 scale.",
        f"- Mean expected-direction risk gap: {risk_gap:.3f} points on the 1-5 scale.",
        "",
        "| Case | Intervention | Expected quality | Judge quality | Expected risk | Judge risk |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for r in summary:
        lines.append(
            f"| {r['case_id']} | {r['intervention']} | {r['expected_quality']} | {r['judge_quality_winner']} | {r['expected_riskier']} | {r['judge_riskier']} |"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {LONG_CSV}")
    print(f"Wrote {SUMMARY_CSV}")
    print(f"Wrote {SUMMARY_MD}")


if __name__ == "__main__":
    main()
