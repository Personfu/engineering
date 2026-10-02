# ORION Model Foundry

Eight executable reduced-model demonstrations and one separate real catalog exploration support the portfolio's proposed research. They expose assumptions, conservation laws, numerical error and inverse-problem limitations. The synthetic examples contain invented teaching parameters and generated data; they are not completed research findings or NASA-approved designs.

Each of the nine figures is available as vector SVG and raster PNG in `figures/`. Tabular outputs and model-specific parameter/units/limitations records are in `data/`. [`manifest.json`](manifest.json) records SHA-256 hashes and sizes. Run from this folder:

```sh
python -m pip install -r requirements.txt
python -m unittest -v test_models.py
python models.py --out .
# Optional: replace the saved real snapshot with a newly retrieved one.
python models.py --out . --fetch-exoplanets
```

The ordinary generation command uses the included public catalog snapshot and needs no network. The optional refresh explicitly updates that snapshot and its retrieval metadata. Code has no machine-specific paths. Seed `20261002`, stable SVG IDs, and fixed figure metadata make synthetic outputs reproducible within the recorded NumPy/Matplotlib versions; library versions and rendering platforms can change binary image output. The included snapshot has its own retrieval time and hash and is not described as synthetic.

## Model map

| Demonstration | Portfolio starting points | Output and scientific question |
|---|---|---|
| [Mandelbrot / Julia](figures/01_fractal_escape_distance.svg) | A01 | How do finite escape counts and a derivative exterior-distance estimator reveal different structure? |
| [Ideal cryogenic binary](figures/02_ideal_binary_liquidus.svg) | A02 | How does chemical-potential balance produce a eutectic in an ideal binary with immiscible solids? |
| [Balloon thermal network](figures/03_balloon_thermal.svg) | E06, E03, I05 | Which assumed environmental exchanges dominate two-node temperature response? |
| [Sphere drag reference](figures/04_sphere_drag.svg) | D04 | Does a proposed CFD result recover creeping-flow drag before comparison with finite-Re references? |
| [Catchment reservoir](figures/05_hydrologic_reservoir.svg) | B14, B23 | Does a conceptual hydrologic model conserve storage plus discharged water? |
| [Attitude control](figures/06_one_axis_attitude.svg) | I10 | How do inertia, PD gains and explicit torque saturation change pointing response? |
| [Two-body numerical convergence](figures/07_two_body_convergence.svg) | I08, I12 | Are conservation error and timestep refinement consistent with the numerical method? |
| [Spectral identifiability](figures/08_spectral_identifiability.svg) | C08, H09 | Can noisier or nearly indistinguishable endmembers support a meaningful abundance estimate? |
| [Real exoplanet sample](figures/09_real_exoplanet_sample.svg) | C05, C23 | What catalog parameter range is present in this small, explicitly biased sample? |

These are shared research starting points, not one completed simulation per portfolio project. Every other project remains in the portfolio's individual research dossier. Neither the ideal phase diagram nor the invented spectra encode measured Pluto/Mars chemistry. The normalized orbit has no engine, maneuver, mission or deflection design.

## Equations, parameters and domain

The formulations below define the code's exact scope. `models.py` implements the equations directly; JSON sidecars record numerical values and CSV column units.

**Fractals.** Iterate `z[n+1] = z[n]^2 + c`, escaping once `|z| > 2`. Mandelbrot uses `z[0]=0` and derivative `d[n+1]=2*z[n]*d[n]+1`, `d[0]=0`; Julia uses variable `z[0]` and constant `c=-0.75+0.11i`, so `d[n+1]=2*z[n]*d[n]`, `d[0]=1`. The exterior estimator is `D=|z|*ln(|z|)/|d|`. The finite grid is 241 × 181 for each set; the iteration cap is 160. Count zero means unresolved under the cap, not mathematically proved membership. `NaN` denotes no exterior estimate. For the exactly solvable Julia case `c=0`, the estimator equals `r ln r`; the exact geometric distance is `r−1`, demonstrating why the estimator must not be labeled exact distance.

