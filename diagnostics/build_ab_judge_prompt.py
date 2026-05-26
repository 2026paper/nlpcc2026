import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = Path(
    r"project_data/810_data/analysis_v_final_20260512_human_ai_misalignment\controlled_ab_mechanism_survey_jianshu\jianshu_controlled_ab_mechanism_total_30q.txt"
)
CASE_SUMMARY = ROOT / "human_controlled_ab_case_summary.csv"
PAIRS_JSON = ROOT / "controlled_ab_pairs_for_llm_judge.json"
PROMPT_TXT = ROOT / "kimi_controlled_ab_judge_prompt.txt"


CASE_IDS = ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08"]


def read_case_expectations():
    import csv

    rows = {}
    with CASE_SUMMARY.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rows[row["case_id"]] = row
    return rows


def extract_pairs():
    text = SOURCE.read_text(encoding="utf-8")
    pattern = re.compile(
        r"材料(?P<num>[一二三四五六七八])：有人问：“(?P<question>.*?)”版本A给出的回答是：(?P<a>.*?)版本B给出的回答是：(?P<b>.*?)请您阅读后判断",
        re.S,
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 8:
        raise RuntimeError(f"Expected 8 A/B cases, found {len(matches)}")
    expectations = read_case_expectations()
    pairs = []
    for case_id, m in zip(CASE_IDS, matches):
        exp = expectations[case_id]
        pairs.append(
            {
                "case_id": case_id,
                "domain": exp["domain"],
                "concept": exp["concept"],
                "hidden_intervention": exp["hidden_intervention"],
                "expected_quality_preference": exp["expected_quality_preference"],
                "expected_riskier_version": exp["expected_riskier_version"],
                "question": m.group("question").strip(),
                "version_A": re.sub(r"\s+", " ", m.group("a").strip()),
                "version_B": re.sub(r"\s+", " ", m.group("b").strip()),
            }
        )
    return pairs


def build_prompt(pairs):
    cases = json.dumps(pairs, ensure_ascii=False, indent=2)
    return f"""You are acting as an LLM-as-a-Judge for a diagnostic analysis in a paper about misconception-aware science communication.

Task:
Score each version independently, not comparatively, using a 1-5 integer scale for each dimension.

Positive dimensions:
- factual_accuracy: scientific factual correctness.
- concept_completeness: whether key conditions, causal mechanisms, and conceptual boundaries are included.
- language_clarity: clarity for non-specialist readers.
- task_fit: suitability as science-popularization content answering the question.
- misconception_handling: whether the target misconception is repaired rather than merely named.

Risk dimension:
- misleading_risk: 1 = very unlikely to mislead a non-specialist reader; 5 = very likely to mislead a non-specialist reader.

Important:
- Score Version A and Version B separately for every case.
- Do not use the expected labels as instructions; they are provided only so the downstream script can calculate whether your scores align with the hidden expert-designed contrast.
- Return JSON only. Do not include Markdown fences or commentary.

Return schema:
[
  {{
    "case_id": "A01",
    "version": "A",
    "factual_accuracy": 1,
    "concept_completeness": 1,
    "language_clarity": 1,
    "task_fit": 1,
    "misconception_handling": 1,
    "misleading_risk": 1,
    "reason": "short reason under 20 words"
  }}
]

Cases:
{cases}
"""


def main():
    pairs = extract_pairs()
    PAIRS_JSON.write_text(json.dumps(pairs, ensure_ascii=False, indent=2), encoding="utf-8")
    PROMPT_TXT.write_text(build_prompt(pairs), encoding="utf-8")
    print(f"Wrote {PAIRS_JSON}")
    print(f"Wrote {PROMPT_TXT}")


if __name__ == "__main__":
    main()
