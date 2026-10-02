"""Deterministic educational kernels, not complete project research solvers.

All examples are synthetic. Units and limitations are included in each result.
Uses standard library only; no live services, hardware, or scientific claims.
"""
from __future__ import annotations
import math
import random


def positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be finite and positive')


def escape(c: complex, z: complex = 0j, iterations: int = 128) -> int:
    """Mandelbrot-only helper: fixed radius two requires the z0=0 domain."""
    if z != 0j:
        raise ValueError('This reference requires Mandelbrot z0=0; arbitrary Julia starts are unsupported.')
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError('iterations must be a positive integer')
    for n in range(1, iterations + 1):
        z = z*z+c
        if abs(z) > 2:
            return n
    return 0  # unresolved, not proof of membership


def liquidus(x, tm=270.0, enthalpy=6000.0):
    positive(tm, 'tm'); positive(enthalpy, 'enthalpy')
    if not 0 < x <= 1:
        raise ValueError('mole fraction must be in (0,1]')
    return 1/(1/tm-8.314462618*math.log(x)/enthalpy)


def phase():
    rows = []
    for i in range(1, 100):
        x = i/100
        rows.append([x, liquidus(1-x), liquidus(x, 230, 4500)])
    return result(['fraction_B', 'liquidus_A_K', 'liquidus_B_K'], rows,
                  'Illustrative ideal binary phase curves; parameters are invented, not Pluto materials.')


def orbit(e=0.35, steps=1200, periods=1):
    if not 0 <= e < 0.9 or steps < 40 or periods < 1:
        raise ValueError('use 0<=e<0.9, steps>=40, periods>=1')
    # GM=a=1, nondimensional two-body orbit, periapsis initial state.
    r = [1-e, 0.0]; v = [0.0, math.sqrt((1+e)/(1-e))]
    dt = 2*math.pi/steps
    def acceleration(p):
        norm = math.hypot(*p)
        return [-q/norm**3 for q in p]
    rows = []
    for i in range(steps*periods+1):
        energy = (v[0]**2+v[1]**2)/2-1/math.hypot(*r)
        angular = r[0]*v[1]-r[1]*v[0]
        rows.append([i*dt, *r, energy, angular])
        a = acceleration(r)
        rn = [r[j]+v[j]*dt+0.5*a[j]*dt*dt for j in range(2)]
        an = acceleration(rn)
        v = [v[j]+0.5*(a[j]+an[j])*dt for j in range(2)]
        r = rn
    return result(['time_dimensionless','x_a','y_a','energy_GM_over_a','angular_dimensionless'], rows,
                  'Nondimensional two-body velocity Verlet; no ephemeris, encounters, CR3BP, DRO or Apophis risk.')


def thermal(power=2.0, conductance=0.08, capacity=100.0, ambient=250.0):
    positive(conductance, 'conductance'); positive(capacity, 'capacity'); positive(ambient, 'ambient')
    if not math.isfinite(power) or power < 0:
        raise ValueError('power must be finite and nonnegative')
    # Exact one-node solution, no radiation or changing atmospheric convection.
    initial = 293.15; steady = ambient+power/conductance
    rows = [[t, steady+(initial-steady)*math.exp(-conductance*t/capacity)]
            for t in range(0, 7201, 60)]
    return result(['time_s','temperature_K'], rows,
                  'Exact lumped thermal reference; constant boundary, illustrative parameters; not a balloon or engine solver.')


def sphere_drag(re):
    positive(re, 'Re')
    if re > 1000:
        raise ValueError('reference correlation limited here to Re<=1000')
    return 24/re*(1+0.15*re**0.687)


def drag():
    rows = [[10**(-2+5*i/100), sphere_drag(10**(-2+5*i/100))] for i in range(101)]
    return result(['Re','Cd'], rows, 'Schiller-Naumann reference correlation, not a CFD algorithm; excludes drag crisis.')


def spectral():
    rng=random.Random(17)
    rows=[]
    for i in range(161):
        x=480+i*0.075
        truth=1+0.8*math.exp(-0.5*((x-486.3)/0.65)**2)
        rows.append([x, truth, truth+rng.gauss(0,0.035)])
    return result(['wavelength_nm','truth_relative_flux','synthetic_relative_flux'], rows,
                  'Synthetic Gaussian line near H-beta; not an Eta Carinae observation or fitted radial velocity.')


