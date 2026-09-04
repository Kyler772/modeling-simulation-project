print("GUI file is running")

from src.rocket import Rocket
from src.simulation import run_simulation
import tkinter as tk

rocket = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0, 10.0)

max_altitude, flight_time, telemetry = run_simulation(rocket, 0.1)
telemetry_index = 0
is_running = False

window = tk.Tk()
window.title("Rocket Flight Simulator")
window.geometry("500x700")

canvas = tk.Canvas(window, width=500, height=550)
canvas.pack()

time_label = tk.Label(window, text="Time: 0.00 s")
time_label.pack()

altitude_label = tk.Label(window, text="Altitude: 0.00 m")
altitude_label.pack()

velocity_label = tk.Label(window, text="Velocity: 0.00 m/s")
velocity_label.pack()

fuel_label = tk.Label(window, text="Fuel: 500.00 kg")
fuel_label.pack()


canvas.create_line(0, 500, 500, 500)

rocket_shape = canvas.create_polygon(
    250, 450,
    225, 500,
    275, 500
)

def animate_rocket():
    global telemetry_index
    if not is_running:
        return


    if telemetry_index >= len(telemetry):
        return

    data = telemetry[telemetry_index]
    altitude = data["altitude"]

    time_label.config(text=f"Time: {data['time']:.2f} s")
    altitude_label.config(text=f"Altitude: {data['altitude']:.2f} m")
    velocity_label.config(text=f"Velocity: {data['velocity']:.2f} m/s")
    fuel_label.config(text=f"Fuel: {data['fuel_mass']:.2f} kg")

    scaled_altitude = altitude / max_altitude * 400

    canvas.coords(
        rocket_shape,
        250, 450 - scaled_altitude,
        225, 500 - scaled_altitude,
        275, 500 - scaled_altitude
    )

    telemetry_index += 1

    window.after(20, animate_rocket)

def start_animation():
    global is_running

    if not is_running:
        is_running = True
        animate_rocket()

def pause_animation():
    global is_running
    is_running = False

def reset_animation():
    global telemetry_index, is_running

    is_running = False
    telemetry_index = 0

    canvas.coords(
        rocket_shape,
        250, 450,
        225, 500,
        275, 500
    )

    time_label.config(text="Time: 0.00 s")
    altitude_label.config(text="Altitude: 0.00 m")
    velocity_label.config(text="Velocity: 0.00 m/s")
    fuel_label.config(text="Fuel: 500.00 kg")


start_button = tk.Button(
    window,
    text="Start",
    command=start_animation
)
start_button.pack()

pause_button = tk.Button(
    window,
    text="Pause",
    command=pause_animation
)
pause_button.pack()

reset_button = tk.Button(
    window,
    text="Reset",
    command=reset_animation
)
reset_button.pack()

window.mainloop()