**Ideal binary phase diagram.** Equating the pure-solid and ideal-liquid chemical potentials with constant fusion enthalpy gives `ln x_i = −ΔH_i/R * (1/T − 1/Tm_i)`, hence `T_i = [1/Tm_i − (R/ΔH_i)ln x_i]^-1`. The equilibrium liquidus is the maximum of the A and B saturation branches, which intersect at the eutectic. The fictitious components use `Tm_A=63 K`, `Tm_B=60 K`, `ΔH_A=900 J/mol`, `ΔH_B=700 J/mol`. All four are invented illustrative values. Fixed unspecified pressure, ideal liquid activity, immiscible pure solids and constant enthalpy are strong assumptions. Real N₂/CO/CH₄ systems require measured phase equilibria, pressure, nonideal activity, solid solutions and kinetics. The toy intersection is `x_B≈0.562`, `T≈42.54 K`; it is not a predicted Pluto eutectic.

**Thermal network.** For wall and payload temperatures `Tw,Tp`, use `Cw*dTw/dt = Qabs + h*A*(Tair−Tw) + εσA*(Trad^4−Tw^4) − K*(Tw−Tp)` and `Cp*dTp/dt = K*(Tw−Tp) + Qelec`. Capacitances are 1200 and 850 J/K; area is 0.15 m²; emissivity is 0.75; conductance is 0.8 W/K; absorbed solar power and payload dissipation are 8 and 3 W. Air temperature falls linearly from 270 to 220 K over 2 h, the radiative sink is 12 K colder, and `h=0.6+7.4 exp(−t/3600)` W/m²/K. These histories are prescribed synthetic forcing, not an altitude model. The radiation area assumes an effective view factor. Integrate for 4 h at 10 s steps. Numerical energy-conservation tests do not validate material emissivity, heat-transfer coefficients, ascent physics or operational temperature limits. NASA's [thermal-control technology review](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) and [Passive Thermal Control Engineering Guidebook](https://ntrs.nasa.gov/citations/20230013900) explain why model correlation and verification must follow analytical design.