def mixture():
    rows=[]
    for i in range(121):
        x=1+i/100
        a=0.7-0.25*math.exp(-((x-1.3)/0.08)**2)
        b=0.5-0.20*math.exp(-((x-1.9)/0.10)**2)
        rows.append([x,a,b,0.4*a+0.6*b])
    return result(['wavelength_um','synthetic_endmember_A','synthetic_endmember_B','areal_mix'],rows,
                  'Invented endmember spectra, linear areal mixing only; no real mineral, isotope or chemical identification.')


def poisson(rng, mean):
    if mean < 0 or mean > 100 or not math.isfinite(mean):
        raise ValueError('Poisson demo mean must be finite in [0,100]')
    limit=math.exp(-mean); p=1.0; n=0
    while p>limit:
        n+=1; p*=rng.random()
    return max(0,n-1)


def radiation():
    rng=random.Random(42); rows=[]
    for h in range(0,31000,500):
        rate=0.2+1.1*math.exp(-((h-17000)/6000)**2)
        live=30; n=poisson(rng,rate*live)
        rows.append([h,live,n,n/live,math.sqrt(n)/live])
    return result(['altitude_m','live_time_s','synthetic_counts','count_rate_per_s','approx_sigma_per_s'],rows,
                  'Invented altitude/count profile; Gaussian count uncertainty invalid at low counts; not measured radiation or dose.')


def calibration():
    rows=[]
    for raw in range(100,1101,10):
        corrected=(raw-100-10)/(0.95*2)
        rows.append([raw,corrected])
    return result(['raw_ADU','bias_dark_flat_corrected_ADU_per_s'],rows,
                  'Synthetic scalar detector correction; not OCAMS, NIRCam or absolute flux calibration.')


def hydraulic():
    rows=[]
    alpha=0.04; n=1.6; m=1-1/n
    for i in range(121):
        suction=10**(-1+5*i/120)
        se=(1+(alpha*suction)**n)**(-m)
        theta=0.08+(0.43-0.08)*se
        rows.append([suction,theta,se])
    return result(['suction_cm','volumetric_water_fraction','effective_saturation'],rows,
                  'Illustrative van Genuchten retention; no Frye Fire measurements and no Richards PDE solution.')


def adsorption():
    rows=[[i/10,2*0.7*(i/10)/(1+0.7*(i/10))] for i in range(101)]
    return result(['concentration_arbitrary','uptake_arbitrary'],rows,
                  'Single-solute Langmuir illustration; no selectivity, recovery, algae experiment or moisture-swing cycle.')


def kinetics():
    return result(['time_arbitrary','fraction_remaining'],[[i/10,math.exp(-0.25*i/10)] for i in range(121)],
                  'Synthetic first-order reference decay; not a biological treatment or detoxification model.')


def antenna():
    """Polar theta is measured from the dipole axis, not above the horizon."""
    rows=[]
    for degree in range(181):
        theta=math.radians(degree)
        power=0 if degree in (0,180) else (math.cos(math.pi/2*math.cos(theta))/math.sin(theta))**2
        rows.append([degree,power])
    return result(['theta_degree','normalized_ideal_dipole_power'],rows,
                  'Ideal lossless thin half-wave dipole elevation pattern; not measured ground-station gain.')


def pendulum():
    rows=[]
    zeta=0.05
    for i in range(121):
        ratio=10**(-1+2*i/120)
        transmissibility=math.sqrt((1+(2*zeta*ratio)**2)/((1-ratio*ratio)**2+(2*zeta*ratio)**2))
        rows.append([ratio,transmissibility])
    return result(['frequency_over_resonance','base_motion_transmissibility'],rows,
                  'Linear single-stage base excitation; excludes LIGO multistage suspension and thermal noise.')


def beam():
    length=0.1; modulus=2e9; inertia=1e-12; force=1e-3
    rows=[]
    for i in range(101):
        x=length*i/100
        y=force*x*x*(3*length-x)/(6*modulus*inertia)
        rows.append([x,y])
    return result(['position_m','deflection_m'],rows,
                  'Small-deflection homogeneous cantilever reference; not calibrated cilia, bone or launch-vehicle FEA.')


def consensus():
    n=12; state=[1.0]+[0.0]*(n-1); rows=[]
    for step in range(101):
        rows.append([step,*state])
        state=[state[i]+0.2*(state[(i-1)%n]+state[(i+1)%n]-2*state[i]) for i in range(n)]
    return result(['iteration']+[f'node_{i}' for i in range(n)],rows,
                  'Synthetic connected-ring consensus; no moving algorithmic matter or general target detector.')


