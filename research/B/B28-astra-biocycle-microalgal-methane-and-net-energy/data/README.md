# B28 · Data blueprint

[ASTRA BIOCYCLE — Microalgal Methane and Net Energy](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B28 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| study_treatment | record | none | Biomass/source/treatment evidence identity. | Separate versus combined provenance required. |
| volatile_solids_added | float | kg VS | Yield normalization denominator. | Method and dry/volatile fraction uncertainty saved. |
| cumulative_gas | nullable float[] | L | Measured replicate/blank volumes. | Time correlation and conditions retained. |
| methane_fraction | nullable float[] | 0–1 | Measured composition on stated basis. | Wet/dry convention explicit. |
| gas_conditions | record | K Pa | Measured and normalization state. | Water-vapor correction metadata required. |
| kinetic_parameters | float[] | L L/day day | M_inf, R_max and lag ensemble. | Covariance/plateau support retained. |
| pretreatment_energy | record | kWh | Cooling/heating/auxiliary inventory. | COP/recovery/boundary source required. |
| net_energy | float[] | kWh/kg VS | Usable-energy scenario distribution. | Include negative outcomes and synergy uncertainty. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Influence of temperature and pretreatments on anaerobic digestion of microalgae](https://pubmed.ncbi.nlm.nih.gov/24726994/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Impact of low-temperature pretreatment on anaerobic digestion of microalgal biomass](https://pubmed.ncbi.nlm.nih.gov/23619135/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
