# I08 · Data blueprint

[VOYAGER FRAMEFORGE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| state_vector | float64[6] | m, m s^-1 | Position and velocity relative to named center. | No implicit frame/time defaults. |
| epoch_context | struct | s or JD | Time value, scale and conversion pedigree. | Leap/time kernels and source scale required. |
| source_manifest | struct | 1 | Kernel hashes or complete query/output. | Validity intervals and retrieval date. |
| frame_correction | struct | 1 | Reference frame and aberration mode. | Apparent and geometric states distinct. |
| gravity_parameters | struct | m^3 s^-2, m, 1 | mu, radius and coefficient normalization. | Mass/shape/spin provenance independent. |
| mesh_density | measurement<struct>&#124;null | m, kg m^-3 | Closed shape and physical density. | Oriented closed topology and uncertainty. |
| potential_acceleration | float64[4] | m^2 s^-2, m s^-2 | Model output with sign convention. | Singular/out-of-domain locations flagged. |
| state_covariance | float64[6,6]&#124;null | mixed state^2 | Source-supported uncertainty only. | Null if unavailable; synthetic ensembles labeled illustrative. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA/JPL NAIF SPICE tutorials and kernels](https://naif.jpl.nasa.gov/naif/tutorials.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [JPL Horizons reference queries](https://ssd.jpl.nasa.gov/horizons/manual.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![I08 included data diagnostic](../../../../data/figures/14_orbit_conservation_and_refinement.svg)

Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
