# ATLAS release verification

Reviewed on 2026-10-02. This records completed checks of this repository snapshot, not validation of future experiments.

| Check | Result |
|---|---|
| Exact input-title coverage | All 117 listed entries; A12, B28, C30, D7, E8, F2, G8, H9, I13 |
| Combined entry D03 | Both autorotation and laminar-separation-bubble work packages retained |
| Creative names | 117 unique mission-inspired identities |
| Model and data specifications | Required model, units, assumptions, limitations, data-access and validation fields present |
| Citations | 279 dossier citation instances; 240 distinct source URLs |
| Visuals | 117 conceptual SVGs; 9 scientific figures in SVG and PNG; additional editable Mermaid specifications |
| Numerical tests | 22 passed; analytical limits, conservation, convergence, identifiability and domain rejection |
| Portfolio checks | 8 passed; coverage, uniqueness, schema, source protocols, internal links, diagrams, D03 and offline explorer |
| LaTeX rendering | 167 equations parsed successfully with KaTeX 0.19.0 |
| Included public catalog | 200 NASA Exoplanet Archive rows; query, retrieval time and SHA-256 provenance checked |
| Asset integrity | Saved manifest hashes verified; 36 synthetic assets regenerated identically in the recorded runtime by the numerical reviewer |
| Browser checks | Search, selection, hash link, session count, empty results, D03 packages and local equation rendering verified |
| Responsive layout | No document overflow at measured CSS widths 375, 972 and 1265 pixels; temporary overrides reset |
| Content review | All dossiers inspected by a separate agent; 13 identified mathematical/definition issues corrected and reread |

Details: [coverage audit](coverage_audit.json), [independent review](INDEPENDENT_CONTENT_REVIEW.md), [portfolio test output](portfolio_test_results.txt), [math audit](math_render_audit.json), [numerical regeneration record](numerical_regeneration_verification.json), and [current asset verification](../models/verification.json).

The current asset-verification run checked saved files without regenerating them, so its reproducibility field is `null`; the separately preserved numerical regeneration record contains the successful two-run comparison. Reproducibility is conditional on the recorded dependency versions and rendering platform.

Seven specialist/review agents contributed across successive waves, plus the primary assembly author. The environment permits four concurrent agents; hundreds were not available. Automated checks and agent review do not substitute for domain-expert peer review, institutional approvals, calibrated experiments, clinical evidence, or flight qualification.
