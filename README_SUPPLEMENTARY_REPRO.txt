Supplementary and reproducibility material for the NLPCC 2026 anonymous submission

This package is intended for double-blind review. It contains anonymized or aggregate data needed to audit the paper's main claims, plus credential-free scripts and metadata.

Included:

main_study_data/
  Core corpus and reference tables used by the current paper: 810 generated Chinese science-popularization items, 6,929 parsed valid web-judge score rows, 6,839 deduplicated valid judge-item pairs after collapsing 90 duplicate rows, the expanded primary professional-reference score table with 1,728 validator-item rows, the 180-item human--AI alignment table under the expanded reference, figure-input summaries, qualitative theme summaries, and mechanism-validation summaries. The paper's primary quality metric is mean(fa, cc, lc, tf, mq); risk is analyzed separately. Professional survey procedure metadata, including Credamo/Jianshu collection, RMB 15 compensation, informed consent, and independent blinded scoring, is summarized under reproducibility_metadata/. Earlier preliminary professional-reference files are not included in this GitHub-clean review package to keep the audit path focused on the current manuscript.

api_replication_180_item/
  Official API judge-side replication on the same 180 professional-reference items. This includes anonymized inputs, parsed long-format scores, provider/model availability summaries, item-level API means, API--professional alignment summaries, dimension gaps, risk-scale diagnostics, and sanitized run metadata. Raw provider logs and credentials are not included.

diagnostics/
  Controlled A/B diagnostic materials and summaries, including the eight A/B pairs, human A/B summaries, official API A/B parsed scores, pair-level diagnostics, and credential-free helper scripts.

robustness_checks/
  Additional review-response and sensitivity analyses: expanded professional-reference processing from the latest validation data, professional reliability and repeated-check summaries, split-half item-mean reliability, all-50-validator sensitivity, rater-count sensitivity, leave-one-domain/generator checks, same-family judge-generator exclusion, risk-floor diagnostics, fixed-effect checks, individual-judge alignment, science-relevant quality sensitivity using FA+CC+MQ only, and API quality stratified/residualized diagnostics under the expanded professional reference.

reproducibility_metadata/
  Prompt templates, rubric/codebook notes, model-family registry, known-unavailable metadata, data-availability statement, sanitized dataset manifest, and package hash manifest.

Excluded deliberately:

- API credentials, .env files, access credentials, credential strings, and credential material.
- Raw API request/response logs or provider-sensitive traces.
- Raw professional/reader survey xlsx files, location fields, answer IDs tied to collection platforms, and free-text identity/background fields that could identify participants.
- Withheld item-mapping files marked as not-for-judges or do-not-share.
- Local source notes about manuscript editing, submission operations, emails, or author-side workflow.
- Local absolute paths; retained provenance paths are sanitized to logical package/project locations.

Double-blind note:

No author names, author emails, institutions, local usernames, chat IDs, or submission-operation notes are intentionally included. The model and provider names are retained because they are part of the experimental design and paper claims, not author identity.

Recommended citation in an anonymous submission:

An anonymized supplementary package with items, prompts, rubrics, parser scripts, metadata, aggregate scores, API replication summaries, and robustness checks is provided for review.
