# Rubric Anchors and Codebook

All automated and expert quantitative scores use a five-point scale.

The paper's primary non-risk quality score is the item-level mean of `fa`, `cc`, `lc`, `tf`, and `mq`. The `risk` dimension is directional in the opposite sense and is analyzed separately. Legacy composite fields that mix reversed risk are retained only for audit/backward compatibility and are not the primary paper metric.

## Positive Quality Dimensions

- `fa` factual accuracy: 1 = major scientific error; 3 = mostly correct with omissions or weak qualifications; 5 = accurate for the intended public level without misleading factual claims.
- `cc` concept completeness: 1 = misses the core concept; 3 = covers the main idea but omits mechanisms or conditions; 5 = covers the main idea, mechanism, and necessary scope conditions.
- `lc` language clarity: 1 = confusing or incoherent; 3 = generally understandable but uneven or vague; 5 = clear and accessible without sacrificing necessary precision.
- `tf` task fit: 1 = fails the assigned genre; 3 = partly satisfies the genre; 5 = fully satisfies the assigned task genre and communicative purpose.
- `mq` misconception handling: 1 = ignores or reinforces the misconception; 3 = mentions the misconception or correct answer but does not explain why it fails; 5 = diagnoses and repairs the misconception with mechanism-level explanation.

## Risk Dimension

`risk` is directional in the opposite sense: higher scores indicate greater expert-perceived misleading risk.

- 1 = unlikely to mislead a non-specialist reader.
- 3 = may mislead through ambiguity, missing conditions, shallow correction, or overgeneralization.
- 5 = likely to reinforce or create a serious misconception despite surface fluency.
