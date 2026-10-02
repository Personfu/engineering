# C09 · Data blueprint

[EAGLESAT COSMIC PIXEL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C09 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| frame_adc | uint16[h,w] | ADC unit | Raw sensor values. | Preserve saturation codes and shutter metadata. |
| temperature | measurement<float64> | K | Sensor thermal state. | Missing temperature blocks domain-specific energy claims. |
| gain_map | float64[h,w] | electron ADC^-1 | Electronic conversion by pixel/region. | Versioned; nonlinearity envelope required. |
| cluster_charge | float64[n] | electron | Calibrated charge within event pixels. | Negative noise values retained before thresholding. |
| charge_cov | float64[n,n] | electron^2 | Bias/gain/readout covariance. | Shared bias/gain terms retained. |
| deposited_energy | posterior<float64> | keV | Charge-conditioned silicon energy loss. | Saturation yields lower-bound state. |
| incident_energy | posterior<float64>&#124;null | MeV | Transport-conditioned incoming energy. | Null or bound outside validated response domain. |
| response_domain | struct | species, degree, K | Validated conditions for response matrix. | Explicit extrapolation flag mandatory. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NIST PSTAR proton stopping powers](https://physics.nist.gov/PhysRefData/Star/Text/PSTAR.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [New calibration and dark-frame campaign](https://arxiv.org/abs/2607.02106) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
