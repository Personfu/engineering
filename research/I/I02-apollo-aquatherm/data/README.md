# I02 · Data blueprint

[APOLLO AQUATHERM](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| heat_input | measurement<float64[n]> | W | Known electrical/supplied thermal load. | Meter/reference and spatial allocation documented. |
| mass_flow | measurement<float64[n]> | kg s^-1 | Loop or branch flow. | Positive accepted range; missing flow blocks heat-rate estimate. |
| fluid_state | struct<float64[]> | K, Pa | Inlet/outlet and domain-monitoring states. | Single-phase status and fluid-property source. |
| wall_temperature | float64[n,nsensor] | K | Distributed wall observation. | Location/lag/calibration required. |
| thermal_graph | struct<C,G,hA> | J K^-1, W K^-1 | Wall/contact/convection network. | Conservative internal links and verified geometry. |
| sensor_cov | covariance | mixed declared | Power/temperature/flow/lag uncertainty. | Shared thermometer offset retained. |
| energy_ledger | float64[n,terms] | W or J | Input, uptake, loss and stored energy. | Instantaneous power and cumulative energy separate. |
| hotspot_prediction | posterior<float64> | K | Maximum conditional wall temperature. | Sensor coverage and model discrepancy attached. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA cooling technical reference](https://ntrs.nasa.gov/api/citations/19810012596/downloads/19810012596.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed inert thermal-loop dataset](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
