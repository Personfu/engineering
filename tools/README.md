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
npm ci --ignore-scripts
cd ..
python tests/install-secure-browser.py
python tools/render_engineering_diagrams.py
```

Node.js and the reviewed headless renderer are required only to regenerate figures. `--cli` accepts an alternative path to the CLI's `src/cli.js`, and `--workers` sets rendering concurrency. The renderer adds accessible titles/descriptions and records source/output hashes. The checked-in files require no rendering software to read. Architecture figures describe modeled interfaces and evidence flow, not empirical results or manufacturing drawings.

## Numerical demonstrations

Follow [models/README.md](../models/README.md) for the separate model environment, the 22 numerical tests, generation, manifest and optional archive refresh. Documentation regeneration does not alter numerical data or figures. Changing a numerical parameter or dependency requires renewed numerical verification and an updated asset manifest; the preserved two-run regeneration evidence identifies its tested environment.

## Reviewed browser runtime

Before this patch, the diagram CLI's locked Puppeteer25.12.0 defaulted to Chrome154.0.8037.57,
below the156.0.8078.73 fix for [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306).
Updating the driver alone does not update that browser payload. The renderer now
supplies an explicit, reviewed Chrome for Testing157.0.8103.38 executable to every
Mermaid invocation. It verifies its receipt and executable SHA-256, then launches
an empty browser and checks the actual version before opening any diagram.
Puppeteer's sandbox remains enabled; unavailable or unsupported platforms stop.
The compatible lock refresh also updates Puppeteer to25.16.0, DOMPurify to3.4.17,
lodash-es to4.18.1 and Zod to4.6.7 without dependency overrides.
Even Puppeteer25.16.0 defaults to Chrome156.0.8078.47, still below the fix, per its
[immutable revision source](https://github.com/puppeteer/puppeteer/blob/puppeteer-v25.16.0/packages/puppeteer-core/src/revisions.ts).
The explicit executable gate therefore remains necessary. The job audits all
severities in the optional tools lock, including development dependencies.

The installer downloads only the pinned official HTTPS archive, verifies its exact
size and SHA-256 and rejects unsafe archive paths, symlinks and duplicate entries.
Those hashes identify the retrieved archive; they are not a vendor signature.
Linuxx64 and Windowsx64 pins are in
[chrome-pin.json](../tests/security/chrome-pin.json). Use a fresh checkout for a new
installation; an existing cache is never overwritten automatically. Package
lifecycle scripts are disabled during the strict locked tool install to avoid
fetching Puppeteer's older default browser. No global browser profile changes.

The dedicated Linux job checks the installer boundaries and actual renderer,
regenerates all117 controlled SVGs, and runs their existing provenance and
accessibility checks. Its matching hash-checked setuid sandbox helper is installed
only in a root-protected directory on an unprivileged disposable GitHub runner;
it does not relax host user-namespace policy. This is CI runtime evidence, not an
attestation of another workstation or deployment. Review the pin against the
[current official Chrome for Testing feed](https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json)
and the [locked Puppeteer revision source](https://github.com/puppeteer/puppeteer/blob/puppeteer-v25.12.0/packages/puppeteer-core/src/revisions.ts)
when refreshing it. Scientific source records and checked-in figures remain
unchanged by this security change.

## November 3 browser security release

Reviewed November 4, 2026: [Google's Chrome 157 release](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop.html) lists 213 security fixes, including seven critical issues: CVE-2026-121156, CVE-2026-121229, CVE-2026-121246, CVE-2026-121035, CVE-2026-121247, CVE-2026-121203 and CVE-2026-121126. The reviewed runtime and minimum accepted version are now 157.0.8103.38. The earlier 156.0.8078.73 floor addressed CVE-2026-118306 only; the previously reviewed 156.0.8078.80 pin is no longer sufficient for this release. This does not establish that every fixed issue was exploitable in this harness.

Both supported archives have fresh size/SHA-256 pins; Linux uses the matching helper from the same archive. Boundary tests reject the former pin and 157.0.8103.37, and accept 157.0.8103.38. Archive validation, executable receipts, actual browser-version preflight, sandbox enforcement and all existing application assertions remain required. No package-manager, release-age, host-security or retry policy is relaxed. Running services, previously downloaded caches and published artifacts still require independent rollout evidence.
