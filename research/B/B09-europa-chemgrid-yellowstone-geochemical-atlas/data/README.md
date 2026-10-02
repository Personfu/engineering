# B09 · Data blueprint

[EUROPA CHEMGRID — Yellowstone Geochemical Atlas](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B09 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| feature_key | string | none | Persistent thermal-feature identity. | Reviewed alias/coordinate lineage. |
| sample_date | nullable date | calendar day | Collection date and precision. | No invented timestamp. |
| analyte_value | nullable float | mg/L | Original measured concentration. | Qualifier/limit retained. |
| charge | integer | elementary charges | Ionic valence for balance. | Neutral species excluded. |
| equivalent_value | nullable float | meq/L | Converted major-ion concentration. | Molar mass/valence version required. |
| basin_support | polygon key | none | Permitted interpolation domain. | Unmapped boundaries marked uncertain. |
| prediction_covariance | matrix | log-concentration² | Joint map uncertainty. | Include method and temporal covariance. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USGS Yellowstone water chemistry and isotope data, version 2.0](https://www.usgs.gov/data/water-chemistry-and-isotope-data-selected-springs-geysers-streams-and-rivers-yellowstone) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USGS chemical analyses of Yellowstone thermal features, 1980–1993](https://www.usgs.gov/publications/chemical-analyses-hot-springs-pools-and-geysers-yellowstone-national-park-wyoming-and) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
