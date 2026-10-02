# I01 · Data blueprint

[SATURN TRANSIENT SHIELD](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| scenario_label | struct | 1 | External phi/chemistry comparator identity. | No encoded firing/flow schedule. |
| heat_flux_history | measurement<float64[n,npatch]> | W m^-2 | Externally provided boundary heat load. | Source/covariance and spatial interpolation required. |
| coupon_properties | measurement<struct> | m, kg m^-3, J kg^-1 K^-1, W m^-1 K^-1 | Verified inert geometry and material. | Temperature validity range recorded. |
| contact_boundary | posterior<struct> | W m^-2 K^-1, K | Contact/environment thermal conditions. | Independent calibration or prior-dominance flag. |
| temperature_observation | float64[n,nsensor] | K | Sensor measurements/predictions. | Missing samples masked; lag response retained. |
| thermal_cov | float64[n,n] | K^2 | Sensor/input/model covariance. | Common heat/load and calibration terms preserved. |
| stress_strain | distribution<struct> | Pa, 1 | Conditional restrained mechanical response. | Constraint/inelastic model version explicit. |
| damage_proxy | posterior<float64>&#124;null | 1 | Screening cycle accumulation. | Null without applicable material-cycle evidence. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA CEA reference](https://ntrs.nasa.gov/api/citations/19950013764/downloads/19950013764.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA rocket cooling technical reference](https://ntrs.nasa.gov/api/citations/19810012596/downloads/19810012596.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