def power():
    """load_W is requested demand; clipped storage omits unserved/curtailed energy."""
    rows=[]; energy=50.0; previous=0
    for i in range(145):
        hour=i/6; pv=max(0,80*math.sin(math.pi*(hour-6)/12)) if 6<=hour<=18 else 0
        load=20; net=pv-load
        if i: energy=min(150,max(0,energy+previous/6))
        rows.append([hour,pv,load,energy]); previous=net
    return result(['hour','synthetic_PV_W','load_W','storage_Wh'],rows,
                  'Synthetic solar profile and clipped ideal storage; not dispatch optimization, measured weather, EPS qualification or electrolysis.')


def nlms():
    rng=random.Random(12); taps=8; weights=[0.0]*taps; history=[0.0]*taps; rows=[]
    for i in range(1000):
        desired=math.sin(2*math.pi*0.017*i)
        reference=rng.gauss(0,1)
        history=[reference]+history[:-1]
        interference=0.8*history[0]+0.3*history[3]
        measured=desired+interference
        predicted=sum(w*x for w,x in zip(weights,history)); error=measured-predicted
        denom=1e-6+sum(x*x for x in history)
        weights=[w+0.15*error*x/denom for w,x in zip(weights,history)]
        rows.append([i,desired,measured,error])
    return result(['sample','desired_synthetic','measured_synthetic','filtered_synthetic'],rows,
                  'Synthetic NLMS with ideal independent noise reference; desired-signal leakage can invalidate cancellation.')


def result(columns, rows, limitation):
    return {'evidence_class':'SYNTHETIC EDUCATIONAL REFERENCE','columns':columns,'rows':rows,'limitations':limitation}


def fractal():
    rows=[]
    for j in range(48):
        for i in range(64):
            x=-2+3*i/63; y=-1.2+2.4*j/47
            rows.append([x,y,escape(complex(x,y))])
    return result(['real','imaginary','escape_iteration_zero_unresolved'],rows,
                  'Finite-resolution escape-time Mandelbrot; unresolved iterates do not prove membership.')


def image():
    rng=random.Random(31); rows=[]
    for j in range(32):
        for i in range(32):
            sky=100+0.1*i
            source=70*math.exp(-((i-15)**2+(j-17)**2)/8)
            truth=sky+source
            rows.append([i,j,sky,truth,truth+rng.gauss(0,math.sqrt(truth+9))])
    return result(['pixel_x','pixel_y','truth_background_count','truth_total_count','synthetic_count'],rows,
                  'Synthetic Gaussian source with Gaussian approximation to Poisson/read noise; no instrument-calibrated image.')


def attitude():
    # Spherical inertia J=1 kg m^2, one axis quaternion attitude, bounded PD torque.
    angle=1.0; rate=0.0; dt=0.02; rows=[]
    def derivative(a,w):
        torque=max(-0.1,min(0.1,-0.18*math.sin(a/2)-0.6*w))
        return w,torque
    for i in range(2001):
        torque=derivative(angle,rate)[1]
        rows.append([i*dt,math.cos(angle/2),math.sin(angle/2),angle,rate,torque])
        k1=derivative(angle,rate)
        k2=derivative(angle+dt*k1[0]/2,rate+dt*k1[1]/2)
        k3=derivative(angle+dt*k2[0]/2,rate+dt*k2[1]/2)
        k4=derivative(angle+dt*k3[0],rate+dt*k3[1])
        angle+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        rate+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
    return result(['time_s','quaternion_w','quaternion_x','angle_rad','rate_rad_per_s','torque_Nm'],rows,
                  'Single-axis spherical-inertia quaternion PD example; excludes full coupled 3-axis dynamics and flight sensors.')


DEMOS = {'phase':phase,'orbit':orbit,'thermal':thermal,'drag':drag,'spectrum':spectral,
         'mixture':mixture,'radiation':radiation,'calibration':calibration,'hydrology':hydraulic,
         'adsorption':adsorption,'kinetics':kinetics,'antenna':antenna,'mechanics':beam,
         'suspension':pendulum,'swarm':consensus,'power':power,'adaptive':nlms,
         'fractal':fractal,'image':image,'attitude':attitude}
