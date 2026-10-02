"""Run numerical tests and integrity/reproducibility checks on included assets.

Usage: python verify_assets.py --regenerate-twice
The optional regeneration replaces synthetic files and plots only, reusing
the saved real catalog snapshot without network access.
"""
import argparse
import csv
import hashlib
import io
import json
import platform
import sys
import unittest
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import matplotlib
import models


def synthetic_hashes(out):
    paths = [p for p in (out/"data").glob("*") if not p.name.startswith("exoplanet_sample")]
    paths += [p for p in (out/"figures").glob("*") if not p.name.startswith("09_real")]
    return {p.relative_to(out).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def generate(out):
    out = models.setup(out)
    for demo in (models.demo_fractals, models.demo_liquidus, models.demo_thermal,
                 models.demo_drag, models.demo_hydrology, models.demo_attitude,
                 models.demo_orbit, models.demo_spectra):
        demo(out)
    models.demo_exoplanets(out)
    models.manifest(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate-twice", action="store_true")
    args = parser.parse_args()
    out = Path(__file__).resolve().parent
    reproducible = None
    if args.regenerate_twice:
        generate(out)
        first = synthetic_hashes(out)
        generate(out)
        second = synthetic_hashes(out)
        reproducible = first == second
        if not reproducible:
            raise AssertionError("Synthetic file hashes changed on identical rerun")
    else:
        first = synthetic_hashes(out)

    log = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(out), pattern="test_models.py")
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    (out/"test-results.txt").write_text(log.getvalue(), encoding="utf-8")
    if not result.wasSuccessful():
        raise AssertionError(log.getvalue())

    raw = (out/"data"/"exoplanet_sample.csv").read_bytes()
    provenance = json.loads((out/"data"/"exoplanet_sample.provenance.json").read_text(encoding="utf-8"))
    digest = hashlib.sha256(raw).hexdigest()
    if digest != provenance["sha256"]:
        raise AssertionError("Catalog CSV does not match provenance hash")
    catalog_rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    if len(catalog_rows) != provenance["rows"] or len(catalog_rows) != 200:
        raise AssertionError("Catalog row count mismatch")
    if any(float(r["pl_orbper"]) <= 0 or float(r["pl_rade"]) <= 0 for r in catalog_rows):
        raise AssertionError("Nonpositive catalog period/radius")
    for record in json.loads((out/"manifest.json").read_text(encoding="utf-8"))["assets"]:
        path = out/record["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            raise AssertionError("Manifest hash mismatch: "+record["path"])

    report = {"verified_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": sys.version, "platform": platform.platform(),
                    "numpy": np.__version__, "matplotlib": matplotlib.__version__},
        "numerical_tests": {"run": result.testsRun, "failures": len(result.failures),
                            "errors": len(result.errors), "passed": result.wasSuccessful()},
        "synthetic_files": {"checked_count": len(first), "identical_regeneration_sha256": reproducible,
                            "seed": models.SEED, "hashes": first},
        "assets": {"svg": len(list((out/"figures").glob("*.svg"))),
                   "png": len(list((out/"figures").glob("*.png"))),
                   "csv": len(list((out/"data").glob("*.csv"))),
                   "manifest_integrity": True},
        "real_catalog": {"rows": len(catalog_rows), "sha256_matches_provenance": True,
                         "positive_periods_and_radii": True,
                         "missing_stellar_metallicity_rows": sum(not row["st_met"] for row in catalog_rows),
                         "discovery_methods": sorted({row["discoverymethod"] for row in catalog_rows})},
        "numerical_metrics": {name: json.loads((out/"data"/(name+".json")).read_text(encoding="utf-8"))["metrics"]
            for name in ("ideal_binary_liquidus", "hydrologic_reservoir", "two_body_orbit", "spectral_mixture")},
        "scope": "Mathematical reduced-model checks and file integrity; no empirical validation or mission qualification."}
    (out/"verification.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {result.testsRun} numerical tests; {len(first)} synthetic files reproducible={reproducible}; "
          f"{len(catalog_rows)} catalog rows; 9 SVG + 9 PNG figures")


if __name__ == "__main__":
    main()
