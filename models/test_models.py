"""Independent limiting cases, conservation laws and convergence checks.

Run: python -m unittest -v test_models.py
These checks verify reduced-model mathematics; they do not establish empirical
accuracy, mission readiness or validity outside the declared model domain.
"""
import unittest
import numpy as np
import models as m


class FractalTests(unittest.TestCase):
    def test_known_mandelbrot_orbits(self):
        # 0 is a fixed point; -1 has period 2; 1 escapes via 0,1,2,5.
        count, distance = m.fractal_escape(np.array([0, -1, 1]), max_iter=30)
        np.testing.assert_array_equal(count, [0, 0, 3])
        self.assertTrue(np.isnan(distance[0]))
        self.assertGreater(distance[2], 0)

    def test_julia_unit_circle_limit(self):
        # For c=0, the filled Julia set is the closed unit disk.
        points = np.array([0, .5, 1., 1.1, 1.7, 3.])
        count, distance = m.fractal_escape(points, julia_c=0., max_iter=50)
        np.testing.assert_array_equal(count[:3], [0, 0, 0])
        self.assertTrue(np.all(count[3:] > 0))
        # Closed form derivative of z^(2^n) gives r log r, not r-1.
        np.testing.assert_allclose(distance[3:], points[3:]*np.log(points[3:]), rtol=1e-12)


class PhaseTests(unittest.TestCase):
    def test_pure_component_and_temperature_depression(self):
        self.assertAlmostEqual(float(m.liquidus(1., 80., 1400.)), 80.)
        self.assertLess(float(m.liquidus(.7, 80., 1400.)), 80.)

    def test_symmetric_eutectic_analytical_limit(self):
        x, t = m.eutectic(tm_a=80., tm_b=80., h_a=1400., h_b=1400.)
        analytical = 1/(1/80.+m.R_GAS*np.log(2)/1400.)
        self.assertAlmostEqual(x, .5, places=12)
        self.assertAlmostEqual(t, analytical, places=11)

    def test_invalid_composition_rejected(self):
        for fraction in (0., -1., 1.1):
            with self.assertRaises(ValueError):
                m.liquidus(fraction, 60., 900.)


class ThermalTests(unittest.TestCase):
    def setUp(self):
        self.params = {"C_wall_J_K": 2., "C_payload_J_K": 3., "area_m2": 0.,
                       "emissivity": .8, "conductance_W_K": .4, "payload_power_W": 0.}
        self.environment = lambda t: (250., 250., 0., 0.)

    def test_isolated_network_energy_and_equilibrium(self):
        times = np.linspace(0, 20, 201)
        y = m.rk4(lambda t, y: m.thermal_rhs(t, y, self.params, self.environment), [300, 270], times)
        energy = 2*y[:, 0]+3*y[:, 1]
        np.testing.assert_allclose(energy, np.full(len(times), 1410.), atol=1e-9)
        equilibrium = 1410/5
        rate = .4*(1/2+1/3)
        exact_wall = equilibrium+3/5*30*np.exp(-rate*times)
        np.testing.assert_allclose(y[:, 0], exact_wall, rtol=1e-8)

    def test_radiative_and_convective_equilibrium(self):
        p = dict(self.params, area_m2=.3)
        derivative = m.thermal_rhs(0., [250., 250.], p, lambda t: (250., 250., 2., 0.))
        np.testing.assert_array_equal(derivative, [0., 0.])

    def test_fourth_order_against_exact_isolated_solution(self):
        equilibrium = (2*300+3*270)/5
        exact_wall = equilibrium+3/5*30*np.exp(-.4*(1/2+1/3)*8)
        errors = []
        for steps in (8, 16, 32):
            y = m.rk4(lambda t, y: m.thermal_rhs(t, y, self.params, self.environment),
                      [300, 270], np.linspace(0, 8, steps+1))
            errors.append(abs(y[-1, 0]-exact_wall))
        self.assertGreater(errors[0]/errors[1], 14.)
        self.assertGreater(errors[1]/errors[2], 14.)


class DragTests(unittest.TestCase):
    def test_creeping_flow_force_matches_stokes(self):
        # Dimensional force from Cd must approach the independent exact
        # creeping-flow result F=3*pi*dynamic_viscosity*diameter*speed.
        density, viscosity, diameter, speed = 1000., 1., .001, 1e-10
        reynolds = density*speed*diameter/viscosity
        force = .5*density*speed**2*(np.pi*diameter**2/4)*m.sphere_cd(reynolds)
        exact_stokes = 3*np.pi*viscosity*diameter*speed
        self.assertAlmostEqual(float(force/exact_stokes), 1., delta=1e-6)

    def test_extrapolation_rejected(self):
        for re in (0., -2., 1001.):
            with self.assertRaises(ValueError):
                m.sphere_cd(re)


