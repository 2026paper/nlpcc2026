# Controlled A/B Mechanism-Validation Analysis, 60 Respondents

## Data Status

- Raw export: `WITHHELD_RAW_SURVEY_EXPORT`
- Valid respondents analyzed: 60.
- Case-level judgments: 480 = 60 respondents x 8 cases.
- Mean science-popularization review familiarity: 6.93/10.
- Mean AI/LLM-evaluation familiarity: 6.62/10.

## Main A/B Alignment Results

- Expected higher-quality version selected in 419/480 case judgments (87.3%); among directional choices: 419/455 (92.1%).
- Expected riskier version selected in 411/480 case judgments (85.6%); among directional choices: 411/451 (91.1%).
- Both expected quality and expected riskier version selected in 400/480 case judgments (83.3%).
- Mean signed quality-alignment score: 1.448 on a -2 to +2 scale.
- Mean signed risk alignment score: 1.292 on a -2 to +2 scale.

## Case-Level Summary

| Case | Domain | Intervention | Quality expected | Risk expected | Both expected | Top mechanism |
|---|---|---|---:|---:|---:|---|
| A01 | Physics | boundary condition | 54/60 (90.0%) | 55/60 (91.7%) | 54/60 (90.0%) | Boundary/scope conditions (43/60) |
| A02 | Physics | causal distinction | 52/60 (86.7%) | 52/60 (86.7%) | 50/60 (83.3%) | Factual/causal/conceptual error (37/60) |
| A03 | Biology | misconception repair depth | 45/60 (75.0%) | 37/60 (61.7%) | 36/60 (60.0%) | Misconception-causal repair (38/60) |
| A04 | Biology | mechanism and boundary | 54/60 (90.0%) | 55/60 (91.7%) | 53/60 (88.3%) | Factual/causal/conceptual error (39/60) |
| A05 | Geoscience | analogy boundary | 55/60 (91.7%) | 56/60 (93.3%) | 54/60 (90.0%) | Boundary/scope conditions (21/60) |
| A06 | Climate/Environment | scale distinction | 50/60 (83.3%) | 51/60 (85.0%) | 49/60 (81.7%) | Factual/causal/conceptual error (37/60) |
| A07 | Chemistry | dynamic mechanism | 53/60 (88.3%) | 53/60 (88.3%) | 52/60 (86.7%) | Factual/causal/conceptual error (40/60) |
| A08 | Climate/Environment | format compliance vs semantic accuracy | 56/60 (93.3%) | 52/60 (86.7%) | 52/60 (86.7%) | Factual/causal/conceptual error (39/60) |

## Most Frequent Mechanisms

| Scope | Mechanism | Count | Rate |
|---|---|---:|---:|
| case_level_primary_mechanism | Factual/causal/conceptual error | 218 | 45.4% |
| case_level_primary_mechanism | Boundary/scope conditions | 89 | 18.5% |
| case_level_primary_mechanism | Misconception-causal repair | 78 | 16.2% |
| case_level_primary_mechanism | Overconfident or absolute language | 41 | 8.5% |
| case_level_primary_mechanism | Surface mention only | 29 | 6.0% |
| case_level_primary_mechanism | Fluency/format masks problem | 17 | 3.5% |
| case_level_primary_mechanism | Uncertain | 6 | 1.2% |
| case_level_primary_mechanism | Other | 2 | 0.4% |
| overall_multiselect | Factual/causal/conceptual error | 47 | 78.3% |
| overall_multiselect | Boundary/scope conditions | 47 | 78.3% |
| overall_multiselect | Misconception-causal repair | 43 | 71.7% |
| overall_multiselect | New wrong inference | 33 | 55.0% |
| overall_multiselect | Overconfident or absolute language | 32 | 53.3% |
| overall_multiselect | Non-expert readability | 26 | 43.3% |
| overall_multiselect | Surface mention only | 23 | 38.3% |
| overall_multiselect | Fluency/format masks problem | 15 | 25.0% |
| open_text_keyword_theme | Non-expert readability | 37 | 61.7% |
| open_text_keyword_theme | New wrong inference | 34 | 56.7% |
| open_text_keyword_theme | Factual/causal/conceptual error | 33 | 55.0% |
| open_text_keyword_theme | Misconception-causal repair | 24 | 40.0% |
| open_text_keyword_theme | Overconfident or absolute language | 19 | 31.7% |
| open_text_keyword_theme | Boundary/scope conditions | 15 | 25.0% |
| open_text_keyword_theme | Fluency/format masks problem | 2 | 3.3% |

## Interpretation for Paper

- The controlled A/B survey supports the construct-mismatch mechanism more directly than open-ended case discussion alone.
- Respondents overwhelmingly identify the intended better version and intended riskier version across matched pairs.
- The dominant mechanisms are factual/causal/conceptual error, missing boundary conditions, and shallow misconception repair.
- Fluency/format masking appears less frequently as a primary explanation, but remains relevant as part of the broader construct-mismatch account.
- Because this is an A/B perception and mechanism-validation survey, it should be reported as controlled mechanism evidence rather than as a new corpus-scale expert scoring experiment.
