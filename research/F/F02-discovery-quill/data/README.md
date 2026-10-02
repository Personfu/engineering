# F02 · Data blueprint

[DISCOVERY QUILL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![F02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| claim_id | string | 1 | Versioned factual/uncertainty proposition. | Primary source and exact evidence location required. |
| article_variant | record | 1 | Format, topic and claim mapping. | Matched factual set and revisions retained. |
| expert_accuracy | nullable<record> | rubric | Blind factual/uncertainty ratings. | Reviewer agreement and corrections recorded. |
| reader_id | string | 1 | Pseudonymous participant key. | Consented access only; identity separate. |
| assessment_score | nullable<float64> | rubric | Pre/immediate/delayed comprehension. | Timepoint/rubric version and missing reason. |
| item_confidence | nullable<float64> | 1 | Probability of correctness for exact item. | Range zero to one; missing not 0.5. |
| reading_context | record | s,1 | Time, accessibility and exposure conditions. | Burden/visual complexity/attrition metadata. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA educational outreach evaluation framework](https://ntrs.nasa.gov/citations/20000033841) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Science Activation](https://science.nasa.gov/learn/about-science-activation/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
