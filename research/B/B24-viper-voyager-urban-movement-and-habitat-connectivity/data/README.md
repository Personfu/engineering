# B24 · Data blueprint

[VIPER VOYAGER — Urban Movement and Habitat Connectivity](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B24 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| animal_key | restricted string | none | Pseudonymous telemetry individual. | Not exported with refuge coordinates. |
| fix_time | datetime | UTC | Measurement time. | Cadence/gap flags preserved. |
| position_covariance | float64[2,2] | m² | Horizontal location error in declared [x,y] projected coordinates. | Exactly 2x2, symmetric PSD; CRS and covariance basis required. |
| landcover_key | string | none | Dated GIS classification product. | Acquisition/effective date retained. |
| cover_fraction | float[] | 0–1 | Scale-specific habitat exposure. | Class covariance/resolution saved. |
| step_stratum | string | none | Used/available matched alternatives. | Shared start/cadence audited. |
| range_area | nullable float | km² | Specified utilization contour area. | Contour/estimator/cadence recorded. |
| effect_covariance | matrix | mixed | Joint selection/range uncertainty. | Individual and GIS terms included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [University of Arizona Stone Canyon Project](https://herpetology.arizona.edu/content/stone-canyon-project.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Tiger rattlesnake urban movement study, Conservation Science and Practice](https://conbio.onlinelibrary.wiley.com/doi/10.1111/csp2.70313) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Harmonized Landsat Sentinel-2 data](https://hls.gsfc.nasa.gov/hls-data/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
