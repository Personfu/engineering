# A08 · Data blueprint

[HELIOS PULSE FORGE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| time_grid | vector<float64> | s | Retarded time samples. | Uniform spacing, window and origin recorded. |
| input_field | vector<complex128> | sqrt(W) | Retrieved complex envelope. | Phase reference, covariance and retrieval method required. |
| pass_geometry | array<record> | m | Path lengths and beam radii. | No missing radius silently replaced. |
| nonlinear_index | float64 | m^2/W | Material n2 at declared conditions. | Source and uncertainty required. |
| dispersion | array<float64> | s^2/m | Per-medium beta2. | Higher-order terms separately labeled. |
| optic_phase | nullable<vector<float64>> | rad | Mirror/compressor spectral phase. | Unknown null; interpolation domain checked. |
| energy_metrics | record | J,1 | Output, main-window energy and throughput. | Window rule immutable across comparisons. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Gas-filled multipass compression study](https://opg.optica.org/ol/abstract.cfm?uri=ol-43-9-2070) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Dispersion-engineered high-quality compression study](https://pubmed.ncbi.nlm.nih.gov/37966747/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
