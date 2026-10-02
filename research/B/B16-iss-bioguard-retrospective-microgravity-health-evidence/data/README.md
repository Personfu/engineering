# B16 · Data blueprint

[ISS BIOGUARD — Retrospective Microgravity Health Evidence](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B16 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| accession | string | none | Archived experiment/file identity. | Actual availability and checksums recorded. |
| exposure_class | enum | none | flight, analogue or matched control. | Categories never assumed equivalent. |
| replicate_key | string | none | Independent biological sample unit. | Technical replicates linked, not independent. |
| measurement_type | enum | none | counts, array intensity or phenotype. | Select compatible analysis branch. |
| confounder_metadata | nullable record | declared | Platform/strain/batch/oxygen descriptors. | Unknown remains null. |
| effect_interval | float[3] | log contrast | Estimate and uncertainty bounds. | Design rank and family recorded. |
| phenotype_evidence | nullable record | author-reported units | Direct published susceptibility endpoint. | No inference from expression alone. |
| evidence_grade | enum | none | Replicated, limited or unresolved support. | Reasons and source links retained. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA dataset: response of Pseudomonas aeruginosa PAO1 to low-shear modeled microgravity](https://data.nasa.gov/dataset/response-of-pseudomonas-aeruginosa-pao1-to-low-shear-modeled-microgravity-ff431) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA researcher guide to GeneLab](https://www.nasa.gov/science-research/for-researchers/researchers-guide-to-genelab/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
