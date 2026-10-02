# C20 · Data blueprint

[TRINITY ACCRETION ECHO](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C20 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| population_draw | struct | solar mass, 1 | TRINITY mass/accretion/host draw and weight. | Native posterior/commit identity attached. |
| variability_law | enum/version | 1 | OU or alternative extension family. | Never labeled native TRINITY time evolution. |
| tau_sigma | posterior<float64[2]> | day, X day^-1/2 | Rest-frame process parameters. | Positive timescale; convention of X explicit. |
| epoch_window | float64[n,2] | observer day | Observed exposure intervals. | Missing epochs absent; time origin/scale recorded. |
| redshift | measurement<float64> | 1 | Object redshift. | Positive 1+z and uncertainty retained. |
| host_flux | measurement<float64> | flux unit | Nonvariable dilution component. | Add in flux space with shared uncertainty. |
| lightcurve_cov | float64[n,n] | X^2 | Observed process plus noise covariance. | PSD and covariance validity checks required. |
| autocorrelation | measurement<float64[]> | 1 | Selected ensemble temporal correlation by lag. | Population weights and lag exposure recorded. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [TRINITY public repository](https://github.com/HaowenZhang/TRINITY) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [SDSS Stripe 82 variability study](https://arxiv.org/abs/1004.0276) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
