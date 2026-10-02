# H02 · Data blueprint

[OSIRIS PHOTONFORGE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| ocams_product | string | none | Camera/filter/PDS product identity. | Label and calibration version required. |
| detector_dn | float matrix | DN | Raw or bias-qualified pixels. | Readout coordinates/saturation retained. |
| exposure_time | float | s | Documented integration duration. | Positive; definition source required. |
| dark_rate | float matrix | DN/s | Temperature-dependent dark model. | Calibration covariance saved. |
| gain | float | DN/electron | Declared conversion convention. | No reciprocal-gain ambiguity. |
| transfer_operator | sparse matrix | dimensionless | Camera-specific smear coupling. | Sequence/timing provenance required. |
| unsmeared_signal | nullable matrix | electrons | Estimated scene signal. | Support/regularization flags retained. |
| scene_covariance | matrix/operator | electrons² | Joint corrected-signal uncertainty. | Shared calibration and timing terms included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [OSIRIS-REx OCAMS PDS bundle](https://arcnav.psi.edu/urn%3Anasa%3Apds%3Aorex.ocams) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Ground and in-flight calibration publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC6979463/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
