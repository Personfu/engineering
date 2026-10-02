# C26 · Data blueprint

[LISA PENDULUM PATHFINDER](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C26 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| geometry | struct | m, kg | Verified masses, lengths and coordinates. | Measured/assumed properties distinguished. |
| drive_force | measurement<float64[n]> | N | Calibrated test excitation. | Actuator transfer and range attached. |
| displacement | measurement<float64[n]> | m | Readout of chosen mass/axis. | Sensor floor, calibration and gaps retained. |
| ground_tilt | float64[n,components] | m, radian | Independent support motion. | Common time base and cross-axis sign. |
| temperature | measurement<float64> | K | Thermal state. | Passive equilibrium applicability flagged. |
| transfer_function | complex128[nf] | m N^-1 or 1 | Force or base-motion response. | Input/output type and coherence mandatory. |
| noise_psd | float64[nf] | m^2 Hz^-1 | One-sided displacement spectrum. | Window/averaging and confidence limits recorded. |
| identified_model | struct<M,C,K> | kg, N s m^-1, N m^-1 | Multi-axis local dynamics. | Covariance and amplitude validity range. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [New suspension bench data](https://arxiv.org/abs/1707.07309) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Multi-loop suspension theory](https://arxiv.org/abs/physics/9909015) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
