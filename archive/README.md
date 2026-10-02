# Archive & reference kernels

**Preserved engineering history, with runnable educational examples.**

The [current ATLAS research register](../ENGINEERING_DOCUMENTATION.md) contains all 117 supplied entries in their exact A–I order. This folder preserves the parallel ASTRA FORGE contribution from [commit 4026dd0](https://github.com/Personfu/engineering/commit/4026dd081171e3ca60f42530c2ed4f9c8dfc544b): earlier dossiers, source records, 20 standard-library kernels, their synthetic outputs and technical figures. The original commit remains in Git history.

| Explore | Open |
| --- | --- |
| Preserved revision overview | [ASTRA FORGE](astra_forge/README.md) |
| Historical project dossiers | [Earlier project index](astra_forge/docs/project-index.md) |
| Historical resource records | [Source registry](astra_forge/docs/source-registry.md) |
| Runnable reference kernels | [Source code](astra_forge/models/reference.py) |
| Synthetic outputs and checksums | [Data manifest](astra_forge/data/synthetic/manifest.json) |
| Independent inspection and corrections | [Incoming numerical review](../evidence/INCOMING_REFERENCE_REVIEW.md) |
| Preservation integrity | [Incoming asset integrity](../evidence/incoming_asset_integrity.json) |

## Run a reference

From the repository root, enter the preserved collection:

```sh
cd archive/astra_forge
python -m models.run --model orbit --output run_outputs/orbit.json
python -m unittest discover -s tests -v
```

Python 3.12+ is sufficient. The educational kernels use the standard library. Generation writes to the explicitly selected output path; it does not acquire observations or operate equipment.

<details>
<summary><strong>Browse all 20 reference kernels</strong></summary>

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

</details>

## Reading the historical record

ASTRA FORGE split the supplied combined D03 title into two records, producing 118 historical work-package entries. Its D05–D08 correspond to current D04–D07. Both combined-title investigations remain in [current D03](../research/D/D03-ingenuity-descent-bubble-lab/README.md). The archived numbering describes that earlier contribution; the current registry retains the supplied 117-title baseline.

The maintained escape helper restricts its radius-two bailout to Mandelbrot z0=0 and rejects the bounded Julia counterexample c=−6, z0=3. Original received code remains accessible in the incoming commit. The ATLAS [model foundry](../models/README.md) separately provides its explicitly supported Julia demonstration.

The Windows archive/export copy had CRLF endings while the incoming manifest described LF bytes. The 20 synthetic JSON files were normalized only after every LF candidate matched its stored SHA-256. A Git attribute protects those bytes; the [integrity record](../evidence/incoming_asset_integrity.json) documents the correction without changing numerical content.

In the power kernel, `load_W` denotes requested demand. Storage clipping omits unmet-load and curtailment ledgers, so its curve does not establish continuous service or energy closure. In the antenna kernel, theta is the polar angle from the dipole axis: nulls at 0°/180° and maximum at 90°. A horizon elevation interpretation requires a stated orientation and conversion. These limits also appear in the maintained function docstrings.

These are synthetic educational references with declared, narrow domains. Their presence does not execute every project model or validate any project hypothesis. Current mathematical design records, acquired data and executed checks are discoverable through the [research atlas](../research/README.md), [data gallery](../data/README.md) and [evidence room](../evidence/README.md).
