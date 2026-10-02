# G07 · Data blueprint

[HUBBLE SPECTRAL ANCHOR](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| interface_revision | string | 1 | Instrument drawing/datums version. | Required before final CAD dimensions. |
| optical_geometry | record | m,rad | d, order and grating/slit angles. | Sign/frame convention and units required. |
| mount_parameters | record | m,kg,Pa | Dimensions, mass and elastic properties. | Material source and tolerance covariance. |
| thermal_state | record | K | Temperature increment/gradient. | Reference temperature and field uncertainty. |
| boundary_stiffness | nullable<record> | N/m,N m/rad | Attachment compliance. | Unknown never replaced ideal fixed without flag. |
| line_centroid | nullable<float64> | m | Calibrated spectral wavelength. | Line source/resolution and fit error retained. |
| verification_link | record | 1 | Requirement-to-analysis/inspection/test evidence. | Pending evidence explicitly TBD. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA photonic validation handbook](https://nepp.nasa.gov/docuploads/0D2C2285-A001-4F95-BC3BDA2EE6A282C6/photonic_validation_methods.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
