# ATLAS Scientific Figure Gallery

**Nine new scientific spreads. Every plot opens onto its numerical evidence.**

[Data Observatory](../README.md) · [Original model gallery](../../models/README.md) · [Figure manifest](DATA_FIGURES.json) · [Engineering register](../../ENGINEERING_DOCUMENTATION.md)

![Real public catalog](badge-catalog.svg) ![Synthetic illustrative](badge-synthetic.svg) ![Proposed empty template](badge-proposed.svg)

**Real public catalog** means published archive values with recorded provenance. **Synthetic / illustrative** means generated teaching examples or formula references. **Proposed / empty template** identifies future acquisition specifications elsewhere in the portfolio. Empty templates are never plotted as observations.

| Scientific spread | What becomes visible | Evidence |
|:--|:--|:--|
| [Catalog values and coverage](#catalog-values-and-coverage) | Selected values, discovery categories and field missingness | Real public catalog |
| [Thermal power and response](#thermal-power-and-response) | The heat budget alongside the temperature response | Synthetic model |
| [Hydrologic water accounting](#hydrologic-water-ledger) | Input, delayed release and a closed water ledger | Synthetic model |
| [Control authority](#attitude-phase-and-authority) | State evolution and torque saturation | Synthetic model |
| [Orbital numerical accuracy](#orbital-numerical-accuracy) | Conservation and timestep refinement | Synthetic model |
| [Spectral information](#spectral-information) | Noise-driven variability and weak identifiability | Synthetic noise experiment |
| [Ideal-binary phase regions](#ideal-binary-phase-regions) | Liquid and solid coexistence regions | Hypothetical thermodynamic model |
| [Fractal numerical resolution](#fractal-numerical-resolution) | Escape iterations and explicitly unresolved points | Numerical fields |
| [Drag reference departures](#drag-reference-departures) | The difference between a correlation and an asymptote | Formula reference |

## Catalog values and coverage

![Real public catalog](badge-catalog.svg)

![Period and radius values with archive-field coverage](10_catalog_values_and_coverage.svg)

**200 rows · 193 distinct host names · nine missing metallicity fields.** The scatter preserves discovery categories, while the coverage panel shows which values the query required and which are missing. The rows were selected alphabetically; this sample cannot establish population occurrence rates, physical planet classes or causal metallicity relationships. Composite values may combine publications, and per-parameter uncertainties were not acquired.

[CSV](../../models/data/exoplanet_sample.csv) · [Acquisition provenance](../../models/data/exoplanet_sample.provenance.json) · [Figure provenance](10_catalog_values_and_coverage.provenance.json) · [PNG](10_catalog_values_and_coverage.png)

Research connections: [C05 · KEPLER WORLDFORGE](../../research/C/C05-kepler-worldforge/README.md), [C23 · KEPLER METAL WORLDS](../../research/C/C23-kepler-metal-worlds/README.md). Source documentation: [NASA Exoplanet Archive TAP guide](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html), [column definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_TD_columns.html), [composite-table DOI](https://doi.org/10.26133/NEA13).

## Thermal power and response

![Synthetic illustrative](badge-synthetic.svg)

![Wall heat-flow components and thermal response](11_thermal_power_and_response.svg)

**Signed heat flows · two thermal nodes · four illustrative hours.** Positive power enters the wall. The component curves sum to net wall power; wall-to-payload conduction changes sign when viewed from the wall balance. Node temperatures expose thermal lag against the prescribed air and radiative-sink histories. The payload has an assumed 3 W internal source. These are model responses rather than balloon-flight measurements or temperature qualification limits.

[CSV](../../models/data/balloon_thermal.csv) · [Parameters, units and assumptions](../../models/data/balloon_thermal.json) · [Figure provenance](11_thermal_power_and_response.provenance.json) · [PNG](11_thermal_power_and_response.png)

Research connection: [E06 · APOLLO THERMALIS](../../research/E/E06-apollo-thermalis/README.md). Model definition: [thermal-network formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). Engineering context: [NASA thermal-control technology review](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/).

## Hydrologic water ledger

![Synthetic illustrative](badge-synthetic.svg)

![Recharge fluxes, outflow and cumulative water accounting](12_hydrologic_water_ledger.svg)

**Effective recharge · delayed outflow · a conserved ledger.** The shaded components account for remaining storage and cumulative discharge, bounded by initial storage plus accumulated recharge. The maximum accounting residual is approximately 4.26 × 10⁻¹⁴ mm, demonstrating arithmetic conservation under this model. Recharge is water entering storage, rather than rainfall; the example omits evapotranspiration, interception and catchment structure. Conservation does not establish watershed predictive accuracy.

[CSV](../../models/data/hydrologic_reservoir.csv) · [Parameters, units and assumptions](../../models/data/hydrologic_reservoir.json) · [Figure provenance](12_hydrologic_water_ledger.provenance.json) · [PNG](12_hydrologic_water_ledger.png)

Research connection: [B23 · HYDRA MISSION CONTROL](../../research/B/B23-hydra-mission-control-watershed-decisions-under-uncertainty/README.md). Model definition: [reservoir formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). Wider hydrologic context: [USACE HEC-HMS linear-reservoir documentation](https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/baseflow/linear-reservoir-model); this educational example is a simpler formulation.

## Attitude phase and authority

![Synthetic illustrative](badge-synthetic.svg)

![Time-colored attitude phase portrait and torque saturation](13_attitude_phase_and_authority.svg)

**State evolution · a ±8 mN·m actuator limit · visible saturation.** The phase portrait uses the full 120-second record; its color scale denotes time. The torque panel focuses on the first 40 seconds and compares the PD request reconstructed from recorded states with the applied control torque. The model assumes one rigid axis, exact states and a fixed target; estimator, delay, wheel momentum and three-axis dynamics remain outside its scope.

[CSV](../../models/data/one_axis_attitude.csv) · [Gains, units and assumptions](../../models/data/one_axis_attitude.json) · [Figure provenance](13_attitude_phase_and_authority.provenance.json) · [PNG](13_attitude_phase_and_authority.png)

Research connection: [I10 · GEMINI POINTLOCK](../../research/I/I10-gemini-pointlock/README.md). Model definition: [one-axis formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). Engineering context: [NASA guidance, navigation and control technology review](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/).

## Orbital numerical accuracy

![Synthetic illustrative](badge-synthetic.svg)

![Orbital conservation diagnostics and timestep refinement](14_orbit_conservation_and_refinement.svg)

**Ten normalized periods · three step resolutions · an approximately second-order signature.** The stored 400-step-per-period run shows bounded relative energy error and nearly conserved angular momentum. Refinement from 100 to 400 steps per period gives an endpoint energy-error order of approximately 2.003. The dashed reference is anchored to the coarsest run. This checks the numerical integrator within a two-body model; it does not validate an operational ephemeris, maneuver or planetary-defense solution.

[Orbit CSV](../../models/data/two_body_orbit.csv) · [Refinement CSV](../../models/data/two_body_convergence.csv) · [Normalized units and assumptions](../../models/data/two_body_orbit.json) · [Figure provenance](14_orbit_conservation_and_refinement.provenance.json) · [PNG](14_orbit_conservation_and_refinement.png)

Research connections: [I08 · VOYAGER FRAMEFORGE](../../research/I/I08-voyager-frameforge/README.md), [I12 · PIONEER PHOBOS PATHFINDER](../../research/I/I12-pioneer-phobos-pathfinder/README.md), [I13 · OSIRIS APOPHIS HORIZON](../../research/I/I13-osiris-apophis-horizon/README.md). Exact demonstration equations: [two-body formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). The baseline includes no third bodies or passive-encounter uncertainty propagation.

## Spectral information

![Synthetic illustrative](badge-synthetic.svg)

![Synthetic fraction-estimator distributions for distinct and nearly identical endmembers](15_spectral_information_and_noise.svg)

**2,000 noise realizations · one injected fraction · sharply different information.** With separated endmembers, empirical fraction variability is approximately 0.0086. Nearly identical endmembers increase it to approximately 8.615; estimates outside [0,1] remain visible. Dashed lines mark central 95% intervals of synthetic noise draws. The panels use different scales deliberately. These intervals are descriptive simulation intervals, rather than measured mineral-abundance uncertainty or posterior credible intervals.

[Spectral CSV](../../models/data/spectral_mixture.csv) · [Noise-realization CSV](../../models/data/spectral_monte_carlo.csv) · [Parameters and assumptions](../../models/data/spectral_mixture.json) · [Figure provenance](15_spectral_information_and_noise.provenance.json) · [PNG](15_spectral_information_and_noise.png)

Research connections: [C08 · MARS NILI SPECTRAL VAULT](../../research/C/C08-mars-nili-spectral-vault/README.md), [H09 · PERSEVERANCE LAKE ARCHIVE](../../research/H/H09-perseverance-lake-archive/README.md). Exact estimator and noise assumptions: [spectral-mixture formulation](../../models/README.md#equations-parameters-and-domain), [executable source](../../models/models.py) and [uncertainty rules](../../engineering/UNCERTAINTY_AND_DECISION_RULES.md). The absorption bands are invented; no measured Mars mineral library was ingested.

## Ideal-binary phase regions

![Synthetic illustrative](badge-synthetic.svg)

![Hypothetical binary phase regions with toy eutectic point](16_ideal_binary_phase_regions.svg)

**An ideal liquid · immiscible pure solids · a hypothetical eutectic.** Region fills show liquid above the liquidus, liquid plus the appropriate pure solid between the liquidus and eutectic, and two solids below the eutectic. The toy intersection is B mole fraction approximately 0.562 and temperature approximately 42.54 K. These phase regions follow declared assumptions and invented constants; they are not measurements or calibrated predictions of Pluto's volatile mixtures.

[CSV](../../models/data/ideal_binary_liquidus.csv) · [Invented constants and limits](../../models/data/ideal_binary_liquidus.json) · [Figure provenance](16_ideal_binary_phase_regions.provenance.json) · [PNG](16_ideal_binary_phase_regions.png)

Research connection: [A02 · NEW HORIZONS CRYOPHASE](../../research/A/A02-new-horizons-cryophase/README.md). Exact equilibrium relation: [ideal-binary formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). Real phase behavior would require pressure-dependent measurements, nonideal activities, solid solutions and kinetics.

## Fractal numerical resolution

![Synthetic illustrative](badge-synthetic.svg)

![Finite-grid Mandelbrot and Julia first-escape maps](17_fractal_resolution_and_escape.svg)

**43,621 sampled points per map · a 160-iteration budget · unresolved points made explicit.** The color scale reports first escape iteration logarithmically. A distinct navy fill denotes the 9,873 Mandelbrot and 808 Julia points that did not escape under this budget. Finite precision, spatial resolution and iteration cannot certify those points as members. The domains differ, and the unresolved fractions describe only these sampled grids. Julia uses c = −0.75 + 0.11i.

The map uses escape counts directly. In the Julia CSV, the critical starting point (0,0) escapes at iteration 29 but has an undefined derivative-based distance estimate. A `NaN` distance therefore means no usable exterior estimate; it does not by itself determine escape status.

[Mandelbrot CSV](../../models/data/mandelbrot.csv) · [Mandelbrot metadata](../../models/data/mandelbrot.json) · [Julia CSV](../../models/data/julia.csv) · [Julia metadata](../../models/data/julia.json) · [Figure provenance](17_fractal_resolution_and_escape.provenance.json) · [PNG](17_fractal_resolution_and_escape.png)

Research connection: [A01 · ARTEMIS FRACTAL NAVIGATOR](../../research/A/A01-artemis-fractal-navigator/README.md). Exact recurrence and unresolved-value semantics: [fractal formulation](../../models/README.md#equations-parameters-and-domain) and [executable source](../../models/models.py). The images are numerical fields, rather than physical observations.

## Drag reference departures

![Synthetic illustrative](badge-synthetic.svg)

![Sphere-drag correlation and departure from the creeping-flow asymptote](18_sphere_drag_reference_departure.svg)

**A correlation reference · an asymptotic comparison · explicitly different domains.** Schiller–Naumann reference values are compared with Stokes drag. The percentage difference reaches a descriptive 10% marker near Reynolds number 0.554. That marker is computed from the same formula and is not an empirical acceptance tolerance. Stokes behavior applies asymptotically at Re ≪ 1; neither panel contains a wind-tunnel measurement or CFD solver result.

[CSV](../../models/data/sphere_drag.csv) · [Correlation domain and limits](../../models/data/sphere_drag.json) · [Figure provenance](18_sphere_drag_reference_departure.provenance.json) · [PNG](18_sphere_drag_reference_departure.png)

Research connection: [D04 · GLENN SPHERE STANDARD](../../research/D/D04-glenn-sphere-standard/README.md). Source context: [OpenFOAM Foundation correlation implementation](https://cpp.openfoam.org/v12/SchillerNaumann_8C_source.html), [NASA drag equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) and [the exact included model definition](../../models/README.md#equations-parameters-and-domain).

---

**Every image has a ledger.** The [figure manifest](DATA_FIGURES.json) records repository-relative source/output paths, SHA-256 hashes, units, assumptions, linked project IDs and descriptive calculations. Reproduce these spreads with [the portable renderer](../../tools/render_data_figures.py), following the [Data Observatory instructions](../README.md#reproduce-the-gallery). The original [40-asset model manifest](../../models/manifest.json) remains intact, and raw tables remain in their single original location.
