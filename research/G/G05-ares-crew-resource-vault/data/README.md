# G05 · Data blueprint

[ARES CREW RESOURCE VAULT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| resource_batch | string | 1 | Produced/imported resource identity. | Provenance and state required. |
| production_rate | nullable<float64> | kg/s | Measured/scenario gross output. | Demonstration versus scale-up labeled. |
| quality_record | record | native concentration | Contaminants, methods and limits. | Censoring and standard revision retained. |
| qualified_fraction | nullable<float64> | 1 | Accepted output fraction. | Unknown remains null; not automatically one. |
| inventory | record | kg | Qualified storage and independent reserve. | Batch ledger and leakage terms required. |
| demand_schedule | array<time,rate> | s,kg/s | Mission-specific resource demand. | Crew count/context and uncertainty recorded. |
| esm_factors | nullable<record> | kg/native | Mission equivalence coefficients. | Unknown factors prohibit complete scalar ESM. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [MOXIE operations research](https://www.sciencedirect.com/science/article/pii/S0094576523002187) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA human-system standard record](https://standards.nasa.gov/node/237) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Mars perchlorate research context](https://www.nasa.gov/general/detoxifying-mars/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
