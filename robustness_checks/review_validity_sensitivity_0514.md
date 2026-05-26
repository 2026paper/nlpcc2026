# Review Validity Sensitivity Analyses

## Rater-count and agreement subsets
| analysis                       |   n |   quality_spearman |   quality_pearson |   risk_spearman |   risk_pearson |   quality_spearman_ci_low |   quality_spearman_ci_high |   risk_spearman_ci_low |   risk_spearman_ci_high |
|:-------------------------------|----:|-------------------:|------------------:|----------------:|---------------:|--------------------------:|---------------------------:|-----------------------:|------------------------:|
| all_expert_items               | 180 |             -0.03  |             0.073 |          -0.015 |          0.031 |                    -0.176 |                      0.118 |                 -0.179 |                   0.158 |
| three_expert_raters_only       |  72 |             -0.109 |            -0.106 |          -0.086 |         -0.128 |                    -0.348 |                      0.124 |                 -0.328 |                   0.235 |
| lower_half_expert_disagreement |  93 |             -0.032 |            -0.048 |          -0.124 |         -0.123 |                    -0.231 |                      0.183 |                 -0.262 |                   0.074 |
| upper_half_expert_disagreement |  87 |             -0.052 |             0.116 |           0.024 |          0.107 |                    -0.251 |                      0.17  |                 -0.277 |                   0.338 |

## Leave-one-domain-out correlation range
- Quality Spearman range: -0.067 to 0.016.
- Risk Spearman range: -0.051 to 0.023.

## Leave-one-generator-out correlation range
- Quality Spearman range: -0.096 to -0.009.
- Risk Spearman range: -0.056 to 0.022.

## Floor-adjusted risk summary
| llm_risk_above_floor   |   n |   expert_risk_mean |   expert_risk_sd |   expert_quality_mean |   llm_risk_mean |
|:-----------------------|----:|-------------------:|-----------------:|----------------------:|----------------:|
| False                  | 169 |              1.707 |            0.61  |                 4.311 |           1     |
| True                   |  11 |              1.879 |            1.138 |                 4.121 |           1.193 |
