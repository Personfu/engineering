# Visual and layout revision · 3

**Historical assembly record:** this describes the visual revision at commit `0094c824a753906e8ad1d5733425378e58851489`. The [detailed mission-profile revision](MISSION_PROFILE_VERIFICATION.md) adds later presentation layers and qualifies catalog-selection wording; its current checks supersede this earlier presentation snapshot. Original scientific input bytes remain preserved.

[Evidence library](README.md) · [Data atlas](../data/README.md) · [Visual manifest](../assets/visual_design_manifest.json) · [Scientific figure manifest](../data/figures/DATA_FIGURES.json)

This revision organizes all 117 engineering records into named mission folders under `research/`, preserving the exact supplied A–I title order. Each folder contains its engineering record, local data blueprint, downloads and figure gallery. The root and session guides use original navy, teal and copper artwork; these are independent NASA-inspired creative identifiers.

## Added visual evidence

| Artifact | Count | Meaning |
| --- | ---: | --- |
| Hero and session cards | 10 | Document metadata and decorative orbital motifs |
| Project data maps | 117 | All 877 proposed field names, types, units and meanings |
| Additional scientific SVG/PNG pairs | 9 | One real public catalog view and eight synthetic model diagnostics |
| Project-local data galleries | 117 | Proposed contracts, quality rules and acquisition resources |
| Project-local figure galleries | 117 | Captioned architectures, field maps and relevant numerical views |

The original 117 architecture SVGs, original nine numerical views, 40 ATLAS scientific assets and 20 supplementary synthetic datasets are retained. Raw data have one authoritative copy; presentation galleries link directly to it. Proposed acquisition CSVs remain header-only. The 434 specified cases remain planned project work.

## Verification execution

All **59 software and documentation tests passed**:

| Suite | Passed | Scope |
| --- | ---: | --- |
| `evidence/verify_portfolio.py` | 15 | Ordered coverage, content, local links/anchors, field visibility, accessibility, manifests and evidence labels |
| `evidence/verify_data_contracts.py` | 8 | JSON Schema validity and scientific encoding fixtures |
| `models/test_models.py` | 22 | Numerical implementations and limiting cases |
| `archive/astra_forge/tests/` | 14 | Supplementary kernels, inventory and synthetic-asset hashes |

The [independent migration review](visual_revision_verification.json) records byte preservation of the five controlled source files and all 60 original scientific assets, unchanged 117 schema records, exact titles/names/IDs/order and the retained D03 work packages. The original counts remain **527 requirements, 434 specified cases, 877 fields and 250 distinct cited resources**.

The [gallery verification](data_gallery_verification.json) records **238 independent assertions** covering numerical transformations, input/output hashes, image metadata and data-source links. The [source and visual review](data_gallery_source_review.json) checks eight primary-source links and all nine current PNG spreads. The charts expose missing data, balances, saturation, conservation, noise-driven identifiability, hypothetical phase regions, finite escape classification and reference-formula departures; their captions state their scientific limits.

[Documentation regeneration](visual_regeneration_verification.json) left all **1,511 compared repository files byte-identical**, including generated artwork and local galleries. All **467 display-LaTeX blocks** in the records and their handbook copies match the published baseline; [KaTeX 0.19.0 parsed all 467](visual_equation_rendering.json) without errors. Static Markdown previews of the front page, Session B and the data atlas loaded every embedded image. Hero, session cards, field maps and scientific plots were visually inspected for legibility and clipping.

The [Git index byte check](visual_staged_asset_verification.json) verified **439 staged asset files** against their recorded SHA-256 values: original scientific data, new presentation figures, original architecture sources/SVGs and generated document artwork. This checks the bytes that will enter the repository, including line-ending attributes.

## Historical path references

Earlier revision-2 review records are retained as dated evidence. Paths quoted inside their historical command transcripts refer to the layout at execution time. Current locations are `registry/` for former `catalog/`, `engineering/` for former `docs/`, `evidence/` for former `reviews/`, `handbooks/` for former `documentation/`, and `archive/astra_forge/` for the preserved supplementary contribution. Current executable commands are in the [build guide](../tools/README.md).

These checks establish documentation, presentation and software integrity. They do not close project-specific empirical verification or constitute flight, clinical or NASA qualification.
