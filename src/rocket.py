class Rocket:
    def __init__(
        self,
        name: str,
        dry_mass: float,
        fuel_mass: float,
        altitude: float,
        velocity: float,
        max_thrust: float
    ):
        self.name = name
        self.dry_mass = dry_mass
        self.fuel_mass = fuel_mass
        self.altitude = altitude
        self.velocity = velocity
        self.max_thrust = max_thrust

    def get_total_mass(self):
        return self.dry_mass + self.fuel_mass

    def burn_fuel(self, amount: float):
        if amount < 0:
            raise ValueError("Fuel burn amount cannot be negative")
        elif amount > self.fuel_mass:
            self.fuel_mass = 0
        else:
            self.fuel_mass -= amount