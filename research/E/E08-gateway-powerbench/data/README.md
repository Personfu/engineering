# E08 · Data blueprint

[GATEWAY POWERBENCH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| harness_state | enum | 1 | Local verification/simulation state. | Transition/interlock reason logged. |
| approved_limits | nullable<record> | V,A,K | Controlling DUT/fixture envelope. | Missing blocks stimulus-enabled acceptance. |
| source_dut_voltage | pair<float64> | V | Independent source/terminal observations. | Calibration and sense location required. |
| current | float64 | A | Signed delivered/discharge current. | Direction and path defined. |
| sample_clock | record | s | V/I acquisition timing and skew. | Common clock or offset covariance. |
| harness_resistance | nullable<float64> | ohm | Wiring/contact resistance. | Temperature/source and covariance retained. |
| energy_soc_output | record | J,1 | Ledger and optional SOC estimate. | Chemistry/capacity status; unsupported SOC null. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Small Spacecraft Power](https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [GSFC-STD-7000 GEVS](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
