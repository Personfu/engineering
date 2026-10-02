> Preserved ASTRA FORGE revision from commit 4026dd0. The [current ordered engineering records](../../../ENGINEERING_DOCUMENTATION.md) are the controlled A-I documentation. This earlier revision uses separate D03/D04 IDs for the two combined-title work packages; its D05-D08 map to current D04-D07.

# ASTRA FORGE engineering standard

This repository is an independent FLLC research and education portfolio. Space-inspired project names are proposed names, not official mission designations. No NASA endorsement, affiliation, certification, flight qualification or achieved research result is implied. Original student projects remain credited through the [2021 Arizona NASA Space Grant program](https://spacegrant.arizona.edu/symposium/archive/2021). The repository does not replace their authors' work.

## A research dossier has six distinct evidence layers

| Layer | Required meaning | Current release |
|---|---|---|
| Historical provenance | Original title and source locator | All 118 titles preserved; program locators recorded |
| Published finding | Specific paper/measurement, date and uncertainty | No original abstract result represented as a repository achievement |
| Proposed research model | Question, equations, assumptions and validation experiment | Specified for every project; some projects appropriately use evidence/decision models |
| Executable reference | Bounded educational implementation with known analytic checks | 20 shared kernels; individual projects expose relevant kernels only |
| Measurement | Raw file, archive identifier, calibration, units and permissions | None ingested; data plans and manifests supplied |
| Operational system | Validated deployment, hardware interfaces, authorized procedures | Not implemented or claimed |

Formal specifications are **not** full validated scientific solvers. A shared educational kernel demonstrates a narrow mathematical mechanism; it cannot stand in for an interacting many-body solver, calibrated instrument pipeline, CFD calculation, flight controller, clinical model or CR3BP optimizer. Each project lists that gap openly. NASA-style quality here means traceability and verification discipline, not a certification claim.

## Model formulation and reproducibility

Write the state vector, input vector, observation operator and parameter vector before coding: `dx/dt=f(x,u,theta)` and `y=h(x,theta)+epsilon`. Declare every coordinate frame, time scale, boundary condition, initial condition, dimensional unit and numerical tolerance. Discrete models document update ordering, graph topology and random seed. Statistical models distinguish likelihood, priors, missingness and selection mechanism.

The model contract must contain an equation-source citation. Current project equations are proposed standard reference formulations, not transcriptions of the 2021 abstracts. Agency/archive landing pages are **discovery resources**, not validation of those equations. Before promoting a model to research grade, select and cite the specific textbook, technical report or primary paper and record its section/equation, applicable conditions and differences from the implementation. This release does not fabricate that missing review.

| Quantity | Rule | Frequent failure |
|---|---|---|
| Time | UTC observation/retrieval timestamps; explicit TT/TDB for ephemerides | Comparing spacecraft and telescope clocks without offsets |
| Geometry | Frame, origin, handedness, datum and distance unit | Mixing barycentric and observer-centric states |
| Temperature | Kelvin in thermodynamics/radiation; Celsius only where formula explicitly expects it | Applying `T^4` to Celsius |
| Spectra | Rest wavelength, vacuum/air convention, resolution, spectral units | Claiming line shift from mismatched wavelength frames |
| Radiation | Count, live time and detector response separate | Reporting count rate as dose or incident energy |
| Environmental chemistry | Concentration units, phase, analytical method, censoring and blanks | Replacing below-detection measurements with zero |
| Statistics | Sampling unit and independent replicate count explicit | Treating pixels, seeds or time samples as independent experiments |
| Remote sensing | Product scale factors, QA flags, resolution and observation geometry | Treating greenness as a direct biodiversity measurement |

Each run receipt records code revision, configuration hash, input SHA-256, input evidence class, seed, runtime, output hash, checks and limitations. Never put secrets, exact protected-species positions, human identifiers or spacecraft credentials in a run receipt.

## Uncertainty is part of the output

Separate measurement, calibration, numerical, model, sampling and decision uncertainty. Linear propagation uses `Cov(y)=J Cov(x) J^T`; Monte Carlo draws respect covariance and physical bounds. Bootstrap at the independent sampling level: host star, watershed, site, subject, exposure group or simulation family. Do not bootstrap highly correlated pixels or times as if independent. An uncertainty band from one model cannot stand in for disagreement among models.

Sensitivity analysis changes physically justified parameters over sourced ranges; invented demonstration ranges are labeled synthetic. Pre-register primary outcomes and comparisons. Correct for multiple testing where applicable. Report negative results and withheld data coverage. Explain what evidence would falsify the model.

## Verification and validation gates

1. **Scope review:** preserve original identity; separate historical project, FLLC proposal and present-day science. Establish dataset permissions and an actual scientific question.
2. **Model review:** select equation-level primary references, units and assumptions. List unconstrained parameters and degenerate explanations.
3. **Software verification:** analytic limits, conservation, deterministic seeds, numerical convergence, failure handling and bounded input validation.
4. **Data qualification:** raw-file checksum, calibration versions, missingness, detection limits, coverage and independent review.
5. **Scientific validation:** withheld observations or independent experiment; simulator-family and geographic holdouts when relevant. Compare simpler baselines at the same domain and false-alarm rate.
6. **Result review:** publish uncertainty, model discrepancy, reproducible receipt and limitations. Hardware/clinical/flight conclusions require their own independent qualified review.

## Shared model architecture

| Domain | Full research-model architecture | Reference limitation |
|---|---|---|
| Fractals | Arbitrary precision, interval certification, adaptive tiling, alternate method benchmark | Finite escape-time render |
| Phase behavior | Gibbs minimization, phase stability, nonideal activity, pressure dependence | Ideal binary liquidus with invented values |
| Quantum matter | Interacting Hamiltonian, many-body convergence, pairing and EOS comparison | Specification only |
| Astrophysical populations | Measurement likelihood, catalog identity, selection function and denominator | Specification only; no survey sample |
| Spectroscopy | Calibration, continuum, line-spread function, physical forward model and covariances | Gaussian synthetic line / invented mixture |
| Imaging | PSF, throughput, correlated detector noise, masks and injection/recovery | Synthetic Gaussian scene / scalar correction |
| Geospatial ecology | Spatial sampling, effort/detection, resistance/movement, governance | Specification only; no animal coordinates |
| Hydrology | Water/energy balance, retention, flow/routing, boundaries and decision loss | Analytic retention curve only |
| Fluids | Navier-Stokes, turbulence/transition choice, mesh/time/domain convergence | Empirical sphere correlation only |
| Mechanical structures | Geometry, materials, loads, stiffness/mass matrices, contacts and modal validation | Cantilever and single-stage isolation |
| Space plasma | Instrument response, frame changes, distribution-function fitting and event qualification | Mathematical relationships in dossier only |
| Orbital dynamics | Ephemeris/frame/time alignment, force model, encounter covariance and CR3BP constraints | Nondimensional two-body orbit only |
| Attitude control | Coupled quaternion/inertia dynamics, actuators, sensors, estimation and contingencies | Single-axis spherical inertia |
| Thermal/power | Multi-node conduction/radiation/convection, calibrated environment and loads | Constant-boundary one-node / ideal clipped storage |
| Bioscience | Existing-public-data evidence synthesis, statistical confounding and accession audit | No biological experiment or intervention |
| Command/defensive systems | Authorized requirements, offline simulation, access/replay checks and human review | Architecture only; no live hardware/network action |

## Product boundaries and integration record

GitHub: used to inspect and deliver this repository. Google Drive: searched and read the Phoenix College Spring 2025 deck; sharing unchanged, private media not copied. Web research: used to inspect the symposium provenance and official archive/reference pages; source registry records blocked reads accurately. Python: used for deterministic reference calculations, data manifests, SVGs, coverage checks and atlas generation.

Supabase, Vercel, Stripe, Runway, Notion, Discord, SOFA, Ads Manager, Shopify, Malwarebytes and Cloudflare: **not used in this release**. No production website, advertisement, payment, automated mission, deployment or external notification is included.

The original 118 projects remain independent records. Cross-project connections are research dependencies, not permission to collapse projects or invent shared experimental results.
