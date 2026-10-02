# E07 · Data blueprint

[DISCOVERY TRIDENT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| module_id | enum | 1 | One of three independent record sources. | Hardware/firmware/calibration version required. |
| native_observation | record | native | Raw sensor values and response status. | No conversion discards original units. |
| common_timestamp | nullable<float64> | s | Aligned time coordinate. | Offset/skew covariance retained. |
| placement_response | record | m,s | Sensor position and lag correction. | Comparable-field domain required. |
| bias_covariance | matrix<float64> | native^2 | Cross-module calibration uncertainty. | Common reference terms included. |
| acceptable_record | bool/unknown | 1 | Science-gate event over interval. | Unknown distinct from failure/pass. |
| fault_dependency | record | 1 | Shared/conditional event structure. | Probability provenance or TBD status. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Arizona Space Grant ASCEND program](https://spacegrant.arizona.edu/research/ascend) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
