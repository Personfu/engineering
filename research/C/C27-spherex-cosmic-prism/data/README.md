# C27 · Data blueprint

[SPHEREX COSMIC PRISM](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C27 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| product_id | string | 1 | QR image and checksum identity. | Release/header-correction/calibration status mandatory. |
| pixel_wavelength | float64[h,w] | micrometer | Exposure-position wavelength mapping. | Missing/invalid map pixels excluded. |
| psf_response | model<float64> | release-declared | Position/wavelength flux-to-pixel response. | Normalization and unit conversion documented. |
| source_position | measurement<float64[2]> | degree ICRS | Forced-photometry prior. | Astrometric covariance retained. |
| pixel_data_cov | covariance | pixel-unit^2 | Image uncertainty plus calibration structure. | Masks remain missing; shared calibration modes retained. |
| extracted_flux | measurement<float64[n]> | release flux unit | Response-sampled source spectrum. | Coverage mask and neighbor covariance attached. |
| redshift_posterior | distribution<float64> | 1 | Template-conditioned redshift. | Store alternate modes and template/grid support. |
| selection_surface | model<float64> | 1 | Recovery versus coverage/confusion/flux. | No interpolation beyond tested domain without flag. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [IRSA SPHEREx mission/archive page](https://irsa.ipac.caltech.edu/Missions/spherex.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [IRSA SPHEREx explorer overview](https://irsa.ipac.caltech.edu/onlinehelp/spherex/spherex/overview.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
