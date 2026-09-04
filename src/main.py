from rocket import Rocket
from simulation import run_simulation
import matplotlib.pyplot as plt

rocket1 = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)
rocket2 = Rocket("Nova", 1500.0, 750.0, 0.0, 0.0, 35000.0, 20.0)

max_altitude, flight_time, telemetry = run_simulation(rocket1, 0.01)

times = [data["time"] for data in telemetry]
altitudes = [data["altitude"] for data in telemetry]
velocities = [data["velocity"] for data in telemetry]
fuel_masses = [data["fuel_mass"] for data in telemetry]

print(f"Maximum altitude: {max_altitude:.2f} meters")
print(f"Time to apogee: {flight_time:.2f} seconds")

print("First telemetry entry:", telemetry[0])
print("Last telemetry entry:", telemetry[-1])
print(f"Telemetry records: {len(telemetry)}")


plt.plot(times, altitudes)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Rocket Flight Profile")
plt.show()


plt.plot(times, velocities)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Rocket Velocity")
plt.show()


plt.plot(times, fuel_masses)
plt.xlabel("Time (s)")
plt.ylabel("Fuel Mass (kg)")
plt.title("Rocket Fuel Consumption")
plt.show()