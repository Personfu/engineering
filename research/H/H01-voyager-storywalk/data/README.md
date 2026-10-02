# H01 · Data blueprint

[VOYAGER STORYWALK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| exhibit_item | string | none | Staff-reviewed physical image/panel key. | Photo/crop geometry match required. |
| mission_product | nullable record | none | Verified image ID and processing provenance. | Null blocks confirmed caption. |
| claim_source | edge record | none | Atomic scientific claim and supporting span. | Reviewer/version required. |
| caption_layers | text record | words | Observation/explanation/exploration text. | Scale and processing labels retained. |
| assignment_group | anonymous string | none | Companion/session randomization unit. | No identifiable visitor tracking. |
| comprehension_score | nullable bool | none | Declared rubric outcome. | Nonresponse stays null. |
| effect_covariance | matrix | probability² | Joint learning-effect uncertainty. | Group/day dependence included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Photojournal](https://science.nasa.gov/photojournal/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USGS Astrogeology Science Center](https://www.usgs.gov/centers/astrogeology-science-center) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
