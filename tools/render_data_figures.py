"""Render an additional scientific data gallery from existing repository CSVs.

This script only reads source data. It neither regenerates reduced models nor
changes their manifest. SVG and PNG are paired, with a separate evidence ledger.
Run from the repository: python tools/render_data_figures.py
Dependencies: numpy, matplotlib. Default paths are relative to this repository,
not the caller's working directory. Optional explicit paths are also accepted.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch

NAVY = "#142D4E"
TEAL = "#008C95"
COPPER = "#BD653D"
BLUE = "#6285AA"
INK = "#213349"
MUTED = "#536779"
PALE = "#EDF3F5"
GRID = "#D9E2E8"
WHITE = "#FFFFFF"
REPO_ROOT = Path(__file__).resolve().parents[1]
PALETTE = [TEAL, COPPER, BLUE, "#887496", "#879875"]
CMAP = LinearSegmentedColormap.from_list("atlas", [NAVY, BLUE, TEAL, "#B7DFDA", "#F1D8B2"])


def configure():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.labelsize": 11, "axes.titlesize": 13,
        "axes.titleweight": "bold", "axes.titlepad": 13,
        "axes.labelcolor": INK, "text.color": INK,
        "axes.edgecolor": "#8B9BA9", "axes.linewidth": .7,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.facecolor": WHITE, "figure.facecolor": WHITE,
        "xtick.color": MUTED, "ytick.color": MUTED,
        "grid.color": GRID, "grid.linewidth": .6,
        "legend.frameon": False, "legend.fontsize": 10,
        "lines.linewidth": 2, "svg.fonttype": "none",
        "svg.hashsalt": "ATLAS-data-visibility-20261002",
        "savefig.dpi": 180,
    })


def load(root, name):
    return np.genfromtxt(root / (name + ".csv"), delimiter=",", names=True)


def repo_path(path):
    """Use stable repository-relative paths for the included source/output assets."""
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def source(root, filenames):
    return [{"path": repo_path(root / name),
             "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest(),
             "bytes": (root / name).stat().st_size}
            for name in filenames]


def canvas(title, subtitle, evidence, width=12, height=7):
    fig = plt.figure(figsize=(width, height))
    fig.text(.065, .962, "ATLAS  /  DATA NOTEBOOK", color=TEAL, fontsize=10, weight="bold")
    fig.text(.065, .902, title, color=NAVY, fontsize=23, weight="bold")
    fig.text(.065, .857, subtitle, color=MUTED, fontsize=11)
    fig.text(.94, .962, evidence, ha="right", color=COPPER if "SYNTHETIC" in evidence else TEAL,
             fontsize=10, weight="bold")
    fig.add_artist(plt.Line2D([.065, .94], [.822, .822], color=GRID, linewidth=1,
                             transform=fig.transFigure))
    return fig


def grid(fig, rows=1, cols=2, **kwargs):
    return fig.add_gridspec(rows, cols, left=.085, right=.94, top=.77, bottom=.17,
                           wspace=.32, hspace=.42, **kwargs)


def panel(ax, label, title):
    ax.set_title(label + "  " + title, loc="left", color=NAVY)
    ax.grid(alpha=.7)
    ax.set_axisbelow(True)


def save(fig, root, out, name, caption, evidence, inputs, projects, limits,
         footer, summaries=None):
    fig.text(.065, .074, footer, fontsize=9.5, color=MUTED)
    fig.text(.065, .034, "Read the evidence ledger for source hashes, assumptions and project links.",
             fontsize=9, color=MUTED)
    for ext in ("svg", "png"):
        metadata = {"Creator": "ATLAS engineering data notebook"}
        if ext == "svg":
            metadata["Date"] = "2026-10-02"
            metadata["Title"] = caption.split(".")[0]
            metadata["Description"] = caption
        fig.savefig(out / (name + "." + ext), metadata=metadata)
    plt.close(fig)
    svg = out / (name + ".svg")
    content = svg.read_text(encoding="utf-8")
    start = content.index("<svg ")
    end = content.index(">", start)
    content = content[:end] + ' role="img" aria-labelledby="atlas-title atlas-description"' + content[end:]
    end = content.index(">", start)
    content = content[:end+1] + '\n<title id="atlas-title">' + escape(name.replace("_", " ")) + '</title>\n<desc id="atlas-description">' + escape(caption) + '</desc>' + content[end+1:]
    svg.write_bytes(content.encode("utf-8"))
    record = {
        "id": name, "evidence_kind": evidence,
        "svg": repo_path(out / (name + ".svg")), "png": repo_path(out / (name + ".png")),
        "provenance": repo_path(out / (name + ".provenance.json")),
        "caption": caption, "linked_projects": projects,
        "source_assets": source(root, inputs),
        "output_assets": source(out, [name + ".svg", name + ".png"]),
        "assumptions_and_limits": limits,
        "derivation": "Plot transformations and descriptive statistics only; no new model runs or fitted physical claims.",
        "derived_summaries": summaries or {},
        "uncertainty_note": "No physical uncertainty bands are implied unless a panel explicitly identifies the synthetic noise experiment.",
    }
    (out / (name + ".provenance.json")).write_bytes((json.dumps(record, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return record


def exoplanets(root, out):
    rows = list(csv.DictReader((root / "exoplanet_sample.csv").open(encoding="utf-8", newline="")))
    period = np.array([float(x["pl_orbper"]) for x in rows])
    radius = np.array([float(x["pl_rade"]) for x in rows])
    methods = Counter(x["discoverymethod"] for x in rows)
    fig = canvas("Inside the exoplanet catalog", "200 alphabetically selected archive rows  ·  published catalog values  ·  no occurrence inference", "REAL CATALOG SNAPSHOT")
    gs = grid(fig, width_ratios=[1.15, 1])
    ax = fig.add_subplot(gs[0, 0]); panel(ax, "A", "Period and radius")
    symbols = ["o", "s", "^", "D", "P"]
    for (method, count), color, marker in zip(methods.most_common(), PALETTE, symbols):
        m = np.array([r["discoverymethod"] == method for r in rows])
        ax.scatter(period[m], radius[m], s=32, c=color, marker=marker, alpha=.8,
                   edgecolors=WHITE, linewidths=.35, label=f"{method} ({count})")
    ax.set(xscale="log", yscale="log", xlabel="Orbital period [day]", ylabel="Planet radius [Earth radius]")
    ax.legend(loc="upper left", fontsize=8.5, frameon=True, facecolor=WHITE, edgecolor="none", framealpha=.92)
    ax = fig.add_subplot(gs[0, 1]); panel(ax, "B", "Field coverage in this extract")
    fields = ["Orbital period", "Planet radius", "Host metallicity", "Discovery method"]
    keys = ["pl_orbper", "pl_rade", "st_met", "discoverymethod"]
    available = np.array([sum(bool(r[k].strip()) for r in rows) for k in keys])
    y = np.arange(len(fields))[::-1]
    ax.barh(y, available, color=TEAL, height=.57, label="Available")
    ax.barh(y, 200-available, left=available, color="#E0B89F", height=.57, label="Missing")
    for yy, n in zip(y, available): ax.text(n-4, yy, f"{n}/200", va="center", ha="right", color=WHITE, weight="bold", fontsize=11)
    ax.set(yticks=y, yticklabels=fields, xlabel="Catalog rows", xlim=(0, 205), ylim=(-1, 3.7))
    ax.legend(loc="upper right", bbox_to_anchor=(1, 1.015), ncol=2, fontsize=9.5)
    ax.text(.02, .03, "Period and radius were required by the query.\n193 distinct host names; no quoted error bars.",
            transform=ax.transAxes, fontsize=9, color=MUTED)
    caption = "Real NASA Exoplanet Archive snapshot of the first 200 planet names alphabetically among rows with period and radius. Panel A preserves discovery-method categories and logarithmic scales; panel B makes the selected fields and nine missing host-metallicity values visible. This extract is not representative and cannot establish occurrence rates or physical class labels."
    return save(fig, root, out, "10_catalog_values_and_coverage", caption, "real_public_catalog_snapshot",
                ["exoplanet_sample.csv", "exoplanet_sample.provenance.json"], ["C05", "C23"],
                ["Query selection, discovery and follow-up biases; composite values may mix references.", "No per-parameter uncertainties or selection-efficiency correction in the extract."],
                "Source: NASA Exoplanet Archive  ·  retrieved 02 Oct 2026  ·  alphabetical and detection selection biases apply",
                {"rows": len(rows), "distinct_host_names": len(set(r["hostname"] for r in rows)), "discovery_method_counts": dict(methods), "available_field_counts": dict(zip(keys, available.tolist()))})


def thermal(root, out):
    d = load(root, "balloon_thermal"); t = d["time_s"]/3600
    params=json.loads((root/"balloon_thermal.json").read_text())["parameters"]
    q_wall = d["absorbed_W"] + d["convection_W"] + d["radiation_W"] - d["wall_to_payload_W"]
    q_payload = d["wall_to_payload_W"] + params["payload_power_W"]
    fig = canvas("Follow the heat", "Prescribed environmental histories  ·  two isothermal nodes  ·  4-hour illustrative thermal run", "SYNTHETIC / ILLUSTRATIVE")
    gs = grid(fig)
    ax = fig.add_subplot(gs[0, 0]); panel(ax, "A", "Signed wall energy budget")
    components = [("Absorbed power", "absorbed_W", TEAL), ("Convection into wall", "convection_W", BLUE),
                  ("Radiation into wall", "radiation_W", COPPER)]
    for label, field, color in components: ax.plot(t, d[field], color=color, label=label)
    ax.plot(t, -d["wall_to_payload_W"], color="#887496", linestyle="--", label="Conduction into wall")
    ax.plot(t, q_wall, color=NAVY, linewidth=2.6, label="Net wall power")
    ax.axhline(0, color=MUTED, linewidth=.9)
    ax.set(xlabel="Elapsed time [h]", ylabel="Power [W]; positive enters wall")
    ax.legend(fontsize=9)
    ax = fig.add_subplot(gs[0, 1]); panel(ax, "B", "Temperature lag")
    ax.plot(t, d["wall_K"], color=TEAL, label="Wall node")
    ax.plot(t, d["payload_K"], color=COPPER, label="Payload node")
    ax.plot(t, d["air_K"], color=BLUE, linestyle="--", label="Prescribed air")
    ax.plot(t, d["radiative_sink_K"], color="#8B9BA9", linestyle=":", label="Prescribed radiative sink")
    ax.set(xlabel="Elapsed time [h]", ylabel="Temperature [K]")
    ax.legend(fontsize=9)
    caption = "Synthetic two-node balloon thermal model. Signed component powers sum to net wall power, with wall-to-payload conduction reversed for the wall balance. The payload has a prescribed 3 W internal source. Temperatures show the model response to imposed boundary histories; they are not balloon-flight measurements or qualification limits."
    return save(fig, root, out, "11_thermal_power_and_response", caption, "synthetic_illustrative",
                ["balloon_thermal.csv", "balloon_thermal.json"], ["E06"],
                ["Uniform temperatures per node; view factor folded into radiating area.", "No atmosphere calibration, rarefied-flow correction, measured ascent profile or uncertainty ensemble."],
                "Positive power enters the named node  ·  heat capacities: wall 1,200 J/K; payload 850 J/K  ·  model evidence only",
                {"payload_source_W": params["payload_power_W"], "wall_net_power_range_W": [float(q_wall.min()), float(q_wall.max())], "payload_net_power_range_W": [float(q_payload.min()), float(q_payload.max())]})


def hydrology(root, out):
    d = load(root, "hydrologic_reservoir"); t = d["time_day"]
    params=json.loads((root/"hydrologic_reservoir.json").read_text())["parameters"]
    fig = canvas("A water ledger that closes", "One linear reservoir  ·  exact propagation under piecewise-constant recharge  ·  60 illustrative days", "SYNTHETIC / ILLUSTRATIVE")
    gs = grid(fig)
    ax = fig.add_subplot(gs[0, 0]); panel(ax, "A", "Recharge and delayed release")
    ax.fill_between(t, 0, d["next_bin_recharge_mm_day"], step="post", color=TEAL, alpha=.22, label="Effective recharge")
    ax.step(t, d["next_bin_recharge_mm_day"], where="post", color=TEAL, linewidth=1.3)
    ax.plot(t, d["outflow_mm_day"], color=COPPER, label="Outflow kS")
    ax.set(xlabel="Elapsed time [day]", ylabel="Water flux [mm/day]")
    ax.legend(loc="upper right",frameon=True,facecolor=WHITE,edgecolor="none",framealpha=.92)
    ax = fig.add_subplot(gs[0, 1]); panel(ax, "B", "Water accounting")
    available = params["initial_storage_mm"] + d["cumulative_recharge_mm"]
    accounted = d["storage_mm"] + d["cumulative_outflow_mm"]
    ax.fill_between(t, 0, d["cumulative_outflow_mm"], color=BLUE, alpha=.38, label="Cumulative outflow")
    ax.fill_between(t, d["cumulative_outflow_mm"], accounted, color=TEAL, alpha=.25, label="Remaining storage")
    ax.plot(t, available, color=NAVY, linewidth=2.2, label="Initial storage + cumulative recharge")
    ax.set(xlabel="Elapsed time [day]", ylabel="Water depth ledger [mm]", ylim=(0, 68))
    ax.legend(fontsize=9, loc="upper left")
    residual = float(np.max(np.abs(d["mass_balance_residual_mm"])))
    ax.text(.03, .06, f"Maximum ledger residual: {residual:.2e} mm\nS + cumulative Q = S₀ + cumulative recharge",
            transform=ax.transAxes, color=MUTED, fontsize=9.5, bbox={"facecolor":WHITE,"edgecolor":"none","alpha":.9,"pad":5})
    caption = "Synthetic reservoir fluxes and cumulative water accounting. Recharge means effective water entering storage, rather than rainfall. Panel B decomposes all accounted water into cumulative release and remaining storage, bounded by initial storage plus accumulated recharge. The tiny arithmetic residual verifies this implementation's conservation, not watershed predictive accuracy."
    return save(fig, root, out, "12_hydrologic_water_ledger", caption, "synthetic_illustrative",
                ["hydrologic_reservoir.csv", "hydrologic_reservoir.json"], ["B23"],
                ["Single pedagogical reservoir; evapotranspiration, interception, infiltration thresholds and channels omitted.", "No observed catchment data, calibrated forecast skill or flood decision claim."],
                "Initial storage 20 mm  ·  k = 0.12 day⁻¹  ·  final recharge field is intentionally undefined at the last boundary",
                {"max_abs_mass_balance_residual_mm": residual, "final_storage_mm": float(d["storage_mm"][-1]), "final_cumulative_outflow_mm": float(d["cumulative_outflow_mm"][-1])})


def attitude(root, out):
    d = load(root, "one_axis_attitude"); t = d["time_s"]
    params=json.loads((root/"one_axis_attitude.json").read_text())["parameters"]
    theta = np.rad2deg(d["theta_rad"]); omega = np.rad2deg(d["omega_rad_s"])
    commanded = (-params["kp_Nm_rad"]*d["theta_rad"]-params["kd_Nm_s_rad"]*d["omega_rad_s"])*1000
    fig = canvas("Control authority, made visible", "One rotational degree of freedom  ·  fixed zero-angle target  ·  saturation shown in physical units", "SYNTHETIC / ILLUSTRATIVE")
    gs = grid(fig)
    ax = fig.add_subplot(gs[0, 0]); panel(ax, "A", "Attitude phase portrait")
    points = np.column_stack([theta, omega]); segments = np.stack([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=CMAP, norm=plt.Normalize(t.min(), t.max()), linewidth=2.2)
    lc.set_array(t[:-1]); ax.add_collection(lc); ax.autoscale()
    ax.scatter(theta[0], omega[0], marker="o", s=55, color=COPPER, zorder=3, label="Initial state")
    ax.scatter(theta[-1], omega[-1], marker="x", s=65, color=NAVY, zorder=4, label="Final state")
    ax.axhline(0, color=MUTED, linewidth=.8); ax.axvline(0, color=MUTED, linewidth=.8)
    ax.set(xlabel="Angle error [deg]", ylabel="Angular rate [deg/s]")
    ax.legend(loc="lower right", fontsize=9)
    cbar=fig.colorbar(lc, ax=ax, pad=.035, fraction=.045); cbar.set_label("Elapsed time [s]")
    ax = fig.add_subplot(gs[0, 1]); panel(ax, "B", "Requested versus applied torque")
    ax.axhspan(-8, 8, color=TEAL, alpha=.09)
    ax.axhline(8, color=COPPER, linestyle=":", linewidth=1.4, label="±8 mN·m actuator bounds")
    ax.axhline(-8, color=COPPER, linestyle=":", linewidth=1.4)
    ax.plot(t, commanded, color=BLUE, linestyle="--", label="Unsaturated PD request")
    ax.plot(t, d["control_torque_Nm"]*1000, color=NAVY, label="Applied control torque")
    ax.set(xlabel="Elapsed time [s]", ylabel="Control torque [mN·m]", xlim=(0, 40))
    ax.legend(fontsize=9)
    caption = "Synthetic one-axis PD attitude response and actuator authority. The phase portrait is colored by elapsed model time. Requested torque is reconstructed from the recorded states and sidecar gains; the applied torque is clipped to ±8 mN·m. The right panel focuses on the first 40 seconds, while the phase portrait uses the full 120-second record."
    return save(fig, root, out, "13_attitude_phase_and_authority", caption, "synthetic_illustrative",
                ["one_axis_attitude.csv", "one_axis_attitude.json"], ["I10"],
                ["Exact states, fixed reference and one rigid axis; no estimator, delay or wheel momentum management.", "No three-axis simulation, flight software validation or spacecraft qualification."],
                "Inertia 0.12 kg·m²  ·  Kp 0.03 N·m/rad  ·  Kd 0.08 N·m·s/rad  ·  the color scale denotes time, not uncertainty",
                {"initial_angle_deg": float(theta[0]), "final_angle_deg": float(theta[-1]), "final_angular_rate_deg_s": float(omega[-1]), "record_duration_s": float(t[-1])})


def orbit(root, out):
    d = load(root, "two_body_orbit"); c = load(root, "two_body_convergence")
    periods = d["time_normalized"]/(2*np.pi)
    de = (d["specific_energy"]-d["specific_energy"][0])/abs(d["specific_energy"][0])
    dh = (d["specific_angular_momentum"]-d["specific_angular_momentum"][0])/abs(d["specific_angular_momentum"][0])
    fig = canvas("The signature of numerical accuracy", "Velocity Verlet  ·  point-mass two-body dynamics  ·  normalized units and ten orbital periods", "SYNTHETIC / ILLUSTRATIVE")
    gs = grid(fig)
    ax = fig.add_subplot(gs[0, 0]); panel(ax, "A", "Energy error stays bounded")
    ax.plot(periods, de*1e6, color=TEAL, label="Relative specific-energy error")
    ax.axhline(0, color=MUTED, linewidth=.8)
    ax.set(xlabel="Elapsed orbit count [period]", ylabel="(E − E₀)/|E₀| [parts per million]")
    ax.text(.03,.9, f"400 steps per period\nMaximum |Δh/h₀| = {np.max(np.abs(dh)):.2e}", transform=ax.transAxes, fontsize=10, color=MUTED, bbox={"facecolor":WHITE,"edgecolor":"none","alpha":.93,"pad":5})
    ax = fig.add_subplot(gs[0, 1]); panel(ax, "B", "A refinement signature")
    n=c["steps_per_period"]; err=c["maximum_relative_energy_error"]
    ax.loglog(n, err, "o-", color=TEAL, markersize=8, label="Recorded maximum error")
    ax.loglog(n, err[0]*(n[0]/n)**2, linestyle="--", color=COPPER, label="Second-order reference")
    ax.set(xlabel="Integrator steps per period", ylabel="Maximum |(E − E₀)/E₀| [dimensionless]")
    ax.set_xticks(n, labels=[str(int(x)) for x in n]); ax.minorticks_off()
    ax.legend(loc="upper right",fontsize=9,frameon=True,facecolor=WHITE,edgecolor="none",framealpha=.9)
    observed_order=float(np.log(err[0]/err[-1])/np.log(n[-1]/n[0]))
    ax.text(.05,.07, f"Endpoint refinement order: {observed_order:.3f}\nThree resolutions; fixed initial conditions", transform=ax.transAxes, fontsize=10, color=MUTED)
    caption = "Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation."
    return save(fig, root, out, "14_orbit_conservation_and_refinement", caption, "synthetic_illustrative",
                ["two_body_orbit.csv", "two_body_convergence.csv", "two_body_orbit.json"], ["I08", "I12", "I13"],
                ["Normalized point masses; no maneuver, atmospheric drag, third body or operational ephemeris.", "Energy boundedness does not establish multi-body or planetary-defense solution accuracy."],
                "μ = 1; a = 1; e = 0.3  ·  angular momentum uses the initial value as reference  ·  no physical units are implied",
                {"endpoint_refinement_order": observed_order, "max_abs_relative_energy_error_400_steps": float(np.max(np.abs(de))), "max_abs_relative_angular_momentum_error": float(np.max(np.abs(dh)))})


def spectral(root, out):
    d=load(root, "spectral_mixture"); mc=load(root,"spectral_monte_carlo")
    params=json.loads((root/"spectral_mixture.json").read_text())["parameters"]
    injected=params["true_A_fraction"]
    strong=mc["f_separated"]; weak=mc["f_nearly_identical"]
    fig=canvas("When a fit loses its information", "2,000 synthetic noise realizations  ·  unconstrained linear areal mixture  ·  known invented endmembers", "SYNTHETIC / ILLUSTRATIVE")
    gs=grid(fig)
    ax=fig.add_subplot(gs[0,0]); panel(ax,"A","Separated endmembers")
    bins=np.linspace(strong.min(),strong.max(),40)
    ax.hist(strong,bins=bins,density=True,color=TEAL,alpha=.72,edgecolor=WHITE,linewidth=.4)
    q=np.quantile(strong,[.025,.975]); ax.axvspan(*q,color=TEAL,alpha=.12)
    ax.axvline(injected,color=NAVY,linewidth=1.8,label=f"Injected fraction: {injected}")
    for x in q: ax.axvline(x,color=COPPER,linestyle="--",linewidth=1.3)
    ax.set(xlabel="Estimated fraction of endmember A [dimensionless]",ylabel="Noise-realization density [fraction⁻¹]")
    ax.legend(fontsize=9)
    ax.text(.04,.9,f"Empirical σ = {np.std(strong,ddof=1):.4f}\nCentral 95% of synthetic noise draws",transform=ax.transAxes,fontsize=9.5,color=MUTED,bbox={"facecolor":WHITE,"edgecolor":"none","alpha":.93,"pad":5})
    ax=fig.add_subplot(gs[0,1]); panel(ax,"B","Near-identical endmembers")
    ax.hist(weak,bins=40,density=True,color=COPPER,alpha=.72,edgecolor=WHITE,linewidth=.4)
    ax.axvspan(0,1,color=TEAL,alpha=.16,label="Physical fraction interval [0,1]")
    ax.axvline(injected,color=NAVY,linewidth=1.8)
    qw=np.quantile(weak,[.025,.975])
    for x in qw: ax.axvline(x,color=NAVY,linestyle="--",linewidth=1.3)
    ax.set(xlabel="Unclipped fraction estimate [dimensionless]",ylabel="Noise-realization density [fraction⁻¹]")
    ax.legend(loc="lower left",fontsize=9)
    ax.text(.04,.9,f"Empirical σ = {np.std(weak,ddof=1):.3f}\nDifferent scales expose lost information",transform=ax.transAxes,fontsize=9.5,color=MUTED,bbox={"facecolor":WHITE,"edgecolor":"none","alpha":.93,"pad":5})
    outside=float(np.mean((weak<0)|(weak>1)))
    caption="Synthetic spectral-mixture estimator distributions under the same known band-noise level. Separated endmembers give narrow noise-driven fraction estimates; near-identical endmembers give a broad unconstrained distribution with unphysical values preserved as an identifiability diagnostic. Central 95% noise-realization intervals are descriptive simulation intervals, not posteriors or uncertainty bounds for measured Mars mineral abundance."
    return save(fig,root,out,"15_spectral_information_and_noise",caption,"synthetic_illustrative",
                ["spectral_mixture.csv","spectral_monte_carlo.csv","spectral_mixture.json"],["C08","H09"],
                ["Invented Gaussian bands, independent known-variance noise and exact linear endmembers.","Real intimate mixing, grain size, scattering and correlated calibration are absent.","Panel axes differ intentionally; posterior interpretation is not justified."],
                "Dashed lines mark central 95% of synthetic draws  ·  scales differ between panels  ·  clipping would conceal weak identifiability",
                {"noise_realizations":len(strong),"empirical_sigma_separated":float(np.std(strong,ddof=1)),"empirical_sigma_nearly_identical":float(np.std(weak,ddof=1)),"central_95_interval_separated":q.tolist(),"central_95_interval_nearly_identical":qw.tolist(),"weak_estimates_outside_physical_interval_fraction":outside})


def liquidus(root,out):
    d=load(root,"ideal_binary_liquidus"); meta=json.loads((root/"ideal_binary_liquidus.json").read_text())
    x=d["x_B"]; te=meta["metrics"]["eutectic_T_K"]; xe=meta["metrics"]["eutectic_x_B"]
    fig=canvas("The regions of an ideal phase diagram", "Invented teaching constants  ·  ideal liquid  ·  immiscible pure solids  ·  fixed unspecified pressure", "SYNTHETIC / ILLUSTRATIVE")
    gs=grid(fig,cols=1); ax=fig.add_subplot(gs[0]); panel(ax,"A","Equilibrium phase regions of a hypothetical A–B binary")
    ax.fill_between(x, d["liquidus_K"], 70,color=TEAL,alpha=.16)
    ax.fill_between(x, 30,te,color=BLUE,alpha=.18)
    left=x<=xe; right=x>=xe
    ax.fill_between(x[left],te,d["liquidus_K"][left],color=COPPER,alpha=.2)
    ax.fill_between(x[right],te,d["liquidus_K"][right],color="#8A789E",alpha=.17)
    ax.plot(x,d["liquidus_K"],color=NAVY,linewidth=2.8,label="Stable liquidus envelope")
    ax.axhline(te,color=NAVY,linestyle="--",linewidth=1.2,label="Eutectic isotherm")
    ax.scatter(xe,te,color=COPPER,s=70,zorder=5)
    ax.text(.5,66,"LIQUID",ha="center",fontsize=15,weight="bold",color=TEAL)
    ax.text(.2,47,"LIQUID + A(s)",ha="center",fontsize=12,weight="bold",color=COPPER)
    ax.text(.83,47,"LIQUID + B(s)",ha="center",fontsize=12,weight="bold",color="#77628D")
    ax.text(.2,35,"A(s) + B(s)",ha="center",fontsize=13,weight="bold",color=BLUE)
    ax.annotate(f"Toy eutectic\nxB = {xe:.3f}; T = {te:.2f} K",(xe,te),xytext=(.65,34),
                arrowprops={"arrowstyle":"-", "color":MUTED},color=MUTED,fontsize=10)
    ax.set(xlabel="Overall B mole fraction [dimensionless]",ylabel="Equilibrium temperature [K]",xlim=(0,1),ylim=(30,70))
    ax.legend(loc="upper right",fontsize=9)
    caption="Equilibrium phase regions inferred from the existing ideal-binary liquidus model with invented melting temperatures and fusion enthalpies. Above the liquidus the material is liquid; between the liquidus and eutectic temperature it is liquid plus the indicated pure solid; below the eutectic it is A and B solids. The region labels follow the model assumptions and are not predictions for Pluto's real volatile mixtures."
    return save(fig,root,out,"16_ideal_binary_phase_regions",caption,"synthetic_illustrative",
                ["ideal_binary_liquidus.csv","ideal_binary_liquidus.json"],["A02"],
                ["Invented values: Tm,A 63 K; Tm,B 60 K; ΔHfus,A 900 J/mol; ΔHfus,B 700 J/mol.","No real N₂/CO/CH₄ measurements, solid solutions, calibrated pressure, nonideality or kinetics."],
                "A and B are hypothetical components  ·  equilibrium boundaries under declared assumptions  ·  not measured Pluto chemistry",
                {"toy_eutectic_x_B":xe,"toy_eutectic_temperature_K":te})


def fractals(root,out):
    fig=canvas("Fractals at a finite resolution", "241 × 181 sampled points per field  ·  160-iteration budget  ·  zero escape count is not certified membership", "SYNTHETIC / ILLUSTRATIVE")
    gs=grid(fig); summaries={}
    for col,name in enumerate(["mandelbrot","julia"]):
        d=load(root,name); x=np.unique(d["real"]); y=np.unique(d["imaginary"])
        v=d["escape_iteration_0_unresolved"].reshape(len(y),len(x))
        masked=np.ma.masked_where(v==0,v)
        cmap=LinearSegmentedColormap.from_list("fractal_escape",[BLUE,TEAL,"#B7DFDA","#F1D8B2"]); cmap.set_bad(NAVY)
        ax=fig.add_subplot(gs[0,col]); panel(ax,chr(65+col),name.title()+" finite-grid escape")
        im=ax.imshow(masked,origin="lower",extent=[x.min(),x.max(),y.min(),y.max()],cmap=cmap,
                     norm=matplotlib.colors.LogNorm(vmin=1,vmax=160),interpolation="nearest",aspect="equal")
        ax.set(xlabel="Real coordinate [dimensionless]",ylabel="Imaginary coordinate [dimensionless]")
        ax.set_anchor("N")
        unresolved=int(np.count_nonzero(v==0)); summaries[name]={"points":int(v.size),"unresolved_points":unresolved,"unresolved_fraction":unresolved/v.size}
        ax.text(.03,.06,f"{unresolved:,} / {v.size:,} unresolved points",transform=ax.transAxes,
                fontsize=9,color=WHITE,bbox={"boxstyle":"round,pad=.4","facecolor":NAVY,"edgecolor":"none","alpha":.9})
        cb=fig.colorbar(im,ax=ax,fraction=.046,pad=.035);cb.set_label("Iteration of first escape",fontsize=10)
        cb.set_ticks([1,5,20,80,160]);cb.set_ticklabels(["1","5","20","80","160"])
    caption="Finite-grid escape iteration maps from immutable Mandelbrot and Julia outputs. Logarithmic color records the first iteration whose modulus exceeds two. Navy regions identify points that did not escape within 160 iterations; these points are unresolved by this computation and are not certified members. The Julia parameter is c = −0.75 + 0.11i."
    return save(fig,root,out,"17_fractal_resolution_and_escape",caption,"synthetic_illustrative",
                ["mandelbrot.csv","mandelbrot.json","julia.csv","julia.json"],["A01"],
                ["Finite precision, a finite spatial grid and finite iteration cannot prove membership.","Different sampled domains; unresolved fractions describe only these specific grids.","Maps use escape counts, not distance-estimator missingness. Julia's sampled critical point z0=0 escapes at iteration 29 but has an undefined derivative-based distance estimate."],
                "Navy = unresolved at iteration 160  ·  color = first escape iteration on a logarithmic scale  ·  counts depend on the sampled grid",
                summaries)


def drag(root,out):
    d=load(root,"sphere_drag"); re=d["Re"]; cd=d["Cd_Schiller_Naumann"]; st=d["Cd_Stokes_asymptote"]
    ratio=cd/st
    fig=canvas("Where the drag approximation departs", "Smooth isolated sphere  ·  continuum incompressible flow  ·  Schiller–Naumann correlation for Re ≤ 1,000", "SYNTHETIC / ILLUSTRATIVE")
    gs=grid(fig)
    ax=fig.add_subplot(gs[0,0]);panel(ax,"A","Drag reference curves")
    ax.loglog(re,cd,color=TEAL,label="Schiller–Naumann correlation")
    ax.loglog(re,st,color=COPPER,linestyle="--",label="Stokes asymptote: 24/Re")
    ax.axvspan(re.min(),.1,color=TEAL,alpha=.07)
    ax.set(xlabel="Reynolds number [dimensionless]",ylabel="Drag coefficient Cd [dimensionless]")
    ax.legend(fontsize=9)
    ax=fig.add_subplot(gs[0,1]);panel(ax,"B","Departure from Stokes")
    ax.loglog(re,100*(ratio-1),color=TEAL)
    ax.axhline(10,color=COPPER,linestyle="--",linewidth=1.3,label="10% reference difference")
    re10=float((.1/.15)**(1/.687));ax.scatter([re10],[10],color=COPPER,s=50,zorder=5)
    ax.annotate(f"10% difference at Re ≈ {re10:.3f}",(re10,10),xytext=(.015,170),
                arrowprops={"arrowstyle":"-","color":MUTED},fontsize=10,color=MUTED)
    ax.set(xlabel="Reynolds number [dimensionless]",ylabel="(Cd,correlation/Cd,Stokes − 1) × 100 [%]")
    ax.legend(loc="upper left",fontsize=9)
    caption="Synthetic reference values from the Schiller–Naumann sphere-drag correlation and Stokes creeping-flow asymptote. The percent-departure panel makes the approximation difference explicit, with a descriptive 10% reference crossing computed from the same formula. Neither curve is an observed drag dataset or a CFD solver result; the crossing is not a physical validation tolerance."
    return save(fig,root,out,"18_sphere_drag_reference_departure",caption,"synthetic_illustrative",
                ["sphere_drag.csv","sphere_drag.json"],["D04"],
                ["Stokes law is valid asymptotically for Re ≪ 1; comparing it at larger Re only shows its departure.","No wall effects, compressibility, interactions, measured uncertainty or CFD validation claim."],
                "Correlation reference only  ·  shaded Re < 0.1 region is illustrative  ·  a 10% difference is a display marker, not acceptance evidence",
                {"reference_10_percent_departure_Re":re10,"supported_correlation_Re_max":1000})


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root",type=Path,default=REPO_ROOT/"models"/"data")
    parser.add_argument("--out",type=Path,default=REPO_ROOT/"data"/"figures")
    args=parser.parse_args();configure();args.out.mkdir(parents=True,exist_ok=True)
    records=[]
    for function in [exoplanets,thermal,hydrology,attitude,orbit,spectral,liquidus,fractals,drag]:
        record=function(args.data_root,args.out);records.append(record);print("Rendered "+record["id"],flush=True)
    ledger={"version":1,"source_data_policy":"Read-only immutable existing CSVs and sidecars; original asset manifest is preserved.",
            "path_basis":"Repository-relative paths for included assets; source tables remain under models/data.",
            "renderer":{"path":repo_path(Path(__file__)),"sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"numpy_version":np.__version__,"matplotlib_version":matplotlib.__version__,"svg_metadata_date":"2026-10-02"},
            "figures":records}
    (args.out/"DATA_FIGURES.json").write_bytes((json.dumps(ledger,indent=2,ensure_ascii=False)+"\n").encode("utf-8"))


if __name__=="__main__":
    main()
