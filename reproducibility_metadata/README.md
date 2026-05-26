# Reproducibility Metadata Package

Cleaned for GitHub review upload: 2026-05-26

This package documents what can and cannot be reproduced from the frozen files for the misconception-aware science-popularization evaluation study.

## Included Metadata

- `model_family_registry.csv`: generator/judge model-family registry, exact model labels from user confirmation, web-interface status, and unrecovered run fields.
- `generation_stage_metadata.csv`: raw generation files, parsed item counts, prompt files, parser script, and schema.
- `judging_stage_metadata.csv`: raw score files, judge-family labels, score schema, masking status, and parsing notes.
- `human_validation_metadata.csv`: current professional-reference audit metadata for the expanded 50-response / 48-primary-validator validation layer.
- `dataset_file_manifest.csv`: key data files used by the paper and their provenance.
- `file_hash_manifest_sha256.csv`: SHA256 hashes for files currently included in this GitHub-clean package.
- `prompt_template_manifest.csv`: copied prompt templates and concept-source file.
- `known_unavailable_metadata.csv`: fields not recoverable from frozen files.
- `prospective_logging_schema.csv`: recommended logging schema for future runs.
- `model_version_recovery_form.csv`: form for manually filling remaining exact versions/settings if original run logs are found.
- `rubric_anchors_and_codebook.md`: operational score anchors.
- `reproduction_steps.md`: reproduction workflow from frozen files.
- `data_availability_statement.md`: paper-ready reproducibility wording.
- `prompt_templates/`: available generation and judging prompts copied from the original data folder.

## Summary

- Prompt templates copied: 8 / 8
- Model families registered: 9
- Generation-stage rows: 9
- Judging-stage rows: 9
- Professional-reference metadata rows: 15
- Manifested key files: see `dataset_file_manifest.csv`
- SHA256 hashed files: see `file_hash_manifest_sha256.csv`

## Most Important Caveat

Exact generator and judge model labels have now been recorded from user confirmation, and the interface is recorded as web-based. The remaining gaps are web-session transcripts or session IDs, hidden decoding parameters, per-call request/response/retry logs, and per-call identity-masking audits. This package makes those limitations explicit and provides a schema for future recovery or reruns.
