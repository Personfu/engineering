# E01 · Data blueprint

[APOLLO HELIOSCOPE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| flight_phase | enum | 1 | Ascent/float/descent interval. | Boundary times and missing phase explicit. |
| uv_irradiance | nullable<float64> | W/m^2 | Calibrated declared-band observation. | Spectral response/lag/covariance required. |
| material_endpoint | record | count | Supplied damage count and susceptible denominator. | Noninfectious source, endpoint and detection limit. |
| handling_thermal | record | K,1 | Temperature and handling covariates. | Missing null; no procedure inferred. |
| encoded_frame | record | bit | Frame size, time and usefulness label. | Encoding and rubric version required. |
| channel_trace | record | bit/s,1 | Service and effective loss replay. | Synthetic/observed provenance required. |
| battery_ledger | record | J,W | Storage and subsystem energy terms. | Efficiency/loss boundary and covariance. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Arizona Space Grant ASCEND program](https://spacegrant.arizona.edu/research/ascend) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA RaD-X balloon dosimetry](https://www.nasa.gov/science-research/heliophysics/nasa-studies-cosmic-radiation-to-protect-high-altitude-travelers/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
