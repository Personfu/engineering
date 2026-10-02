# D03 · Data blueprint

[INGENUITY DESCENT & BUBBLE LAB](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| package_id | enum | 1 | D03a or D03b origin. | Never merge datasets without transfer record. |
| atmosphere | record | kg/m^3,Pa s,m/s^2 | Density, viscosity and gravity. | Uncertainty and scenario provenance required. |
| rotor_geometry | array<radius,chord> | m | Blade discretization. | Positive dimensions and deployment state. |
| aero_coefficients | float64[state,2] | 1 | Coefficient rows align to a versioned local-flow-state index; columns are exactly [C_L,C_D]. | State index declares alpha/Re/Mach, row correspondence and interpolation domain; coefficient covariance required. |
| descent_state | pair<float64> | m/s,rad/s | Downward V and Omega. | Directions fixed; failed state null. |
| bubble_length | nullable<float64> | m | Stationary separation-to-reattachment distance. | Method/uncertainty required. |
| pressure_velocity_trace | nullable<record> | Pa,m/s | Synchronized D03b observations. | Sampling/duration/masks required. |
| transfer_envelope | nullable<record> | N,N m | Compatible force/torque perturbation model. | Review ID required; null if unvalidated. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NAU SEED Mars autorotation concept](https://www.ceias.nau.edu/capstone/projects/ME/2022/22F_P17MarsSensor/Project/index.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Original laminar-bubble fluctuation experiment](https://www.jstage.jst.go.jp/article/jjsass/50/582/50_582_293/_article/-char/en) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
