# Reproducibility and Double-Blind Audit

Scope: anonymous supplementary package for NLPCC 2026 review.

Included evidence covers the paper's main reported quantities: 810 generated items, a complete API main matrix with 7,290/7,290 successful judge-item pairs, the current 22-questionnaire human-audit layer with 792 item-level ratings over 180 reference items, 6,929 valid web-interface judge rows used only as auxiliary comparison, task-stratified and residualized alignment checks, eight-pair controlled A/B diagnostics, and historical robustness/sensitivity files retained for audit continuity.

Anonymization decisions:

- Human-audit and reader data are released as anonymized or aggregate tables only.
- Raw survey workbooks and fields such as location, answer IDs tied to platforms, free-text background descriptions, and collection metadata are excluded.
- Withheld item-mapping files are excluded.
- Local absolute paths and author-side workflow notes are excluded or sanitized.
- Model/provider names are retained because they are experimental variables.

Known limits:

- Web-interface hidden system prompts, UI state, exact decoding settings, and per-call session metadata were not recoverable.
- API replication improves auditability but is not a perfect rerun of web-interface judging.
- Raw provider logs are withheld to avoid credentials or provider-sensitive traces; the API main package includes redacted audit summaries and provider completion summaries.

Audit result: no author-identifying files are intentionally included in this package. As with any public supplementary link under double-blind review, the repository account/profile used to host the package should also remain anonymous.
