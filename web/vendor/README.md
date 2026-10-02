# Third-party math renderer

KaTeX **0.19.0** renders the LaTeX equations locally. The plain-text equations remain available if a renderer cannot load. No remote assets are required.

- Source: [official v0.19.0 release](https://github.com/KaTeX/KaTeX/releases/tag/v0.19.0), acquired 2026-10-02.
- Files: `katex.min.js`, `katex.min.css`, bundled fonts, and upstream `LICENSE`.
- License: MIT; preserve the included copyright notice. Font notices are included in the upstream license.
- Integration: [official browser documentation](https://katex.org/docs/browser.html). Rendering uses `trust:false`, MathML plus visual HTML, and falls back to readable source on parse failure.

The mathematical review applies to dossier equations. KaTeX rendering is a presentation check and does not validate their scientific assumptions.
