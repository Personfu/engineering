# Final numerical/package QA

Read-only review of `work/engineering/models` on 2026-10-02. **PASS; no material numerical/package issue found.** No model code, data, figures, saved verification records or Git state were changed. Computer Use/UI tools were not used. The numerical tests verify reduced-model mathematics; they do not establish empirical accuracy or mission qualification.

## Executed test command and result

Working directory: `C:/Users/pfuru/Documents/Codex/2026-10-02/github-in-the-engineering-repository-please-2/work/engineering/models`.

```powershell
$env:PYTHONPATH = (Resolve-Path -LiteralPath ../../pythonlibs).Path
$env:PYTHONDONTWRITEBYTECODE = '1'
& 'C:/Users/pfuru/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B -m unittest -v test_models.py
```

Exit code **0**; **22 tests passed**, **0 failures**, **0 errors**; unittest reported **0.755 s**. `-B` and `PYTHONDONTWRITEBYTECODE` suppressed bytecode writes. This is the README's documented command, using the existing dependency directory instead of installing packages. The instructions explicitly say to run from the models folder, which is necessary for the local `import models`. The numerical suite is distinct from the catalog/documentation suite in `reviews/verify_portfolio.py`.

## Asset and saved-report results

| Check | Result |
|---|---|
| Manifest | All **40** unique asset paths exist; every byte count and SHA-256 matches; no data/figure asset omitted |
| Figure/data counts | **9 SVG**, **9 PNG**, **12 CSV**; both saved reports agree |
| Synthetic subset | **36** hashes match current files, current report and preserved two-run report |
| Original two-run record | `reviews/numerical_regeneration_verification.json`: regeneration comparison **true**, timestamp `2026-10-02T09:05:20.037968+00:00` |
| Later asset-only record | `models/verification.json`: regeneration comparison **null**, timestamp `2026-10-02T09:12:38.047352+00:00` |
| Record coherence | Same runtime, seed `20261002`, synthetic hash dictionary, 22-test success and numerical metrics; `null` is correctly explained in `reviews/RELEASE_VERIFICATION.md` |
| Numerical sidecars | All recorded metrics equal the corresponding data JSON sidecars |
| Real catalog | **200** rows; schema, positive period/radius checks, byte length and provenance hash all match |
| Catalog missingness/categories | **9** missing stellar metallicity values; five discovery categories agree with both reports |
| Real CSV SHA-256 | `31d0b4ecc46e1fb7a57d41e4f35467adbfbd6d37137050b70ac6f39881f8e90e` |

The verifier invokes unittest discovery against its own models directory. Its normal run writes `test-results.txt` and `verification.json`; `--regenerate-twice` additionally replaces synthetic assets and plots. I inspected that implementation and did **not** execute it during this read-only review. The existing two-run evidence was checked against the current files rather than recreated.

## Exact independent integrity check

Working directory: `C:/Users/pfuru/Documents/Codex/2026-10-02/github-in-the-engineering-repository-please-2/work/engineering`. Executed the following Python source through a PowerShell literal here-string named `$qaSource`, then `$qaSource | & 'C:/Users/pfuru/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B -`. Exit code **0**; every assertion passed. The checker reads files and prints JSON; it writes nothing.

<details>
<summary>Executed integrity-check source</summary>

```python
import csv, hashlib, io, json
from pathlib import Path
base = Path.cwd()
model = base / "models"
manifest = json.loads((model / "manifest.json").read_text(encoding="utf-8"))
current = json.loads((model / "verification.json").read_text(encoding="utf-8"))
regenerated = json.loads((base / "reviews" / "numerical_regeneration_verification.json").read_text(encoding="utf-8"))
checks = {}
records = manifest["assets"]
assert len(records) == 40
assert len({record["path"] for record in records}) == 40
for record in records:
    path = model / record["path"]
    raw = path.read_bytes()
    assert len(raw) == record["bytes"], record["path"]
    assert hashlib.sha256(raw).hexdigest() == record["sha256"], record["path"]
actual = {p.relative_to(model).as_posix() for folder in ("data", "figures") for p in (model / folder).iterdir() if p.is_file()}
assert actual == {record["path"] for record in records}
checks["manifest"] = {"assets": len(records), "all_bytes_and_hashes_match": True, "complete_asset_coverage": True}
assert current["numerical_tests"] == regenerated["numerical_tests"] == {"run": 22, "failures": 0, "errors": 0, "passed": True}
assert current["synthetic_files"]["checked_count"] == regenerated["synthetic_files"]["checked_count"] == 36
assert current["synthetic_files"]["identical_regeneration_sha256"] is None
assert regenerated["synthetic_files"]["identical_regeneration_sha256"] is True
assert current["synthetic_files"]["seed"] == regenerated["synthetic_files"]["seed"] == 20261002
assert current["synthetic_files"]["hashes"] == regenerated["synthetic_files"]["hashes"]
assert current["runtime"] == regenerated["runtime"]
for relative, expected in regenerated["synthetic_files"]["hashes"].items():
    assert hashlib.sha256((model / relative).read_bytes()).hexdigest() == expected, relative
assert len(regenerated["synthetic_files"]["hashes"]) == 36
checks["saved_regeneration"] = {"current_reproducibility": None, "preserved_two_run_reproducibility": True, "synthetic_files": 36, "saved_hashes_match_current_files": True, "same_runtime": True, "regeneration_utc": regenerated["verified_utc"], "current_verification_utc": current["verified_utc"]}
counts = {extension: len(list((model / "figures").glob("*." + extension))) for extension in ("svg", "png")}
counts["csv"] = len(list((model / "data").glob("*.csv")))
assert counts == {"svg": 9, "png": 9, "csv": 12}
assert current["assets"] == regenerated["assets"] == dict(counts, manifest_integrity=True)
checks["asset_counts"] = counts
for name, metrics in current["numerical_metrics"].items():
    sidecar = json.loads((model / "data" / (name + ".json")).read_text(encoding="utf-8"))
    assert metrics == sidecar["metrics"] == regenerated["numerical_metrics"][name]
checks["saved_metrics_match_sidecars"] = True
raw = (model / "data" / "exoplanet_sample.csv").read_bytes()
provenance = json.loads((model / "data" / "exoplanet_sample.provenance.json").read_text(encoding="utf-8"))
rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
assert len(rows) == provenance["rows"] == 200
assert hashlib.sha256(raw).hexdigest() == provenance["sha256"]
assert len(raw) == provenance["bytes"]
assert list(rows[0]) == ["pl_name", "hostname", "pl_orbper", "pl_rade", "st_met", "discoverymethod"]
assert all(float(row["pl_orbper"]) > 0 and float(row["pl_rade"]) > 0 for row in rows)
missing_met = sum(not row["st_met"] for row in rows)
methods = sorted({row["discoverymethod"] for row in rows})
assert missing_met == current["real_catalog"]["missing_stellar_metallicity_rows"] == regenerated["real_catalog"]["missing_stellar_metallicity_rows"] == 9
assert methods == current["real_catalog"]["discovery_methods"] == regenerated["real_catalog"]["discovery_methods"]
checks["real_catalog"] = {"rows": len(rows), "sha256": provenance["sha256"], "schema_and_positive_physical_values": True, "missing_stellar_metallicity": missing_met, "discovery_methods": methods}
print(json.dumps(checks, indent=2))
```

</details>
