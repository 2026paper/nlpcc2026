# Official API LLM-Judge Sensitivity on Controlled A/B Pairs

Run directory: `submission_workspace/diagnostics\official_ab_judge_run_20260521_155532`

## Overall

- Successful judge-case pairs: 72
- Available official API judges: 9
- Expected quality direction: 0.944
- Expected risk direction: 0.889
- Both directions correct: 0.875
- Mean expected quality gap: 2.203
- Mean expected risk gap: 2.958

## Case-Level Summary

| Case | Mechanism | Quality dir. | Risk dir. | Both dir. | Q gap | Risk gap |
|---|---|---:|---:|---:|---:|---:|
| A01 | boundary condition | 0.56 | 0.44 | 0.33 | 0.11 | 0.56 |
| A02 | causal distinction | 1.00 | 1.00 | 1.00 | 2.96 | 3.67 |
| A03 | misconception repair depth | 1.00 | 0.67 | 0.67 | 0.98 | 0.67 |
| A04 | mechanism and boundary | 1.00 | 1.00 | 1.00 | 2.42 | 3.56 |
| A05 | analogy boundary | 1.00 | 1.00 | 1.00 | 2.49 | 3.78 |
| A06 | scale distinction | 1.00 | 1.00 | 1.00 | 3.24 | 3.89 |
| A07 | dynamic mechanism | 1.00 | 1.00 | 1.00 | 2.73 | 3.67 |
| A08 | format compliance vs semantic accuracy | 1.00 | 1.00 | 1.00 | 2.69 | 3.89 |
