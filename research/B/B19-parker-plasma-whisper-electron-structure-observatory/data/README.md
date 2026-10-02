# B19 · Data blueprint

[PARKER PLASMA WHISPER — Electron Structure Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B19 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| product_key | string | none | Exact QTN level/version/interval. | Checksums and archive flags retained. |
| frequency | float[] | Hz | Spectral bin coordinates. | Monotone with receiver response key. |
| voltage_psd | nullable float[] | V²/Hz | Calibrated spectrum when available. | Noise/antenna metadata required. |
| electron_density | nullable float | m^-3 | Released or fitted electron density. | Method and units explicit. |
| electron_temperature | nullable float | K or eV | Declared core/effective temperature. | Distribution definition and conversion saved. |
| heliocentric_distance | float | AU | Encounter radial context. | Ephemeris/time alignment recorded. |
| structure_interval | datetime[2] | UTC | Independent boundary definition. | Source/cadence uncertainty retained. |
| parameter_covariance | matrix | mixed | Joint fit/released-product uncertainty. | PSD/support flags and correlations preserved. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [SPASE PSP FIELDS Level 3 simplified quasi-thermal noise metadata](https://spase-metadata.org/CNES/NumericalData/CDPP-Archive/PSP/FIELDS/RFS/LFR/PARKERSP_FIELDS_RFS_SQTN.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Radial evolution of non-Maxwellian electron populations from QTN spectroscopy](https://doi.org/10.3847/1538-4357/ad7d05) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
