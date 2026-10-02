# ASTRA FORGE

**118 connected research projects. Nine disciplines. One evidence-first engineering observatory.**

An independent FLLC research and education portfolio built from all projects in the supplied Sessions A–I list. Every original title remains intact alongside a space-inspired proposed name, scientific question, governing model specification, data plan, validation criteria, original visual architecture, extension and resource citations. Original authorship is linked to the [2021 Arizona NASA Space Grant symposium](https://spacegrant.arizona.edu/symposium/archive/2021).

Start with the [complete project index](docs/project-index.md), [source registry](docs/source-registry.md) and [engineering standard](docs/engineering-standard.md). The [interactive atlas](atlas/index.html) offers search, session/family filters, side-by-side comparison, saved project lists, source states and educational model views.

## What is implemented

- 118 individually specified research dossiers and original conceptual SVGs.
- 20 deterministic Python reference kernels with synthetic data, plots and checksum manifests.
- An offline browser atlas with mathematical visualizations and a rotatable educational CubeSat.
- Requirements, provenance, data qualification, uncertainty and verification standards.
- Automated coverage and numerical checks; a reproducible build.

The full project-specific scientific solvers, measured datasets, equation-level research bibliography review and independent scientific validation are **not complete**. A proposal or educational kernel is not a published finding, validated instrument pipeline or flight/clinical system. No measurements are fabricated. Data resources are labeled as inspected, blocked, metadata-only or reference-only.

| Session | Projects |
|---|---:|
| A · Math, Physics & Chemistry | 12 |
| B · Earth & Environmental Engineering | 28 |
| C · Astronomy & Space Physics | 30 |
| D · Aeronautics | 8 |
| E · ASCEND | 8 |
| F · Education & Public Outreach | 2 |
| G · Exploration Systems Engineering | 8 |
| H · Planetary Science | 9 |
| I · Aerospace Technology | 13 |
| **Total** | **118** |

## Run and reproduce

Python 3.12+; no Python packages, npm installation, API keys or cloud account required.

```bash
python scripts/build.py
python -m unittest discover -s tests -v
node tests/test_atlas.cjs
python -m models.run --model orbit --output /tmp/astra-orbit.json
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/atlas/` or open `atlas/index.html` directly. All catalog content is local. The browser never calls an external API; source links navigate only when selected. Synthetic samples are under `data/synthetic/`; measured-data requirements are in [data-contract.md](docs/data-contract.md).

## Research connections

The imaging projects share calibration and scene-truth concepts; plasma projects share instrument/frame receipts; ASCEND and EagleSat projects share mission evidence schemas; ecological projects share effort-aware observations; orbital projects share coordinate/time contracts. All 118 stay independent. Related-project links identify useful dependencies without merging original work.

## Sources and assets

Google Drive was used to read the Phoenix College Spring 2025 presentation for later mission context; no private measurements or imagery were copied, and sharing is unchanged. Public sources were reviewed as recorded in the registry. All shipped SVGs and educational geometry are original. Source/data licenses remain separate; public availability does not mean unrestricted redistribution.

Space-inspired names are independent educational titles. No NASA endorsement, official mission status, certification, flight qualification or production deployment is implied. See the [integration record](docs/engineering-standard.md#product-boundaries-and-integration-record).

Local numerical and interaction checks passed; actual browser rendering remains unverified. See the [release review](docs/release-review.md) for precise validation scope and remaining research gates.
