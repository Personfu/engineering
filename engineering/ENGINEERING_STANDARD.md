# Engineering documentation standard

ATLAS records the supplied 117 projects as engineering research design records, in the exact A–I sequence. Each project has a stable ID, an unchanged original title, a creative NASA-inspired name, a mathematical model, controlled data interfaces and a plan for producing evidence. The nine session handbooks reproduce those records in sequence. The source of a requirement and the evidence that would close it are both visible.

## Document hierarchy and authority

| Level | Controlled artifact | Purpose |
|---|---|---|
| Program | `ENGINEERING_DOCUMENTATION.md` | Complete ordered document register |
| Session | `handbooks/SESSION_A.md` through `SESSION_I.md` | Continuous engineering handbooks |
| Project | `research/<session>/<id-name>/README.md` | Design basis, equations, interfaces, trades and evidence requirements |
| Data | `research/<session>/<id-name>/data/` | Visual field map, dictionary, record schema and empty acquisition template |
| Figures | `research/<session>/<id-name>/figures/`, `data/figures/` | Project galleries and captioned data diagnostics |
| Traceability | `registry/requirements.csv`, `verification_cases.csv` | Requirement and verification inventories across every project |
| Models | `models/` | Executable reduced models, declared parameters, datasets and test results |
| Review | `evidence/` | Coverage, mathematical review, integrity and release records |

An original research title establishes the retained topic, not ownership of the historical researchers' data or conclusions. A primary paper establishes only the claim or method actually supported by that paper. A NASA method informs engineering practice; it does not confer certification on a concept. Proposed requirements and budgets remain distinguishable from externally imposed interface or qualification requirements.

The documentation structure draws on the [NASA requirements-verification matrix guidance](https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/), [interface document outline](https://www.nasa.gov/reference/appendix-l-interface-requirements-document-outline/), and [verification and validation plan outline](https://www.nasa.gov/reference/appendix-i-verification-and-validation-plan-outline/). These references support the organization of evidence, rather than project-specific performance claims.

## Required content of a design record

1. **Design basis:** intended physical or statistical decision, system boundary, supplied inputs, exclusions and fidelity ladder.
2. **Requirements:** measurable statements or gated prerequisites, rationale, source or proposed status, and a verification method.
3. **Architecture:** components and typed interfaces; time, units, frame, calibration and covariance conventions.
4. **Model:** governing equations, derivation to observables, assumptions, initial/boundary conditions and validity domain.
5. **Data contract:** fields, types, units, missingness, qualifiers, product/version identifiers, sampling and selection rules.
6. **Uncertainty:** measurement, parameter, numerical and model-discrepancy contributions; identifiable versus unconstrained quantities.
7. **Trade study:** realistic alternatives, costs and limits, and an evidence-based decision rule.
8. **Verification/validation:** explicit stimuli, expected limits or criteria, method and evidence artifact.
9. **Implementation:** concrete artifacts and dependencies, reproducibility, resource/discipline interfaces and staged execution.
10. **Failure analysis:** effects, observable detection and design response; avoid unsupported numerical risk rankings.
11. **Outputs and sources:** engineering deliverables, planned scientific figures and precise primary references.

## Model credibility and intended use

[NASA-STD-7009B](https://standards.nasa.gov/standard/nasa/nasa-std-7009) is the current NASA models-and-simulations standard identified during this revision. It emphasizes credibility across development and use, with acceptance criteria set for a program's intended application. ATLAS uses that principle to require a declared decision, validity envelope and evidence state for every model. It does not claim formal compliance with NASA technical-authority approval processes.

Verification establishes whether the equations or implementation were solved correctly. Validation establishes whether the model represents the relevant physical or social system for the stated use. A mesh-convergence result can establish a numerical property without establishing that a material model, observing selection function or stakeholder decision is valid. A held-out prediction can still fail outside the data's environmental, instrumental or population range.

## Review and closure rules

| Review | Minimum evidence | Examples of unresolved blockers |
|---|---|---|
| Definition review | User/research decision, requirements, system boundary, parameter provenance | Undefined target observable; unrelated archive substituted for target data |
| Model review | Equations, dimensions, conventions, limiting cases, validity conditions | Unidentifiable parameters; conservation/sign error; unmodeled platform geometry |
| Preliminary design review | Interface definitions, calibration approach, realistic trades and uncertainty allocation | Missing deployer ICD/load envelope; sensor cannot resolve the stated quantity |
| Test-readiness review | Versioned article/model, frozen criteria, inputs, calibration and anomaly procedure | Unknown instrument response; training/test leakage; insufficient independent units |
| Acceptance review | Actual results, residuals, uncertainty, anomalies, requirement disposition and independent assessment | Proposed tests mistaken for results; failed gate hidden by aggregate accuracy |

These are proposed review gates for this research program, not a declaration that any gate has been passed. “TBD” must have an owner, resolution evidence and consequence for the next decision; it cannot silently become a favorable nominal value.

## Evidence states

Use the following states in results and engineering decisions: **specified**, **derived analytically**, **implemented**, **numerically checked**, **correlated to calibration data**, **validated on independent evidence**, and **qualified for a stated environment**. Record the particular model version, dataset and use case behind a state. The supplied source data, eight executable demonstrations and unexecuted project-specific verification cases occupy different states.

Architecture drawings describe analysis dependencies or design interfaces. They are not photographs of built systems, approved manufacturing drawings or empirical causal results. Future manufactured articles need controlled material, tolerance, fastener, load, electrical and environmental definitions appropriate to their particular application.
