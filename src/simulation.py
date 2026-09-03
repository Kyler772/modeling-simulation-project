from rocket import Rocket

def run_simulation(rocket: Rocket, time_step: float = 1.0):
    time = 0.0
    telemetry = []
    max_altitude = rocket.altitude

    while rocket.velocity >= 0:
        rocket.update_fuel(time_step)
        rocket.update_velocity(time_step)
        rocket.update_altitude(time_step)

        time += time_step

        data = {
            "time": time,
            "altitude": rocket.altitude,
            "velocity": rocket.velocity,
            "fuel_mass": rocket.fuel_mass,
            "acceleration": rocket.get_acceleration()
        }
        telemetry.append(data)

        if rocket.altitude > max_altitude:
            max_altitude = rocket.altitude

        

    return max_altitude, time, telemetry


    