# H09 · PERSEVERANCE LAKE ARCHIVE

**Original project:** Trends in Mineralogy and Grain Size Distribution Across Paleolake Basins on Mars

**Session H:** Planetary Science

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session H](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_H.md) · [← H08](../H08-genesis-rim-chronicle/README.md) · [I01 →](../../I/I01-saturn-transient-shield/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 8 | 4 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Build a comparative sedimentary-material atlas starting at Terby crater and extending to a deliberately selected set of Martian paleolake candidates. Preserve the original mineralogy and grain-size question, using CRISM spectra, morphological context, and independent thermal constraints where available. The key advance is honest separation of directly detected absorption features, model-dependent abundance and effective grain size, and geological interpretation. Terrestrial basins supply process analogs, not automatic ground truth for Mars.

**Question:** Are spatial mineral and effective-grain-size trends better explained by sediment transport and sorting, in-place alteration, or later dust and surface modification?

**Testable hypothesis:** Models conditioned on mapped stratigraphic and geomorphic units will predict independent spectral and thermal observations better than a basin-wide composition model, while some grain-size estimates remain intrinsically nonunique.

## 1. Design basis and analysis boundary

The paleolake-material atlas begins at Terby crater and a predeclared comparison-basin set, using actual CRISM targeted products, morphology and supported thermal observations. It distinguishes diagnostic absorption features, inferred mineral fractions/effective optical grain size and transport/alteration interpretation. Basin membership and lacustrine evidence remain separately reviewed; mineral detection alone does not prove a lake or habitability.

Begin with product/geometry/artifact auditing and conservative band maps, then laboratory-degraded radiative-transfer benchmarks and Bayesian composition/size inference. Optical size is not sieve diameter, while thermal inertia also reflects rocks, cementation, porosity and layering. The full posterior includes model prior p(M), and transport/alteration scenarios remain uncertain contributors rather than hidden assumptions in a single grain-size trend.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| H09-R1 | Every spectral/thermal/context product shall retain actual ID, processing level, geometry, masks and native footprint; Terby coverage is verified before mapping. | Portal presence does not establish basin products. | Archive/product support audit. | PDS CRISM/HiRISE/THEMIS context. |
| H09-R2 | Keep detected band depth, modeled fraction, optical size and geological grain-size interpretation in separate fields. | Different observables have different evidence. | Endpoint/units and figure-label review. | Reviewed spectral/thermal distinctions. |
| H09-R3 | Joint inversion shall include p(M), fraction constraints and transport/alteration/photometric uncertainty with prior sensitivity. | Hidden model priors overstate unique interpretation. | Posterior normalization and odds tests. | Reviewed Bayesian formulation. |
| H09-R4 | Validate using laboratory mixtures degraded to CRISM response and full-basin/stratigraphic holdouts at common actual support. | Spectral fits alone do not establish physical identifiability. | Mixture and basin transfer benchmark. | Primary probabilistic/laboratory studies. |

## 3. Architecture and controlled interfaces

A spectral adapter records TER/MTRDR level, wavelength sampling, observation angles and artifact masks. Morphology/stratigraphy defines basin units and depositional transects independently. A thermal adapter preserves observation time and radiance/temperature processing; thermal inertia is a separate thermophysical estimate, never a direct grain-size measurement.

The registration service aggregates spectra, thermal data and imagery to common supported footprints with uncertainty. A radiative-transfer branch compares areal and intimate mixing using versioned mineral libraries and size distributions. A model registry defines transport, dust and alteration hypotheses with p(M). The posterior engine emits correlated fractions, effective size and model weights; unsupported products or library domains propagate abstention rather than continuous basin trends.

![H09 engineering architecture](figures/architecture.svg)

The diagram separates directly observed features from composition/optical-size inference and explicitly carries p(M), transport and alteration. Common-footprint validation limits geological grain-size and paleolake interpretation to supported scenarios.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
r_\lambda=\mathcal H_\lambda(\mathbf f,\mathbf a,i,e,g,\theta)+\epsilon_\lambda,\quad f_q\ge0,\;\sum_qf_q=1
$$

$$
I_{\rm th}=\sqrt{k\rho c},\quad BD_\lambda=1-r_\lambda/r_{\rm cont,\lambda}
$$

$$
p(\mathbf f,\mathbf a,M\mid\mathbf r,\mathbf T)\propto p(\mathbf r,\mathbf T\mid\mathbf f,\mathbf a,M)\,p(\mathbf f,\mathbf a\mid M) p(M)
$$

### Variables, units and conventions

- r is dimensionless reflectance; f is mineral fraction under a stated mixing convention; a is effective optical grain size in micrometers.
- i, e, and g are incidence, emission, and phase angles; theta includes roughness, porosity, and scattering parameters.
- Thermal inertia I_th has units joules per square meter per kelvin per square-root second; k is conductivity, rho density, c heat capacity.
- BD is continuum-normalized band depth; T denotes thermal observations, and M competing transport/alteration scenarios.
- p(M): declared prior probability of each competing model or scenario; report sensitivity to prior choices.

### Assumptions and boundary conditions

- Optical effective grain size is not identical to geological sieve diameter, and thermal inertia is affected by rocks, cementation, porosity, and layering.
- Linear areal mixing and intimate particulate radiative transfer are distinct models requiring separate comparison.
- Atmospheric correction, photometric effects, and mineral-library variability contribute correlated spectral uncertainty.

### Derivation step 1

```text
BD_lambda=1-r_lambda/r_cont,lambda.
```

Reflectance and band depth are dimensionless; continuum choice and correlated spectral calibration contribute uncertainty, and a nondetection is not mineral absence.

### Derivation step 2

```text
r_lambda=H_lambda(f,a,i,e,g,theta)+epsilon_lambda; f_q>=0, sum_q f_q=1.
```

Fractions use a declared area/mass/volume convention and effective optical sizes are micrometres. Areal and intimate mixing are distinct forward families.

### Derivation step 3

```text
I_th=sqrt(k rho c).
```

k W/m/K, rho kg/m³ and c J/kg/K give J/m²/K/sqrt(s). Thermal constraints include porosity, rock fraction and layering, not a one-to-one size conversion.

### Derivation step 4

```text
p(f,a,M|r,T) proportional p(r,T|f,a,M)p(f,a|M)p(M); Var(a)=E_M[Var(a|M)]+Var_M[E(a|M)].
```

Model averaging includes within-model uncertainty and between-model transport/alteration differences. Registration, dust and library discrepancy enter the likelihood or explicit nuisance priors.

### Inference or simulation procedure

Define a basin-selection rubric that records evidence for lacustrine deposition and includes comparison units with uncertain or nonlacustrine histories. Start with Terby and identify actual CRISM target products and morphology coverage before assigning mineral trends. Use map-projected targeted products with quality masks, then compare repeat observations and alternative continuum choices. Map diagnostic mineral features conservatively; fit probabilistic radiative-transfer models to estimate sets of acceptable compositions and effective grain sizes. Build laboratory-mixture tests spanning candidate clays, mafic minerals, carbonates, and dust with known particle distributions. Degrade those spectra to CRISM sampling and noise to measure identifiability. Register spectral, thermal, and imagery products at their true spatial resolutions and aggregate to common footprints. Compare predicted trends along mapped depositional transects and across stratigraphic units with full-basin holdouts.

### Validity domain and fidelity limits

Spectral non-detection does not prove mineral absence. Surface dust can conceal underlying sediment, and compositional/grain-size tradeoffs can be large. Neither clay nor carbonate detection alone establishes an ancient lake or habitability.

## 5. Data specifications and provenance

![H09 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| crism_product | string | none | Actual target/level/version identity. | Terby/basin coverage and masks verified. |
| reflectance_spectrum | nullable float[] | dimensionless | Corrected native spectral observations. | Wavelength/geometry and covariance retained. |
| band_depth | nullable float[] | dimensionless | Declared continuum feature metric. | Continuum alternatives and artifact flags saved. |
| mineral_fraction | float[][] | declared fraction basis | Posterior compatible compositions. | Nonnegative/simplex and library support checked. |
| optical_size | float[] | micrometre | Effective radiative-transfer particle size. | Distinct from geological sieve distribution. |
| thermal_constraint | nullable record | K and inertia units | Supported temperature/thermophysical evidence. | Time, rocks/porosity/layering retained. |
| model_prior | float vector | 0–1 | p(M) for mixing/transport/alteration families. | Normalized and sensitivity documented. |
| joint_covariance | matrix | mixed | Spectral/thermal/registration uncertainty. | Correlated errors and native support included. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### PDS CRISM archive

[Product, archive or reference](https://pds-geosciences.wustl.edu/missions/mro/crism.htm)

**Fields:** TER/MTRDR cubes, observation geometry, quality and instrument documentation

**Access:** Public holdings; Terby coverage, repeated targets, wavelengths, and artifact masks require product-level selection.

**Role:** Spectral observations and correction provenance.

### HiRISE images and DTM discovery

[Product, archive or reference](https://hirise.lpl.arizona.edu/dtm/)

**Fields:** Geomorphology, stratigraphic context, stereo elevation where available

**Access:** Public; site-specific DTM coverage cannot be assumed.

**Role:** Independent sedimentary context and spatial registration.

### PDS Odyssey THEMIS thermal image products

[Product, archive or reference](https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=ODY-M-THM-5-IRGEO-V2.0)

**Fields:** Spatially registered thermal infrared imagery derived from calibrated radiance, geometry and processing documentation

**Access:** Public archive route; temperature and thermal inertia require appropriate thermophysical processing and viewing-time selection.

**Role:** Independent thermophysical constraints rather than direct grain-size measurements.

## 6. Uncertainty, sensitivity and identifiability

Atmospheric/photometric correction, mineral-library variation and surface dust create correlated spectral errors. Grain size and abundance can compensate, especially under intimate mixing; profile posterior ridges and test known mixtures degraded to the actual instrument response. Repeat observations and continuum alternatives expose systematic discrepancy beyond nominal channel noise.

Thermal inertia depends on cementation, rocks, porosity and layering, while deposition, sorting and later alteration modify geological grain distributions. Compare explicit M scenarios with declared priors and retain between-model size variance. Spatial registration and unequal footprints can create false transect gradients. Full-basin holdouts assess transfer; supported effective-size trends remain conditional rather than recovered sediment sieve distributions.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Conservative band-feature atlas | Closest to spectral observations. | Does not quantify unique mineral abundance. | Required initial product. |
| Bayesian radiative-transfer ensembles | Exposes composition/size correlations. | Library/mixing assumptions remain. | Use where laboratory identifiability supports it. |
| Joint spectral/thermal geological scenarios | Adds independent process constraints. | Thermal nonuniqueness and model priors matter. | Adopt with explicit p(M) and transport/alteration sensitivity. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| H09-V1 | No absorption feature | BD=0; r=0.8 r_cont gives BD=0.2. | Condition/fixture: r_lambda=r_cont,lambda with valid continuum. Verification procedure: Exact feature-ratio test.. | Exact feature-ratio test. |
| H09-V2 | Thermal scaling | I_th increases by sqrt(2), not factor two. | Condition/fixture: Double k with rho and c fixed. Verification procedure: Analytic thermophysical check.. | Analytic thermophysical check. |
| H09-V3 | Model prior odds | Posterior odds=1:2, yielding probabilities 1/3 and 2/3. | Condition/fixture: Two models have prior odds 1:4 and likelihood ratio 2. Verification procedure: Exact Bayes odds calculation.. | Exact Bayes odds calculation. |
| H09-V4 | Mixture/basin holdout | Report fraction/size coverage, degeneracy and unsupported-trend flags. | Condition/fixture: Reserve known laboratory mixtures and entire comparison basins/units. Verification procedure: Instrument-degraded and spatial validation.. | Instrument-degraded and spatial validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Recover known laboratory-mixture properties after resolution degradation; report ambiguity rather than forcing point estimates.
- Test atmospheric, photometric, endmember, and dust sensitivity across repeated observations.
- Require cross-sensor agreement at common footprints and report residual spatial autocorrelation and basin-transfer failures.

## 9. Implementation and reproducible work packages

1. Freeze basin-selection, lacustrine-evidence and actual product coverage manifests.
2. Implement wavelength/geometry/artifact and native-footprint registration adapters.
3. Create conservative band maps with continuum covariance.
4. Build versioned mixing/transport/alteration model priors and laboratory-degraded fixtures.
5. Fit joint composition/size/thermal posteriors and full-basin holdouts.
6. Release feature, effective-size and geological-scenario products with model-averaged uncertainty.

### Investigation sequence

1. Freeze basin evidence criteria, spatial footprints, and archive manifests.
2. Establish reliable mineral-feature detections and repeat-observation consistency.
3. Calibrate inversion uncertainty with known laboratory mixtures.
4. Compare transport, alteration, and surface-overprint predictions across withheld units and basins.

### Resources and interfaces to expertise

- PDS spectral readers, GIS registration, radiative-transfer inference, laboratory VNIR spectrometer and sieved standards, sedimentology mentor.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Optical size called sieve size | False sedimentological precision. | Endpoint/library review. | Separate modeled and geological size. |
| p(M) omitted | Unstated preferred history. | Posterior/odds audit. | Explicit model priors and averaging. |
| Footprint mismatch gradient | Artificial stratigraphic trend. | Registration/support sensitivity. | Common actual-resolution aggregation. |

- Assumed lake origins, unresolved mixed pixels, mineral-library mismatch, and reporting grain-size precision unsupported by the observations.

## 11. Required engineering outputs

- A Terby-centered basin atlas, mineral-detection confidence layers, composition/grain-size posterior sets, and competing sedimentary-history assessment.

### Scientific result figures to produce during execution

Terby geomorphology with spectral footprints, diagnostic-band maps, grain-size/composition ambiguity plots, and model predictions along depositional transects; inferred lake histories are labeled.

### Included shared numerical starting point

![H09 shared reduced-model or catalog demonstration](../../../models/figures/08_spectral_identifiability.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![H09 data diagnostic](../../../data/figures/15_spectral_information_and_noise.svg)

Synthetic spectral-mixture estimator distributions under the same known band-noise level. Separated endmembers give narrow noise-driven fraction estimates; near-identical endmembers give a broad unconstrained distribution with unphysical values preserved as an identifiability diagnostic. Central 95% noise-realization intervals are descriptive simulation intervals, not posteriors or uncertainty bounds for measured Mars mineral abundance.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [PDS CRISM mission archive](https://pds-geosciences.wustl.edu/missions/mro/crism.htm) — Targeted spectral products and correction/geometry documentation.
- [Lapotre et al., A probabilistic approach to remote compositional analysis of planetary surfaces](https://www.usgs.gov/publications/a-probabilistic-approach-remote-compositional-analysis-planetary-surfaces) — Bayesian Hapke inversion and composition/grain-size tradeoffs.
- [Harris et al. (2018), Hapke mixture modeling of mafic minerals and shergottites](https://onlinelibrary.wiley.com/doi/full/10.1111/maps.13065) — Laboratory validation and limits on quantitative satellite unmixing.
- [HiRISE DTM archive](https://hirise.lpl.arizona.edu/dtm/) — Morphological/topographic product discovery.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
