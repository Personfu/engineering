# ATLAS model assurance and review plan

These are research proposals, with reduced numerical examples where explicitly supplied. NASA-inspired names and systems-engineering practices communicate intent; they do not establish NASA sponsorship, qualification or certification. The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) provides process context. Requirements below are proposed portfolio controls.

## Evidence states

| State | What it establishes | What it does not establish |
|---|---|---|
| Cited model or reference | An external scientific basis or resource exists | Validity for a new parameter range |
| Conceptual diagram | A proposed dependency or inference path | Measured causation or performance |
| Reduced-model calculation | Behavior of stated equations and parameters | Experimental realism or flight readiness |
| Acquired archive sample | A specific query returned recorded observations | Completeness, representativeness or original team data |
| Verification test | A limiting case, conservation law or convergence check passed | Validation against an independent physical system |
| Prospective validation gate | A measurable criterion has been proposed | That the criterion was achieved |

All 117 dossiers begin in the proposal state. No TRL is assigned without traceable demonstrations and environment-specific evidence. A proposed threshold is not a sourced requirement.

## Review gates

1. **Concept review:** retain the original scientific objective, define scope, users and observable outcomes. Identify broad titles and unsupported assumptions. D03 keeps both autorotation and laminar-separation-bubble investigations.
2. **Requirements review:** define quantities, units, frames, clocks, limits, controls and success/failure/inconclusive outcomes. Identify the authority for each externally imposed requirement.
3. **Model review:** document governing equations, discretization, parameter sources, boundary/initial conditions, domain and excluded physics. Test identifiability before optimizing. A precise fit can remain nonunique.
4. **Data readiness review:** verify actual product IDs, access rights, calibration, licenses, selection function, consent and sufficient independent units. A source portal alone does not retire this gate.
5. **Verification review:** check analytic limits, numerical convergence, conservation and implementation provenance. Use independent code or calculations for material results.
6. **Validation review:** compare against withheld observations or independent instruments, report residual structure and uncertainty coverage. Do not calibrate and validate on the same events, objects, sites or teams.
7. **Release review:** retain negative results, limitations and reproducibility instructions. Link claims to supporting sources and underlying data. Have a qualified domain reviewer assess material conclusions.

The [GEVS standard](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000) is a reference for environmental verification; actual tests must be tailored to the controlling mission requirements and hardware. This portfolio supplies neither approved launch loads nor launch-provider interface control documents.

## Uncertainty and inference

For a measurement-derived quantity y=f(x), use first-order covariance propagation only where linearization is justified: Cov(y) approximately J Cov(x) J^T, with J=df/dx. Use simulation or posterior propagation for nonlinear/censored/multimodal cases. Include correlation between observations and shared calibration errors. Do not add systematic errors as though they were independent random scatter.

For inverse problems, write the forward model and likelihood explicitly: p(theta|d) proportional to p(d|theta)p(theta). Check prior sensitivity, parameter degeneracy and posterior predictive residuals. A posterior narrower than justified by model discrepancy is overconfident. Profile likelihood or posterior intervals describe conditional uncertainty, not proof of the model.

Machine-learning projects require independent splits at the scientific unit: star, flight, storm, image field, catchment, organism, crew or simulation family. Folds that contain adjacent pixels or time windows from the same event can leak information. Freeze final evaluation data and preprocessing before confirmatory comparison. Compare to physically interpretable baselines at matched compute/data budgets.

## Biomedical, biological and operational scope

Biomedical dossiers are analytical research designs with supervised measurement and ethics pathways; they are not clinical advice or validated implants/therapies. Pathogen-related entries remain intact as retrospective data and non-operational characterization proposals. No pathogen cultivation, resistance selection, genetic manipulation or therapeutic intervention protocol is supplied.

Aviation-ISAC and mission-control work addresses defensive governance, isolated simulation, telemetry integrity and authorized operations. The portfolio does not connect to a spacecraft or issue operational commands. Propulsion dossiers study normalized thermal/material integrity; they supply no engine shutdown sequence or flight-hardware operating recipe.

## Scientific corrections that affect interpretation

- SPHEREx’s historical title is preserved while its dossier uses checked active-mission/archive context.
- Candidate magnetar evidence does not uniquely establish a magnetar in a binary.
- CMOS deposited energy does not uniquely identify incident particle energy.
- Tracer velocity dispersion is not directly the dark-matter velocity distribution.
- Gravitational-wave memory continuation must preserve its persistent offset; convenient tapering can change the physics.
- Ground riometer geometry must be confirmed before calling data space based.
- Elemental aluminum recovery cannot establish rare-earth yttrium recovery.
- Tribal climate support remains community-governed Earth climate work despite the supplied Session H placement.
- NASA’s [Apophis assessment](https://science.nasa.gov/solar-system/asteroids/apophis-facts/) rules out an impact for at least 100 years. I13 is a hypothetical sensitivity study, not a response to a known impact threat.

## Review artifact

For each executed project, record: requirement ID, model/data revision, reviewer, comparison case, numerical tolerance, observed residual, uncertainty, pass/fail/indeterminate status, and rationale. This repository’s coverage audit checks document completeness. It does not certify scientific truth.
