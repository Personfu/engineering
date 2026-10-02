# ATLAS Engineering

**117 engineering research records, preserving every original project in its exact A–I session order.** Each project has a NASA-inspired name and a detailed design basis, requirements, mathematical formulation and derivation, data specification, uncertainty analysis, trade study, verification plan, implementation work packages, failure analysis, technical architecture figure and cited primary resources.

Start with the [ordered engineering document register](ENGINEERING_DOCUMENTATION.md). For continuous reading, use the nine session handbooks below. The combined D03 title retains both the autorotating probe and laminar-separation-bubble investigations as distinct work packages.

| Session | Engineering handbook | Original projects |
| --- | --- | ---: |
| A | [Math, Physics & Chemistry](documentation/SESSION_A.md) | 12 |
| B | [Earth & Environmental Engineering](documentation/SESSION_B.md) | 28 |
| C | [Astronomy & Space Physics](documentation/SESSION_C.md) | 30 |
| D | [Aeronautics](documentation/SESSION_D.md) | 7 |
| E | [ASCEND](documentation/SESSION_E.md) | 8 |
| F | [Education & Public Outreach](documentation/SESSION_F.md) | 2 |
| G | [Exploration Systems Engineering](documentation/SESSION_G.md) | 8 |
| H | [Planetary Science](documentation/SESSION_H.md) | 9 |
| I | [Aerospace Technology](documentation/SESSION_I.md) | 13 |

## Engineering artifacts

- [117 individually addressable project records](ENGINEERING_DOCUMENTATION.md), totaling approximately 247,000 words.
- [527 requirements](catalog/requirements.csv) and [434 specified verification cases](catalog/verification_cases.csv), with persistent IDs and evidence fields.
- [117 JSON record schemas, field dictionaries and empty acquisition CSVs](data/contracts/README.md), covering 877 defined data fields.
- 117 editable engineering architecture diagrams and their rendered SVGs, linked from the relevant records.
- [Eight executable reduced-model demonstrations](models/README.md), nine numerical figures, tabular outputs and a separately acquired 200-row NASA Exoplanet Archive snapshot with query and retrieval provenance.
- [250 distinct cited resources](catalog/source_index.csv), with project-to-source mappings.

## Design and evidence controls

Use the [engineering documentation standard](docs/ENGINEERING_STANDARD.md), [interface control procedure](docs/INTERFACE_CONTROL.md), [model assurance plan](docs/MODEL_ASSURANCE.md), [uncertainty and decision rules](docs/UNCERTAINTY_AND_DECISION_RULES.md), [data management plan](docs/DATA_MANAGEMENT.md) and [execution roadmap](docs/EXECUTION_ROADMAP.md) to turn a record into an investigation with reviewable evidence.

These are research design and analysis documents. Project-specific empirical validation remains pending. Header-only CSVs are acquisition templates; synthetic model parameters and outputs are labeled; the public exoplanet snapshot is separately identified as real data. The 434 specified cases are future verification work, distinct from the executed software checks. NASA-inspired names and use of NASA engineering references do not imply NASA affiliation, certification, clinical efficacy or flight qualification.

The original-title register is preserved in [original_titles.json](catalog/original_titles.json). The supplied titles correspond to the [2021 Arizona Space Grant symposium program](https://spacegrant.arizona.edu/sites/spacegrant.arizona.edu/files/AZSGC%20Symposium%20Booklet%202021_website.pdf). These documents develop new engineering proposals; they do not reproduce its abstracts or claim authorship of the historical work.

## Review and reproducibility

[Release verification](reviews/RELEASE_VERIFICATION.md) records the completed assembly checks, [independent revision-2 review](reviews/INDEPENDENT_ENGINEERING_REVIEW.md), numerical verification and their limits. [Documentation build instructions](tools/README.md) explain how to regenerate records and diagrams from the versioned sources. Model execution instructions are in [models/README.md](models/README.md).
