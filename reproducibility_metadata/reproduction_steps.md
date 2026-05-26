# Reproduction Steps from Frozen Files

This GitHub-clean package is designed for audit rather than exact rerun of closed hosted web interfaces. The current manuscript can be checked from the preserved anonymized tables as follows.

1. Inspect the generated corpus in `main_study_data/generated_items_810.csv`.
2. Inspect parsed web-judge scores in `main_study_data/llm_judge_scores_6929.csv`.
3. Inspect the expanded professional reference in `main_study_data/professional_reference_scores_1728_expanded.csv`.
4. Recompute web judge alignment from `main_study_data/human_ai_item_alignment_180_expanded_reference.csv`.
5. Recompute dimension-gap summaries for Fig. 2 from `main_study_data/dimension_gap_summary.csv`.
6. Recompute official-API replication summaries from `api_replication_180_item/api_judge_scores_long.csv` and `api_replication_180_item/api_expert_alignment_summary_expanded_reference.csv`.
7. Inspect professional-reference reliability, all-50 sensitivity, repeated-check summaries, and expanded-reference API diagnostics under `robustness_checks/expanded_professional_reference_from_latest_data/`.
8. Inspect professional survey metadata, including Credamo/Jianshu collection, compensation, consent/anonymization, and independent blinded scoring, in `reproducibility_metadata/human_validation_metadata.csv`.
9. Inspect prompts and rubric definitions under `reproducibility_metadata/prompt_templates/` and `reproducibility_metadata/rubric_anchors_and_codebook.md`.

These steps audit the frozen outputs used by the current manuscript. They do not recreate exact hosted-model behavior unless hidden web-session transcripts/session IDs, hidden decoding parameters, per-call request/response/retry logs, and per-call identity-masking audits are later recovered and filled in `model_version_recovery_form.csv`.
