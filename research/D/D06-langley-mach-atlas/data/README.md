# D06 · Data blueprint

[LANGLEY MACH ATLAS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D06 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| configuration_id | string | 1 | Nozzle/gas/instrument condition. | Changed repair or wall state gets new ID. |
| reservoir_state | record | Pa,K | Absolute p0 and T0. | Timestamp/calibration covariance required. |
| probe_position | vector<float64>[3] | m | Nozzle-frame coordinate. | Origin, axes and encoder error recorded. |
| pitot_pressure | nullable<float64> | Pa | Shock-downstream stagnation reading. | Absolute pressure; missing null. |
| probe_orientation | vector<float64> | rad | Alignment relative to local flow. | Uncertainty and disturbance model retained. |
| inferred_mach | nullable<float64> | 1 | Gas-model-specific local Mach. | Branch/domain flags required. |
| core_membership | record | 1 | Tolerance/confidence mask classification. | Uncertain/extrapolated distinct from failed core. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA hypersonic calibration using design of experiments](https://ntrs.nasa.gov/citations/20050192473) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA/TM-101597 hypersonic-facilities section](https://ntrs.nasa.gov/api/citations/19890016576/downloads/19890016576.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
