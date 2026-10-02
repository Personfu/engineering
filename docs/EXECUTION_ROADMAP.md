# ATLAS engineering execution roadmap

The program baseline contains all 117 original projects in the supplied A–I order. The [document register](../ENGINEERING_DOCUMENTATION.md) is the work-breakdown register: A01–A12, B01–B28, C01–C30, D01–D07, E01–E08, F01–F02, G01–G08, H01–H09 and I01–I13. D03 contains both retained investigations. Dependencies may affect execution timing; they do not remove or reorder the baseline documentation.

## Review gates for every project

| Gate | Required artifacts | Decision and closure evidence |
| --- | --- | --- |
| Concept and scope review | Original-title trace, question, observable, intended decision, model boundary, stakeholder/context record | Owner and reviewer agree what the investigation can establish; incompatible interpretations are recorded. |
| Requirements review | Project R-series requirements, controlling sources, measurable acceptance rules, TBD register | Every requirement has a verification method and evidence owner. Proposed targets are distinguished from externally controlling limits. |
| Preliminary analysis review | Governing equations, derivation, dimensions, conservation/limiting cases, trade table, parameter sources | An independent reviewer can reconstruct the baseline; parameter degeneracies and fidelity limits are visible. |
| Data and interface review | Versioned schema, populated provenance sidecar, exact archive/product selection, frames, clocks, calibration, quality flags, rights | Domain checks supplement structural JSON validation. Unknowns remain qualified; the review rejects fabricated or unsupported values. |
| Implementation readiness | Frozen code/environment, baseline inputs, specified case fixtures, numerical refinement plan, resource/access evidence | Reproduction succeeds on a second environment or documented replay; failure handling and stop conditions are testable. |
| Verification review | Versioned outputs for each V-series case, independent reference values, uncertainty, exceptions | Cases have pass/fail/inconclusive rationale. A software pass does not establish empirical model validity. |
| Validation and decision review | Withheld observations or approved independent evidence, discrepancy, sensitivity, identifiability, risk and decision margin | The claim remains inside the supported domain. Unsupported parameter estimates or insufficient margins are reported as unresolved. |
| Release and archive | Final methods, figures, input/output hashes, source versions, requirement closure matrix, reviewer record, communication artifact | Another analyst can replay the claim and inspect negative or inconclusive evidence. |

These gates adapt the [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [requirements verification matrix](https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/), [V&V plan outline](https://www.nasa.gov/reference/appendix-i-verification-and-validation-plan-outline/) and [NASA-STD-7009 model credibility framework](https://standards.nasa.gov/standard/nasa/nasa-std-7009). They are a program procedure, not a declaration that NASA reviews have occurred.

## Session execution register

| Order | Session and complete work packages | Shared capabilities and interfaces | Principal evidence closure |
| --- | --- | --- | --- |
| 1 | [A01–A12: Math, Physics & Chemistry](../documentation/SESSION_A.md) | Numerical precision, thermodynamics, spectroscopy, statistical/compositional inference and instrument response | Limiting cases, measured/reference parameters, recovery and selection accounting, identifiability and independent spectra/observations |
| 2 | [B01–B28: Earth & Environmental Engineering](../documentation/SESSION_B.md) | GIS/remote sensing, field/archive provenance, hydrology/transport, ecology, chemistry and energy accounting | Spatial/temporal support, confounding and coverage, independent reference observations, community data authority and conservation |
| 3 | [C01–C30: Astronomy & Space Physics](../documentation/SESSION_C.md) | Time/frames, calibrated images/spectra, likelihoods, selection functions, plasma measurements and gravitational-wave inference | Archive product and calibration versions, injections/held-out families, foreground degeneracy, instrumental transfer and physical interpretation |
| 4 | [D01–D07: Aeronautics](../documentation/SESSION_D.md) | Nondimensional fluid mechanics, CFD refinement, aerodynamic dynamics, instrument calibration and defensive information governance | Independent references, mesh/time-step sensitivity, hysteresis/support, facility envelopes and surrogate/model limits |
| 5 | [E01–E08: ASCEND](../documentation/SESSION_E.md) | Payload timing, environment/thermal interfaces, radiation metrology, structure and isolated EPS verification | Sensor calibration, clock/position alignment, thermal correlation, interface fit, electrical accounting and configuration evidence |
| 6 | [F01–F02: Education & Public Outreach](../documentation/SESSION_F.md) | Accessible communication, source/claim ledgers, evaluation design and participant governance | Comprehension/calibration measures, valid comparison units, accessible artifacts, uncertainty comprehension and approved evaluation scope |
| 7 | [G01–G08: Exploration Systems Engineering](../documentation/SESSION_G.md) | Metrology, adaptive estimation, antennas, materials/transport, mechanical alignment and biomedical evidence appraisal | Sensor/response uncertainty, controls and blanks, material/model validity, interface closure and appropriately limited biological interpretation |
| 8 | [H01–H09: Planetary Science](../documentation/SESSION_H.md) | Exhibit source records, camera calibration, geophysics, mineral/spectral analysis and geologic mapping | Provenance and calibration, nonunique inverse solutions, geomorphic context, resolution/selection support and independent reference products |
| 9 | [I01–I13: Aerospace Technology](../documentation/SESSION_I.md) | Externally specified thermal/structural loads, avionics, inert simulators, ephemerides, attitude and passive orbital analysis | Conservation, solver refinement, timing/state invariants, requirement margins and surrogate/domain boundaries |

## Resource planning and critical dependencies

Each project's implementation section supplies six concrete work packages plus its original investigation sequence. For each package create a resource record with owner, relevant specialty, analyst/reviewer hours, compute and storage, instrument or archive access, calibration/reference materials, interfaces, predecessor artifacts, uncertainty in effort and the quoted basis of any cost. A missing quote or facility envelope remains TBD. This release does not invent a schedule, budget, laboratory access or original-team dataset.

Reusable services can share infrastructure: clock/frame transforms; data validation and provenance; calibration/response libraries; spatial and spectral covariance; numerical conservation/refinement checks; selection-aware validation; versioned figures and requirements closure. Shared service outputs remain project-specific at their interfaces. A calibration or model validated for one detector, sensor, environment or population cannot be transferred without a recorded compatibility analysis.

For mechanical handoff, issue a parameter table, units, origin and axes, contact/interface definitions, keep-outs, material sources, tolerances, load cases, boundary conditions, mesh assumptions and correlation plan before accepting a CAD or finite-element result. E05, G07, I06 and I09 identify applicable design workflows. The current release includes mathematical design records and editable engineering diagrams; native Fusion models and hardware qualification require separately recorded execution evidence.

## Program status

All 117 design records and their data/verification specifications are documented. The [requirements register](../catalog/requirements.csv) and [case register](../catalog/verification_cases.csv) preserve evidence-pending status. Completed software and document checks appear in [release verification](../reviews/RELEASE_VERIFICATION.md). Future execution closes evidence against the corresponding project IDs, rather than silently replacing a proposal with an unsupported success claim.
