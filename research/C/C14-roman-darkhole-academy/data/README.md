# C14 · Data blueprint

[ROMAN DARKHOLE ACADEMY](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C14 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| optical_prescription | struct | m, radian | Aperture, propagation planes and OPD. | Versioned geometry and wavelength grid. |
| command | float64[m] | actuator-specific | Real modal/actuator coefficients. | Bounds and calibration units required. |
| probe_images | float64[n,h,w] | electron | Plus/minus probe measurements. | Background, exposure and saturation flags retained. |
| field_estimate | complex128[nroi] | normalized field | Estimated focal-plane field. | Covariance on both quadratures required. |
| jacobian | complex128[nroi,m] | field per command | Local command response. | Calibration state and validity range attached. |
| camera_cov | covariance | electron^2 | Read/photon/background covariance. | Missing pixels masked, never assigned zero field. |
| contrast_throughput | measurement<float64[2]> | 1 | Joint contrast and desired-source throughput. | Reference/ROI/source offset and noise floor attached. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [JPL PROPER software](https://science.jpl.nasa.gov/projects/proper/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [New optical bench campaign](https://ao.jpl.nasa.gov/compact_dm_electronics.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
