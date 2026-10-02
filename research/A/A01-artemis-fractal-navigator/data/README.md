# A01 · Data blueprint

[ARTEMIS FRACTAL NAVIGATOR](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| scene_id | string | 1 | Map and coordinate manifest hash. | Required; alternative maps use new IDs. |
| center_decimal | pair<string> | 1 | Real and imaginary center. | Never cast first to float. |
| footprint_width | float64 | 1 | Complex-plane pixel width. | Positive; height supplied if anisotropic. |
| precision_bits | uint32 | bit | Reference and working precisions. | Both recorded with library version. |
| escape_iteration | nullable<uint64> | iteration | First validated radius crossing. | Null for nonescape; zero is valid. |
| classification | enum | 1 | Evidence-qualified pixel status. | Certificates require bound metadata. |
| error_bound | nullable<float64> | 1 | Absolute coordinate/iteration uncertainty. | Bound versus heuristic flagged; unknown null. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Self-generated, versioned numerical benchmark](https://mathr.co.uk/mandelbrot/perturbation.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![A01 included data diagnostic](../../../../data/figures/17_fractal_resolution_and_escape.svg)

Finite-grid escape iteration maps from immutable Mandelbrot and Julia outputs. Logarithmic color records the first iteration whose modulus exceeds two. Navy regions identify points that did not escape within 160 iterations; these points are unresolved by this computation and are not certified members. The Julia parameter is c = −0.75 + 0.11i.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
