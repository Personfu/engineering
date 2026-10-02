# Incoming ASTRA FORGE numerical-reference review

Reviewed incoming commit 4026dd0 as extracted under `work/docs_revision/incoming_main`, on 2026-10-02. The extracted files and current repository were not edited. No computer UI or Fusion action was performed.

Reviewed sources: `models/reference.py`, the `NumericalChecks` class in `tests/test_reference.py`, and `data/synthetic/manifest.json`. The reference.py SHA-256 at review was `b50ea43a2304e2b4ba64d95676b698b8016fff4f6e939284d014cc68c8612ee8`.

## Executed checks

Only the requested numerical class was executed, with bytecode writes disabled:

```text
python -X utf8 -m unittest tests.test_reference.NumericalChecks -v
Ran 9 tests in 0.115s
OK
```

PortfolioChecks, manifest-hash/visual tests, website checks, and unrelated repository tests were not run. The nine tests cover selected analytic/property checks plus determinism, finite values, row widths, synthetic labeling and limitations for all 20 default demonstrations. They do not establish physical validation or accuracy over all accepted non-default arguments.

## Findings

1. **The exposed escape helper's arbitrary-start domain is too broad for its fixed bailout.** `reference.py:16–21` accepts both c and an arbitrary initial z but always declares escape at |z|>2. That sufficient criterion is appropriate for the supplied Mandelbrot use with z0=0, but can misclassify bounded Julia orbits for general c. An analytic counterexample is c=−6 and z0=3: z_next=3²−6=3 at every iteration, while the current function returns 1. The supplied `fractal()` default is unaffected because it always starts at zero. Preserve this snapshot as a Mandelbrot-only helper, explicitly restricting/documenting z0=0; alternatively a separately maintained future implementation can use a c-dependent sufficient bailout and test bounded fixed points. For example, R=max(2,|c|) with strict |z|>R is sufficient for quadratic escape. This counterexample was derived by inspection; no additional test suite was executed.

2. **The power example is deliberately clipped, rather than a conservation-closed served-load calculation.** At `reference.py:203–211`, storage is clamped to [0,150] Wh, while `load_W` remains 20 W even after storage reaches zero. The code does not record unmet load or curtailed energy. Its existing limitation says “clipped ideal storage,” so there is no unsupported qualification claim. Before reusing it as an engineering ledger, label `load_W` as requested demand and explain that it is not always delivered; add curtailment/unserved-load bookkeeping only in a separately maintained extension. In an unclipped six-hour night, requested load is 120 Wh while initial storage is 50 Wh, so at least 70 Wh cannot be served under this ideal example. Do not interpret its storage curve as evidence of continuous service, dispatch feasibility, or energy closure.

3. **Minor antenna convention clarification.** `reference.py:162–169` uses polar theta measured from the dipole axis: nulls at 0°/180°, maximum at 90°. “Elevation pattern” is ambiguous without this convention. Label the angular cut explicitly; it is not conventional elevation above the horizon unless converted for a stated dipole orientation.

No other substantive mathematical error was found in the default educational kernels inspected. The liquidus sign/pure-component limit, velocity-Verlet update, exact one-node thermal solution, limited Schiller–Naumann expression, synthetic spectral/areal-mixture arithmetic, Poisson generator, scalar calibration, van Genuchten retention, Langmuir/first-order decay, half-wave pattern, base-motion transmissibility, cantilever, ring consensus, NLMS update and one-axis attitude example are internally consistent with their narrow labels. A second read-only reviewer agreed on these default-form checks and independently noted the antenna-angle convention.

## Evidence and claim boundaries

All 20 manifest entries have distinct IDs, the `SYNTHETIC EDUCATIONAL REFERENCE` class and nonempty limitations. They explicitly distinguish invented curves from Pluto materials, Eta Carinae observations, radiation dose, planetary mineral identification, wildfire measurements and qualified hardware. Orbit output is nondimensional two-body propagation; attitude is one-axis spherical inertia; suspension excludes multistage/thermal-noise physics; radiation count uncertainty warns against low-count Gaussian interpretation. These boundaries should be retained in any preserved library.

The educational labels appropriately avoid representing these kernels as completed ATLAS projects, original-team results, instrument-calibrated data, flight qualification or NASA validation. The broad README/library integration should continue that distinction. Merely preserving a kernel next to a project does not execute its full governing model or validate that project's empirical hypothesis.

The stored manifest paths and hashes were inspected as metadata, not independently verified against every extracted data file, because only NumericalChecks was authorized for execution. Relocation into a separate reference_library should preserve the synthetic labels and provenance and adjust any maintained path/import documentation separately; this review does not certify relocation integrity.

## Disposition

Maintained integration closure by the assembly author: the relocated helper now rejects nonzero Julia starts, with a regression case for c=-6,z0=3. Power requested-demand and antenna polar-angle conventions are recorded in the library guide and function docstrings. Relocation testing exposed CRLF endings in the Windows archive/export copy against LF manifest hashes: every asset was normalized only after exact SHA-256 agreement, and byte-preserving Git attributes were added. See `incoming_asset_integrity.json` and the combined release test results for execution evidence beyond the original read-only review scope.

The 20 supplied default demonstrations can be preserved as a separate, clearly labeled educational reference snapshot, with the escape-domain restriction and power/angle caveats recorded. The broader arbitrary-start escape API should not be advertised as a general Julia classifier as received. Keep the original commit and any future corrected extension distinct. No unsupported project-specific empirical or qualified-hardware result was identified in the reviewed files.
