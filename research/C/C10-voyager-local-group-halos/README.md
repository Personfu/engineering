# C10 · VOYAGER LOCAL GROUP HALOS

**Original project:** MW-Andromeda Dark Matter Halo Velocity Dispersion Profiles

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C09](../C09-eaglesat-cosmic-pixel/README.md) · [C11 →](../C11-orion-core-inference/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 4 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Infer the gravitational potentials of the Milky Way and Andromeda through matched stellar-tracer models. Measured stellar velocity dispersions are not direct measurements of dark-matter particle velocity dispersions. Use tracer-density and anisotropy assumptions explicitly, separate equilibrium halo stars from tidal debris, and then predict a dark-matter dispersion profile only under an additional distribution-function or Jeans model.

**Question:** Which differences between Milky Way and M31 potential and dispersion profiles survive matched tracer selection, anisotropy uncertainty, and removal of tidal substructure?

**Testable hypothesis:** Jointly modeling halo membership, tracer density, and anisotropy will broaden mass uncertainties but reduce spurious galaxy-to-galaxy differences caused by unmatched stellar populations.

## 1. Design basis and analysis boundary

The halo pipeline fits stellar-tracer phase-space data to a gravitational potential, then optionally predicts dark-matter velocity dispersion under a separate equilibrium model. Stellar density nu_star is never substituted for dark-matter density rho_DM. SPLASH measurements provide M31 tracer context; Milky Way astrometry has different dimensional information and selection, requiring matched comparison rather than a shared raw-dispersion plot.

Begin with spherical Jeans models and separate contamination mixtures, then flexible anisotropy and flattened or disequilibrium stress tests. A dark-matter dispersion is a conditional secondary calculation. Tracer catalog availability, distance calibration and outer-density coverage remain TBD. The comparison domain is chosen where both galaxies have useful tracer constraints; streams and cluster selection are modeled explicitly.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C10-R1 | Stellar and dark-matter dispersion outputs shall have separate density and anisotropy inputs. | They are different dynamical populations. | Type-contract and tracer/DM substitution test. | Existing scientific distinction. |
| C10-R2 | Every likelihood shall forward apply the catalog's distance, velocity and spatial selection. | Selection affects measured radial profiles. | Mock-catalog recovery through selection operator. | Proposed observation requirement. |
| C10-R3 | Jeans integration shall converge to 0.5% in analytic fixtures, a proposed numerical target. | Outer boundaries and singular projections bias profiles. | Grid/tail refinement and analytic comparator. | Proposed solver target. |
| C10-R4 | M31/Milky Way comparisons shall report matched tracer class and radial support. | Projected and 3D data contain unequal information. | Comparison-domain manifest and support audit. | SPLASH provides M31 tracer context. |
| C10-R5 | Mass results shall include anisotropy and substructure sensitivity. | Equilibrium mass is not uniquely measured by dispersion. | Posterior branches and stream-contamination injections. | Proposed robustness requirement. |

## 3. Architecture and controlled interfaces

A Milky Way adapter transforms astrometry and distances with full covariance into a stated Galactocentric frame. An M31 adapter retains projected radii, line-of-sight velocities and foreground membership probabilities. The tracer-density module uses selection-aware spatial data; disk/bulge potentials are separate from the halo family.

A Jeans solver produces stellar radial moments and projects them into each observed data space. Mixture likelihoods retain halo, disk, foreground and debris probabilities. Posterior potential draws feed a second solver using rho_DM and beta_DM, yielding conditional dark-matter predictions. Solar-motion or M31 systemic-velocity uncertainties remain shared terms and propagate through the entire comparison.

![C10 engineering architecture](figures/architecture.svg)

Stellar observations constrain a potential through their own density and anisotropy; dark-matter moments are derived in a separate conditional branch.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\frac{d(\nu_*\sigma_r^2)}{dr}+\frac{2\beta\nu_*\sigma_r^2}{r}=-\nu_*\frac{GM(<r)}{r^2}
$$

$$
\rho_{\rm NFW}(r)=\rho_s/[x(1+x)^2],\quad x=r/r_s
$$

$$
\Sigma(R)\sigma_{\rm los}^2(R)=2\int_R^\infty[1-\beta R^2/r^2]\nu_*\sigma_r^2\frac{r\,dr}{\sqrt{r^2-R^2}}
$$

### Variables, units and conventions

- r and R in kpc; masses in solar masses; dispersion in km s^-1
- nu_* is stellar tracer density, distinct from dark-matter density rho
- beta=1-(sigma_theta^2+sigma_phi^2)/(2 sigma_r^2)
- NFW scale density and radius describe a tested potential family, not established exact profiles
- Proper-motion, distance, line-of-sight velocity, and solar-frame covariance are propagated jointly

### Assumptions and boundary conditions

- Spherical equilibrium is a baseline approximation and must be stress-tested against substructure and flattening.
- A dark-matter velocity prediction requires a separately specified density and anisotropy/distribution function.

### Derivation step 1

$$
J(r)=\exp[\int^r2\beta(s)ds/s]
$$

This integrating factor converts the spherical Jeans differential equation into a solvable pressure-like moment equation; its normalization cancels.

### Derivation step 2

$$
\sigma_r^2(r)=\frac{1}{\nu_*(r)J(r)}\int_r^\infty\nu_*(s)J(s)\frac{GM(s)}{s^2}ds
$$

Assume the boundary moment vanishes at infinity. Integrand and denominator give velocity squared; test finite outer truncation.

### Derivation step 3

$$
\Sigma(R)=2\int_R^\infty\nu_*(r)r\,dr/\sqrt{r^2-R^2}
$$

Projected tracer density provides the normalization for the line-of-sight moment, including the anisotropy projection factor in the existing model.

### Derivation step 4

$$
\sigma_{r,DM}^2=\frac{1}{\rho_{DM}J_{DM}}\int_r^\infty\rho_{DM}(s)J_{DM}(s)GM(s)/s^2\,ds
$$

A separate density and anisotropy generate a dark-matter prediction; substituting stellar moments is not a particle-dispersion measurement.

### Inference or simulation procedure

Fit mixture membership for halo, disk, foreground, and identified debris components. Use Milky Way phase-space data where available and M31 line-of-sight tracer measurements through their distinct selection functions. Combine an NFW or alternate halo with constrained disk and bulge potentials; compare constant and flexible anisotropy. Perform forward selection and observation of mock catalogs, including measurement errors. Compare profiles at matched scaled radii and tracer classes. Derive dark-matter dispersions through a separate equilibrium solution and label them as conditional predictions.

### Validity domain and fidelity limits

The mass-anisotropy degeneracy, non-equilibrium streams, uncertain outer tracer density, and Milky Way frame conversion can dominate. M31 projected data and Milky Way 3D data provide unequal information.

## 5. Data specifications and provenance

![C10 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| tracer_id | string | 1 | Catalog identity and tracer population. | Duplicate crossmatches resolved. |
| phase_space | struct<float64[]> | kpc, km s^-1 | Observed or transformed positions/velocities. | Frame and available dimensions explicit. |
| phase_cov | float64[n,n] | mixed declared | Joint astrometry/distance/velocity covariance. | Missing velocity dimension stays absent. |
| projected_radius | measurement<float64> | kpc | M31 plane-of-sky radius. | Distance/system center uncertainty shared. |
| membership | float64[components] | 1 | Halo/disk/debris/foreground weights. | Nonnegative normalized probability vector. |
| tracer_density | model<float64> | kpc^-3 | Selection-corrected nu_star. | Radial support and extrapolation marked. |
| potential_parameters | posterior<struct> | solar mass, kpc | Baryonic and halo model parameters. | Model family and boundary conditions recorded. |
| dm_dispersion | posterior<float64[]> | km s^-1 | Conditional dark-matter velocity profile. | rho_DM/beta_DM assumptions accompany every export. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### SPLASH stellar-halo dispersion publication

[Product, archive or reference](https://arxiv.org/abs/1711.02700)

**Fields:** M31 field positions, stellar velocities, mixture memberships, radial dispersion

**Access:** Open paper; retrieve associated tables or author-provided catalog and inspect permissions.

**Role:** M31 stellar-tracer measurements.

### M31 outer globular cluster kinematics

[Product, archive or reference](https://arxiv.org/abs/1406.0186)

**Fields:** Projected radii, cluster velocities, rotation and substructure

**Access:** Publication tables; independent tracer selection and calibration required.

**Role:** Independent M31 tracer validation.

### ESA Gaia Archive

[Product, archive or reference](https://gea.esac.esa.int/archive/)

**Fields:** Astrometry, covariance, proper motions, radial velocities, quality and crossmatch fields

**Access:** Public DR3 data; distant halo tracers often require ground-based velocities and independent distance estimates.

**Role:** Milky Way phase-space measurements.

## 6. Uncertainty, sensitivity and identifiability

Mass and stellar anisotropy are strongly degenerate in projected M31 data; tracer-density slope and outer boundary add correlated uncertainty. Milky Way proper motions help but distant distances and solar-frame parameters can dominate. Include shared frame covariance and membership uncertainty; a hard stream cut understates sensitivity to unidentified debris.

Use mock catalogs with controlled beta profiles and stream fractions to locate radial domains where mass is recoverable. Compare constant and flexible anisotropy under matched predictive tests, and profile halo mass versus tracer slope. Then vary beta_DM independently to show how much conditional particle dispersion changes without changing the stellar likelihood. Report that difference as model uncertainty, not new observed information.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Spherical Jeans | Fast and interpretable moment constraints. | Equilibrium/sphericity and anisotropy degeneracy. | Use baseline where residuals and mock recovery are acceptable. |
| Distribution-function modeling | Enforces a phase-space model. | Stronger structure assumptions and computation. | Adopt if higher-dimensional data constrain the distribution. |
| Simulation-calibrated disequilibrium mocks | Tests streams and flattening. | Simulations are not exact galaxy truth. | Use for discrepancy envelopes, not automatic corrections. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C10-V1 | Isotropic power-law tracer in flat circular-speed potential | For nu proportional to r^-alpha, sigma_r squared equals v_c squared/alpha under the stated boundary. | Evaluate Jeans quadrature against analytic integral. | Analytic Jeans limit. |
| C10-V2 | Projection dimensional check | Projected density has kpc^-2 and normalized moment has velocity squared. | Unit-aware integration fixture. | Projection equation. |
| C10-V3 | Contaminating stream | Recovered uncertainty responds to injected non-equilibrium component. | Forward observe mock catalogs with stream mixture. | Proposed model-stress test. |
| C10-V4 | Tracer/DM separation | Changing beta_DM changes secondary predictions while leaving stellar likelihood unchanged. | Hold potential posterior fixed and rerun DM solver. | Distinct population contracts. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out radial ranges and observing fields and test predicted velocity distributions.
- Recover mass profiles from mock halos with streams, anisotropy gradients, and flattened potentials.
- Cross-check M31 inference against globular clusters and Milky Way inference against independent tracer families.

## 9. Implementation and reproducible work packages

1. Build catalog selection/frame manifests for each galaxy.
2. Implement covariance-preserving phase-space transformations.
3. Fit tracer density and contamination mixtures.
4. Implement Jeans/projection solvers with analytic fixtures.
5. Fit potential/anisotropy branches and matched radial comparison.
6. Generate separately typed DM dispersion predictions and mock recovery reports.

### Investigation sequence

1. Declare comparable tracer populations and radial domains; establish Milky Way catalog provenance before fitting.
2. Fit mixture memberships and survey selection, retaining low-probability cases probabilistically.
3. Infer baryonic and halo potentials with anisotropy uncertainty; create matched mock catalogs.
4. Publish measured stellar dispersions separately from conditional dark-matter velocity predictions.

### Resources and interfaces to expertise

- Dynamics code, Bayesian sampler, stellar catalog expertise, Gaia/ground-spectroscopy access, mock-halo simulations.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Tracer dispersion labeled DM measurement | Incorrect physical inference. | Output field/provenance audit. | Separate solvers and conditional labels. |
| Stream fit as equilibrium halo | Biased mass/anisotropy. | Spatially coherent velocity residuals. | Mixture membership and discrepancy stress tests. |
| Outer boundary truncated too near data | Artificial falling dispersion. | Profile changes under extended integration bounds. | Tail convergence and explicit outer-density uncertainty. |

- Calling stellar dispersion dark-matter dispersion would overstate the measurement; equilibrium failures must appear in the uncertainty budget.

## 11. Required engineering outputs

- Selection-aware tracer catalog, potential posterior atlas, matched Local Group comparison, and explicit conditional DM predictions.

### Scientific result figures to produce during execution

Measured stellar-dispersion profiles and separately labeled conditional dark-matter profiles, showing anisotropy bands and held-out tracer points.

## 12. Cited technical and scientific resources

- [Gilbert et al. (2017), SPLASH dispersion profile](https://arxiv.org/abs/1711.02700) — M31 stellar-halo mixture modeling and data.
- [Veljanoski et al. (2014), M31 cluster kinematics](https://arxiv.org/abs/1406.0186) — Independent tracer and substructure evidence.
- [Bird et al. (2022), Milky Way stellar-halo Jeans analysis](https://arxiv.org/abs/2207.08839) — Milky Way tracer-density, anisotropy, and systematic-error treatment.
- [ESA Gaia Archive](https://gea.esac.esa.int/archive/) — Milky Way astrometric measurement access.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
