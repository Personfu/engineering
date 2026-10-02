# C07 · Data blueprint

[ARTEMIS MEMORY BRIDGE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| time | float64[n] | s | Simulation times relative to a declared origin. | Strictly increasing; gaps are not interpolated silently. |
| polarization | float64[n,2] | strain | h_plus and h_cross at reference distance. | Offset convention and modeled memory terms required. |
| endpoint_slope | measurement<float64[2]> | s^-1 | Tail initial strain rate. | Derivative method and covariance recorded. |
| tail_timescale | posterior<float64> | s | Continuation timescale. | Positive; physically unsupported ranges flagged. |
| memory_offset | posterior<float64[2]> | strain | Asymptotic minus initial strain. | Physical offset retained independently of FFT window. |
| transfer_function | complex128[nf] | 1 | Selected detector response/filter. | Frequency range and phase convention required. |
| spectral_cov | complex covariance | strain^2 s^2 | Continuation spectral uncertainty. | Keep cross-frequency correlation from shared tail parameters. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Richardson et al. memory modeling](https://arxiv.org/abs/2109.01582) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [GWOSC noise and technical data](https://gwosc.org/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
