# B07 · Data blueprint

[REGENESIS CLEANFLOW — Environmental Fate and Remediation Model](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| analyte_id | string | none | Verified parent/product identity. | Formula and assay identity required. |
| dissolved_concentration | nullable float | mg/L | Measured aqueous concentration. | Limit, recovery and qualifier retained. |
| sorbed_concentration | nullable float | mg/kg dry | Solid-associated analyte. | Extraction basis and dry mass required. |
| element_count | integer vector | atoms/molecule | C/N counts for molar accounting. | Check formula consistency. |
| reaction_rate | float[] | mol/L/day | Fitted pathway-rate ensemble. | Source matrix/redox domain recorded. |
| inventory_covariance | matrix | mol² | Joint compartment uncertainty. | Include shared recovery/background bias. |
| benchmark | nullable float | mg/L | Applicable environmental comparison value. | Null remains unresolved, never zero risk. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Combined biological and abiotic reactions with iron and Fe(III)-reducing microorganisms for remediation](https://pubs.rsc.org/en/content/articlehtml/2015/ew/c4ew00062e) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [SERDP insensitive munitions environmental health, fate and transport resources](https://serdp-estcp.mil/resources/details/67fdfd78-7528-443c-a3f9-d7f109407801) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
