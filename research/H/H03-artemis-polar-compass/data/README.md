# H03 · Data blueprint

[ARTEMIS POLAR COMPASS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| mag_product | string | none | LMAG/Prospector pass provenance. | Observation-level coverage and flags required. |
| field_vector | nullable float[3] | nT | Measured magnetic components. | Frame/time transformation recorded. |
| position_xyz | float[3] | m | Observation geometry. | Lunar origin/frame and altitude explicit. |
| dipole_moment | float vector | A m² | Equivalent-source estimator. | Depth/grid/gauge not physical truth. |
| nuisance_design | matrix | declared | Pass external-field basis H. | Rank and constraints retained. |
| observation_covariance | matrix | T² | Correlated measurement/environment error. | PSD and unit conversion checked. |
| projected_resolution | matrix | dimensionless | Nuisance-aware R_m. | Supported singular modes documented. |
| reference_map | record | nT | Modeled altitude field and uncertainty. | Altitude/continuation support explicit. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [JAXA DARTS Kaguya archive](https://darts.isas.jaxa.jp/en/missions/kaguya) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [PDS Lunar Prospector holdings](https://pds-geosciences.wustl.edu/missions/lunarp/index.htm) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
