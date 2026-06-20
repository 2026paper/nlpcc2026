# Anonymous Supplementary Package

This repository contains the anonymized supplementary and audit material for an NLPCC 2026 submission. It is intended for double-blind review.

Start with `api_main_full810_latest22_reference/README_API_MAIN_LATEST22.txt`. The current manuscript uses the complete API score matrix as the main automated evidence: 810 anonymized judge inputs were scored by 9 API judges, yielding 7,290/7,290 successful judge-item pairs. A post hoc input-integrity audit found that the API-main Task-C quiz inputs were serialized as answer labels only; those Task-C API scores are therefore retained as an input-serialization/task-format diagnostic, not as calibrated quiz-item judging evidence. The main human-audit layer is defined by the single current 22-questionnaire Credamo/见数 export batch, yielding 792 item-level ratings over the 180-item reference subset. Earlier pilot survey exports are retained only under `archive_historical/` and are not pooled into the revised main analysis. The web-interface test remains an auxiliary comparison with 6,929 parsed valid web-judge rows and 6,839 deduplicated valid judge-item pairs; web quality in revised analyses is the five-dimension mean, not the archival `overall` field.

## Main Evidence Path

| Paper claim | Primary file(s) |
|---|---|
| 810 generated Chinese science-popularization items | `main_study_data/generated_items_810.csv` |
| Complete API score matrix, 7,290/7,290 successful judge-item pairs | `api_main_full810_latest22_reference/api_judge_scores_long_7290_redacted.csv`, `api_main_full810_latest22_reference/api_full810_item_mean_scores_with_source.csv`, and `api_main_full810_latest22_reference/full810_provider_completion_summary.csv` |
| API judge inputs and input-integrity audit | `api_main_full810_latest22_reference/judge_inputs_anonymized_810.csv`, `api_main_full810_latest22_reference/input_integrity_report.csv`, and `api_main_full810_latest22_reference/input_integrity_summary.json` |
| Task A/B sensitivity after excluding diagnostic-only Task C API scores | `api_main_full810_latest22_reference/alignment_sensitivity_excluding_task_c_latest22.csv` |
| Limited current 22-questionnaire human reference, 792 item-level evaluations | `api_main_full810_latest22_reference/human_audit_latest22_scores_long.csv` |
| Current human survey metadata, anonymized | `api_main_full810_latest22_reference/latest_human_rater_metadata_anonymized.csv` |
| API/Web alignment against current 22-response reference | `api_main_full810_latest22_reference/alignment_summary_latest22.csv` |
| Within-task and residualized alignment checks | `api_main_full810_latest22_reference/task_stratified_alignment_latest22.csv` and `api_main_full810_latest22_reference/residualized_alignment_latest22.csv` |
| 19-response domain-familiarity sensitivity | `api_main_full810_latest22_reference/alignment_summary_latest19_domain_qualified_sensitivity.csv` |
| Dimension-level scale-use / Fig. 2 input | `api_main_full810_latest22_reference/dimension_gap_summary_latest22.csv` |
| Archival web rows used as auxiliary comparison | `main_study_data/llm_judge_scores_6929.csv` |
| API completion and audit summaries | `api_main_full810_latest22_reference/full810_provider_completion_summary.csv`, `api_main_full810_latest22_reference/api_call_audit_summary_full810_by_provider.csv`, and `api_main_full810_latest22_reference/api_call_audit_summary_resume_block_628items.csv` |
| A/B diagnostic reported as auxiliary evidence | `diagnostics/controlled_ab_pairs_for_llm_judge.json` and `diagnostics/official_ab_judge_summary_latest.csv` |
| Historical expanded-reference and 180-item API files not used in the revised main analysis | `archive_historical/` |

The current 22-questionnaire human layer is intentionally treated as a lightweight and noisy reference. The manuscript reports its low reliability and uses it only for score-interpretation validity checks, not as a generator leaderboard or oracle.

This is an audit package for frozen anonymized outputs, not an exact executable rerun package for closed hosted systems. Prompt templates, rubrics, score matrices, summary tables, input-integrity reports, and SHA-256 manifests are included so reviewers can inspect the evidence chain. API keys, raw provider traces, raw survey exports, local absolute paths, platform answer identifiers, and identifying participant fields are excluded.

## Double-Blind Scope

No author names, author emails, institutions, local usernames, chat IDs, or submission-operation notes are intentionally included. Model and provider names are retained because they are part of the experimental design. Human-audit raters scored independently and did not see generator model names, LLM-judge scores, or other raters' ratings.
