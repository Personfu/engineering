# Engineering documentation build

The controlled sources are [projects.json](../registry/projects.json) (original titles, order, names, governing models and resources) and [engineering_annexes.json](../registry/engineering_annexes.json) (requirements, detailed derivations, interfaces, data fields, uncertainty, trades, specified cases, implementation and architecture). Preserve stable project IDs and exact original-title strings.

Run from the repository root:

```sh
python tools/build_engineering_documentation.py
python evidence/verify_portfolio.py
python -m pip install -r tools/requirements-dev.txt
python evidence/verify_data_contracts.py
```

The builder asserts all 117 original titles and their exact A–I order before generating named mission folders, project/data/figure READMEs, nine continuous handbooks, session galleries, registers, diagram sources and empty data contracts. It also regenerates the original hero, session cards and complete field maps using the Python standard library. CSV templates contain only headers; the builder never acquires or invents project measurements. Review changes to scientific source records before accepting regenerated documentation.

## Visual design and data diagnostics

The visual design generator reads the controlled registry and produces 127 accessible SVGs with exact metadata and field definitions. Its manifest records inputs, outputs, palette and evidence labels:

```sh
python tools/build_visual_design.py --repo . --out assets --co-locate
```

The richer profile generator adds 117 source-bound mission profiles and the portfolio mission-control dashboard. It wraps the full scientific question, hypothesis, model framing and traceability content without inventing measurements or readiness scores:

```sh
python tools/build_mission_profiles.py --repo .
python tools/build_data_inventory.py
```

The table inventory reads all 12 original CSVs and their recorded provenance. It exposes headers, units and their sources, missing/non-finite values, finite ranges, full-precision raw preview rows, parameters and linked plots in JSON and a readable notebook. Unknown units remain explicit. Both generators use the Python standard library and are called by the documentation builder. Profile generation runs after final register generation so its input hashes cover the exact source revision.

The builder also writes the mission-control portal and a transparent resource-connection register. Rankings use actual shared citations, supplied sessions and shared included illustrations. Reading connections are separate from physical dependencies or validation.

The [data diagnostic gallery](../data/figures/README.md) adds nine scientific figure pairs from the existing, immutable model CSVs. Regeneration requires the model plotting dependencies:

```sh
python -m pip install -r models/requirements.txt
python tools/render_data_figures.py
```

The renderer records source hashes, captions, assumptions and derived summaries. Inspect changed plots and provenance before committing regenerated outputs. Plot appearance can vary with plotting-library versions; the checked-in files and hashes identify the reviewed revision.

## Editable technical diagrams

All 117 diagrams have Mermaid source and checked-in SVG. SVGs render as ordinary figures in the project records and handbooks. To regenerate them using [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli), install the local tools and run:

```sh
cd tools
npm install
cd ..
python tools/render_engineering_diagrams.py
```

Node.js and the CLI's supported headless renderer are required only to regenerate figures. `--cli` accepts an alternative path to the CLI's `src/cli.js`, and `--workers` sets rendering concurrency. The renderer adds accessible titles/descriptions and records source/output hashes. The checked-in files require no rendering software to read. Architecture figures describe modeled interfaces and evidence flow, not empirical results or manufacturing drawings.

## Numerical demonstrations

Follow [models/README.md](../models/README.md) for the separate model environment, the 22 numerical tests, generation, manifest and optional archive refresh. Documentation regeneration does not alter numerical data or figures. Changing a numerical parameter or dependency requires renewed numerical verification and an updated asset manifest; the preserved two-run regeneration evidence identifies its tested environment.
