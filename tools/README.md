# Engineering documentation build

The controlled sources are [projects.json](../catalog/projects.json) (original titles, order, names, governing models and resources) and [engineering_annexes.json](../catalog/engineering_annexes.json) (requirements, detailed derivations, interfaces, data fields, uncertainty, trades, specified cases, implementation and architecture). Preserve stable project IDs and exact original-title strings.

Run from the repository root:

```sh
python tools/build_engineering_documentation.py
python reviews/verify_portfolio.py
python -m pip install -r tools/requirements-dev.txt
python reviews/verify_data_contracts.py
```

The builder asserts all 117 original titles and their exact A–I order before generating project Markdown, nine combined session handbooks, indices, requirement/case registers, editable diagram sources and empty data contracts. CSV templates contain only headers; the builder never acquires or invents project measurements. Review changes to scientific source records before accepting regenerated documentation.

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
