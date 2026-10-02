# E04 · AURA VERTICAL

**Original project:** A Measurement of the Concentration of Greenhouse Gases as Altitude Increases

**Session E:** ASCEND

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session E](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_E.md) · [← E03](../E03-artemis-stratodose/README.md) · [E05 →](../E05-orion-truss/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![E04 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | A Measurement of the Concentration of Greenhouse Gases as Altitude Increases | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 3 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Estimate a hierarchical vertical-profile model with flight effects and correlated residuals. Fit instrument lag using independent response characterization; compare dry-air profiles to colocated or regionally relevant NOAA observations. Separate ascent and descent to detect hysteresis and avoid converting pressure decline into a concentration result.

**Operating envelope:** NOAA flights are comparison observations, not contemporaneous ground truth for Arizona. Balloon horizontal drift and diurnal boundary-layer change complicate an altitude-only analysis.

**Variables and conventions**

- p Pa; T K; n_air molecules/m^3
- x dimensionless mole fraction, reported ppm CO2 or ppb CH4
- tau s; b mole fraction per m; u_flight flight-specific intercept

### Artifact wall

![E04 proposed analysis architecture](figures/architecture.svg)

Calibration, humidity basis and response lag precede the altitude model. External profiles provide context; molecular density, horizontal/time confounding and missing analyzer selectivity remain distinct limitations.

**Scientific result to produce:** Raw voltage, corrected wet/dry mole fractions and number density in aligned altitude panels, with systematic uncertainty bands.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create analyzer_calibration_manifest.json and gas_basis_schema.json. |
| 02 | Planned | Implement humidity_conversion.py and ideal_gas_density.py. |
| 03 | Planned | Build flight_clock_position.py with phase/path metadata. |
| 04 | Planned | Create first_order_response.py and latent_vertical_profile.py. |
| 05 | Planned | Implement noaa_profile_adapter.py preserving calibration scale. |
| 06 | Planned | Publish withheld_flight.ipynb and dry_profile.parquet with domain/identity/lag flags. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [E03 · ARTEMIS STRATODOSE](../E03-artemis-stratodose/README.md) | UArizona ASCEND: Profiling High-Altitude Radiation with a General Data Logger | Session E |
| [E05 · ORION TRUSS](../E05-orion-truss/README.md) | EagleSat Team: Design and Refinement of 3U CubeSat Structure | Session E |
| [E02 · GEMINI HELIX](../E02-gemini-helix/README.md) | Project Helix | Session E |
| [E06 · APOLLO THERMALIS](../E06-apollo-thermalis/README.md) | Study of Thermal Heat Transfer Within a High-Altitude Balloon Payload | Session E |
| [E01 · APOLLO HELIOSCOPE](../E01-apollo-helioscope/README.md) | Phoenix College: Video Streaming and DNA Studies | Session E |
| [E07 · DISCOVERY TRIDENT](../E07-discovery-trident/README.md) | Glendale Community College (GCC) ASCEND Team | Session E |

[Machine-readable connection register and ranking rule](../../../registry/mission_connections.json)

### Reading playlist

| Route | Start here | Continue to |
| --- | --- | --- |
| Understand the idea | [Scientific objective](#purpose-and-scientific-objective) | [Design boundary](#1-design-basis-and-analysis-boundary) → [Mathematics](#4-mathematical-model-and-derivation) |
| Inspect the data | [Visual blueprint](data/README.md) | [Provenance](#5-data-specifications-and-provenance) → [Uncertainty](#6-uncertainty-sensitivity-and-identifiability) |
| Make a design decision | [Trade study](#7-engineering-trade-study) | [Failure modes](#10-failure-modes-and-interpretation-controls) → [Required outputs](#11-required-engineering-outputs) |
| Prepare execution | [Requirements](#2-requirements-and-verification-traceability) | [Verification](#8-verification-and-validation-cases) → [Implementation](#9-implementation-and-reproducible-work-packages) |

## Complete engineering dossier

The profile above is a browsing layer. The full design basis, equations, derivations, data contract, uncertainty, trades and controlled case definitions follow.

## Purpose and scientific objective

Make the greenhouse-gas balloon concept a traceable atmospheric profile study. Report dry-air mole fraction separately from number density and raw sensor voltage. Combine pressure, water vapor, temperature and response-time corrections so a trend with altitude has a physical meaning; compare with NOAA profiles before interpreting local atmospheric transport.

**Question:** Does a calibrated vertical gas profile contain an altitude-dependent mole-fraction signal beyond pressure, humidity, response lag and flight-path variability?

**Testable hypothesis:** Pressure compensation and lag correction will change apparent gradients from inexpensive sensors; remaining gradients may differ between boundary-layer air and the free troposphere.

## 1. Design basis and analysis boundary

The gas-profile system tests altitude-associated dry-air mole-fraction structure after pressure/temperature calibration, humidity conversion, sensor lag and flight-path effects. Its boundary includes a selective analyzer, intake/response behavior, timestamps and geolocation. Declining molecular number density with altitude is not itself declining mole fraction, and a broad nonspecific gas sensor cannot identify CO2 or CH4 uniquely.

Begin with independently characterized response and calibration, then a hierarchical profile with separate ascent/descent and flight effects. NOAA aircraft/AirCore data provide a scale- and context-matched comparison rather than contemporaneous Arizona truth. Lag correction is uncertainty-aware; unsupported low-pressure calibration blocks a quantitative profile.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| E04-R1 | All gas values shall state dry/wet basis, calibration scale, species and ppm/ppb conversion. | Humidity and unit confusion can create altitude trends. | Round-trip conversion and source-column audit. | NOAA comparison schema; measurement contract. |
| E04-R2 | Quantitative profile points shall remain inside analyzer pressure/temperature calibration domain. | Room calibration may fail aloft. | Domain flags and calibration-envelope review. | Instrument validity requirement. |
| E04-R3 | Lag shall be independently characterized or jointly reported as confounded with vertical gradient. | Response time changes apparent ascent/descent slopes. | Known-step response and joint profile sensitivity. | Corrected first-order response model. |
| E04-R4 | Proposed gradient gate: b interval excludes zero under lag/humidity/path alternatives and withheld-flight evaluation. | A single fitted slope can reflect drift or diurnal change. | Hierarchical block holdout and scenario comparison. | Proposed inferential criterion; no concentration trend claimed. |

## 3. Architecture and controlled interfaces

An intake/analyzer adapter returns selective wet- or dry-basis mole fraction with calibration metadata and pressure/temperature. Humidity records convert only compatible wet observations. Flight alignment maps time to altitude and horizontal position, retaining ascent/descent classification and sensor transport delay.

A response-state model predicts measured y from latent true concentration, rather than noisily differentiating observations without regularization. The vertical model includes flight effects and correlated residuals; geolocation/time covariates remain available to test altitude-only inadequacy. NOAA ingestion preserves calibration scale and native fields before comparison.

![E04 engineering architecture](figures/architecture.svg)

Calibration, humidity basis and response lag precede the altitude model. External profiles provide context; molecular density, horizontal/time confounding and missing analyzer selectivity remain distinct limitations.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
n_air=p/(k_B*T)
```

```text
x_dry=x_wet/(1-x_H2O)
```

```text
tau*dy/dt+y=x_true(t)
```

```text
x(z)=a+b*z+u_flight+epsilon
```

### Variables, units and conventions

- p Pa; T K; n_air molecules/m^3
- x dimensionless mole fraction, reported ppm CO2 or ppb CH4
- tau s; b mole fraction per m; u_flight flight-specific intercept

### Assumptions and boundary conditions

- Calibrate over the actual pressure/temperature envelope; nominal room conditions are insufficient.
- Infer gas identity only from a selective calibrated analyzer; broad gas sensors do not resolve CO2/CH4.

### Derivation step 1

```text
n_{air}=p/(k_BT)
```

Ideal-gas molecular number density has molecules/m^3. A trace-gas number density n_g=x n_air can decline with pressure even when mole fraction x is constant.

### Derivation step 2

```text
x_{dry}=x_{wet}/(1-x_{H_2O})
```

Dry-air denominator removes water molecules. All fractions are dimensionless before ppm or ppb reporting; humidity uncertainty induces common covariance.

### Derivation step 3

$$
\tau\dot y+y=x_{true};\quad y(t)=x_1+(y_0-x_1)e^{-t/\tau}
$$

For a true step to x1, the sensor responds exponentially. During ascent, delay maps into apparent vertical displacement roughly climb rate times tau.

### Derivation step 4

$$
x(z,t)=a+bz+u_{flight}+g(location,time)+\epsilon
$$

b has mole fraction/m. Fit response dynamics jointly with this latent profile; derivative-based inversion x=y+tau dot y amplifies high-frequency measurement noise.

### Inference or simulation procedure

Estimate a hierarchical vertical-profile model with flight effects and correlated residuals. Fit instrument lag using independent response characterization; compare dry-air profiles to colocated or regionally relevant NOAA observations. Separate ascent and descent to detect hysteresis and avoid converting pressure decline into a concentration result.

### Validity domain and fidelity limits

NOAA flights are comparison observations, not contemporaneous ground truth for Arizona. Balloon horizontal drift and diurnal boundary-layer change complicate an altitude-only analysis.

## 5. Data specifications and provenance

![E04 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| species_basis | record | 1 | CO2/CH4 and dry/wet calibration scale. | Selective analyzer evidence required. |
| gas_reading | nullable<float64> | mol/mol | Native calibrated mole fraction. | ppm/ppb conversion explicit; missing null. |
| water_fraction | nullable<float64> | mol/mol | Compatible water mole fraction. | Between zero and one; unknown blocks conversion. |
| pressure_temperature | record | Pa,K | Analyzer/environment state. | Calibration domain and covariance retained. |
| flight_position | record | m,degree | Altitude/geolocation at timestamp. | Reference datum and horizontal drift retained. |
| response_time | nullable<float64> | s | Transport/sensor lag tau. | Positive and independently sourced or latent flagged. |
| profile_covariance | matrix<float64> | (mol/mol)^2 | Joint profile/measurement uncertainty. | Shared scale/humidity terms retained. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NOAA greenhouse-gas data

[Product, archive or reference](https://gml.noaa.gov/ccgg/data/getdata.php?gas=co2)

**Fields:** UTC, latitude/longitude, pressure Pa, temperature K, water-vapor mole fraction, selective gas mole fraction, calibration scale and instrument response time

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

### NOAA aircraft CO2 data dictionary

[Product, archive or reference](https://erddap.gml.noaa.gov/erddap/info/greenhouse_gases_co2_aircraft_insitu_10_second_values/index.html)

**Fields:** Independent benchmark metadata, reference assumptions and calibration context; select actual products before execution.

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

## 6. Uncertainty, sensitivity and identifiability

Analyzer calibration, humidity, pressure/temperature response and intake delay correlate with inferred altitude slope. Balloon drift and evolving boundary-layer conditions create confounding between altitude, place and time. NOAA profiles add contextual differences in season, location and calibration scale rather than exact ground-truth uncertainty.

Profile b against tau and humidity correction, compare ascent/descent at matched conditions and block residuals by flight segment. Fit withheld flights and examine geolocation/time effects before asserting altitude causation. Report points outside calibration and gas identity limits as unavailable, while preserving their raw observations for future calibration.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Raw wet profile | Direct reported analyzer stream. | Humidity and response bias. | Retain for provenance only. |
| Dry-basis lag-aware hierarchy | Corrects key measurement pathways. | Depends on calibration/humidity/time constants. | Primary inference inside validated envelope. |
| Regional NOAA comparison | External calibrated context. | Different time/place/sample path. | Use for plausibility and scale checks, not exact truth. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| E04-V1 | Constant mole fraction | Pressure decline changes number density while x remains constant. | Ideal-gas synthetic altitude fixture. | Density versus composition distinction. |
| E04-V2 | Humidity conversion | At zero water, dry equals wet; positive water raises dry value for fixed wet. | Analytic endpoint fixture. | Denominator algebra. |
| E04-V3 | Step/flight lag | First-order response matches exponential and produces speed-times-lag displacement. | Simulated ascent/descent known-profile replay. | Response model; observed gradient pending. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Proposed gate: calibration bias is below one-third of the smallest scientific gradient targeted.
- Hold out complete profiles; compare to constant-mole-fraction and uncorrected-sensor baselines.
- Do a humidity/lag sensitivity envelope and disclose non-identifiability when corrections dominate.

## 9. Implementation and reproducible work packages

1. Create analyzer_calibration_manifest.json and gas_basis_schema.json.
2. Implement humidity_conversion.py and ideal_gas_density.py.
3. Build flight_clock_position.py with phase/path metadata.
4. Create first_order_response.py and latent_vertical_profile.py.
5. Implement noaa_profile_adapter.py preserving calibration scale.
6. Publish withheld_flight.ipynb and dry_profile.parquet with domain/identity/lag flags.

### Investigation sequence

1. Choose target gas and allowable uncertainty from expected atmospheric gradients.
2. Characterize pressure, humidity and lag sensitivity; replay NOAA profiles through the sensor model.
3. Fit ascent/descent jointly and report gradients only if larger than propagated systematic uncertainty.

### Resources and interfaces to expertise

- Atmospheric chemist, trace-gas metrologist and flight data engineer.
- Selective analyzer, pressure/humidity references, calibration access and dry-air conversion pipeline.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Density labeled concentration | False altitude composition trend. | Units/basis audit. | Use mole fraction and separate number density. |
| Missing humidity assumed dry | Biased profile. | Conversion input missing flag. | Null corrected output or bounded humidity scenario. |
| Lag ignored | Spurious hysteresis/slope. | Ascent/descent residual dependence. | Independent response calibration and joint latent model. |

- Pressure-driven sensor response can masquerade as atmospheric depletion.
- Any local profile conclusion needs representativeness and calibration caveats.

## 11. Required engineering outputs

- Versioned analysis configuration, raw-to-derived provenance and uncertainty report.
- Project-specific model comparison, a publication figure with units, and an explicit outcome including inconclusive findings.

### Scientific result figures to produce during execution

Raw voltage, corrected wet/dry mole fractions and number density in aligned altitude panels, with systematic uncertainty bands.

## 12. Cited technical and scientific resources

- [NOAA greenhouse-gas data](https://gml.noaa.gov/ccgg/data/getdata.php?gas=co2) — Aircraft and AirCore vertical profile archive.
- [NOAA aircraft CO2 data dictionary](https://erddap.gml.noaa.gov/erddap/info/greenhouse_gases_co2_aircraft_insitu_10_second_values/index.html) — Explicit variables and calibration scale for a comparison dataset.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
