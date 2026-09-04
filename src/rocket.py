class Rocket:
    def __init__(
        self,
        name: str,
        dry_mass: float,
        fuel_mass: float,
        altitude: float,
        velocity: float,
        max_thrust: float,
        fuel_burn_rate: float
    ):
        self.name = name
        self.dry_mass = dry_mass
        self.fuel_mass = fuel_mass
        self.altitude = altitude
        self.velocity = velocity
        self.max_thrust = max_thrust
        self.fuel_burn_rate = fuel_burn_rate

    def get_total_mass(self):
        return self.dry_mass + self.fuel_mass

    def burn_fuel(self, amount: float):
        if amount < 0:
            raise ValueError("Fuel burn amount cannot be negative")
        elif amount > self.fuel_mass:
            self.fuel_mass = 0
        else:
            self.fuel_mass -= amount

    def get_weight(self):
        gravity = 9.81
        return self.get_total_mass() * gravity

    def get_net_force(self):
         if self.fuel_mass == 0:
            return -self.get_weight()
         else:
             return self.max_thrust - self.get_weight()
         

    def get_acceleration(self):
        return self.get_net_force() / self.get_total_mass()

    def update_velocity(self, time_step: float):
        self.velocity += self.get_acceleration() * time_step

    def update_altitude(self, time_step: float):
        self.altitude += self.velocity * time_step   

    def update_fuel(self, time_step: float): 
        self.burn_fuel(self.fuel_burn_rate * time_step)
    
    
   
   