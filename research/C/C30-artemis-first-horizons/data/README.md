# C30 · Data blueprint

[ARTEMIS FIRST HORIZONS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C30 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| seed_scenario | enum/version | 1 | Light, cluster or heavy initial model. | Distribution and host-occupation assumptions recorded. |
| birth_mass_time | distribution<float64[2]> | solar mass, yr | Seed initial conditions. | Cosmology/time origin and support required. |
| growth_history | float64[n,fields] | yr, 1, solar mass | Accretion/duty/efficiency and mass evolution. | Efficiency bounds and on/off convention explicit. |
| merger_ledger | table&#124;null | solar mass, yr | Added mass, delay and loss assumptions. | Absent module does not imply measured zero mergers. |
| intrinsic_luminosity | distribution<float64> | erg s^-1 | Active SED/bolometric model. | Bolometric correction and lambda convention. |
| lensing_host_cov | covariance | mixed declared | Magnification/host/BH observation dependence. | Shared lensing errors retained. |
| selection_probability | float64 | 1 | Survey inclusion after obscuration/flux/cadence. | Nonnegative; unsupported domains flagged. |
| seed_evidence | struct | 1 | Conditional model score and predictive checks. | Separate measured constraints from forecasts and reused model products. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [TRINITY population products](https://github.com/HaowenZhang/TRINITY) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [UHZ1 heavy-seed candidate studies](https://arxiv.org/abs/2305.15458) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
