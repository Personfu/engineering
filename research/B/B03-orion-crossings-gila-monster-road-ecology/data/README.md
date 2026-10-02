# B03 · Data blueprint

[ORION CROSSINGS — Gila Monster Road Ecology](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| animal_key | restricted string | none | Pseudonymous individual identity. | Never exported with precise tracks. |
| fix_time | datetime | UTC | Observation timestamp. | Sorted; cadence gaps explicit. |
| position_xy | float[2] | m | Projected telemetry coordinate. | CRS and covariance required. |
| road_version | string | none | Geometry and effective-date key. | No future road assigned. |
| traffic_rate | nullable float | vehicles/day | Observed or scenario traffic. | Separate measurements from assumptions. |
| fate_interval | nullable datetime[2] | UTC | Bounds of confirmed event or censoring. | Death and transmitter loss distinct. |
| avoided_loss | float[] | animals | Intervention benefit ensemble. | Include zero/negative outcomes and horizon. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Does urbanization influence the spatial ecology of Gila monsters in the Sonoran Desert?](https://pubs.usgs.gov/publication/70032684) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Harmonized Landsat Sentinel-2 data](https://hls.gsfc.nasa.gov/hls-data/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
