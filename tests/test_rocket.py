import pytest
from src.rocket import Rocket
from src.simulation import run_simulation

@pytest.fixture
def atlas():
    return Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)

def test_burn_fuel(atlas):
    initial_fuel_mass = atlas.fuel_mass
    burn_amount = 100.0

    atlas.burn_fuel(burn_amount)

    assert atlas.fuel_mass == initial_fuel_mass - burn_amount


def test_burn_fuel_exceeding_amount():
    rocket = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)

    burn_amount = 600.0

    rocket.burn_fuel(burn_amount)

    assert rocket.fuel_mass == 0.0


def test_burn_fuel_negative_amount():
    rocket = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)
    with pytest.raises(ValueError) as excinfo:
        rocket.burn_fuel(-100.0)

    assert str(excinfo.value) == "Fuel burn amount cannot be negative"


def test_get_total_mass(atlas):
    assert atlas.get_total_mass() == 1500.0

def test_get_weight(atlas):
    assert atlas.get_weight() == pytest.approx(14715.0)

def test_get_net_force(atlas):
    assert atlas.get_net_force() == pytest.approx(10285.0)

    atlas.fuel_mass = 0.0
    assert atlas.get_net_force() == pytest.approx(-9810.0)


def test_get_acceleration(atlas):
    assert atlas.get_acceleration() == pytest.approx(6.856666666666667)

    atlas.fuel_mass = 0.0
    assert atlas.get_acceleration() == pytest.approx(-9.81)


def test_update_velocity(atlas):
    time_step = 1.0
    atlas.update_velocity(time_step)

    assert atlas.velocity == pytest.approx(6.8566666667)


def test_update_altitude(atlas):
    atlas.velocity = 10.0
    time_step = 1.0
    atlas.update_altitude(time_step)

    assert atlas.altitude == pytest.approx(10.0)


def test_update_fuel(atlas):
    time_step = 1.0
    atlas.update_fuel(time_step)

    assert atlas.fuel_mass == pytest.approx(490.0)


def test_simulation_produces_telemetry():
    rocket = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)

    max_altitude, flight_time, telemetry = run_simulation(rocket, 0.1)

    assert len(telemetry) > 0
    assert "time" in telemetry[0]
    assert "altitude" in telemetry[0]
    assert "velocity" in telemetry[0]
    assert "fuel_mass" in telemetry[0]
    assert "acceleration" in telemetry[0]


def test_simulation_reaches_apogee():
    rocket = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)

    max_altitude, flight_time, telemetry = run_simulation(rocket, 0.1)

    assert max_altitude > 0
    assert flight_time > 0
    assert telemetry[-1]["velocity"] < 0


def test_simulation_uses_all_fuel(atlas):
    max_altitude, flight_time, telemetry = run_simulation(atlas, 0.1)

    assert telemetry[-1]["fuel_mass"] == pytest.approx(0.0)