Redacted API call audit for the 180-item official API replication

This directory contains a public-review-safe derivative of the final nine official API judge raw logs. It is intended to make the API replication auditable without releasing provider-sensitive traces.

Files:

- api_call_audit_redacted.csv
  One row per raw API call attempt from the final nine run directories. Retains anonymized item IDs, model/provider labels, public decoding parameters, HTTP status, parse-success flags, parsed scores, token counts, and hashes/byte counts for omitted raw responses.

- api_call_audit_summary_by_provider.csv
  Provider-level line counts, parsed-success counts, unique-item coverage, status-code counts, retry/error indicators, date range, and SHA-256 hash of each withheld source raw log.

- api_call_audit_redaction_log.csv
  Field-level description of what was retained, hashed, generalized, or dropped.

Redaction policy:

Full provider response bodies, provider backend identifiers, exact timestamps, full endpoint strings, and raw provider error text are not released. They are represented through hashes, presence flags, date-only fields, host-level endpoint information, or byte counts. API keys and authorization strings were not detected in the scanned source files. Local absolute source paths are not included; only logical final run-directory names are retained.

Scope:

These files cover only the final nine API replication runs used by the current manuscript, not pilot or failed exploratory runs in the local workspace.

Generated rows: 1696 raw call attempts across 9 final provider runs.