**Sphere drag.** `Re=ρUD/μ` and `Fd=0.5ρU²CdA`, with frontal area `A=πD²/4`. Use the Schiller–Naumann reference `Cd=(24/Re)(1+0.15 Re^0.687)` only over `0<Re≤1000`; the code rejects extrapolation. At `Re≪1`, recover the independent analytical force `Fd=3πμDU`. Assume continuum incompressible flow, a smooth isolated sphere and no walls. This is a reference curve, not a CFD solution or experimental dataset. NASA's [drag equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) supplies the dimensional relation; the [OpenFOAM Foundation's source implementation](https://cpp.openfoam.org/v12/SchillerNaumann_8C_source.html) independently documents the correlation. The toolkit does not copy OpenFOAM code or implement its high-Re branch.

**Hydrologic reservoir.** For storage `S` in mm, recharge `R` in mm/day and `k=0.12 day^-1`, use `dS/dt=R−kS`, `Q=kS`. Under each 0.25-day piecewise constant forcing bin, update `S_next = S exp(−kΔt) + (R/k)(1−exp(−kΔt))`. Integrate outflow from the same bin's mass balance. Initial storage is 20 mm; 22 of 240 bins receive deterministic randomly generated recharge. Recharge represents effective input to storage, not measured rainfall. Evapotranspiration, interception, channels and spatial variability are absent. The [USACE HEC-HMS linear-reservoir documentation](https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/baseflow/linear-reservoir-model) describes its use as a baseflow component; this example is a smaller pedagogical formulation, not HEC-HMS replication or calibrated flood guidance.

**One-axis attitude.** `dθ/dt=ω`, `I*dω/dt=clip(−Kpθ−Kdω,±τmax)+τdist`. Use `I=0.12 kg m²`, `Kp=0.03 N m/rad`, `Kd=0.08 N m s/rad`, `τmax=0.008 N m`, initial angle 35°, initial rate zero and disturbance `2.5e−5 sin(0.3t) N m`. A 120 s simulation uses 0.05 s RK4 steps. The independent undamped analytical case has angular frequency `sqrt(Kp/I)`. The dissipative ideal case obeys `dE/dt=−Kdω²`. The single-axis baseline omits wheel momentum, sensor dynamics, estimators, delays, flexibility and full three-axis attitude. NASA's [guidance, navigation and control technology review](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/) provides the actual subsystem context; it does not certify these gains.

**Two-body orbit.** Integrate `r''=−μr/|r|³` with velocity Verlet, `μ=1`, semimajor axis `a=1`, eccentricity `e=0.3`, initial periapsis radius `1−e`, and transverse velocity `sqrt((1+e)/(1−e))`. Time unit is `sqrt(a_ref³/μ_ref)`, length unit `a_ref`, velocity unit `sqrt(μ_ref/a_ref)`. Specific energy is `|v|²/2−μ/|r|`; specific angular momentum is `x*vy−y*vx`. Compare 100, 200 and 400 steps per period over 10 periods. Expect second-order energy-error refinement and bounded symplectic error, not monotonic energy loss. No external ephemeris is ingested; the model omits third bodies, perturbations and maneuvers. JPL's [periodic-orbit API documentation](https://ssd-api.jpl.nasa.gov/doc/periodic_orbits.html) is a separate resource for extending a future study to CR3BP families; this demonstration remains two-body and does not compute a Jacobi constant.

**Spectral mixture.** For two known endmembers `a,b`, generate `y=f*a+(1−f)*b+ε`, true fraction `f=0.65`, independent Gaussian noise `σ=0.008`, and 180 bands from 1–2.5 µm. Estimate `f_hat=(a−b)ᵀ(y−b)/||a−b||²`; its analytical standard deviation is `σ_f=σ/||a−b||`. Compare distinct endmembers with a nearly identical pair `b_weak=a+0.001(b−a)` in 2,000 Monte Carlo realizations. The latter raises uncertainty by 1000×. Retain unconstrained estimates outside [0,1] to expose nonidentifiability; bounds would mask this diagnostic. Exact identical endmembers raise an error. The Gaussian bands are invented; no physical mineral abundance inference is justified without real endmembers, calibrated errors, scattering/grain-size physics and an appropriate mixture model.

## Real data provenance and bias

[`data/exoplanet_sample.csv`](data/exoplanet_sample.csv) contains **200 real catalog rows** retrieved from the NASA Exoplanet Archive's `pscomppars` table. The exact query is:

```sql
SELECT TOP 200 pl_name,hostname,pl_orbper,pl_rade,st_met,discoverymethod
FROM pscomppars
WHERE pl_orbper IS NOT NULL AND pl_rade IS NOT NULL
ORDER BY pl_name
```

[`data/exoplanet_sample.provenance.json`](data/exoplanet_sample.provenance.json) records the complete encoded request/response URL, UTC retrieval timestamp, bytes, row count, schema, selection effects, documentation URLs and SHA-256. The checked-in snapshot was retrieved at **2026-10-02 09:01:19 UTC**, with SHA-256 `31d0b4ecc46e1fb7a57d41e4f35467adbfbd6d37137050b70ac6f39881f8e90e`. Orbital period is in days; planet radius is in Earth radii; stellar metallicity is in dex with a nullable value whose abundance basis requires additional metadata. Plot markers and colors distinguish discovery methods.

The extract is alphabetically truncated, discovery selected, incomplete, and conditioned on radius and period availability. `pscomppars` combines catalog parameters from different publications and is not necessarily a single self-consistent fit. This small schema omits per-parameter references, error bars, metallicity abundance basis, detection efficiency and survey denominator. It supports a data-ingestion demonstration and descriptive scatterplot only; **it cannot estimate planet occurrence, causal metallicity trends, or scientifically established planet classes**. To make those inferences, obtain a defined target sample, homogeneous measurements, uncertainties and the survey selection/completeness function.

Use the Archive's [official TAP guide](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html) and [column definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_TD_columns.html) when extending the query. Cite the [Planetary Systems Composite Table DOI](https://doi.org/10.26133/NEA13), and record the access version/time and exact row selection, as described by [IPAC's citation guidance](https://www.ipac.caltech.edu/dois/exoplanet-archive). These links were checked on 2026-10-02.

## Verification and next research gate

The 22 passing tests compare independent fixed-point and analytic Julia behavior; pure and symmetric phase limits; isolated-network energy and thermal equilibrium; RK4 fourth-order refinement; dimensional Stokes force and unsupported-Re rejection; exponential recession, steady recharge and reservoir mass balance; free rotation, exact harmonic motion and PD dissipation; exact circular-orbit refinement, central-force angular momentum and bounded/refining energy error; exact noiseless inversion, degeneracy rejection and Monte Carlo versus analytic uncertainty. They verify mathematics in the declared domains. They do not verify the empirical accuracy of invented parameters or qualify a physical system.

[`verification.json`](verification.json) stores the executed environment, test count, aggregate numerical metrics, asset counts, real-data integrity and synthetic file reproducibility check. Before treating any example as a research result, specify requirements and observables, substitute traceable measured/calibrated data, quantify systematic error and parameter identifiability, perform independent validation on withheld conditions, and use the individual portfolio dossier's subject-specific study design.
