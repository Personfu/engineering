# B22 · Data blueprint

[NIF ODYSSEY — Comparative Nitrogen-Fixation Evolution](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B22 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| accession | string | none | Reference genome/protein/expression identity. | Release and source checksum retained. |
| ortholog_group | string | none | Reviewed homolog family. | Paralog/transfer ambiguity flagged. |
| alignment_mask | bool[] | sites | Eligible comparative positions. | Gap/coverage exclusions recorded. |
| branch_support | float[] | 0–1 | Tree uncertainty measures. | Support type and resampling method explicit. |
| expression_contrast | nullable float | declared normalized units | Published retrospective regulatory comparison. | Batch/replicate metadata retained. |
| stoichiometry | sparse matrix | mol/mol | Reaction network coefficients. | Atom/charge and cofactor checks required. |
| flux_bounds | float[2][] | mmol/gDW/hour | Literature/scenario constraints. | Measured versus assumed bounds labeled. |
| flux_interval | float[2][] | mmol/gDW/hour | Feasible reaction ranges. | Solver status and unbounded flags saved. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Genome sequence of Azotobacter vinelandii](https://pmc.ncbi.nlm.nih.gov/articles/PMC2704721/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Transcriptional profiling of nitrogen fixation in Azotobacter vinelandii](https://pmc.ncbi.nlm.nih.gov/articles/PMC3165507/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
