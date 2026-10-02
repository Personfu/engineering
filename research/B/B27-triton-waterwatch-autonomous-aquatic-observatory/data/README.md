# B27 · Data blueprint

[TRITON WATERWATCH — Autonomous Aquatic Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B27 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| sensor_time | datetime | UTC | Original and aligned reading times. | Clock source/offset covariance required. |
| position_xy | float[2] | m | Projected vessel location. | CRS and GPS covariance saved. |
| sensor_depth | nullable float | m | Measurement support below surface. | Null cannot imply full-column reading. |
| temperature | nullable float | °C | Calibrated water temperature. | Reference check and drift flags retained. |
| conductivity | nullable float | µS/cm | Specified reference-temperature channel. | Compensation method required. |
| dissolved_oxygen | nullable float | mg/L | Compensated oxygen measurement. | Pressure/salinity metadata retained. |
| response_model | record | s | Dead-time/first-order response description. | Correction support and noise amplification saved. |
| map_covariance | matrix | parameter-unit² | Joint spatial/temporal prediction uncertainty. | Calibration and position covariance included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USGS North Saluda Reservoir bathymetric and water-quality mapping](https://pubs.usgs.gov/sim/3289/pdf/sim3289.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Design and development of an autonomous surface vehicle for water-quality monitoring](https://arxiv.org/abs/2201.10685) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Water Quality Portal](https://www.waterqualitydata.us/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
