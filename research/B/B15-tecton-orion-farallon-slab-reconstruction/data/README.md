# B15 · Data blueprint

[TECTON ORION — Farallon Slab Reconstruction](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B15 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| scenario_key | string | none | Boundary/rheology ensemble identity. | Hash complete configuration. |
| convergence_velocity | float[] | m/s | Prescribed plate history. | Ma-to-second conversion explicit. |
| viscosity | float field | Pa s | Temperature/pressure/strain dependent rheology. | Positive; cutoff provenance retained. |
| temperature | float field | K | Thermal model state. | Boundary and initial condition keys required. |
| density_anomaly | float field | kg/m³ | Buoyancy relative to reference. | Reference density and composition law explicit. |
| slab_metrics | float vector | degrees km | Dip and flattening/arc descriptors. | Extraction method/version retained. |
| geology_covariance | matrix | mixed | Joint observation-group uncertainty. | Age/spatial correlations documented. |
| run_status | enum | none | converged, failed or unsupported. | Failed runs never silently discarded. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Farallon plate dynamics prior to the Laramide orogeny: numerical models of flat subduction](https://www.sciencedirect.com/science/article/abs/pii/S0040195115005594) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Basal continental mantle lithosphere displaced by flat-slab subduction](https://www.nature.com/articles/s41561-018-0263-9) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
