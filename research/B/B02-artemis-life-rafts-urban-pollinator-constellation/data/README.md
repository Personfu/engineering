# B02 · Data blueprint

[ARTEMIS LIFE RAFTS — Urban Pollinator Constellation](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| patch_id | string | none | Candidate or surveyed habitat patch. | Persistent boundary version required. |
| visit_effort | float | min | Standardized observation duration. | Zero effort invalid for absence inference. |
| detection_history | bool[] | none | Taxon observations across repeat visits. | Missing visits stored as null. |
| effective_distance | float | m | Taxon-specific least-cost graph separation. | Nonnegative; resistance version required. |
| weekly_bloom | float[] | probability | Species flowering ensemble. | Preserve species/site covariance. |
| annual_water | float | L/year | Maintenance scenario demand. | Identify measured versus assumed demand. |
| portfolio_score | float[] | none | Occupancy/resource ensemble by taxon. | Publish distribution with constraint failures. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Urban areas as hotspots for bees and pollination but not a panacea for all insects](https://www.nature.com/articles/s41467-020-14496-6) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USA National Phenology Network observational data](https://nn.usanpn.org/data/observational) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
