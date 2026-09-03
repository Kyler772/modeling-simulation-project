from rocket import Rocket

rocket1 = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0)
rocket2 = Rocket("Nova", 1500.0, 750.0, 0.0, 0.0, 35000.0)


for second in range(5):
    rocket1.update_velocity(1.0)
    rocket1.update_altitude(1.0)

    print(second + 1, rocket1.velocity, rocket1.altitude)