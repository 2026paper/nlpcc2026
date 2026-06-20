Supplementary and audit material for the NLPCC 2026 anonymous submission

This package is intended for double-blind review. It contains anonymized or aggregate data needed to audit the paper's main claims, plus prompts, rubrics, summary metadata, input-integrity reports, and hash manifests.

Included:

main_study_data/
  Current generated corpus and auxiliary web-interface tables: 810 generated Chinese science-popularization items, 6,929 parsed valid web-judge score rows, and 6,839 deduplicated valid judge-item pairs after collapsing 90 duplicate rows. Web-interface results are auxiliary only.

api_main_full810_latest22_reference/
  Revised main-analysis files. The current manuscript uses the complete API score matrix as the main automated evidence: 810 anonymized judge inputs scored by 9 API judges, yielding 7,290/7,290 successful judge-item pairs. The directory includes the long redacted score matrix, item means, provider completion summaries, redacted audit summaries, API input files, input-integrity reports, current 22-questionnaire human-audit files, item-level alignment tables, task-stratified and residualized checks, and Fig. 2 inputs. A post hoc input-integrity audit shows that Task-C API judge inputs were answer-label only, so Task-C API scores are treated as diagnostic evidence of input serialization/task-format fragility rather than calibrated quiz-item judging.

diagnostics/
  Controlled A/B diagnostic materials and summaries, including the eight A/B pairs, human A/B summaries, official API A/B parsed scores, and pair-level diagnostics. Executable API-rerun helper scripts are not included in the anonymous upload package.

robustness_checks/
  Current auxiliary checks and historical robustness summaries. The revised manuscript's primary sensitivity checks are in api_main_full810_latest22_reference/.

reproducibility_metadata/
  Prompt templates, rubric/codebook notes, model-family registry, known-unavailable metadata, data-availability statement, sanitized dataset manifest, and package hash manifest.

archive_historical/
  Earlier pilot survey exports, expanded-reference files, and the superseded 180-item API replication retained for audit continuity only. These files are not pooled into the revised manuscript's headline analysis.

Excluded deliberately:

- API credentials, environment files, access credentials, credential strings, and credential material.
- Full raw API request/response logs or provider-sensitive traces. Redacted or summary API audit tables are included under api_main_full810_latest22_reference/.
- Raw professional/reader survey workbooks, location fields, answer IDs tied to collection platforms, and free-text identity/background fields that could identify participants.
- Withheld item-mapping files marked as not-for-judges or do-not-share.
- Local source notes about manuscript editing, submission operations, emails, or author-side workflow.
- Local absolute paths; retained provenance paths are sanitized to logical package locations.

Double-blind note:

No author names, author emails, institutions, local usernames, chat IDs, or submission-operation notes are intentionally included. The model and provider names are retained because they are part of the experimental design and paper claims, not author identity.

Recommended citation in an anonymous submission:

An anonymized supplementary audit package with items, prompts, rubrics, anonymized score matrices, input-integrity reports, summary metadata, API audit summaries, and robustness checks is provided for review.
