# ATLAS Data Observatory

**See the values. Read the assumptions. Follow every figure to its table.**

[Scientific figure gallery](figures/README.md) · [Acquired and generated CSVs](../models/data) · [Proposed data contracts](CONTRACTS.md) · [Research register](../ENGINEERING_DOCUMENTATION.md)

![Exoplanet catalog values and field coverage](figures/10_catalog_values_and_coverage.svg)

*A real 200-row NASA Exoplanet Archive snapshot: period and radius values, discovery methods, and missing host-metallicity fields. The query selects the first 200 planet names alphabetically among rows with period and radius; it supports descriptive exploration rather than population occurrence inference.*

[Open the CSV](../models/data/exoplanet_sample.csv) · [Read acquisition provenance](../models/data/exoplanet_sample.provenance.json) · [Inspect figure provenance](figures/10_catalog_values_and_coverage.provenance.json)

## Three evidence classes

| Visible label | What is actually present | Where to read it |
|:--|:--|:--|
| ![Real public catalog](figures/badge-catalog.svg) | Published archive values with a saved query, access time, row selection and original-file hash. Composite catalog values may include estimates or combine publications; no error bars were acquired in this small extract. | [200-row exoplanet snapshot](../models/data/exoplanet_sample.csv) and [acquisition record](../models/data/exoplanet_sample.provenance.json) |
| ![Synthetic illustrative](figures/badge-synthetic.svg) | Eight reduced-model demonstrations, with invented teaching parameters, generated numerical fields, simulated noise draws or a formula-based reference curve. | [Model definitions and limits](../models/README.md), [CSV outputs](../models/data) and [immutable asset manifest](../models/manifest.json) |
| ![Proposed empty template](figures/badge-proposed.svg) | 117 proposed record schemas, field dictionaries and header-only acquisition CSVs covering 877 defined fields. These describe future evidence and contain no original project measurements. | [Contract guide](CONTRACTS.md) and the data companions in each [research project folder](../ENGINEERING_DOCUMENTATION.md) |

## Read a scientific spread

Nine additional figure pairs expose relationships that are easier to assess visually: a heat budget, a water ledger, actuator saturation, orbital conservation, inverse-problem information, phase regions, finite numerical resolution and approximation error. Each pairs a vector SVG with a shareable PNG and an evidence ledger. The original nine model figures remain available in the [Model Foundry](../models/README.md).

| Explore | Data to inspect | Engineering record |
|:--|:--|:--|
| [Catalog values and coverage](figures/README.md#catalog-values-and-coverage) | 200 rows, discovery-method categories and nine missing metallicity values | [Session C](../research/C/README.md) |
| [Thermal power and response](figures/README.md#thermal-power-and-response) | Signed component powers and two node temperatures | [Session E](../research/E/README.md) |
| [Hydrologic water accounting](figures/README.md#hydrologic-water-ledger) | Effective recharge, outflow, storage and conservation residual | [Session B](../research/B/README.md) |
| [Control authority](figures/README.md#attitude-phase-and-authority) | Angle/rate states, requested torque and actuator bounds | [Session I](../research/I/README.md) |
| [Orbital numerical accuracy](figures/README.md#orbital-numerical-accuracy) | Energy error, angular momentum and three timestep resolutions | [Session I](../research/I/README.md) |
| [Spectral information](figures/README.md#spectral-information) | 2,000 synthetic noise-realization fraction estimates | [Sessions C](../research/C/README.md) and [H](../research/H/README.md) |
| [Ideal-binary phase regions](figures/README.md#ideal-binary-phase-regions) | A hypothetical liquidus and eutectic under declared assumptions | [Session A](../research/A/README.md) |
| [Fractal numerical resolution](figures/README.md#fractal-numerical-resolution) | Finite escape iteration fields and unresolved sampled points | [Session A](../research/A/README.md) |
| [Drag reference departures](figures/README.md#drag-reference-departures) | A drag correlation compared with its creeping-flow asymptote | [Session D](../research/D/README.md) |

## Follow the evidence

The tables in [`models/data`](../models/data) are the single copy of the included numerical inputs and outputs. The new [`data/figures`](figures) folder contains presentation assets and their source/output hashes; it duplicates no raw datasets. The [figure manifest](figures/DATA_FIGURES.json) connects each plot to its exact source files, captions, transformations and linked projects.

For an analysis to become empirical evidence, retain dataset version, calibration applicability, units, coordinate/time frame, uncertainty, missingness, exclusions and transformation history as specified in the [data management plan](../engineering/DATA_MANAGEMENT.md). The [uncertainty rules](../engineering/UNCERTAINTY_AND_DECISION_RULES.md) distinguish model uncertainty, numerical error and noise-draw intervals. Specified verification work is visible in the [case register](../registry/verification_cases.csv); it remains separate from the checks already executed on software.

## Reproduce the gallery

From the repository root, with the existing model plotting dependencies available:

```sh
python -m pip install -r models/requirements.txt
python tools/render_data_figures.py
```

The renderer reads the checked-in CSVs and sidecars, writes the nine additional SVG/PNG pairs and provenance records, and records dependency versions and its own hash. It uses no network access and does not regenerate model outputs or overwrite the original asset manifest. Exact rendered bytes can differ across plotting-library versions or platforms; numerical inputs remain identified by their hashes.
