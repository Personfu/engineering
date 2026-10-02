# A09 · Data blueprint

[SPITZER RADIO ORIGINS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A09 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| source_id | string | 1 | Native radio source key. | Stable catalog version and deblend flags. |
| flux_density | float64 | Jy | Observed radio flux. | Frequency, integrated/peak basis and error required. |
| redshift_pdf | nullable<distribution> | 1 | Spectroscopic/photo-z uncertainty. | No-redshift sources retained as missing likelihood. |
| spectral_index | nullable<float64> | 1 | Exponent in S proportional nu^alpha. | Convention required; assumed values flagged. |
| infrared_luminosity | nullable<record> | W | TIR or SF-only estimate/limit. | Definition and upper-limit flag required. |
| completeness | nullable<float64> | 1 | Detection probability at true properties. | Between zero and one; covariance/version retained. |
| sf_probability | nullable<float64> | 1 | Primary radio-power label probability. | Definition fixed; unclassified is null, not zero. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [IRSA COSMOS 3 GHz AGN catalog definitions](https://irsa.ipac.caltech.edu/data/COSMOS/gator_docs/cosmos_3ghzagn_colDescriptions.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [VLA-COSMOS radio project](https://cosmos.astro.caltech.edu/page/radio) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
