"""Reproducible reduced models for an exploratory research portfolio.

All model outputs are SYNTHETIC / ILLUSTRATIVE. The separately fetched
Exoplanet Archive CSV contains real catalog values, with explicit provenance.
Run: python models.py --out . --fetch-exoplanets
Dependencies: numpy, matplotlib. No SciPy, network credentials, or fixed paths.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 20261002
SIGMA = 5.670374419e-8  # Stefan–Boltzmann constant, W m^-2 K^-4
R_GAS = 8.31446261815324  # J mol^-1 K^-1
SYNTHETIC = "SYNTHETIC / ILLUSTRATIVE — reduced model; no mission validation"
QUERY = ("SELECT TOP 200 pl_name,hostname,pl_orbper,pl_rade,st_met,discoverymethod "
         "FROM pscomppars WHERE pl_orbper IS NOT NULL AND pl_rade IS NOT NULL "
         "ORDER BY pl_name")
ARCHIVE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?" + urlencode(
    {"query": QUERY, "format": "csv"})


def rk4(rhs, y0, t):
    """Fourth-order fixed-step integrator. Time may use any consistent unit."""
    t = np.asarray(t, dtype=float)
    if t.ndim != 1 or len(t) < 2 or np.any(np.diff(t) <= 0):
        raise ValueError("Time must be a strictly increasing one-dimensional array")
    y = np.empty((len(t), len(y0)), dtype=float)
    y[0] = y0
    for i, h in enumerate(np.diff(t)):
        k1 = np.asarray(rhs(t[i], y[i]))
        k2 = np.asarray(rhs(t[i]+h/2, y[i]+h*k1/2))
        k3 = np.asarray(rhs(t[i]+h/2, y[i]+h*k2/2))
        k4 = np.asarray(rhs(t[i]+h, y[i]+h*k3))
        y[i+1] = y[i] + h*(k1+2*k2+2*k3+k4)/6
    return y


def fractal_escape(points, max_iter=160, julia_c=None):
    """Escape counts and derivative exterior distance estimate.

    Mandelbrot: z0=0, c=points, dz/dc starts at zero.
    Julia: z0=points, c=julia_c, dz/dz0 starts at one.
    Distance is |z| log|z| / |derivative| on escaped pixels only. It is
    an asymptotic exterior estimator, not an exact distance or inside test.
    Count 0 means 'unresolved / did not escape within max_iter'.
    """
    points = np.asarray(points, dtype=complex)
    z = np.zeros_like(points) if julia_c is None else points.copy()
    c = points if julia_c is None else np.full_like(points, julia_c)
    d = np.zeros_like(points) if julia_c is None else np.ones_like(points)
    count = np.zeros(points.shape, dtype=int)
    distance = np.full(points.shape, np.nan)
    active = np.ones(points.shape, dtype=bool)
    for n in range(1, max_iter+1):
        d[active] = 2*z[active]*d[active] + (1 if julia_c is None else 0)
        z[active] = z[active]**2+c[active]
        escaped = active & (np.abs(z) > 2)
        count[escaped] = n
        radius = np.abs(z[escaped])
        deriv = np.abs(d[escaped])
        distance[escaped] = np.divide(radius*np.log(radius), deriv,
            out=np.full(radius.shape, np.nan), where=deriv > 0)
        active[escaped] = False
        if not np.any(active):
            break
    return count, distance


def liquidus(x, tm, enthalpy):
    """Ideal-liquid / pure-solid liquidus; x is component mole fraction."""
    x = np.asarray(x, dtype=float)
    if np.any((x <= 0) | (x > 1)) or tm <= 0 or enthalpy <= 0:
        raise ValueError("Require 0 < mole fraction <= 1 and positive constants")
    return 1/(1/tm - R_GAS*np.log(x)/enthalpy)


def eutectic(tm_a=63., tm_b=60., h_a=900., h_b=700.):
    """Bisection intersection for an ideal binary with immiscible solids."""
    lo, hi = 1e-10, 1-1e-10
    for _ in range(70):
        mid = (lo+hi)/2
        if liquidus(1-mid, tm_a, h_a) > liquidus(mid, tm_b, h_b):
            lo = mid
        else:
            hi = mid
    x = (lo+hi)/2
    return x, float(liquidus(1-x, tm_a, h_a))


def thermal_rhs(time_s, temperatures_k, params, environment):
    """Two isothermal nodes exchanging conduction, convection and radiation.

    environment(t) returns T_air [K], T_rad [K], h [W/m2/K], Q_abs [W].
    Positive powers enter the wall/payload. View factor is absorbed into area.
    """
    tw, tp = temperatures_k
    tair, trad, h, qabs = environment(time_s)
    qconv = h*params["area_m2"]*(tair-tw)
    qrad = params["emissivity"]*SIGMA*params["area_m2"]*(trad**4-tw**4)
    qconduct = params["conductance_W_K"]*(tw-tp)
    return np.array([(qabs+qconv+qrad-qconduct)/params["C_wall_J_K"],
                     (qconduct+params["payload_power_W"])/params["C_payload_J_K"]])


def sphere_cd(reynolds):
    """Schiller–Naumann correlation only for 0 < Re <= 1000.

    Smooth isolated sphere, continuum incompressible flow; educational
    reference curve, not a CFD solution. Stokes comparison is valid Re << 1.
    """
    re = np.asarray(reynolds, dtype=float)
    if np.any(re <= 0) or np.any(re > 1000):
        raise ValueError("The supported correlation domain is 0 < Re <= 1000")
    return 24/re*(1+.15*re**.687)


def reservoir(recharge_mm_day, initial_storage_mm, k_day, dt_day):
    """Exact propagation under piecewise-constant recharge; Q=k*S.

    Return storage at bin boundaries and cumulative outflow at boundaries.
    No ET, infiltration threshold, channels, or catchment spatial structure.
    """
    if k_day <= 0 or dt_day <= 0 or initial_storage_mm < 0:
        raise ValueError("Positive k and dt, nonnegative storage are required")
    recharge = np.asarray(recharge_mm_day, dtype=float)
    if np.any(recharge < 0):
        raise ValueError("Recharge must be nonnegative")
    storage = np.empty(len(recharge)+1)
    outflow = np.zeros(len(recharge)+1)
    storage[0] = initial_storage_mm
    decay = np.exp(-k_day*dt_day)
    for i, rain in enumerate(recharge):
        storage[i+1] = storage[i]*decay + rain/k_day*(1-decay)
        outflow[i+1] = outflow[i] + rain*dt_day-(storage[i+1]-storage[i])
    return storage, outflow


def attitude_rhs(time_s, state, inertia, kp, kd, torque_limit=np.inf,
                 disturbance=lambda t: 0.):
    """One-axis rigid-body PD control, fixed target theta=0, SI units.

    State: theta [rad], omega [rad/s]. No reaction-wheel momentum,
    sensing delay, flexure, three-dimensional kinematics, or flight software.
    """
    theta, omega = state
    torque = np.clip(-kp*theta-kd*omega, -torque_limit, torque_limit)
    return np.array([omega, (torque+disturbance(time_s))/inertia])


def orbit_verlet(r0, v0, dt, steps, mu=1.):
    """Velocity Verlet for normalized Newtonian two-body dynamics."""
    if dt <= 0 or steps < 1 or mu <= 0:
        raise ValueError("Positive dt, step count and mu required")
    r = np.empty((steps+1, 2))
    v = np.empty_like(r)
    r[0], v[0] = r0, v0
    def acceleration(position):
        norm = np.linalg.norm(position)
        if norm == 0:
            raise ValueError("Two-body collision singularity")
        return -mu*position/norm**3
    a = acceleration(r[0])
    for i in range(steps):
        r[i+1] = r[i]+dt*v[i]+.5*dt**2*a
        anew = acceleration(r[i+1])
        v[i+1] = v[i]+.5*dt*(a+anew)
        a = anew
    energy = .5*np.sum(v*v, axis=1)-mu/np.linalg.norm(r, axis=1)
    angular_momentum = r[:, 0]*v[:, 1]-r[:, 1]*v[:, 0]
    return r, v, energy, angular_momentum


def mixture_fraction(observed, a, b, sigma):
    """Unconstrained 2-endmember linear mixture with sum of weights=1.

    Returns f_hat and analytic standard deviation for independent Gaussian
    band noise with known common sigma. Values outside [0,1] are retained
    to expose weak identifiability; clipping would conceal this diagnostic.
    """
    difference = np.asarray(a)-np.asarray(b)
    information = np.sum(difference*difference)
    if information <= np.finfo(float).eps:
        raise ValueError("Identical endmembers: mixture is unidentifiable")
    estimate = np.sum(difference*(np.asarray(observed)-b))/information
    return float(estimate), float(sigma/np.sqrt(information))


def setup(out):
    out = Path(out)
    for folder in ("data", "figures"):
        (out/folder).mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "axes.titlesize": 11,
                        "figure.dpi": 120, "savefig.dpi": 170,
                        "axes.spines.top": False, "axes.spines.right": False,
                        "svg.fonttype": "none", "svg.hashsalt": str(SEED)})
    return out


def write_csv(path, headers, arrays):
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        for row in zip(*arrays):
            writer.writerow(row)


def save_figure(fig, out, name, real=False):
    fig.text(.5, .012, "REAL CATALOG SAMPLE — discovery and alphabetical selection biases" if real
             else SYNTHETIC, ha="center", fontsize=8, color="#8b2525")
    fig.tight_layout(rect=(0, .045, 1, .98))
    for suffix in ("svg", "png"):
        metadata = {"Creator": "ORION reduced-model toolkit"}
        if suffix == "svg":
            # Fixed synthetic figure metadata makes byte-level reruns reproducible.
            metadata["Date"] = "2026-10-02"
        fig.savefig(out/"figures"/(name+"."+suffix), metadata=metadata)
    plt.close(fig)


def write_meta(out, name, parameters, schema, notes, metrics=None):
    meta = {"kind": "synthetic_illustrative", "random_seed": SEED,
            "parameters": parameters, "schema": schema,
            "assumptions_and_limits": notes, "metrics": metrics or {}}
    (out/"data"/(name+".json")).write_text(json.dumps(meta, indent=2)+"\n", encoding="utf-8")


def demo_fractals(out):
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    for row, (name, ext, jc) in enumerate([
            ("mandelbrot", (-2.1, .7, -1.2, 1.2), None),
            ("julia", (-1.7, 1.7, -1.2, 1.2), -.75+.11j)]):
        x, y = np.linspace(ext[0], ext[1], 241), np.linspace(ext[2], ext[3], 181)
        xx, yy = np.meshgrid(x, y)
        count, distance = fractal_escape(xx+1j*yy, max_iter=160, julia_c=jc)
        first = axes[row, 0].imshow(count, origin="lower", extent=ext, cmap="magma")
        axes[row, 0].set_title(name.title()+": escape count (0 unresolved)")
        fig.colorbar(first, ax=axes[row, 0], label="Iteration")
        second = axes[row, 1].imshow(np.log10(np.maximum(distance, 1e-12)),
            origin="lower", extent=ext, cmap="viridis", vmin=-5, vmax=0)
        axes[row, 1].set_title(name.title()+": exterior distance estimator")
        fig.colorbar(second, ax=axes[row, 1], label="log10 distance [complex-plane units]")
        for ax in axes[row]:
            ax.set_xlabel("Real coordinate [dimensionless]")
            ax.set_ylabel("Imaginary coordinate [dimensionless]")
        write_csv(out/"data"/(name+".csv"), ["real", "imaginary", "escape_iteration_0_unresolved", "distance_estimator"],
            [xx.ravel(), yy.ravel(), count.ravel(), distance.ravel()])
        write_meta(out, name, {"grid": [241, 181], "max_iter": 160,
            "julia_c": None if jc is None else [jc.real, jc.imag], "escape_radius": 2},
            {"real": "dimensionless", "imaginary": "dimensionless", "escape_iteration_0_unresolved": "integer",
             "distance_estimator": "dimensionless; NaN unresolved"},
            ["Finite iteration cannot certify set membership.",
             "Distance is an asymptotic exterior estimator, not exact distance."])
    save_figure(fig, out, "01_fractal_escape_distance")


def demo_liquidus(out):
    x = np.linspace(.0001, .9999, 600)
    ta, tb = liquidus(1-x, 63, 900), liquidus(x, 60, 700)
    xe, te = eutectic()
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(x, ta, "--", label="A branch: Tm=63 K, ΔH=900 J/mol")
    ax.plot(x, tb, "--", label="B branch: Tm=60 K, ΔH=700 J/mol")
    ax.plot(x, np.maximum(ta, tb), color="#152c4c", linewidth=2.5, label="Equilibrium liquidus envelope")
    ax.scatter([xe], [te], color="#bb4e2a", zorder=5)
    ax.annotate(f"Toy eutectic\nxB={xe:.3f}, T={te:.2f} K", (xe, te), xytext=(.56, 36),
                arrowprops={"arrowstyle": "->"})
    ax.set(xlabel="Liquid mole fraction xB [dimensionless]", ylabel="Temperature [K]",
           title="Cryogenic phase-diagram concept: fictitious A–B components", ylim=(15, 67))
    ax.legend(fontsize=8)
    write_csv(out/"data"/"ideal_binary_liquidus.csv", ["x_B", "T_A_K", "T_B_K", "liquidus_K"],
              [x, ta, tb, np.maximum(ta, tb)])
    write_meta(out, "ideal_binary_liquidus", {"Tm_A_K": 63, "Tm_B_K": 60, "fusion_A_J_mol": 900,
        "fusion_B_J_mol": 700, "parameter_origin": "Invented teaching values, not N2/CO/CH4 measurements"},
        {"x_B": "mole fraction", "T_A_K": "K", "T_B_K": "K", "liquidus_K": "K"},
        ["Ideal liquid; immiscible pure solids; constant fusion enthalpy; fixed unspecified pressure.",
         "No calibrated prediction of actual Pluto volatile chemistry, pressure, solid solutions or kinetics."],
        {"eutectic_x_B": xe, "eutectic_T_K": te})
    save_figure(fig, out, "02_ideal_binary_liquidus")


def demo_thermal(out):
    params = {"C_wall_J_K": 1200., "C_payload_J_K": 850., "area_m2": .15,
              "emissivity": .75, "conductance_W_K": .8, "payload_power_W": 3.}
    def environment(t):
        air = 270.-50.*min(t/7200, 1.)
        return air, air-12., .6+7.4*np.exp(-t/3600), 8.
    t = np.linspace(0, 14400, 1441)
    states = rk4(lambda t, y: thermal_rhs(t, y, params, environment), [285, 285], t)
    env = np.array([environment(time) for time in t])
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    axes[0].plot(t/3600, states[:, 0], label="Wall")
    axes[0].plot(t/3600, states[:, 1], label="Payload")
    axes[0].plot(t/3600, env[:, 0], "--", label="Prescribed air")
    axes[0].plot(t/3600, env[:, 1], ":", label="Prescribed radiative sink")
    axes[0].set(xlabel="Time [h]", ylabel="Temperature [K]", title="Two-node balloon-payload thermal model")
    axes[0].legend(fontsize=8)
    conv = env[:, 2]*params["area_m2"]*(env[:, 0]-states[:, 0])
    rad = params["emissivity"]*SIGMA*params["area_m2"]*(env[:, 1]**4-states[:, 0]**4)
    cond = params["conductance_W_K"]*(states[:, 0]-states[:, 1])
    axes[1].plot(t/3600, conv, label="Convection into wall")
    axes[1].plot(t/3600, rad, label="Radiation into wall")
    axes[1].plot(t/3600, cond, label="Conduction wall → payload")
    axes[1].set(xlabel="Time [h]", ylabel="Heat flow [W]", title="Heat-flow signs expose the energy budget")
    axes[1].legend(fontsize=8)
    write_csv(out/"data"/"balloon_thermal.csv", ["time_s", "wall_K", "payload_K", "air_K", "radiative_sink_K",
        "h_W_m2_K", "absorbed_W", "convection_W", "radiation_W", "wall_to_payload_W"],
        [t, states[:, 0], states[:, 1], env[:, 0], env[:, 1], env[:, 2], env[:, 3], conv, rad, cond])
    write_meta(out, "balloon_thermal", params,
        {"time_s": "s", "wall_K": "K", "payload_K": "K", "air_K": "K", "radiative_sink_K": "K",
         "h_W_m2_K": "W m^-2 K^-1", "absorbed_W": "W", "convection_W": "W", "radiation_W": "W", "wall_to_payload_W": "W"},
        ["Uniform temperature per node; radiation area includes assumed view factor.",
         "Air, radiative sink, convection and solar forcing are prescribed synthetic histories.",
         "No ascent trajectory, atmosphere calibration, rarefied-flow correction or qualification claim."])
    save_figure(fig, out, "03_balloon_thermal")


def demo_drag(out):
    re = np.logspace(-4, 3, 450)
    cd = sphere_cd(re)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    axes[0].loglog(re, cd, label="Schiller–Naumann reference")
    axes[0].loglog(re, 24/re, "--", label="Stokes asymptote (Re ≪ 1)")
    axes[0].axvspan(1e-4, .1, color="#a6d6bc", alpha=.3, label="Low-Re comparison interval")
    axes[0].set(xlabel="Reynolds number [dimensionless]", ylabel="Drag coefficient [dimensionless]",
                title="Smooth isolated sphere: 0 < Re ≤ 1000")
    axes[0].legend(fontsize=8)
    axes[1].semilogx(re, cd/(24/re), color="#ac4930")
    axes[1].axhline(1, color="#555", linestyle="--")
    axes[1].set(xlabel="Reynolds number [dimensionless]", ylabel="Cd / (24/Re) [dimensionless]",
                title="Departure from creeping-flow scaling")
    write_csv(out/"data"/"sphere_drag.csv", ["Re", "Cd_Schiller_Naumann", "Cd_Stokes_asymptote"], [re, cd, 24/re])
    write_meta(out, "sphere_drag", {"Re_range": [1e-4, 1000], "formula": "Cd=(24/Re)(1+0.15 Re^0.687)"},
        {"Re": "dimensionless", "Cd_Schiller_Naumann": "dimensionless", "Cd_Stokes_asymptote": "dimensionless"},
        ["Continuum incompressible flow around a smooth isolated sphere; no walls or particle interactions.",
         "Educational correlation reference; not a CFD validation dataset or high-Mach model.",
         "Stokes values are asymptotic comparisons and invalid at moderate/high Re."])
    save_figure(fig, out, "04_sphere_drag")


def demo_hydrology(out):
    rng = np.random.default_rng(SEED)
    n, dt, k, initial = 240, .25, .12, 20.
    recharge = np.zeros(n)
    wet = rng.choice(n, size=22, replace=False)
    recharge[wet] = rng.uniform(2, 12, size=len(wet))
    storage, cumout = reservoir(recharge, initial, k, dt)
    times = np.arange(n+1)*dt
    cumin = np.r_[0., np.cumsum(recharge*dt)]
    residual = storage+cumout-initial-cumin
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].step(times[:-1], recharge, where="post", color="#335c88", label="Prescribed effective recharge")
    axes[0].plot(times, k*storage, color="#ba552a", label="Outflow Q=kS")
    axes[0].set(ylabel="Water flux [mm/day]", title="Linear catchment reservoir with intermittent synthetic recharge")
    axes[0].legend(fontsize=8)
    axes[1].plot(times, storage, label="Storage")
    axes[1].plot(times, cumout, "--", label="Cumulative outflow")
    axes[1].plot(times, cumin, ":", label="Cumulative recharge")
    axes[1].set(xlabel="Time [day]", ylabel="Water depth [mm]")
    axes[1].legend(fontsize=8)
    write_csv(out/"data"/"hydrologic_reservoir.csv", ["time_day", "storage_mm", "outflow_mm_day", "cumulative_outflow_mm",
              "cumulative_recharge_mm", "mass_balance_residual_mm", "next_bin_recharge_mm_day"],
              [times, storage, k*storage, cumout, cumin, residual, np.r_[recharge, np.nan]])
    write_meta(out, "hydrologic_reservoir", {"k_day_inverse": k, "dt_day": dt, "initial_storage_mm": initial},
        {"time_day": "day", "storage_mm": "mm", "outflow_mm_day": "mm/day", "cumulative_outflow_mm": "mm",
         "cumulative_recharge_mm": "mm", "mass_balance_residual_mm": "mm", "next_bin_recharge_mm_day": "mm/day; final NaN"},
        ["Recharge is effective water entering storage, not rainfall; ET and interception are omitted.",
         "One linear reservoir is a pedagogical baseline, not calibrated flood decision support."],
        {"maximum_mass_balance_residual_mm": float(np.max(np.abs(residual)))})
    save_figure(fig, out, "05_hydrologic_reservoir")


def demo_attitude(out):
    p = {"inertia_kg_m2": .12, "kp_Nm_rad": .03, "kd_Nm_s_rad": .08, "torque_limit_Nm": .008,
         "initial_angle_deg": 35., "disturbance_amplitude_Nm": .000025}
    t = np.linspace(0, 120, 2401)
    y = rk4(lambda t, y: attitude_rhs(t, y, p["inertia_kg_m2"], p["kp_Nm_rad"],
        p["kd_Nm_s_rad"], p["torque_limit_Nm"], lambda t: .000025*np.sin(.3*t)),
        [np.deg2rad(35), 0.], t)
    command = np.clip(-p["kp_Nm_rad"]*y[:, 0]-p["kd_Nm_s_rad"]*y[:, 1], -.008, .008)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    axes[0].plot(t, np.rad2deg(y[:, 0]), label="Pointing error")
    axes[0].plot(t, np.rad2deg(y[:, 1]), "--", label="Rate [deg/s]")
    axes[0].set(xlabel="Time [s]", ylabel="Angle [deg]; angular rate [deg/s]", title="One-axis PD attitude-control baseline")
    axes[0].legend(fontsize=8)
    axes[1].plot(t, command*1000, label="Clipped command")
    axes[1].axhline(8, color="#777", linestyle="--")
    axes[1].axhline(-8, color="#777", linestyle="--")
    axes[1].set(xlabel="Time [s]", ylabel="Applied control torque [mN m]", title="Actuator saturation is explicit")
    write_csv(out/"data"/"one_axis_attitude.csv", ["time_s", "theta_rad", "omega_rad_s", "control_torque_Nm"],
        [t, y[:, 0], y[:, 1], command])
    write_meta(out, "one_axis_attitude", p, {"time_s": "s", "theta_rad": "rad", "omega_rad_s": "rad/s", "control_torque_Nm": "N m"},
        ["Single rigid rotational degree of freedom, exact states and a fixed zero-angle reference.",
         "No wheel momentum management, three-axis quaternion dynamics, estimator or sensor delay.",
         "Illustrates control tradeoffs; no spacecraft implementation or qualification."])
    save_figure(fig, out, "06_one_axis_attitude")


def demo_orbit(out):
    e, period, periods = .3, 2*np.pi, 10
    r0, v0 = [1-e, 0], [0, np.sqrt((1+e)/(1-e))]
    errors = []
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.6))
    for steps_per_orbit in (100, 200, 400):
        dt = period/steps_per_orbit
        r, v, energy, am = orbit_verlet(r0, v0, dt, steps_per_orbit*periods)
        t = np.arange(len(r))*dt
        rel = (energy-energy[0])/abs(energy[0])
        errors.append(np.max(np.abs(rel)))
        axes[1].plot(t/period, rel, label=f"{steps_per_orbit} steps/orbit")
        if steps_per_orbit == 400:
            axes[0].plot(r[:, 0], r[:, 1], color="#375b7d")
            axes[0].scatter([0], [0], s=40, color="#cba24c")
            write_csv(out/"data"/"two_body_orbit.csv", ["time_normalized", "x", "y", "vx", "vy", "specific_energy", "specific_angular_momentum"],
                [t, r[:, 0], r[:, 1], v[:, 0], v[:, 1], energy, am])
    axes[0].axis("equal")
    axes[0].set(xlabel="x / reference semimajor axis", ylabel="y / reference semimajor axis", title="Two-body ellipse; e=0.3")
    axes[1].set(xlabel="Time [orbital periods]", ylabel="Relative specific-energy error", title="Bounded symplectic energy error")
    axes[1].legend(fontsize=7)
    counts = np.array([100, 200, 400])
    axes[2].loglog(counts, errors, "o-", label="Measured max energy error")
    axes[2].loglog(counts, errors[0]*(counts[0]/counts)**2, "--", label="Second-order reference")
    axes[2].set(xlabel="Steps / orbital period", ylabel="Max |relative energy error|", title="Timestep refinement")
    axes[2].legend(fontsize=7)
    write_csv(out/"data"/"two_body_convergence.csv", ["steps_per_period", "maximum_relative_energy_error"], [counts, errors])
    write_meta(out, "two_body_orbit", {"normalized_mu": 1, "normalized_semimajor_axis": 1, "eccentricity": e,
        "period_normalized_time": period, "duration_periods": periods},
        {"time_normalized": "sqrt(a_ref^3 / mu_ref)", "x": "a_ref", "y": "a_ref", "vx": "sqrt(mu_ref/a_ref)",
         "vy": "sqrt(mu_ref/a_ref)", "specific_energy": "mu_ref/a_ref", "specific_angular_momentum": "sqrt(mu_ref*a_ref)"},
        ["Point-mass two-body gravity in normalized units; no maneuvers, atmospheric drag or third bodies.",
         "Demonstrates numerical conservation, not an operational trajectory or planetary-defense solution."],
        {"energy_error_by_steps_per_period": dict(zip(map(str, counts), map(float, errors)))})
    save_figure(fig, out, "07_two_body_convergence")


def demo_spectra(out):
    rng = np.random.default_rng(SEED)
    wave = np.linspace(1, 2.5, 180)
    a = .55-.18*np.exp(-((wave-1.08)/.08)**2)-.10*np.exp(-((wave-2.05)/.11)**2)
    b = .50-.17*np.exp(-((wave-2.30)/.045)**2)
    weak_b = a+.001*(b-a)
    fraction, noise = .65, .008
    observed = fraction*a+(1-fraction)*b+rng.normal(0, noise, len(wave))
    weak_observed = fraction*a+(1-fraction)*weak_b+rng.normal(0, noise, len(wave))
    estimate, standard_deviation = mixture_fraction(observed, a, b, noise)
    weak_estimate, weak_sd = mixture_fraction(weak_observed, a, weak_b, noise)
    samples = rng.normal(0, noise, size=(2000, len(wave)))
    delta, weak_delta = a-b, a-weak_b
    mc_strong = fraction+samples@delta/(delta@delta)
    mc_weak = fraction+samples@weak_delta/(weak_delta@weak_delta)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.8))
    axes[0].plot(wave, a, label="Synthetic endmember A")
    axes[0].plot(wave, b, label="Synthetic endmember B")
    axes[0].scatter(wave, observed, s=4, alpha=.5, label="Noisy mixture")
    axes[0].plot(wave, estimate*a+(1-estimate)*b, "--", label="Least-squares fit")
    axes[0].set(xlabel="Wavelength [µm]", ylabel="Synthetic reflectance [dimensionless]", title="Linear endmember mixture")
    axes[0].legend(fontsize=7)
    axes[1].hist(mc_strong, bins=35, color="#456c91")
    axes[1].axvline(fraction, color="#ba5229", linestyle="--")
    axes[1].set(xlabel="Estimated A fraction", ylabel="Realizations", title=f"Separated spectra: σf={standard_deviation:.4f}")
    axes[2].hist(mc_weak, bins=35, color="#9b624f")
    axes[2].axvline(fraction, color="#263f57", linestyle="--")
    axes[2].set(xlabel="Unconstrained estimated A fraction", ylabel="Realizations", title=f"Nearly identical spectra: σf={weak_sd:.1f}")
    write_csv(out/"data"/"spectral_mixture.csv", ["wavelength_um", "endmember_A", "endmember_B", "weak_B", "observed", "weak_observed", "fit"],
        [wave, a, b, weak_b, observed, weak_observed, estimate*a+(1-estimate)*b])
    write_csv(out/"data"/"spectral_monte_carlo.csv", ["realization", "f_separated", "f_nearly_identical"],
        [np.arange(len(mc_strong)), mc_strong, mc_weak])
    write_meta(out, "spectral_mixture", {"true_A_fraction": fraction, "noise_sigma": noise, "monte_carlo_runs": 2000},
        {"wavelength_um": "µm", "endmember_A": "reflectance", "endmember_B": "reflectance", "weak_B": "reflectance",
         "observed": "reflectance", "weak_observed": "reflectance", "fit": "reflectance"},
        ["Invented Gaussian absorption bands; no measured mineral library or Mars observations.",
         "Linear areal mixture, independent known-variance Gaussian errors, exactly known endmembers.",
         "Near-collinear endmembers produce unphysical unconstrained weights; adding priors does not add new information.",
         "Real intimate mixtures, scattering, grain size and correlated calibration need a richer model."],
        {"f_hat": estimate, "analytic_sigma_f": standard_deviation, "weak_f_hat": weak_estimate, "weak_analytic_sigma_f": weak_sd,
         "monte_carlo_sigma_f": float(np.std(mc_strong, ddof=1)), "weak_monte_carlo_sigma_f": float(np.std(mc_weak, ddof=1))})
    save_figure(fig, out, "08_spectral_identifiability")


def fetch_exoplanets(out):
    """Download a small public archive query; validate before writing files."""
    request = Request(ARCHIVE_URL, headers={"User-Agent": "ORION-research-portfolio/1.0"})
    with urlopen(request, timeout=90) as response:
        raw = response.read()
        final_url = response.url
        content_type = response.headers.get("Content-Type", "")
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    columns = ["pl_name", "hostname", "pl_orbper", "pl_rade", "st_met", "discoverymethod"]
    if len(rows) != 200 or list(rows[0]) != columns:
        raise ValueError(f"Unexpected archive response: {len(rows)} rows; expected 200 and exact schema")
    for row in rows:
        if float(row["pl_orbper"]) <= 0 or float(row["pl_rade"]) <= 0:
            raise ValueError("Nonpositive physical period/radius in selected catalog sample")
    (out/"data"/"exoplanet_sample.csv").write_bytes(raw)
    provenance = {"kind": "real_public_catalog_snapshot", "provider": "NASA Exoplanet Archive",
        "retrieved_utc": datetime.now(timezone.utc).isoformat(), "table": "pscomppars", "query_adql": QUERY,
        "request_url": ARCHIVE_URL, "response_url": final_url, "response_content_type": content_type,
        "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "rows": len(rows),
        "schema": {"pl_name": "planet name string", "hostname": "host name string", "pl_orbper": "days",
                   "pl_rade": "Earth radii", "st_met": "dex relative to solar; nullable; abundance basis requires archive metadata",
                   "discoverymethod": "categorical archive discovery method"},
        "limitations": ["First 200 names alphabetically among rows with period and radius; not random or representative.",
            "Discovery method, completeness, missing-radius selection, alphabetical ordering and follow-up biases apply.",
            "Composite parameter rows may combine values from different publications; not necessarily self-consistent.",
            "No uncertainties, detection-efficiency correction, metallicity basis or per-parameter references in this small educational extract.",
            "No occurrence rates, physical class labels, mass-radius claims or causal metallicity inference from this plot."],
        "source_documentation": ["https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html",
                                 "https://exoplanetarchive.ipac.caltech.edu/docs/API_TD_columns.html",
                                 "https://doi.org/10.26133/NEA13"]}
    (out/"data"/"exoplanet_sample.provenance.json").write_text(json.dumps(provenance, indent=2)+"\n", encoding="utf-8")
    return rows


def demo_exoplanets(out):
    path = out/"data"/"exoplanet_sample.csv"
    if not path.exists():
        return
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    fig, ax = plt.subplots(figsize=(9, 5.2))
    markers = ("o", "s", "^", "D", "v", "P", "X", "<", ">")
    for index, method in enumerate(sorted({row["discoverymethod"] for row in rows})):
        subset = [row for row in rows if row["discoverymethod"] == method]
        ax.scatter([float(row["pl_orbper"]) for row in subset],
                   [float(row["pl_rade"]) for row in subset], s=27, alpha=.7, marker=markers[index % len(markers)],
                   label=f"{method} (n={len(subset)})")
    ax.set(xscale="log", yscale="log", xlabel="Catalog orbital period [day]", ylabel="Catalog planet radius [Earth radii]",
           title=f"NASA Exoplanet Archive: {len(rows)} alphabetically selected composite rows")
    ax.legend(fontsize=8, loc="best")
    save_figure(fig, out, "09_real_exoplanet_sample", real=True)


def manifest(out):
    records = []
    for folder in ("data", "figures"):
        for path in sorted((out/folder).glob("*")):
            data = path.read_bytes()
            records.append({"path": path.relative_to(out).as_posix(), "bytes": len(data),
                            "sha256": hashlib.sha256(data).hexdigest()})
    (out/"manifest.json").write_text(json.dumps({"seed": SEED, "assets": records}, indent=2)+"\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--fetch-exoplanets", action="store_true", help="Refresh the 200-row real catalog snapshot")
    args = parser.parse_args()
    out = setup(args.out)
    for demo in (demo_fractals, demo_liquidus, demo_thermal, demo_drag,
                 demo_hydrology, demo_attitude, demo_orbit, demo_spectra):
        demo(out)
    if args.fetch_exoplanets:
        fetch_exoplanets(out)
    demo_exoplanets(out)
    manifest(out)
    print(f"Generated {len(list((out/'figures').glob('*.svg')))} figure pairs in {out}")


if __name__ == "__main__":
    main()
