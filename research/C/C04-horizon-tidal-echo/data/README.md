# C04 · Data blueprint

[HORIZON TIDAL ECHO](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| epoch_obs | float64 | MJD with scale | Exposure time or interval. | Time scale required before rest-frame conversion. |
| redshift | struct<float64,error> | 1 | Host or transient redshift. | Reference and uncertainty mandatory. |
| flux_obs | float64&#124;null | erg s^-1 cm^-2 Hz^-1 | Measured spectral flux with band identity. | A limit is a separate censoring record, never zero flux. |
| response | versioned array | documented | Filter throughput or count response. | Normalize with the declared count/flux convention. |
| host_cov | float64[n,n] | flux^2 | Shared host-subtraction covariance. | Keep cross-epoch covariance. |
| temperature | posterior<float64> | K | Thermal-model temperature. | Flag Rayleigh-Jeans-only unidentifiability. |
| mass_bh | posterior<float64> | solar mass | Model-conditioned black-hole mass. | Record stellar and efficiency prior versions. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [HEASARC Swift archive](https://heasarc.gsfc.nasa.gov/docs/archive.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Published TDE host measurements](https://academic.oup.com/mnras/article/471/2/1694/4056151) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
