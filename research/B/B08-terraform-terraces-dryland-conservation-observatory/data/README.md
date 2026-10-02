# B08 · Data blueprint

[TERRAFORM TERRACES — Dryland Conservation Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| structure_id | string | none | Dated conservation intervention. | Condition and maintenance history required. |
| install_bounds | date[2] | calendar day | Installation interval. | Uncertain dates propagate to event bins. |
| cover_vector | float[3] | percent | Herb, shrub and bare fraction. | Sum and classification covariance checked. |
| channel_distance | float | m | Signed distance from structure. | Positive downstream; CRS recorded. |
| reach_area | float | m² | Water-ledger support area. | Positive and fixed per comparison. |
| rainfall | nullable float | mm/day | Reach forcing. | Coverage and gauge uncertainty retained. |
| effect_covariance | matrix | percentage-point² | Treatment-effect uncertainty. | Spatial and temporal covariance included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USDA ARS research on porous rock check dams](https://www.ars.usda.gov/research/publications/publication/?seqNo115=363913) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Dryland rock detention structures increase herbaceous vegetation cover and stabilize shrub cover over 10 years](https://pubmed.ncbi.nlm.nih.gov/38280600/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Harmonized Landsat Sentinel-2 data](https://hls.gsfc.nasa.gov/hls-data/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
