# Reproducibility and Double-Blind Audit

Scope: anonymous supplementary package for NLPCC 2026 review.

Included evidence covers the paper's main reported quantities: 810 generated items, 6,929 valid web-judge scores, 432 professional validation rows, 180 aligned validation items, nine-model official API replication on the 180 validation items, eight-pair controlled A/B diagnostics, professional-reliability diagnostics, and robustness/sensitivity checks.

Anonymization decisions:

- Professional and reader data are released as anonymized or aggregate tables only.
- Raw survey workbooks and fields such as location, answer IDs tied to platforms, free-text background descriptions, and collection metadata are excluded.
- Withheld item-mapping files are excluded.
- Local absolute paths and author-side workflow notes are excluded or sanitized.
- Model/provider names are retained because they are experimental variables.

Known limits:

- Web-interface hidden system prompts, UI state, exact decoding settings, and per-call session metadata were not recoverable.
- API replication improves auditability but is not a perfect rerun of web-interface judging.
- Raw provider logs are withheld to avoid credentials or provider-sensitive traces.

Audit result: no author-identifying files are intentionally included in this package. As with any public supplementary link under double-blind review, the repository account/profile used to host the package should also remain anonymous.