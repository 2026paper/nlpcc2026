# Anonymous Supplementary Package

This repository contains the anonymized supplementary and reproducibility material for an NLPCC 2026 submission. It is intended for double-blind review.

Start with `reproducibility_metadata/dataset_file_manifest.csv`. The current manuscript uses the expanded professional reference: 50 completed Credamo/Jianshu professional questionnaires, 48 primary validators, 1,728 item-level professional evaluations, 180 professional-reference items, 6,929 parsed valid web-judge rows, 6,839 deduplicated valid judge-item pairs after collapsing 90 duplicate rows, and a 9-judge official API replication on the same 180 items.

## Main Evidence Path

| Paper claim | Primary file(s) |
|---|---|
| 810 generated Chinese science-popularization items | `main_study_data/generated_items_810.csv` |
| 6,929 parsed valid web-judge rows; 6,839 deduplicated valid judge-item pairs | `main_study_data/llm_judge_scores_6929.csv` |
| Expanded professional reference, 1,728 item-level evaluations | `main_study_data/professional_reference_scores_1728_expanded.csv` |
| Professional survey procedure, compensation, consent, and blinded scoring metadata | `reproducibility_metadata/human_validation_metadata.csv` |
| Web judge vs. professional-reference alignment | `main_study_data/human_ai_item_alignment_180_expanded_reference.csv` |
| Dimension-level construct mismatch / Fig. 2 input | `main_study_data/dimension_gap_summary.csv` |
| Official API replication on 180 items | `api_replication_180_item/api_judge_scores_long.csv` |
| API/Web alignment summary under the expanded reference | `api_replication_180_item/api_expert_alignment_summary_expanded_reference.csv` |
| A/B diagnostic reported as auxiliary evidence | `diagnostics/controlled_ab_pairs_for_llm_judge.json` and `diagnostics/official_ab_judge_summary_latest.csv` |
| Robustness and sensitivity checks | `robustness_checks/` |
| Professional split-half item-mean reliability | `robustness_checks/professional_split_half_reliability.csv` |

Earlier preliminary professional-reference tables are not included in this GitHub-clean package, because they are not used by the current manuscript and can obscure the audit path. The expanded-reference processing files are retained under `robustness_checks/expanded_professional_reference_from_latest_data/`.

## Double-Blind Scope

The package excludes API keys, credentials, raw provider logs, raw survey exports, local absolute paths, author-side workflow notes, platform answer identifiers, and identifying participant fields. Model and provider names are retained because they are part of the experimental design. Domain-qualified validators scored independently and did not see generator model names, LLM-judge scores, or other validators' ratings.
