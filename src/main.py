from rocket import Rocket
from simulation import run_simulation

rocket1 = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)
rocket2 = Rocket("Nova", 1500.0, 750.0, 0.0, 0.0, 35000.0, 20.0)

max_altitude, flight_time, telemetry = run_simulation(rocket1, 0.01)

print("Maximum altitude:", f"{max_altitude:.2f} meters")
print("Time to apogee:", f"{flight_time:.2f} seconds")
print("Telemetry data:", telemetry[0])  

print("First telemetry entry:", telemetry[0])
print("Last telemetry entry:", telemetry[-1])


