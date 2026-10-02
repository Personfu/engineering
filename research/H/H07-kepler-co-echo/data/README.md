# H07 · Data blueprint

[KEPLER CO ECHO](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| alma_product | string | none | Project/cube/measurement-set identity. | Selection and calibration versions retained. |
| intensity_cube | nullable array | Jy/beam | Continuum-subtracted channel image. | Beam/primary-beam flags required. |
| velocity_axis | float[] | km/s | Declared spectral frame/convention. | Rest frequency and channel width saved. |
| beam_solid_angle | float | sr | Synthesized Gaussian support. | Major/minor axes and position angle retained. |
| disk_geometry | record | kg m rad km/s | Stellar/disk alignment parameters. | Independent source and covariance required. |
| noise_covariance | matrix | (Jy/beam)² | Spatial/spectral noise model. | Line-free selection and PSD check saved. |
| search_trial | record | none | Radius/geometry/velocity/isotopologue attempt. | All attempts enter global null. |
| line_flux | nullable float[] | Jy km/s | Aperture integrated flux/limit. | Distinct from normalized stack and gas mass. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [ALMA Science Archive](https://almascience.nrao.edu/alma-data) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Long et al. Chamaeleon I CO survey](https://arxiv.org/abs/1706.03320) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
