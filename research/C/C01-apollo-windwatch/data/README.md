# C01 · Data blueprint

[APOLLO WINDWATCH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 6 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| epoch | float64 | BJD | Barycentric exposure midpoint. | Null until time scale and correction are documented. |
| exposure | float64[2] | day | Start and end in the common time system. | End must exceed start. |
| velocity | float64[n] | km s^-1 | Line-relative gas velocity grid. | Rest wavelength and air/vacuum convention required. |
| profile | float64[n] | 1 | Continuum-normalized line flux. | Masked pixels stay missing; no zero filling. |
| profile_cov | float64[n,n] | 1 | Pixel and continuum covariance. | Symmetric positive semidefinite; preserve shared continuum terms. |
| line_delay | posterior<float64> | day | Conditional response delay relative to a named reference line. | Report multimodality and reference-line identity. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [CHIRON study and associated publication material](https://arxiv.org/abs/2310.15986) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [MAST mission holdings](https://archive.stsci.edu/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