class HydrologyTests(unittest.TestCase):
    def test_no_recharge_matches_analytical_recession(self):
        storage, outflow = m.reservoir(np.zeros(100), 15., .2, .5)
        t = np.arange(101)*.5
        np.testing.assert_allclose(storage, 15*np.exp(-.2*t), rtol=1e-12)
        np.testing.assert_allclose(storage+outflow, 15., atol=1e-12)

    def test_steady_recharge_storage_and_outflow(self):
        storage, outflow = m.reservoir(np.full(80, 3.), 3/.12, .12, .25)
        np.testing.assert_allclose(storage, 25., atol=1e-12)
        np.testing.assert_allclose(outflow, np.arange(81)*.25*3, atol=1e-12)

    def test_variable_recharge_mass_balance(self):
        rain = np.array([0, 0, 2, 7, 0, 0, 1, 3.], dtype=float)
        storage, outflow = m.reservoir(rain, 4., .15, .2)
        cumulative_in = np.r_[0., np.cumsum(.2*rain)]
        np.testing.assert_allclose(storage+outflow, 4+cumulative_in, atol=1e-12)
        self.assertTrue(np.all(storage >= 0))


class AttitudeTests(unittest.TestCase):
    def test_torque_free_rotation(self):
        times = np.linspace(0, 12, 121)
        y = m.rk4(lambda t, y: m.attitude_rhs(t, y, .5, 0., 0.), [.3, .02], times)
        np.testing.assert_allclose(y[:, 0], .3+.02*times, atol=1e-12)
        np.testing.assert_allclose(y[:, 1], .02, atol=1e-12)

    def test_undamped_spring_analytical_oscillation(self):
        times = np.linspace(0, 10, 1001)
        inertia, stiffness = .5, .08
        y = m.rk4(lambda t, y: m.attitude_rhs(t, y, inertia, stiffness, 0.), [.3, 0.], times)
        exact = .3*np.cos(np.sqrt(stiffness/inertia)*times)
        np.testing.assert_allclose(y[:, 0], exact, atol=1e-11)
        energy = .5*inertia*y[:, 1]**2+.5*stiffness*y[:, 0]**2
        np.testing.assert_allclose(energy, energy[0], atol=1e-12)

    def test_pd_dissipates_mechanical_energy(self):
        times = np.linspace(0, 30, 3001)
        y = m.rk4(lambda t, y: m.attitude_rhs(t, y, .5, .08, .2), [.3, 0.], times)
        energy = .25*y[:, 1]**2+.04*y[:, 0]**2
        self.assertTrue(np.all(np.diff(energy) <= 1e-12))
        self.assertLess(energy[-1], energy[0]*1e-3)


class OrbitTests(unittest.TestCase):
    def test_second_order_convergence_to_exact_circular_orbit(self):
        errors = []
        for count in (100, 200, 400):
            r, _, _, _ = m.orbit_verlet([1., 0], [0, 1.], 2*np.pi/count, count)
            errors.append(np.linalg.norm(r[-1]-[1., 0]))
        self.assertGreater(errors[0]/errors[1], 3.9)
        self.assertGreater(errors[1]/errors[2], 3.9)

    def test_central_force_preserves_angular_momentum(self):
        e = .3
        _, _, _, angular = m.orbit_verlet([1-e, 0], [0, np.sqrt((1+e)/(1-e))], .01, 3000)
        expected = np.sqrt(1-e*e)  # h^2=mu*a*(1-e^2), normalized a=mu=1.
        np.testing.assert_allclose(angular, expected, atol=1e-12)

    def test_energy_error_bounded_and_refines(self):
        maximum_errors = []
        for count in (100, 200):
            _, _, energy, _ = m.orbit_verlet([.7, 0], [0, np.sqrt(1.3/.7)], 2*np.pi/count, count*10)
            maximum_errors.append(np.max(abs(energy-energy[0]))/abs(energy[0]))
        self.assertLess(maximum_errors[0], .02)
        self.assertGreater(maximum_errors[0]/maximum_errors[1], 3.9)


class InverseTests(unittest.TestCase):
    def test_exact_mixture_recovers_fraction(self):
        a, b, fraction = np.array([1., .8, .5]), np.array([.6, .4, .9]), .37
        observed = fraction*a+(1-fraction)*b
        estimated, _ = m.mixture_fraction(observed, a, b, .01)
        self.assertAlmostEqual(estimated, fraction, places=13)

    def test_identical_endmembers_cannot_be_inverted(self):
        with self.assertRaises(ValueError):
            m.mixture_fraction(np.ones(5), np.ones(5), np.ones(5), .01)

    def test_sampling_uncertainty_matches_analytic_information(self):
        rng = np.random.default_rng(m.SEED)
        a, b = np.array([.6, .5, .3, .2]), np.array([.3, .2, .4, .5])
        sigma, fraction = .008, .65
        estimates = [m.mixture_fraction(fraction*a+(1-fraction)*b+noise, a, b, sigma)[0]
                     for noise in rng.normal(0, sigma, size=(6000, 4))]
        _, analytic = m.mixture_fraction(fraction*a+(1-fraction)*b, a, b, sigma)
        self.assertAlmostEqual(np.std(estimates, ddof=1)/analytic, 1., delta=.04)


if __name__ == "__main__":
    unittest.main()
