# I10 · Data blueprint

[GEMINI POINTLOCK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I10 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| source_time | float64 | s | Synchronized sensor/control/power time. | Clock/reset generation and gaps retained. |
| reference_angle | float64 | radian | Commanded one-axis orientation. | Wrap/trajectory policy version. |
| angle_rate | measurement<float64[2]> | radian, radian s^-1 | Calibrated body angle and rate. | Bias covariance and missing-sensor state. |
| plant_parameters | posterior<struct> | kg m^2, N m s rad^-1, s | Inertia, friction and lag. | Identification conditions and near-zero-rate discrepancy. |
| wheel_state | measurement<struct> | N m s, radian s^-1 | Wheel momentum/speed and limits. | Sign/inertia convention and saturation flag. |
| torque_command | float64 | N m | Requested/applied wheel torque. | Both values retained when saturated. |
| electrical_ledger | measurement<struct> | W, J | Input draw, cumulative consumed/returned energy. | Current sign and power calibration; no mechanical-energy substitution. |
| mechanical_energy | measurement<float64> | J | Wheel kinetic energy from state. | Separate field/inertia covariance. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA small-spacecraft GNC reference](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed turntable characterization dataset](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![I10 included data diagnostic](../../../../data/figures/13_attitude_phase_and_authority.svg)

Synthetic one-axis PD attitude response and actuator authority. The phase portrait is colored by elapsed model time. Requested torque is reconstructed from the recorded states and sidecar gains; the applied torque is clipped to ±8 mN·m. The right panel focuses on the first 40 seconds, while the phase portrait uses the full 120-second record.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
