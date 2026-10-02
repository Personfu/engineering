"""Build a readable, deterministic inventory of the included scientific CSVs.

No network, optional packages, generated measurements, or scientific-file writes.
CLI: python tools/build_data_inventory.py
Python API: generate(repo_root: Path) -> dict
Writes only data/DATA_INVENTORY.json and data/TABLES.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]

# Reading order groups paired CSVs with the model that produced them. All other
# CSVs discovered in models/data are appended by filename, with unknown metadata
# made explicit. This list never invents an acquisition record.
READING_ORDER = ["exoplanet_sample", "balloon_thermal", "hydrologic_reservoir",
                 "one_axis_attitude", "two_body_orbit", "two_body_convergence",
                 "spectral_mixture", "spectral_monte_carlo",
                 "ideal_binary_liquidus", "mandelbrot", "julia", "sphere_drag"]

MODEL_MAP = {
    "exoplanet_sample": ("Exoplanet catalog snapshot", "exoplanet_sample.provenance.json", ["C05", "C23"], "09_real_exoplanet_sample", "10_catalog_values_and_coverage", "fetch_exoplanets"),
    "balloon_thermal": ("Balloon thermal network", "balloon_thermal.json", ["E06"], "03_balloon_thermal", "11_thermal_power_and_response", "demo_thermal"),
    "hydrologic_reservoir": ("Hydrologic reservoir ledger", "hydrologic_reservoir.json", ["B23"], "05_hydrologic_reservoir", "12_hydrologic_water_ledger", "demo_hydrology"),
    "one_axis_attitude": ("One-axis attitude response", "one_axis_attitude.json", ["I10"], "06_one_axis_attitude", "13_attitude_phase_and_authority", "demo_attitude"),
    "two_body_orbit": ("Two-body orbit states", "two_body_orbit.json", ["I08", "I12", "I13"], "07_two_body_convergence", "14_orbit_conservation_and_refinement", "demo_orbit"),
    "two_body_convergence": ("Orbital timestep refinement", "two_body_orbit.json", ["I08", "I12", "I13"], "07_two_body_convergence", "14_orbit_conservation_and_refinement", "demo_orbit"),
    "spectral_mixture": ("Synthetic spectral mixture", "spectral_mixture.json", ["C08", "H09"], "08_spectral_identifiability", "15_spectral_information_and_noise", "demo_spectra"),
    "spectral_monte_carlo": ("Spectral noise-realization estimates", "spectral_mixture.json", ["C08", "H09"], "08_spectral_identifiability", "15_spectral_information_and_noise", "demo_spectra"),
    "ideal_binary_liquidus": ("Hypothetical binary liquidus", "ideal_binary_liquidus.json", ["A02"], "02_ideal_binary_liquidus", "16_ideal_binary_phase_regions", "demo_liquidus"),
    "mandelbrot": ("Mandelbrot finite-grid field", "mandelbrot.json", ["A01"], "01_fractal_escape_distance", "17_fractal_resolution_and_escape", "demo_fractals"),
    "julia": ("Julia finite-grid field", "julia.json", ["A01"], "01_fractal_escape_distance", "17_fractal_resolution_and_escape", "demo_fractals"),
    "sphere_drag": ("Sphere drag reference values", "sphere_drag.json", ["D04"], "04_sphere_drag", "18_sphere_drag_reference_departure", "demo_drag"),
}

DESCRIPTIONS = {
    "time_s": "Elapsed model time.", "wall_K": "Uniform wall-node temperature.",
    "payload_K": "Uniform payload-node temperature.", "air_K": "Prescribed air temperature.",
    "radiative_sink_K": "Prescribed radiative-sink temperature.",
    "h_W_m2_K": "Prescribed convective heat-transfer coefficient.",
    "absorbed_W": "Prescribed absorbed power entering the wall.",
    "convection_W": "Convective power; positive enters the wall.",
    "radiation_W": "Radiative power; positive enters the wall.",
    "wall_to_payload_W": "Conductive power from wall to payload; negative means the direction reverses.",
    "pl_name": "Published planet name.", "hostname": "Published host name.",
    "pl_orbper": "Composite-table orbital-period value.", "pl_rade": "Composite-table planet-radius value.",
    "st_met": "Published host metallicity; abundance basis and per-value references are absent from this extract.",
    "discoverymethod": "Archive discovery-method category.",
    "time_day": "Elapsed reservoir model time at bin boundaries.",
    "storage_mm": "Remaining water depth in the conceptual storage reservoir.",
    "outflow_mm_day": "Instantaneous outflow k times storage.",
    "cumulative_outflow_mm": "Accumulated released water depth.",
    "cumulative_recharge_mm": "Accumulated effective input water depth.",
    "mass_balance_residual_mm": "Storage + cumulative outflow − initial storage − cumulative recharge.",
    "next_bin_recharge_mm_day": "Effective recharge assigned to the next forcing bin; final boundary has no next bin.",
    "x_B": "B mole fraction at the plotted liquidus boundary of a hypothetical A–B binary.",
    "T_A_K": "A-component saturation branch under ideal-liquid/pure-solid assumptions.",
    "T_B_K": "B-component saturation branch under ideal-liquid/pure-solid assumptions.",
    "liquidus_K": "Maximum of the two saturation branches: stable liquidus envelope.",
    "escape_iteration_0_unresolved": "First escape iteration; zero means unresolved at the finite iteration budget.",
    "distance_estimator": "Derivative-based asymptotic exterior estimate; undefined values cannot determine escape status by themselves.",
    "theta_rad": "One-axis angle error relative to the fixed zero-angle target.",
    "omega_rad_s": "One-axis angular rate.",
    "control_torque_Nm": "Applied, clipped PD control torque; excludes the separate disturbance torque.",
    "wavelength_um": "Synthetic spectral band coordinate.",
    "endmember_A": "Invented endmember-A reflectance.",
    "endmember_B": "Invented separated endmember-B reflectance.",
    "weak_B": "Invented endmember close to A, used to expose weak identifiability.",
    "observed": "Synthetic noisy linear mixture of the separated pair; not a measured spectrum.",
    "weak_observed": "Synthetic noisy mixture of the nearly identical pair.",
    "fit": "Unconstrained least-squares linear mixture fitted to the separated-pair noisy spectrum.",
    "realization": "Zero-based synthetic noise-realization index; not a physical observable.",
    "f_separated": "Unconstrained estimated A fraction from separated endmembers.",
    "f_nearly_identical": "Unconstrained estimated A fraction from near-identical endmembers; values outside [0,1] are retained.",
    "Re": "Reynolds number used to evaluate the reference formula.",
    "Cd_Schiller_Naumann": "Formula-based Schiller–Naumann drag coefficient, not a CFD result.",
    "Cd_Stokes_asymptote": "Creeping-flow asymptotic drag coefficient; inappropriate as a general finite-Re model.",
    "steps_per_period": "Number of numerical integrator steps per normalized orbital period.",
    "maximum_relative_energy_error": "Maximum absolute relative specific-energy error across the ten-period integration.",
    "time_normalized": "Elapsed time divided by the reference gravitational time scale.",
    "x": "Normalized Cartesian x-coordinate.", "y": "Normalized Cartesian y-coordinate.",
    "vx": "Normalized Cartesian x-velocity.", "vy": "Normalized Cartesian y-velocity.",
    "specific_energy": "Specific orbital energy, normalized by its reference scale.",
    "specific_angular_momentum": "Planar specific angular momentum, normalized by its reference scale.",
}

VERIFIED_UNITS = {
    ("spectral_monte_carlo", "realization"): ("index (dimensionless)", "demo_spectra writes np.arange(len(mc_strong))."),
    ("spectral_monte_carlo", "f_separated"): ("dimensionless fraction", "demo_spectra generates fractions; mixture_fraction defines a dimensionless linear mixture weight."),
    ("spectral_monte_carlo", "f_nearly_identical"): ("dimensionless fraction", "demo_spectra uses the same unconstrained mixture-weight definition for the near-identical pair."),
    ("two_body_convergence", "steps_per_period"): ("count per orbital period (dimensionless)", "demo_orbit writes its explicit steps_per_orbit counts."),
    ("two_body_convergence", "maximum_relative_energy_error"): ("dimensionless", "demo_orbit defines rel=(energy-energy[0])/abs(energy[0]) and stores max(abs(rel))."),
}


def digest(path: Path) -> dict:
    raw=path.read_bytes()
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}


def asset(root: Path, path: Path) -> dict:
    return {"path":path.relative_to(root).as_posix(),**digest(path)}


def unit_record(stem, name, descriptor, provenance_path):
    verified=VERIFIED_UNITS.get((stem,name))
    if verified:
        return verified[0],"verified_model_definition",{"path":"models/models.py","detail":verified[1]}
    if name=="escape_iteration_0_unresolved":
        return "iteration count (dimensionless)","verified_model_definition",{"path":"models/models.py","detail":"fractal_escape records an integer iteration count; its coordinates and map are dimensionless. Sidecar 'integer' states a representation rather than a physical unit."}
    if stem=="exoplanet_sample" and name in ("pl_name","hostname","discoverymethod"):
        return "not applicable (identifier/category)","documented_sidecar",{"path":provenance_path,"detail":descriptor}
    if descriptor=="reflectance":
        return "dimensionless reflectance","verified_model_definition",{"path":"models/models.py","detail":"demo_spectra explicitly labels synthetic reflectance as dimensionless; raw sidecar says reflectance."}
    if descriptor:
        return descriptor.split(";",1)[0],"documented_sidecar",{"path":provenance_path,"detail":descriptor}
    return "unit not recorded / TBD","not_recorded",{"path":provenance_path,"detail":"No applicable column-unit entry found; no unit guessed from the name or numerical values."}


def numeric_profile(values):
    blanks=nans=other=0; finite=[]; text=[]
    for value in values:
        if not value.strip():
            blanks+=1
            continue
        try:
            number=float(value)
        except ValueError:
            text.append(value)
            continue
        if math.isnan(number): nans+=1
        elif not math.isfinite(number): other+=1
        else: finite.append(number)
    encoding="text" if text and not finite else "mixed text/numeric" if text else "numeric tokens"
    return {"blank_count":blanks,"nan_count":nans,"other_nonfinite_count":other,
            "finite_min":min(finite) if finite else None,"finite_max":max(finite) if finite else None,
            "observed_encoding":encoding,"distinct_text_values":len(set(text)) if text else None}


def format_value(value):
    if value is None or not str(value).strip(): return "— blank"
    try: number=float(value)
    except ValueError: return str(value)
    if math.isnan(number): return "NaN · undefined"
    if not math.isfinite(number): return str(value)+" · nonfinite"
    if number==0: return "0"
    return f"{number:.4g}"


def cell(value):
    return str(value).replace("|","&#124;").replace("\n"," ")


def link_from_data(repo_path, label):
    return f"[{label}](../{repo_path})"


def markdown(inventory):
    s=inventory["summary"]
    lines=["# ATLAS Table Archive","", "**Every included scientific CSV, visibly cataloged. Every field retains its exact header.**","",
           "[Data Observatory](README.md) · [Scientific spreads](figures/README.md) · [Machine-readable inventory](DATA_INVENTORY.json) · [Original input manifest](../models/manifest.json)","",
           f"**{s['dataset_count']} CSVs · {s['total_csv_rows']:,} table rows · {s['total_columns']} column definitions · one real archive extract · {s['evidence_counts'].get('synthetic_illustrative',0)} synthetic/reference tables.** Row totals combine different kinds of numerical records; they are not a count of independent observations.","",
           "Units below come from the recorded sidecar or an explicitly identified model definition. An unknown unit is shown as **unit not recorded / TBD**. Storage ranges describe the checked-in file; they do not supply confidence intervals, physical bounds or calibration. Preview values are rounded for reading; source CSV bytes retain full precision.","",
           "| Table | Rows | Columns | Evidence | View |",
           "|:--|--:|--:|:--|:--|"]
    for d in inventory["datasets"]:
        evidence="Real public catalog" if d["evidence_kind"]=="real_public_catalog_snapshot" else "Synthetic / illustrative" if d["evidence_kind"]=="synthetic_illustrative" else "Unclassified / review required"
        lines.append(f"| [{d['title']}](#{d['id'].replace('_','-')}) | {d['row_count']:,} | {d['column_count']} | {evidence} | {link_from_data(d['csv_path'],'CSV')} · [Fields](#{d['id'].replace('_','-')}) |")
    lines.extend(["", "## What the missingness flags mean", "",
                  f"The included files contain **{s['blank_cells']} blank cells**, **{s['nan_cells']:,} NaN cells**, and **{s['other_nonfinite_cells']} other nonfinite numeric tokens**. The nine blank host-metallicity values in the catalog are separate from undefined numerical quantities in synthetic models.", "",
                  "A NaN exterior-distance estimate does not itself imply an unresolved fractal point: the Julia critical point (0,0) escapes at iteration 29 but has a vanishing derivative and no usable derivative-based distance estimate. Use the explicit escape-count column. The reservoir's last recharge cell is intentionally NaN because there is no next forcing bin. Zero remains a numerical value; it is not substituted for missingness.", ""])
    for d in inventory["datasets"]:
        badge={"real_public_catalog_snapshot":"badge-catalog.svg",
               "synthetic_illustrative":"badge-synthetic.svg"}.get(d["evidence_kind"])
        evidence_label=(f"![{d['evidence_kind']}](figures/{badge})" if badge else
                        "**Unclassified evidence / review required.**")
        missing=d["missingness"]
        lines.extend([f"## {d['id'].replace('_',' ')}","",f"### {d['title']}","",
                      evidence_label, "",
                      f"**{d['row_count']:,} rows · {d['column_count']} columns · {d['bytes']:,} bytes.** {missing['rows_with_blank_or_undefined']:,} rows contain a blank or undefined numeric field; this count reflects file representation rather than validity of every other field in that row.", "",
                      f"{link_from_data(d['csv_path'],'Open / download CSV')} · {link_from_data(d['provenance_path'],'Source sidecar')} · {link_from_data(d['original_figure_path'],'Original figure')} · {link_from_data(d['diagnostic_figure_path'],'Diagnostic spread')} · {link_from_data(d['diagnostic_provenance_path'],'Figure ledger')}", "",
                      "**Engineering starting points:** "+(" · ".join(link_from_data(p['path'],p['id']) for p in d['linked_project_documents']) or "Project association not recorded / TBD.")+" These records remain proposals; table illustrations do not become project measurements.", "",
                      f"**Exact column order:** "+", ".join("`"+c+"`" for c in d["column_names"])+".","",
                      "| Exact field | Recorded/verified unit | Meaning | Blank | NaN | Other nonfinite | Finite stored range |",
                      "|:--|:--|:--|--:|--:|--:|:--|"])
        for c in d["columns"]:
            value_range="— text / no finite numbers" if c["finite_min"] is None else f"{format_value(c['finite_min'])} → {format_value(c['finite_max'])}"
            lines.append(f"| `{c['name']}` | {cell(c['unit'])} | {cell(c['description'])} | {c['blank_count']:,} | {c['nan_count']:,} | {c['other_nonfinite_count']:,} | {value_range} |")
        lines.extend(["", "<details>", "<summary><strong>Open a compact field preview</strong> — first two rows, transposed</summary>", "",
                      "| Field | First row | Second row |", "|:--|:--|:--|"])
        previews=d["representative_rows"]
        for c in d["column_names"]:
            a=format_value(previews[0]["values"][c]) if previews else "— no rows"
            b=format_value(previews[1]["values"][c]) if len(previews)>1 else "— no second row"
            lines.append(f"| `{c}` | {cell(a)} | {cell(b)} |")
        lines.extend(["", "The JSON inventory retains the original preview text. Rounded display values are not a replacement dataset.","", "</details>", "",
                      "<details>", "<summary><strong>Open source, assumptions and unit traceability</strong></summary>", "",
                      f"**Original CSV SHA-256:** `{d['sha256']}`", "",
                      f"**Model/source function:** `{d['model_function']}` in [models.py](../models/models.py). Shared definitions: [Model Foundry](../models/README.md#equations-parameters-and-domain).", "",
                      "**Current reading limits:**", ""])
        lines.extend("- "+x for x in d["domain_limits"])
        if d["id"]=="exoplanet_sample":
            lines.extend(["", "**Historical source wording:** The unchanged acquisition sidecar and original numerical view describe an alphabetically truncated selection. That is the recorded acquisition interpretation. The saved request and response are retained, but global first-200 ranking against the complete archive was not independently verified. Current captions describe the returned 200-row query-ordered extract."])
        lines.extend(["", "| Field | Unit evidence |", "|:--|:--|"])
        for c in d["columns"]:
            basis=c["unit_basis"]
            lines.append(f"| `{c['name']}` | {link_from_data(basis['path'],c['unit_status'])}: {cell(basis['detail'])} |")
        if d["parameters"]:
            lines.extend(["", "**Recorded parameters / query context**", "", "```json", json.dumps(d["parameters"],indent=2,ensure_ascii=False),"```"])
        lines.extend(["", "</details>", ""])
    lines.extend(["---", "", "This document and [DATA_INVENTORY.json](DATA_INVENTORY.json) are generated by [build_data_inventory.py](../tools/build_data_inventory.py). It reads the immutable CSVs, sidecars and model documentation, verifies all original model-manifest assets before writing, and writes only these two inventory products. It performs no acquisition or new scientific simulation.", ""])
    return "\n".join(lines)


def generate(repo_root: Path) -> dict:
    root=Path(repo_root).resolve();source_dir=root/"models"/"data"
    manifest_path=root/"models"/"manifest.json"
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    for item in manifest["assets"]:
        actual=digest(root/"models"/item["path"])
        if actual["sha256"]!=item["sha256"] or actual["bytes"]!=item["bytes"]:
            raise ValueError("Original model asset differs from its manifest: "+item["path"])
    found={p.stem:p for p in source_dir.glob("*.csv")}
    ordered=[x for x in READING_ORDER if x in found]+sorted(set(found)-set(READING_ORDER))
    datasets=[];sources={}
    for stem in ordered:
        csv_path=found[stem]
        title,sidecar_name,projects,old_fig,new_fig,function=MODEL_MAP.get(stem,(stem,None,[],None,None,"not recorded / TBD"))
        provenance_path="models/data/"+sidecar_name if sidecar_name else "models/README.md"
        metadata_path=root/provenance_path
        metadata=json.loads(metadata_path.read_text(encoding="utf-8")) if sidecar_name else {}
        with csv_path.open(encoding="utf-8-sig",newline="") as handle:
            reader=csv.DictReader(handle);names=reader.fieldnames or [];rows=list(reader)
        if len(names)!=len(set(names)) or any(None in row or any(value is None for value in row.values()) for row in rows):
            raise ValueError("Ambiguous CSV field layout: "+csv_path.name)
        columns=[]
        for name in names:
            raw=metadata.get("schema",{}).get(name)
            unit,status,basis=unit_record(stem,name,raw,provenance_path)
            description=DESCRIPTIONS.get(name,"Meaning not recorded / TBD; consult the producing analysis interface.")
            if name in ("real","imaginary"):
                description=("Real" if name=="real" else "Imaginary")+" coordinate of "+("parameter c." if stem=="mandelbrot" else "starting value z₀.")
            columns.append({"name":name,"unit":unit,"unit_status":status,"unit_basis":basis,
                            "raw_schema_entry":raw,"description":description,**numeric_profile([row[name] for row in rows])})
        missing={"blank_cells":sum(x["blank_count"] for x in columns),"nan_cells":sum(x["nan_count"] for x in columns),"other_nonfinite_cells":sum(x["other_nonfinite_count"] for x in columns),"rows_with_blank_or_undefined":0}
        for row in rows:
            for value in row.values():
                try: undefined=not value.strip() or not math.isfinite(float(value))
                except ValueError: undefined=False
                if undefined:
                    missing["rows_with_blank_or_undefined"]+=1;break
        paths=[csv_path,metadata_path,root/"models"/"models.py",root/"models"/"README.md",manifest_path]
        assets=[asset(root,p) for p in dict.fromkeys(paths)]
        for a in assets:sources[a["path"]]=a
        parameters=metadata.get("parameters",{})
        if stem=="exoplanet_sample":
            parameters={k:metadata[k] for k in ("provider","retrieved_utc","table","query_adql") if k in metadata}
        domain_limits=metadata.get("assumptions_and_limits",metadata.get("limitations",["Domain limits not recorded / TBD."]))
        if stem=="exoplanet_sample":
            domain_limits=["Saved 200-row query-ordered extract; the source sidecar records an intended TOP 200 ORDER BY pl_name request. Global first-200 ranking was not independently verified.",
                           "Discovery method, completeness, missing-radius selection, request truncation and follow-up biases apply; not random or representative."]+domain_limits[2:]
        project_documents=[]
        for project in projects:
            matches=sorted((root/"research"/project[0]).glob(project+"-*/README.md"))
            if len(matches)==1:
                project_documents.append({"id":project,"path":matches[0].relative_to(root).as_posix()})
        datasets.append({"id":stem,"title":title,"csv_path":csv_path.relative_to(root).as_posix(),
                         "provenance_path":provenance_path,"evidence_kind":metadata.get("kind","not_classified / review required"),
                         "row_count":len(rows),"column_count":len(names),"column_names":names,"columns":columns,
                         "representative_rows":[{"row_index_0_based":i,"values":row} for i,row in enumerate(rows[:2])],
                         "missingness":missing,"source_assets":assets,"linked_projects":projects,
                         "linked_project_documents":project_documents,
                         "original_figure_path":"models/figures/"+old_fig+".svg" if old_fig else "models/README.md",
                         "diagnostic_figure_path":"data/figures/"+new_fig+".svg" if new_fig else "data/figures/README.md",
                         "diagnostic_provenance_path":"data/figures/"+new_fig+".provenance.json" if new_fig else "data/figures/DATA_FIGURES.json",
                         "model_function":function,"parameters":parameters,
                         "domain_limits":domain_limits,
                         **digest(csv_path)})
    summary={"dataset_count":len(datasets),"evidence_counts":dict(sorted(Counter(d["evidence_kind"] for d in datasets).items())),
             "total_csv_rows":sum(d["row_count"] for d in datasets),"total_columns":sum(d["column_count"] for d in datasets),
             "blank_cells":sum(d["missingness"]["blank_cells"] for d in datasets),"nan_cells":sum(d["missingness"]["nan_cells"] for d in datasets),
             "other_nonfinite_cells":sum(d["missingness"]["other_nonfinite_cells"] for d in datasets),
             "unit_status_counts":dict(sorted(Counter(c["unit_status"] for d in datasets for c in d["columns"]).items()))}
    script_path=Path(__file__).resolve()
    result={"schema_version":1,"generated_by":{"path":script_path.relative_to(root).as_posix(),**digest(script_path)},
            "source_policy":"Read-only actual CSVs and sidecars. Counts/ranges are descriptive storage diagnostics; no manufactured observations or inferred physical uncertainties.",
            "preview_policy":"First two CSV data rows; original text retained in JSON, human previews rounded to four significant digits.",
            "unit_policy":"Recorded sidecar or explicitly verified model definition; unknown fields state unit not recorded / TBD.",
            "summary":summary,"source_assets":[sources[k] for k in sorted(sources)],"datasets":datasets}
    destination=root/"data";destination.mkdir(exist_ok=True)
    (destination/"DATA_INVENTORY.json").write_bytes((json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8"))
    (destination/"TABLES.md").write_bytes(markdown(result).encode("utf-8"))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=DEFAULT_ROOT)
    args=parser.parse_args();result=generate(args.root)
    print(json.dumps(result["summary"],indent=2))


if __name__=="__main__":main()
