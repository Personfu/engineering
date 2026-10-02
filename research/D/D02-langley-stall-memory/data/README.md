# D02 · Data blueprint

[LANGLEY STALL MEMORY](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| run_history | record | 1 | Direction, dwell and initialization. | Surface state and sequence required. |
| time | vector<float64> | s | Synchronized experiment clock. | Offset uncertainty recorded; missing samples masked. |
| angle | vector<float64> | rad | Measured angle of attack. | Encoder convention and rate derivation stated. |
| lift_coefficient | vector<float64> | 1 | Tared C_L trace. | Reference area and shared calibration retained. |
| separated_fraction | nullable<vector<float64>> | 1 | Defined spatial separation measure. | Between zero and one; diagnostic limitations flagged. |
| turbulence_level | nullable<float64> | 1 | Declared inflow intensity. | Definition/bandwidth required. |
| loop_metrics | record | rad | Signed area and angle difference. | Threshold rule and joint uncertainty retained. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA dynamic-stall propfan analysis](https://ntrs.nasa.gov/citations/19890005741) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA lift-enhancing-tab experiment](https://ntrs.nasa.gov/citations/19980019443) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
