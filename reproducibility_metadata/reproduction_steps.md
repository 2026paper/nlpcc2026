# Reproduction Steps from Frozen Files

This GitHub-clean package is designed for audit rather than exact rerun of closed hosted web/API systems. The current manuscript can be checked from the preserved anonymized tables as follows.

1. Inspect the generated corpus in `main_study_data/generated_items_810.csv`.
2. Inspect parsed web-judge scores in `main_study_data/llm_judge_scores_6929.csv`; these are auxiliary only.
3. Inspect the complete API score matrix in `api_main_full810_latest22_reference/api_judge_scores_long_7290_redacted.csv`, item means in `api_main_full810_latest22_reference/api_full810_item_mean_scores_with_source.csv`, and provider completion in `api_main_full810_latest22_reference/full810_provider_completion_summary.csv`.
4. Inspect actual API-main judge inputs and the integrity audit in `api_main_full810_latest22_reference/judge_inputs_anonymized_810.csv`, `api_main_full810_latest22_reference/input_integrity_report.csv`, and `api_main_full810_latest22_reference/input_integrity_summary.json`.
5. Treat Task-C API-main rows as diagnostic-only because the integrity audit shows answer-label-only quiz inputs. Use `api_main_full810_latest22_reference/alignment_sensitivity_excluding_task_c_latest22.csv` for Task A/B-only alignment sensitivity.
6. Inspect the current 22-questionnaire human-audit layer in `api_main_full810_latest22_reference/human_audit_latest22_scores_long.csv` and `api_main_full810_latest22_reference/human_audit_latest22_item_means.csv`.
7. Recompute API/Web alignment against the current human-audit reference from `api_main_full810_latest22_reference/api_web_alignment_items_latest22.csv` and `api_main_full810_latest22_reference/alignment_summary_latest22.csv`.
8. Recompute within-task and residualized checks from `api_main_full810_latest22_reference/task_stratified_alignment_latest22.csv` and `api_main_full810_latest22_reference/residualized_alignment_latest22.csv`.
9. Recompute dimension-gap summaries for Fig. 2 from `api_main_full810_latest22_reference/dimension_gap_summary_latest22.csv`.
10. Inspect human survey metadata, including Credamo/见数 collection, compensation, consent/anonymization, independent blinded scoring, and current-vs-historical audit scope, in `reproducibility_metadata/human_validation_metadata.csv` and `api_main_full810_latest22_reference/latest_human_rater_metadata_anonymized.csv`.
11. Inspect prompts and rubric definitions under `reproducibility_metadata/prompt_templates/` and `reproducibility_metadata/rubric_anchors_and_codebook.md`.
12. Treat `archive_historical/` as historical audit material only. It is not the revised manuscript's main evidence path.

These steps audit the frozen outputs used by the current manuscript. They do not recreate exact hosted-model behavior unless hidden web-session transcripts/session IDs, hidden decoding parameters, per-call request/response/retry logs, and per-call identity-masking audits are later recovered and filled in `model_version_recovery_form.csv`.
