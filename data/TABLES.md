# ATLAS Table Archive

**Every included scientific CSV, visibly cataloged. Every field retains its exact header.**

[Data Observatory](README.md) · [Scientific spreads](figures/README.md) · [Machine-readable inventory](DATA_INVENTORY.json) · [Original input manifest](../models/manifest.json)

**12 CSVs · 98,759 table rows · 61 column definitions · one real archive extract · 11 synthetic/reference tables.** Row totals combine different kinds of numerical records; they are not a count of independent observations.

Units below come from the recorded sidecar or an explicitly identified model definition. An unknown unit is shown as **unit not recorded / TBD**. Storage ranges describe the checked-in file; they do not supply confidence intervals, physical bounds or calibration. Preview values are rounded for reading; source CSV bytes retain full precision.

| Table | Rows | Columns | Evidence | View |
|:--|--:|--:|:--|:--|
| [Exoplanet catalog snapshot](#exoplanet-sample) | 200 | 6 | Real public catalog | [CSV](../models/data/exoplanet_sample.csv) · [Fields](#exoplanet-sample) |
| [Balloon thermal network](#balloon-thermal) | 1,441 | 10 | Synthetic / illustrative | [CSV](../models/data/balloon_thermal.csv) · [Fields](#balloon-thermal) |
| [Hydrologic reservoir ledger](#hydrologic-reservoir) | 241 | 7 | Synthetic / illustrative | [CSV](../models/data/hydrologic_reservoir.csv) · [Fields](#hydrologic-reservoir) |
| [One-axis attitude response](#one-axis-attitude) | 2,401 | 4 | Synthetic / illustrative | [CSV](../models/data/one_axis_attitude.csv) · [Fields](#one-axis-attitude) |
| [Two-body orbit states](#two-body-orbit) | 4,001 | 7 | Synthetic / illustrative | [CSV](../models/data/two_body_orbit.csv) · [Fields](#two-body-orbit) |
| [Orbital timestep refinement](#two-body-convergence) | 3 | 2 | Synthetic / illustrative | [CSV](../models/data/two_body_convergence.csv) · [Fields](#two-body-convergence) |
| [Synthetic spectral mixture](#spectral-mixture) | 180 | 7 | Synthetic / illustrative | [CSV](../models/data/spectral_mixture.csv) · [Fields](#spectral-mixture) |
| [Spectral noise-realization estimates](#spectral-monte-carlo) | 2,000 | 3 | Synthetic / illustrative | [CSV](../models/data/spectral_monte_carlo.csv) · [Fields](#spectral-monte-carlo) |
| [Hypothetical binary liquidus](#ideal-binary-liquidus) | 600 | 4 | Synthetic / illustrative | [CSV](../models/data/ideal_binary_liquidus.csv) · [Fields](#ideal-binary-liquidus) |
| [Mandelbrot finite-grid field](#mandelbrot) | 43,621 | 4 | Synthetic / illustrative | [CSV](../models/data/mandelbrot.csv) · [Fields](#mandelbrot) |
| [Julia finite-grid field](#julia) | 43,621 | 4 | Synthetic / illustrative | [CSV](../models/data/julia.csv) · [Fields](#julia) |
| [Sphere drag reference values](#sphere-drag) | 450 | 3 | Synthetic / illustrative | [CSV](../models/data/sphere_drag.csv) · [Fields](#sphere-drag) |

## What the missingness flags mean

The included files contain **9 blank cells**, **10,683 NaN cells**, and **0 other nonfinite numeric tokens**. The nine blank host-metallicity values in the catalog are separate from undefined numerical quantities in synthetic models.

A NaN exterior-distance estimate does not itself imply an unresolved fractal point: the Julia critical point (0,0) escapes at iteration 29 but has a vanishing derivative and no usable derivative-based distance estimate. Use the explicit escape-count column. The reservoir's last recharge cell is intentionally NaN because there is no next forcing bin. Zero remains a numerical value; it is not substituted for missingness.

## exoplanet sample

### Exoplanet catalog snapshot

![real_public_catalog_snapshot](figures/badge-catalog.svg)

**200 rows · 6 columns · 14,272 bytes.** 9 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/exoplanet_sample.csv) · [Source sidecar](../models/data/exoplanet_sample.provenance.json) · [Original figure](../models/figures/09_real_exoplanet_sample.svg) · [Diagnostic spread](../data/figures/10_catalog_values_and_coverage.svg) · [Figure ledger](../data/figures/10_catalog_values_and_coverage.provenance.json)

**Engineering starting points:** [C05](../research/C/C05-kepler-worldforge/README.md) · [C23](../research/C/C23-kepler-metal-worlds/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `pl_name`, `hostname`, `pl_orbper`, `pl_rade`, `st_met`, `discoverymethod`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `pl_name` | not applicable (identifier/category) | Published planet name. | 0 | 0 | 0 | — text / no finite numbers |
| `hostname` | not applicable (identifier/category) | Published host name. | 0 | 0 | 0 | — text / no finite numbers |
| `pl_orbper` | days | Composite-table orbital-period value. | 0 | 0 | 0 | 0.5735 → 2.061e+04 |
| `pl_rade` | Earth radii | Composite-table planet-radius value. | 0 | 0 | 0 | 0.338 → 23.99 |
| `st_met` | dex relative to solar | Published host metallicity; abundance basis and per-value references are absent from this extract. | 9 | 0 | 0 | -0.65 → 0.545 |
| `discoverymethod` | not applicable (identifier/category) | Archive discovery-method category. | 0 | 0 | 0 | — text / no finite numbers |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `pl_name` | 24 Sex b | CD-35 2722 B b |
| `hostname` | 24 Sex | CD-35 2722 B |
| `pl_orbper` | 452.8 | 171.1 |
| `pl_rade` | 13.4 | 13.9 |
| `st_met` | -0.03 | 0.27 |
| `discoverymethod` | Radial Velocity | Radial Velocity |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `31d0b4ecc46e1fb7a57d41e4f35467adbfbd6d37137050b70ac6f39881f8e90e`

**Model/source function:** `fetch_exoplanets` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Saved 200-row query-ordered extract; the source sidecar records an intended TOP 200 ORDER BY pl_name request. Global first-200 ranking was not independently verified.
- Discovery method, completeness, missing-radius selection, request truncation and follow-up biases apply; not random or representative.
- Composite parameter rows may combine values from different publications; not necessarily self-consistent.
- No uncertainties, detection-efficiency correction, metallicity basis or per-parameter references in this small educational extract.
- No occurrence rates, physical class labels, mass-radius claims or causal metallicity inference from this plot.

**Historical source wording:** The unchanged acquisition sidecar and original numerical view describe an alphabetically truncated selection. That is the recorded acquisition interpretation. The saved request and response are retained, but global first-200 ranking against the complete archive was not independently verified. Current captions describe the returned 200-row query-ordered extract.

| Field | Unit evidence |
|:--|:--|
| `pl_name` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): planet name string |
| `hostname` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): host name string |
| `pl_orbper` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): days |
| `pl_rade` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): Earth radii |
| `st_met` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): dex relative to solar; nullable; abundance basis requires archive metadata |
| `discoverymethod` | [documented_sidecar](../models/data/exoplanet_sample.provenance.json): categorical archive discovery method |

**Recorded parameters / query context**

```json
{
  "provider": "NASA Exoplanet Archive",
  "retrieved_utc": "2026-10-02T09:01:19.367519+00:00",
  "table": "pscomppars",
  "query_adql": "SELECT TOP 200 pl_name,hostname,pl_orbper,pl_rade,st_met,discoverymethod FROM pscomppars WHERE pl_orbper IS NOT NULL AND pl_rade IS NOT NULL ORDER BY pl_name"
}
```

</details>

## balloon thermal

### Balloon thermal network

![synthetic_illustrative](figures/badge-synthetic.svg)

**1,441 rows · 10 columns · 215,252 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/balloon_thermal.csv) · [Source sidecar](../models/data/balloon_thermal.json) · [Original figure](../models/figures/03_balloon_thermal.svg) · [Diagnostic spread](../data/figures/11_thermal_power_and_response.svg) · [Figure ledger](../data/figures/11_thermal_power_and_response.provenance.json)

**Engineering starting points:** [E06](../research/E/E06-apollo-thermalis/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `time_s`, `wall_K`, `payload_K`, `air_K`, `radiative_sink_K`, `h_W_m2_K`, `absorbed_W`, `convection_W`, `radiation_W`, `wall_to_payload_W`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `time_s` | s | Elapsed model time. | 0 | 0 | 0 | 0 → 1.44e+04 |
| `wall_K` | K | Uniform wall-node temperature. | 0 | 0 | 0 | 240.2 → 285 |
| `payload_K` | K | Uniform payload-node temperature. | 0 | 0 | 0 | 244.3 → 285.3 |
| `air_K` | K | Prescribed air temperature. | 0 | 0 | 0 | 220 → 270 |
| `radiative_sink_K` | K | Prescribed radiative-sink temperature. | 0 | 0 | 0 | 208 → 258 |
| `h_W_m2_K` | W m^-2 K^-1 | Prescribed convective heat-transfer coefficient. | 0 | 0 | 0 | 0.7355 → 8 |
| `absorbed_W` | W | Prescribed absorbed power entering the wall. | 0 | 0 | 0 | 8 → 8 |
| `convection_W` | W | Convective power; positive enters the wall. | 0 | 0 | 0 | -18 → -2.227 |
| `radiation_W` | W | Radiative power; positive enters the wall. | 0 | 0 | 0 | -13.82 → -9.289 |
| `wall_to_payload_W` | W | Conductive power from wall to payload; negative means the direction reverses. | 0 | 0 | 0 | -7.082 → 0 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `time_s` | 0 | 10 |
| `wall_K` | 285 | 284.8 |
| `payload_K` | 285 | 285 |
| `air_K` | 270 | 269.9 |
| `radiative_sink_K` | 258 | 257.9 |
| `h_W_m2_K` | 8 | 7.979 |
| `absorbed_W` | 8 | 8 |
| `convection_W` | -18 | -17.8 |
| `radiation_W` | -13.82 | -13.74 |
| `wall_to_payload_W` | 0 | -0.1846 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `e590de3982977a790b462b0c574f7981ffeb0874699a937d1e1fa1ceb218e74a`

**Model/source function:** `demo_thermal` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Uniform temperature per node; radiation area includes assumed view factor.
- Air, radiative sink, convection and solar forcing are prescribed synthetic histories.
- No ascent trajectory, atmosphere calibration, rarefied-flow correction or qualification claim.

| Field | Unit evidence |
|:--|:--|
| `time_s` | [documented_sidecar](../models/data/balloon_thermal.json): s |
| `wall_K` | [documented_sidecar](../models/data/balloon_thermal.json): K |
| `payload_K` | [documented_sidecar](../models/data/balloon_thermal.json): K |
| `air_K` | [documented_sidecar](../models/data/balloon_thermal.json): K |
| `radiative_sink_K` | [documented_sidecar](../models/data/balloon_thermal.json): K |
| `h_W_m2_K` | [documented_sidecar](../models/data/balloon_thermal.json): W m^-2 K^-1 |
| `absorbed_W` | [documented_sidecar](../models/data/balloon_thermal.json): W |
| `convection_W` | [documented_sidecar](../models/data/balloon_thermal.json): W |
| `radiation_W` | [documented_sidecar](../models/data/balloon_thermal.json): W |
| `wall_to_payload_W` | [documented_sidecar](../models/data/balloon_thermal.json): W |

**Recorded parameters / query context**

```json
{
  "C_wall_J_K": 1200.0,
  "C_payload_J_K": 850.0,
  "area_m2": 0.15,
  "emissivity": 0.75,
  "conductance_W_K": 0.8,
  "payload_power_W": 3.0
}
```

</details>

## hydrologic reservoir

### Hydrologic reservoir ledger

![synthetic_illustrative](figures/badge-synthetic.svg)

**241 rows · 7 columns · 26,052 bytes.** 1 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/hydrologic_reservoir.csv) · [Source sidecar](../models/data/hydrologic_reservoir.json) · [Original figure](../models/figures/05_hydrologic_reservoir.svg) · [Diagnostic spread](../data/figures/12_hydrologic_water_ledger.svg) · [Figure ledger](../data/figures/12_hydrologic_water_ledger.provenance.json)

**Engineering starting points:** [B23](../research/B/B23-hydra-mission-control-watershed-decisions-under-uncertainty/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `time_day`, `storage_mm`, `outflow_mm_day`, `cumulative_outflow_mm`, `cumulative_recharge_mm`, `mass_balance_residual_mm`, `next_bin_recharge_mm_day`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `time_day` | day | Elapsed reservoir model time at bin boundaries. | 0 | 0 | 0 | 0 → 60 |
| `storage_mm` | mm | Remaining water depth in the conceptual storage reservoir. | 0 | 0 | 0 | 2.719 → 20.14 |
| `outflow_mm_day` | mm/day | Instantaneous outflow k times storage. | 0 | 0 | 0 | 0.3263 → 2.417 |
| `cumulative_outflow_mm` | mm | Accumulated released water depth. | 0 | 0 | 0 | 0 → 53.72 |
| `cumulative_recharge_mm` | mm | Accumulated effective input water depth. | 0 | 0 | 0 | 0 → 38.59 |
| `mass_balance_residual_mm` | mm | Storage + cumulative outflow − initial storage − cumulative recharge. | 0 | 0 | 0 | -4.263e-14 → 8.882e-16 |
| `next_bin_recharge_mm_day` | mm/day | Effective recharge assigned to the next forcing bin; final boundary has no next bin. | 0 | 1 | 0 | 0 → 11.89 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `time_day` | 0 | 0.25 |
| `storage_mm` | 20 | 19.41 |
| `outflow_mm_day` | 2.4 | 2.329 |
| `cumulative_outflow_mm` | 0 | 0.5911 |
| `cumulative_recharge_mm` | 0 | 0 |
| `mass_balance_residual_mm` | 0 | 0 |
| `next_bin_recharge_mm_day` | 0 | 0 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `54ee19e9ea1a31e587b4479d9ef0581e536fce6d5c0a3441600afae0895043a9`

**Model/source function:** `demo_hydrology` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Recharge is effective water entering storage, not rainfall; ET and interception are omitted.
- One linear reservoir is a pedagogical baseline, not calibrated flood decision support.

| Field | Unit evidence |
|:--|:--|
| `time_day` | [documented_sidecar](../models/data/hydrologic_reservoir.json): day |
| `storage_mm` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm |
| `outflow_mm_day` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm/day |
| `cumulative_outflow_mm` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm |
| `cumulative_recharge_mm` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm |
| `mass_balance_residual_mm` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm |
| `next_bin_recharge_mm_day` | [documented_sidecar](../models/data/hydrologic_reservoir.json): mm/day; final NaN |

**Recorded parameters / query context**

```json
{
  "k_day_inverse": 0.12,
  "dt_day": 0.25,
  "initial_storage_mm": 20.0
}
```

</details>

## one axis attitude

### One-axis attitude response

![synthetic_illustrative](figures/badge-synthetic.svg)

**2,401 rows · 4 columns · 190,136 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/one_axis_attitude.csv) · [Source sidecar](../models/data/one_axis_attitude.json) · [Original figure](../models/figures/06_one_axis_attitude.svg) · [Diagnostic spread](../data/figures/13_attitude_phase_and_authority.svg) · [Figure ledger](../data/figures/13_attitude_phase_and_authority.provenance.json)

**Engineering starting points:** [I10](../research/I/I10-gemini-pointlock/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `time_s`, `theta_rad`, `omega_rad_s`, `control_torque_Nm`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `time_s` | s | Elapsed model time. | 0 | 0 | 0 | 0 → 120 |
| `theta_rad` | rad | One-axis angle error relative to the fixed zero-angle target. | 0 | 0 | 0 | -0.03473 → 0.6109 |
| `omega_rad_s` | rad/s | One-axis angular rate. | 0 | 0 | 0 | -0.1388 → 0.00818 |
| `control_torque_Nm` | N m | Applied, clipped PD control torque; excludes the separate disturbance torque. | 0 | 0 | 0 | -0.008 → 0.003901 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `time_s` | 0 | 0.05 |
| `theta_rad` | 0.6109 | 0.6108 |
| `omega_rad_s` | 0 | -0.003333 |
| `control_torque_Nm` | -0.008 | -0.008 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `7f8c1498b3d766337c7ddf20e8d12860d99f1c33a3e5259096ec935713a93a0d`

**Model/source function:** `demo_attitude` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Single rigid rotational degree of freedom, exact states and a fixed zero-angle reference.
- No wheel momentum management, three-axis quaternion dynamics, estimator or sensor delay.
- Illustrates control tradeoffs; no spacecraft implementation or qualification.

| Field | Unit evidence |
|:--|:--|
| `time_s` | [documented_sidecar](../models/data/one_axis_attitude.json): s |
| `theta_rad` | [documented_sidecar](../models/data/one_axis_attitude.json): rad |
| `omega_rad_s` | [documented_sidecar](../models/data/one_axis_attitude.json): rad/s |
| `control_torque_Nm` | [documented_sidecar](../models/data/one_axis_attitude.json): N m |

**Recorded parameters / query context**

```json
{
  "inertia_kg_m2": 0.12,
  "kp_Nm_rad": 0.03,
  "kd_Nm_s_rad": 0.08,
  "torque_limit_Nm": 0.008,
  "initial_angle_deg": 35.0,
  "disturbance_amplitude_Nm": 2.5e-05
}
```

</details>

## two body orbit

### Two-body orbit states

![synthetic_illustrative](figures/badge-synthetic.svg)

**4,001 rows · 7 columns · 549,951 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/two_body_orbit.csv) · [Source sidecar](../models/data/two_body_orbit.json) · [Original figure](../models/figures/07_two_body_convergence.svg) · [Diagnostic spread](../data/figures/14_orbit_conservation_and_refinement.svg) · [Figure ledger](../data/figures/14_orbit_conservation_and_refinement.provenance.json)

**Engineering starting points:** [I08](../research/I/I08-voyager-frameforge/README.md) · [I12](../research/I/I12-pioneer-phobos-pathfinder/README.md) · [I13](../research/I/I13-osiris-apophis-horizon/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `time_normalized`, `x`, `y`, `vx`, `vy`, `specific_energy`, `specific_angular_momentum`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `time_normalized` | sqrt(a_ref^3 / mu_ref) | Elapsed time divided by the reference gravitational time scale. | 0 | 0 | 0 | 0 → 62.83 |
| `x` | a_ref | Normalized Cartesian x-coordinate. | 0 | 0 | 0 | -1.3 → 0.7 |
| `y` | a_ref | Normalized Cartesian y-coordinate. | 0 | 0 | 0 | -0.954 → 0.9555 |
| `vx` | sqrt(mu_ref/a_ref) | Normalized Cartesian x-velocity. | 0 | 0 | 0 | -1.048 → 1.05 |
| `vy` | sqrt(mu_ref/a_ref) | Normalized Cartesian y-velocity. | 0 | 0 | 0 | -0.7336 → 1.363 |
| `specific_energy` | mu_ref/a_ref | Specific orbital energy, normalized by its reference scale. | 0 | 0 | 0 | -0.5 → -0.4999 |
| `specific_angular_momentum` | sqrt(mu_ref*a_ref) | Planar specific angular momentum, normalized by its reference scale. | 0 | 0 | 0 | 0.9539 → 0.9539 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `time_normalized` | 0 | 0.01571 |
| `x` | 0.7 | 0.6997 |
| `y` | 0 | 0.02141 |
| `vx` | 0 | -0.03205 |
| `vy` | 1.363 | 1.362 |
| `specific_energy` | -0.5 | -0.5 |
| `specific_angular_momentum` | 0.9539 | 0.9539 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `26346ffc7b03f09342a18bb0cdc83d5e31ace0b18e364b79b912455a6712098f`

**Model/source function:** `demo_orbit` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Point-mass two-body gravity in normalized units; no maneuvers, atmospheric drag or third bodies.
- Demonstrates numerical conservation, not an operational trajectory or planetary-defense solution.

| Field | Unit evidence |
|:--|:--|
| `time_normalized` | [documented_sidecar](../models/data/two_body_orbit.json): sqrt(a_ref^3 / mu_ref) |
| `x` | [documented_sidecar](../models/data/two_body_orbit.json): a_ref |
| `y` | [documented_sidecar](../models/data/two_body_orbit.json): a_ref |
| `vx` | [documented_sidecar](../models/data/two_body_orbit.json): sqrt(mu_ref/a_ref) |
| `vy` | [documented_sidecar](../models/data/two_body_orbit.json): sqrt(mu_ref/a_ref) |
| `specific_energy` | [documented_sidecar](../models/data/two_body_orbit.json): mu_ref/a_ref |
| `specific_angular_momentum` | [documented_sidecar](../models/data/two_body_orbit.json): sqrt(mu_ref*a_ref) |

**Recorded parameters / query context**

```json
{
  "normalized_mu": 1,
  "normalized_semimajor_axis": 1,
  "eccentricity": 0.3,
  "period_normalized_time": 6.283185307179586,
  "duration_periods": 10
}
```

</details>

## two body convergence

### Orbital timestep refinement

![synthetic_illustrative](figures/badge-synthetic.svg)

**3 rows · 2 columns · 129 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/two_body_convergence.csv) · [Source sidecar](../models/data/two_body_orbit.json) · [Original figure](../models/figures/07_two_body_convergence.svg) · [Diagnostic spread](../data/figures/14_orbit_conservation_and_refinement.svg) · [Figure ledger](../data/figures/14_orbit_conservation_and_refinement.provenance.json)

**Engineering starting points:** [I08](../research/I/I08-voyager-frameforge/README.md) · [I12](../research/I/I12-pioneer-phobos-pathfinder/README.md) · [I13](../research/I/I13-osiris-apophis-horizon/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `steps_per_period`, `maximum_relative_energy_error`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `steps_per_period` | count per orbital period (dimensionless) | Number of numerical integrator steps per normalized orbital period. | 0 | 0 | 0 | 100 → 400 |
| `maximum_relative_energy_error` | dimensionless | Maximum absolute relative specific-energy error across the ten-period integration. | 0 | 0 | 0 | 0.0001342 → 0.002155 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `steps_per_period` | 100 | 200 |
| `maximum_relative_energy_error` | 0.002155 | 0.0005371 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `91b4d6524ce07e6590807af8f16b793347351240c7475793f630ade259294434`

**Model/source function:** `demo_orbit` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Point-mass two-body gravity in normalized units; no maneuvers, atmospheric drag or third bodies.
- Demonstrates numerical conservation, not an operational trajectory or planetary-defense solution.

| Field | Unit evidence |
|:--|:--|
| `steps_per_period` | [verified_model_definition](../models/models.py): demo_orbit writes its explicit steps_per_orbit counts. |
| `maximum_relative_energy_error` | [verified_model_definition](../models/models.py): demo_orbit defines rel=(energy-energy[0])/abs(energy[0]) and stores max(abs(rel)). |

**Recorded parameters / query context**

```json
{
  "normalized_mu": 1,
  "normalized_semimajor_axis": 1,
  "eccentricity": 0.3,
  "period_normalized_time": 6.283185307179586,
  "duration_periods": 10
}
```

</details>

## spectral mixture

### Synthetic spectral mixture

![synthetic_illustrative](figures/badge-synthetic.svg)

**180 rows · 7 columns · 22,291 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/spectral_mixture.csv) · [Source sidecar](../models/data/spectral_mixture.json) · [Original figure](../models/figures/08_spectral_identifiability.svg) · [Diagnostic spread](../data/figures/15_spectral_information_and_noise.svg) · [Figure ledger](../data/figures/15_spectral_information_and_noise.provenance.json)

**Engineering starting points:** [C08](../research/C/C08-mars-nili-spectral-vault/README.md) · [H09](../research/H/H09-perseverance-lake-archive/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `wavelength_um`, `endmember_A`, `endmember_B`, `weak_B`, `observed`, `weak_observed`, `fit`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `wavelength_um` | µm | Synthetic spectral band coordinate. | 0 | 0 | 0 | 1 → 2.5 |
| `endmember_A` | dimensionless reflectance | Invented endmember-A reflectance. | 0 | 0 | 0 | 0.3704 → 0.55 |
| `endmember_B` | dimensionless reflectance | Invented separated endmember-B reflectance. | 0 | 0 | 0 | 0.3301 → 0.5 |
| `weak_B` | dimensionless reflectance | Invented endmember close to A, used to expose weak identifiability. | 0 | 0 | 0 | 0.3705 → 0.5499 |
| `observed` | dimensionless reflectance | Synthetic noisy linear mixture of the separated pair; not a measured spectrum. | 0 | 0 | 0 | 0.397 → 0.5506 |
| `weak_observed` | dimensionless reflectance | Synthetic noisy mixture of the nearly identical pair. | 0 | 0 | 0 | 0.367 → 0.5692 |
| `fit` | dimensionless reflectance | Unconstrained least-squares linear mixture fitted to the separated-pair noisy spectrum. | 0 | 0 | 0 | 0.4144 → 0.533 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `wavelength_um` | 1 | 1.008 |
| `endmember_A` | 0.4838 | 0.4692 |
| `endmember_B` | 0.5 | 0.5 |
| `weak_B` | 0.4838 | 0.4693 |
| `observed` | 0.4877 | 0.4874 |
| `weak_observed` | 0.4783 | 0.4656 |
| `fit` | 0.4893 | 0.4797 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `af89ffdc0661479ca0f7dbf4561ef10abe46f5ffa06f3f2794f8093db37af5d7`

**Model/source function:** `demo_spectra` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Invented Gaussian absorption bands; no measured mineral library or Mars observations.
- Linear areal mixture, independent known-variance Gaussian errors, exactly known endmembers.
- Near-collinear endmembers produce unphysical unconstrained weights; adding priors does not add new information.
- Real intimate mixtures, scattering, grain size and correlated calibration need a richer model.

| Field | Unit evidence |
|:--|:--|
| `wavelength_um` | [documented_sidecar](../models/data/spectral_mixture.json): µm |
| `endmember_A` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |
| `endmember_B` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |
| `weak_B` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |
| `observed` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |
| `weak_observed` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |
| `fit` | [verified_model_definition](../models/models.py): demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance. |

**Recorded parameters / query context**

```json
{
  "true_A_fraction": 0.65,
  "noise_sigma": 0.008,
  "monte_carlo_runs": 2000
}
```

</details>

## spectral monte carlo

### Spectral noise-realization estimates

![synthetic_illustrative](figures/badge-synthetic.svg)

**2,000 rows · 3 columns · 86,529 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/spectral_monte_carlo.csv) · [Source sidecar](../models/data/spectral_mixture.json) · [Original figure](../models/figures/08_spectral_identifiability.svg) · [Diagnostic spread](../data/figures/15_spectral_information_and_noise.svg) · [Figure ledger](../data/figures/15_spectral_information_and_noise.provenance.json)

**Engineering starting points:** [C08](../research/C/C08-mars-nili-spectral-vault/README.md) · [H09](../research/H/H09-perseverance-lake-archive/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `realization`, `f_separated`, `f_nearly_identical`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `realization` | index (dimensionless) | Zero-based synthetic noise-realization index; not a physical observable. | 0 | 0 | 0 | 0 → 1999 |
| `f_separated` | dimensionless fraction | Unconstrained estimated A fraction from separated endmembers. | 0 | 0 | 0 | 0.6083 → 0.6761 |
| `f_nearly_identical` | dimensionless fraction | Unconstrained estimated A fraction from near-identical endmembers; values outside [0,1] are retained. | 0 | 0 | 0 | -41.07 → 26.76 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `realization` | 0 | 1 |
| `f_separated` | 0.6521 | 0.6585 |
| `f_nearly_identical` | 2.701 | 9.185 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `b8e4ed10b7fa6201e7081cd1557ea5cbb44b6f7109ca237de4c3452c215ba4f3`

**Model/source function:** `demo_spectra` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Invented Gaussian absorption bands; no measured mineral library or Mars observations.
- Linear areal mixture, independent known-variance Gaussian errors, exactly known endmembers.
- Near-collinear endmembers produce unphysical unconstrained weights; adding priors does not add new information.
- Real intimate mixtures, scattering, grain size and correlated calibration need a richer model.

| Field | Unit evidence |
|:--|:--|
| `realization` | [verified_model_definition](../models/models.py): demo_spectra writes np.arange(len(mc_strong)). |
| `f_separated` | [verified_model_definition](../models/models.py): demo_spectra generates fractions; mixture_fraction defines a dimensionless linear mixture weight. |
| `f_nearly_identical` | [verified_model_definition](../models/models.py): demo_spectra uses the same unconstrained mixture-weight definition for the near-identical pair. |

**Recorded parameters / query context**

```json
{
  "true_A_fraction": 0.65,
  "noise_sigma": 0.008,
  "monte_carlo_runs": 2000
}
```

</details>

## ideal binary liquidus

### Hypothetical binary liquidus

![synthetic_illustrative](figures/badge-synthetic.svg)

**600 rows · 4 columns · 45,049 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/ideal_binary_liquidus.csv) · [Source sidecar](../models/data/ideal_binary_liquidus.json) · [Original figure](../models/figures/02_ideal_binary_liquidus.svg) · [Diagnostic spread](../data/figures/16_ideal_binary_phase_regions.svg) · [Figure ledger](../data/figures/16_ideal_binary_phase_regions.provenance.json)

**Engineering starting points:** [A02](../research/A/A02-new-horizons-cryophase/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `x_B`, `T_A_K`, `T_B_K`, `liquidus_K`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `x_B` | mole fraction | B mole fraction at the plotted liquidus boundary of a hypothetical A–B binary. | 0 | 0 | 0 | 0.0001 → 0.9999 |
| `T_A_K` | K | A-component saturation branch under ideal-liquid/pure-solid assumptions. | 0 | 0 | 0 | 9.905 → 63 |
| `T_B_K` | K | B-component saturation branch under ideal-liquid/pure-solid assumptions. | 0 | 0 | 0 | 7.932 → 60 |
| `liquidus_K` | K | Maximum of the two saturation branches: stable liquidus envelope. | 0 | 0 | 0 | 42.56 → 63 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `x_B` | 0.0001 | 0.001769 |
| `T_A_K` | 63 | 62.94 |
| `T_B_K` | 7.932 | 10.88 |
| `liquidus_K` | 63 | 62.94 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `43d76659b57496967f931a3389bf397d08f4dc0a1bf36ec2a30cddd4b4756689`

**Model/source function:** `demo_liquidus` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Ideal liquid; immiscible pure solids; constant fusion enthalpy; fixed unspecified pressure.
- No calibrated prediction of actual Pluto volatile chemistry, pressure, solid solutions or kinetics.

| Field | Unit evidence |
|:--|:--|
| `x_B` | [documented_sidecar](../models/data/ideal_binary_liquidus.json): mole fraction |
| `T_A_K` | [documented_sidecar](../models/data/ideal_binary_liquidus.json): K |
| `T_B_K` | [documented_sidecar](../models/data/ideal_binary_liquidus.json): K |
| `liquidus_K` | [documented_sidecar](../models/data/ideal_binary_liquidus.json): K |

**Recorded parameters / query context**

```json
{
  "Tm_A_K": 63,
  "Tm_B_K": 60,
  "fusion_A_J_mol": 900,
  "fusion_B_J_mol": 700,
  "parameter_origin": "Invented teaching values, not N2/CO/CH4 measurements"
}
```

</details>

## mandelbrot

### Mandelbrot finite-grid field

![synthetic_illustrative](figures/badge-synthetic.svg)

**43,621 rows · 4 columns · 2,432,621 bytes.** 9,873 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/mandelbrot.csv) · [Source sidecar](../models/data/mandelbrot.json) · [Original figure](../models/figures/01_fractal_escape_distance.svg) · [Diagnostic spread](../data/figures/17_fractal_resolution_and_escape.svg) · [Figure ledger](../data/figures/17_fractal_resolution_and_escape.provenance.json)

**Engineering starting points:** [A01](../research/A/A01-artemis-fractal-navigator/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `real`, `imaginary`, `escape_iteration_0_unresolved`, `distance_estimator`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `real` | dimensionless | Real coordinate of parameter c. | 0 | 0 | 0 | -2.1 → 0.7 |
| `imaginary` | dimensionless | Imaginary coordinate of parameter c. | 0 | 0 | 0 | -1.2 → 1.2 |
| `escape_iteration_0_unresolved` | iteration count (dimensionless) | First escape iteration; zero means unresolved at the finite iteration budget. | 0 | 0 | 0 | 0 → 160 |
| `distance_estimator` | dimensionless | Derivative-based asymptotic exterior estimate; undefined values cannot determine escape status by themselves. | 0 | 9,873 | 0 | 3.813e-16 → 2.136 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `real` | -2.1 | -2.088 |
| `imaginary` | -1.2 | -1.2 |
| `escape_iteration_0_unresolved` | 1 | 1 |
| `distance_estimator` | 2.136 | 2.117 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `7555e947d17fe0bc3da2a376aae385e2ebcc8f2f5c2e1590e57c12185cbede4e`

**Model/source function:** `demo_fractals` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Finite iteration cannot certify set membership.
- Distance is an asymptotic exterior estimator, not exact distance.

| Field | Unit evidence |
|:--|:--|
| `real` | [documented_sidecar](../models/data/mandelbrot.json): dimensionless |
| `imaginary` | [documented_sidecar](../models/data/mandelbrot.json): dimensionless |
| `escape_iteration_0_unresolved` | [verified_model_definition](../models/models.py): fractal_escape records an integer iteration count; its coordinates and map are dimensionless. Sidecar 'integer' states a representation rather than a physical unit. |
| `distance_estimator` | [documented_sidecar](../models/data/mandelbrot.json): dimensionless; NaN unresolved |

**Recorded parameters / query context**

```json
{
  "grid": [
    241,
    181
  ],
  "max_iter": 160,
  "julia_c": null,
  "escape_radius": 2
}
```

</details>

## julia

### Julia finite-grid field

![synthetic_illustrative](figures/badge-synthetic.svg)

**43,621 rows · 4 columns · 2,520,905 bytes.** 809 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/julia.csv) · [Source sidecar](../models/data/julia.json) · [Original figure](../models/figures/01_fractal_escape_distance.svg) · [Diagnostic spread](../data/figures/17_fractal_resolution_and_escape.svg) · [Figure ledger](../data/figures/17_fractal_resolution_and_escape.provenance.json)

**Engineering starting points:** [A01](../research/A/A01-artemis-fractal-navigator/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `real`, `imaginary`, `escape_iteration_0_unresolved`, `distance_estimator`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `real` | dimensionless | Real coordinate of starting value z₀. | 0 | 0 | 0 | -1.7 → 1.7 |
| `imaginary` | dimensionless | Imaginary coordinate of starting value z₀. | 0 | 0 | 0 | -1.2 → 1.2 |
| `escape_iteration_0_unresolved` | iteration count (dimensionless) | First escape iteration; zero means unresolved at the finite iteration budget. | 0 | 0 | 0 | 0 → 160 |
| `distance_estimator` | dimensionless | Derivative-based asymptotic exterior estimate; undefined values cannot determine escape status by themselves. | 0 | 809 | 0 | 1.848e-10 → 1.476 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `real` | -1.7 | -1.686 |
| `imaginary` | -1.2 | -1.2 |
| `escape_iteration_0_unresolved` | 1 | 1 |
| `distance_estimator` | 1.476 | 1.46 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `5250e2479adade7c9fea89fb10f4ae9e2d31d7ff17a4c07b1a7b802eea5f62eb`

**Model/source function:** `demo_fractals` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Finite iteration cannot certify set membership.
- Distance is an asymptotic exterior estimator, not exact distance.

| Field | Unit evidence |
|:--|:--|
| `real` | [documented_sidecar](../models/data/julia.json): dimensionless |
| `imaginary` | [documented_sidecar](../models/data/julia.json): dimensionless |
| `escape_iteration_0_unresolved` | [verified_model_definition](../models/models.py): fractal_escape records an integer iteration count; its coordinates and map are dimensionless. Sidecar 'integer' states a representation rather than a physical unit. |
| `distance_estimator` | [documented_sidecar](../models/data/julia.json): dimensionless; NaN unresolved |

**Recorded parameters / query context**

```json
{
  "grid": [
    241,
    181
  ],
  "max_iter": 160,
  "julia_c": [
    -0.75,
    0.11
  ],
  "escape_radius": 2
}
```

</details>

## sphere drag

### Sphere drag reference values

![synthetic_illustrative](figures/badge-synthetic.svg)

**450 rows · 3 columns · 26,087 bytes.** 0 rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.

[Open / download CSV](../models/data/sphere_drag.csv) · [Source sidecar](../models/data/sphere_drag.json) · [Original figure](../models/figures/04_sphere_drag.svg) · [Diagnostic spread](../data/figures/18_sphere_drag_reference_departure.svg) · [Figure ledger](../data/figures/18_sphere_drag_reference_departure.provenance.json)

**Engineering starting points:** [D04](../research/D/D04-glenn-sphere-standard/README.md) These records remain proposals; table illustrations do not become project measurements.

**Exact column order:** `Re`, `Cd_Schiller_Naumann`, `Cd_Stokes_asymptote`.

| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |
|:--|:--|:--|--:|--:|--:|:--|
| `Re` | dimensionless | Reynolds number used to evaluate the reference formula. | 0 | 0 | 0 | 0.0001 → 1000 |
| `Cd_Schiller_Naumann` | dimensionless | Formula-based Schiller–Naumann drag coefficient, not a CFD result. | 0 | 0 | 0 | 0.4383 → 2.401e+05 |
| `Cd_Stokes_asymptote` | dimensionless | Creeping-flow asymptotic drag coefficient; inappropriate as a general finite-Re model. | 0 | 0 | 0 | 0.024 → 2.4e+05 |

<details>
<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>

| Field | First row | Second row |
|:--|:--|:--|
| `Re` | 0.0001 | 0.0001037 |
| `Cd_Schiller_Naumann` | 2.401e+05 | 2.316e+05 |
| `Cd_Stokes_asymptote` | 2.4e+05 | 2.315e+05 |

The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.

</details>

<details>
<summary><strong>Open source, assumptions and unit traceability</strong></summary>

**Original CSV SHA-256:** `e8b262fd7d3b4c37cb39fd2cf67ec5231ed6ce7e8e0b49a1e306b35f3431de2d`

**Model/source function:** `demo_drag` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).

**Current reading limits:**

- Continuum incompressible flow around a smooth isolated sphere; no walls or particle interactions.
- Educational correlation reference; not a CFD validation dataset or high-Mach model.
- Stokes values are asymptotic comparisons and invalid at moderate/high Re.

| Field | Unit evidence |
|:--|:--|
| `Re` | [documented_sidecar](../models/data/sphere_drag.json): dimensionless |
| `Cd_Schiller_Naumann` | [documented_sidecar](../models/data/sphere_drag.json): dimensionless |
| `Cd_Stokes_asymptote` | [documented_sidecar](../models/data/sphere_drag.json): dimensionless |

**Recorded parameters / query context**

```json
{
  "Re_range": [
    0.0001,
    1000
  ],
  "formula": "Cd=(24/Re)(1+0.15 Re^0.687)"
}
```

</details>

---

This document and [DATA_INVENTORY.json](DATA_INVENTORY.json) are generated by [build_data_inventory.py](../tools/build_data_inventory.py). It reads the immutable CSVs, sidecars and model documentation, verifies all original model-manifest assets before writing, and writes only these two inventory products. It performs no acquisition or new scientific simulation.
