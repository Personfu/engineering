# ATLAS · Applied Terrestrial & Lunar/Astrophysical Studies

A mission-inspired research portfolio preserving all **117 listed projects** across nine sessions. The combined D03 entry retains **two distinct research concepts**, so no idea is dropped.

Start with the [interactive explorer](web/atlas.html), [full project index](catalog/PROJECTS.md), [model assurance plan](docs/MODEL_ASSURANCE.md), or [executable demonstrations](models/README.md). The explorer runs locally in a browser without a server or remote libraries. Download the repository, then open `web/atlas.html`; GitHub renders its source.

The dossiers are proposed extensions of the supplied concepts, with primary-source models and archive discovery links. They contain no fabricated experiments, clinical claims, flight qualification, funding commitments or NASA endorsement. Numerical demonstrations identify synthetic data explicitly; the separately acquired exoplanet sample includes retrieval provenance.

## Collections

| Session | Field | Projects |
|---|---|---:|
| [A](projects/A/README.md) | Math, Physics & Chemistry | 12 |
| [B](projects/B/README.md) | Earth & Environmental Engineering | 28 |
| [C](projects/C/README.md) | Astronomy & Space Physics | 30 |
| [D](projects/D/README.md) | Aeronautics | 7 |
| [E](projects/E/README.md) | ASCEND | 8 |
| [F](projects/F/README.md) | Education & Public Outreach | 2 |
| [G](projects/G/README.md) | Exploration Systems Engineering | 8 |
| [H](projects/H/README.md) | Planetary Science | 9 |
| [I](projects/I/README.md) | Aerospace Technology | 13 |

## Research-to-evidence workflow

1. Choose a dossier and freeze its hypothesis, inputs and acceptance gates.
2. Acquire product-level data with access, version, units, calibration and selection metadata.
3. Execute the stated model; assess identifiability and compare independent baselines.
4. Report uncertainties, failure cases and inconclusive outcomes alongside figures.

NASA systems-engineering practices inform requirements and review design through the [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/). A handbook citation does not certify these concepts.

Source-title provenance: the supplied projects match the [2021 Arizona Space Grant symposium program](https://spacegrant.arizona.edu/sites/spacegrant.arizona.edu/files/AZSGC%20Symposium%20Booklet%202021_website.pdf). These are new proposals, not a reproduction of that program’s abstracts or claims of authorship of the historical research.

## Verification and maintenance

[Release verification](reviews/RELEASE_VERIFICATION.md) records 30 passing automated checks, scientific review corrections, browser checks and evidence limits. Run `python reviews/verify_portfolio.py` for catalog checks and the commands in `models/README.md` for numerical checks. After editing `catalog/projects.json`, run `python tools/render_explorer.py` to update the offline explorer; dossier Markdown and concept figures require corresponding edits. The local KaTeX renderer and its license are included under `web/vendor/`.
