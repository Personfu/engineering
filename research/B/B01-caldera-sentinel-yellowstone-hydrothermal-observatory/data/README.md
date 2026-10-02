# B01 · Data blueprint

[CALDERA SENTINEL — Yellowstone Hydrothermal Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| sample_id | string | none | Persistent water-sample key. | Unique; unresolved aliases quarantine joins. |
| collected_at | datetime | UTC | Actual collection timestamp or documented date precision. | Missing time never fabricated. |
| chloride | nullable float | mg/L | Conservative tracer candidate. | Retain censoring limit and method. |
| endmember_pair | float[2] | mg/L | Thermal and meteoric scenario values. | Store full 2x2 covariance and provenance. |
| displacement_up | nullable float | mm | Referenced vertical station displacement. | Offsets and reference epoch required. |
| hydrology | nullable vector | declared | Precipitation and discharge summaries. | Store coverage fraction and missingness. |
| forecast_covariance | matrix | mm² | Joint annual prediction covariance. | Symmetric positive semidefinite; include shared bias. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USGS Yellowstone water chemistry and isotope data, version 2.0](https://www.usgs.gov/data/water-chemistry-and-isotope-data-selected-springs-geysers-streams-and-rivers-yellowstone) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Yellowstone Volcano Observatory 2024 annual report](https://pubs.usgs.gov/publication/cir1566/full) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
