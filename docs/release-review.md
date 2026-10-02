# Release review · 2026-10-02

## Delivered and checked

118 original projects across A=12, B=28, C=30, D=8, E=8, F=2, G=8, H=9, I=13. All titles survive exactly in the authored TSV, compiled catalog, individual dossier and interactive explorer. There are 118 unique proposed names and 118 individual concept SVGs. No project was merged away.

20 deterministic educational reference kernels, 20 synthetic datasets and 20 original reference SVGs. Dataset SHA-256 and row/column manifests are checked. Reference code uses Python's standard library and writes only an explicitly selected local output.

13 Python tests cover escape-time cases, phase pure-component limit, two-body orbit conservation and convergence, exact thermal decay, drag correlation domain, consensus conservation, attitude normalization/settling, adaptive cancellation fidelity, finite deterministic outputs, complete project inventory, dossier/source/dependency/SVG integrity, synthetic checksum manifests and truthful data state.

JavaScript syntax and offline interaction checks passed. The interaction harness exercises all 118 records, search, session filtering, project selection, saved records, two-project comparison, eight laboratory views and 51 source records. It uses a minimal DOM/canvas harness and **does not verify browser rendering**.

## Material limitations

- No browser executable is installed in the workspace; Playwright launch failed before rendering. Desktop/mobile visual layout, touch behavior, CSP behavior and assistive-technology interaction still need a real browser review. Responsive CSS, keyboard controls, textual data samples and reduced-motion support are implemented but not claimed as browser-tested.
- No science measurements or mission imagery were downloaded. All bundled numerical outputs are synthetic. No source portal inspection is represented as actual data use.
- Project-specific full scientific solvers and independent validation remain pending. The formal models are proposed architectures; reference kernels cover bounded mechanisms only.
- Equation-level primary bibliography and instrument-specific calibration review remain project research gates. General archive/agency links are clearly marked discovery resources.
- Blocked or metadata-only source reads are recorded as such; no availability, licensing or specific dataset accession is invented.
- No live spacecraft commands, biological procedures, third-party cyber tests, clinical recommendations, production deployment or NASA certification is included.

## Reproducibility

Run `python scripts/build.py`, `python -m unittest discover -s tests -v`, `node --check atlas/app.js`, and `node tests/test_atlas.cjs`. The generator deterministically rebuilds checked-in dossiers, catalogs, synthetic data, checksums and SVGs from the authored TSVs and reference code. GitHub Actions executes the same checks and rejects generated-file drift. Remote CI status is reported separately from local test results.
