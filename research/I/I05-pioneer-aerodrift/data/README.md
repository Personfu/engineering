# I05 · Data blueprint

[PIONEER AERODRIFT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| source_receive_time | float64[2] | s, declared scale | Measurement and reception timestamps. | Delay/order never overwrites source time. |
| geodetic_state | measurement<float64[3]> | degree, degree, m | Latitude/longitude/height. | Ellipsoid/altitude datum and covariance. |
| pressure_temperature | measurement<float64[2]> | Pa, K | Atmospheric sensor readings. | Lag/bias calibration version and missing flags. |
| illumination_board | float64[] | W m^-2, K | Solar/environment and housing proxy. | Sensor-specific bias model documented. |
| trajectory_cov | float64[n,n] | mixed declared | Position/velocity/wind ensemble uncertainty. | Shared navigation and wind errors retained. |
| power_energy | measurement<struct> | W, J | Harvest/loads and stored energy. | Capacity and cumulative consumption distinguished. |
| packet_quality | struct | 1 | Sequence/checksum/loss/restart state. | Missing samples absent, not repeated last value. |
| comparison_profile | table&#124;null | Pa, K, m s^-1 | Collocated quality-screened IGRA data. | Station history and space/time support recorded. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NOAA Integrated Global Radiosonde Archive](https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed pico-platform telemetry](https://www.nasa.gov/scientificballoons/overview/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
