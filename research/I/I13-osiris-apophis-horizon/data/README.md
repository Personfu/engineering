# I13 · Data blueprint

[OSIRIS APOPHIS HORIZON](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I13 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| passive_reference | struct | m, m s^-1, TDB s | Frozen unaltered Apophis states/query. | NASA safe premise and source checksum attached. |
| initial_covariance | float64[6,6]&#124;null | mixed state^2 | Authoritative or illustrative uncertainty. | Pedigree/type mandatory; null if absent. |
| normalized_offset | float64[6] | 1 | Educational offsets in a declared ellipsoid basis. | Synthetic only; no intervention parameters. |
| state_transition | float64[6,6] | mixed blocks | Variational sensitivity matrix. | Scale convention and derivative convergence. |
| encounter_plane | measurement<float64[2]> | m | Declared geometric sensitivity coordinates. | Plane/event-time convention and covariance. |
| ensemble_trace | distribution<state> | mixed state | Nonlinear passive/synthetic scenario histories. | Seed, force model and scenario type retained. |
| observation_model | struct | radian, m, m s^-1 | Hypothetical passive measurement/noise/cadence. | Assumed versus verified capability explicit. |
| information_gain | measurement<float64> | nat | Expected posterior/prior information. | State support/noise model and numerical uncertainty. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Apophis facts](https://science.nasa.gov/solar-system/asteroids/apophis-facts/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [JPL Horizons passive reference ephemeris](https://ssd.jpl.nasa.gov/horizons/manual.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![I13 included data diagnostic](../../../../data/figures/14_orbit_conservation_and_refinement.svg)

Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
