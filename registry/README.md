# Research registry

**The controlled index behind the readable documents.**

This folder holds the canonical project definitions and traceability tables. The [research atlas](../research/README.md) and [ordered register](../ENGINEERING_DOCUMENTATION.md) provide the visual reading routes; the files below support inspection, regeneration and analysis.

| Record | Contents |
| --- | --- |
| [Original titles](original_titles.json) | The exact 117 supplied titles, grouped in A–I order |
| [Session names](sessions.json) | The nine discipline labels |
| [Project definitions](projects.json) | Persistent IDs, mission names, scientific questions, models, resource pointers and sources |
| [Engineering annexes](engineering_annexes.json) | Detailed requirements, derivations, fields, uncertainty, trades, verification cases and failure analysis |
| [Project paths](project_paths.json) | The controlled location of each project folder and engineering record |
| [Project index CSV](project_index.csv) | A tabular project inventory |
| [Requirements CSV](requirements.csv) | 527 requirement records, with verification and evidence fields |
| [Verification cases CSV](verification_cases.csv) | 434 specified cases and their evidence-pending status |
| [Source index CSV](source_index.csv) | Cited resource titles, links and project mappings |
| [Source records](sources.json) | The same resource collection in JSON |

## Change without losing the thread

Project IDs and supplied titles are stable. Directory names are presentation paths; [project_paths.json](project_paths.json) connects them to the scientific record. Regenerate documents through the [build tools](../tools/README.md) after changing canonical content, then inspect the [coverage and integrity evidence](../evidence/README.md).

Requirements and verification tables describe specified work. Their row counts are documentation metadata; case closure requires executed evidence. Public dataset provenance and scientific outputs remain beside their files in [models/data](../models/data/), while the [data gallery](../data/README.md) exposes them for browsing.

[Ordered document register](../ENGINEERING_DOCUMENTATION.md) · [Data gallery](../data/README.md) · [Repository home](../README.md)
