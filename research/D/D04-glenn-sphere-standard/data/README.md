# D04 · Data blueprint

[GLENN SPHERE STANDARD](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| case_id | string | 1 | Boundary/geometry/regime configuration. | Hash and solver version required. |
| regime | record | 1 | Re, Mach and closure choice. | Continuum/slip status explicit. |
| mesh_scale | float64 | m | Systematic characteristic h. | Refinement ratio and wall measures retained. |
| time_step | nullable<float64> | s | Unsteady integration step. | Steady case null; not zero. |
| drag_components | pair<float64> | N | Pressure and viscous body loads. | Normals/quadrature and sign specified. |
| mass_flux_residual | float64 | kg/s | Net boundary/control-volume flux. | Normalization denominator recorded. |
| validation_reference | record | 1 | Matched experimental/correlation context. | Uncertainty and validity range required. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Glenn sphere-drag reference](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-of-a-sphere/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Sphere no-slip/slip CFD research](https://link.springer.com/article/10.1007/s00162-022-00627-w) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![D04 included data diagnostic](../../../../data/figures/18_sphere_drag_reference_departure.svg)

Synthetic reference values from the Schiller–Naumann sphere-drag correlation and Stokes creeping-flow asymptote. The percent-departure panel makes the approximation difference explicit, with a descriptive 10% reference crossing computed from the same formula. Neither curve is an observed drag dataset or a CFD solver result; the crossing is not a physical validation tolerance.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
