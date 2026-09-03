from rocket import Rocket

rocket1 = Rocket("Atlas", 1000.0, 500.0, 0.0, 0.0, 25000.0)
rocket2 = Rocket("Nova", 1500.0, 750.0, 0.0, 0.0, 35000.0)


rocket1.burn_fuel(50.0)
print(rocket1.fuel_mass)
print(rocket1.get_total_mass())
print(rocket1.dry_mass)