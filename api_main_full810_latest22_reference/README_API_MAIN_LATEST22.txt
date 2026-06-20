This directory contains the revised main-analysis files for the API-primary design and the current 22-questionnaire human-audit layer.

Main analysis scope:
- API score matrix: 810 anonymized judge inputs scored by 9 API judges, yielding 7,290/7,290 successful pairs.
- API input-integrity audit: 540/810 inputs pass the full-text integrity check. All 270 Task-C quiz rows are answer-label-only in the API-main judge inputs even though the source corpus contains full quiz payloads. Task-C API scores are therefore diagnostic-only for input serialization/task-format fragility, not calibrated quiz-item judging evidence.
- Human layer: single current 22-questionnaire export batch, 792 item-level ratings on the 180-item reference subset.
- Earlier pilot survey exports: not pooled, to avoid mixing questionnaire versions and processing rules.
- Web-interface layer: auxiliary comparison only; revised quality analyses use mean(FA, CC, LC, TF, MQ), while the archived web `overall` field is retained separately as `original_web_overall` where present.

Key files:
- api_judge_scores_long_7290_redacted.csv: redacted long score matrix, one row per successful API judge-item pair.
- judge_inputs_anonymized_810.csv: actual anonymized item inputs used by the API-main judge run.
- input_integrity_report.csv and input_integrity_summary.json: item-level and aggregate input-integrity audit.
- alignment_sensitivity_excluding_task_c_latest22.csv: sensitivity table that separates all-task results from Task A/B-only evidence.
- stats_summary_latest22_only.json: headline counts, correlations, reliability, scale diagnostics, and Task-C caveat.
- alignment_summary_latest22.csv: API/Web alignment with the limited current 22-response human reference.
- alignment_summary_latest19_domain_qualified_sensitivity.csv: sensitivity using only responses with self-reported familiarity >= 3.
- task_stratified_alignment_latest22.csv: within-task alignment checks; Task-C rows should be interpreted with the input-integrity caveat.
- residualized_alignment_latest22.csv: task/domain/generator/concept-controlled residualized alignment checks.
- api_provider_alignment_latest22.csv: provider-level API alignment checks.
- api_web_alignment_items_latest22.csv: item-level API/Web/Human alignment table.
- dimension_gap_summary_latest22.csv: Fig. 2 numeric input.
- human_audit_latest22_scores_long.csv: anonymized current human-audit scores in long format.
- human_audit_latest22_item_means.csv: current human-audit item means for the 180-item subset.
- human_audit_latest22_reliability_by_domain.csv: domain-level pairwise
  reliability summary for the current human-audit layer.
- latest_human_rater_metadata_anonymized.csv: anonymized questionnaire metadata.
- full810_provider_completion_summary.csv: API completion audit by provider.
- api_call_audit_summary_full810_by_provider.csv: full810 provider-level audit summary derived from the frozen long score matrix.
- api_call_audit_summary_resume_block_628items.csv: incremental call-attempt audit for a resume block; it is not the full810 completion table.

No API keys, raw credentials, platform answer identifiers, or raw provider responses are included here.
