# Supplementary engineering reference library

The [current engineering document register](../ENGINEERING_DOCUMENTATION.md) preserves all 117 supplied entries in A–I order. This library preserves the parallel ASTRA FORGE contribution from [commit 4026dd0](https://github.com/Personfu/engineering/commit/4026dd081171e3ca60f42530c2ed4f9c8dfc544b), including 20 standard-library educational kernels, their synthetic datasets and figures, source records and earlier design dossiers. The original commit remains in Git history.

The maintained reference copy is under [astra_forge](astra_forge/README.md). Earlier dossiers are explicitly labeled; they do not replace the controlled ATLAS records or create extra original topics. ASTRA FORGE split the combined D03 title into separate D03 and D04 records, producing 118 work-package entries. Its D05–D08 correspond to current D04–D07. Both of those combined-title investigations remain explicit in [current D03](../projects/D/D03.md).

## Runnable reference collection

| Kernel | Narrow demonstrated behavior |
| --- | --- |
| fractal | Finite-cap Mandelbrot escape counts with z0=0 |
| phase | Ideal binary liquidus branches with invented material parameters |
| orbit | Nondimensional two-body velocity-Verlet propagation |
| thermal | Exact one-node constant-boundary thermal response |
| drag | Limited sphere-drag correlation |
| spectrum | Invented Gaussian spectral line |
| image | Synthetic image scene |
| mixture | Invented linear spectral mixture |
| radiation | Poisson count illustration |
| calibration | Scalar calibration relationship |
| hydrology | Synthetic van Genuchten retention curve |
| adsorption | Langmuir equilibrium illustration |
| kinetics | First-order decay |
| antenna | Half-wave dipole angular cut |
| suspension | Single-stage base-excitation transmissibility |
| mechanics | Cantilever scaling |
| swarm | Fixed connected-ring consensus |
| power | Synthetic solar profile and clipped ideal storage |
| adaptive | Synthetic NLMS interference cancellation |
| attitude | Single-axis spherical-inertia control |

Run from the library directory, using Python 3.12+:

```sh
cd reference_library/astra_forge
python -m models.run --model orbit --output run_outputs/orbit.json
python -m unittest discover -s tests -v
```

The [source code](astra_forge/models/reference.py), [synthetic data manifest](astra_forge/data/synthetic/manifest.json), [earlier project index](astra_forge/docs/project-index.md) and [source registry](astra_forge/docs/source-registry.md) remain inspectable. Stored data/figure bytes are preserved; they are historical synthetic reference outputs. Output generation writes only the explicitly chosen path and does not acquire observations or operate equipment.

## Maintained corrections and interpretation

The received escape helper accepted arbitrary initial z while using a radius-two bailout. The maintained copy restricts it to Mandelbrot z0=0 and adds a rejecting regression fixture for the bounded Julia counterexample c=-6,z0=3. The original code remains accessible in the incoming commit. The ATLAS toolkit separately contains its explicitly supported Julia demonstration.

The Windows archive/export copy had CRLF endings, while the incoming manifest records LF asset bytes. The 20 synthetic JSON files were normalized only after every LF candidate matched its stored SHA-256 exactly. A byte-preserving Git attribute now protects those assets. The [integrity record](../reviews/incoming_asset_integrity.json) records this correction; numerical content is unchanged.

In the power example, `load_W` denotes requested demand. Storage clipping omits unmet-load and curtailment ledgers; the curve cannot establish continuous service or energy closure. In the antenna example, theta is the polar angle from the dipole axis: nulls at 0°/180°, maximum at 90°. It is not conventional elevation above a horizon without a stated orientation/conversion. These clarifications accompany the preserved data and are also documented in maintained function docstrings.

These 20 references complement the [eight reduced models and observational snapshot](../models/README.md). They are synthetic educational examples, rather than completed solutions of all project-specific models. The [incoming numerical review](../reviews/INCOMING_REFERENCE_REVIEW.md) records inspection scope and corrections; release verification records the executed relocation and test checks.
