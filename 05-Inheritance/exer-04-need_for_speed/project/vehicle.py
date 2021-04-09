class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = fuel_consumption

    def drive(self, kilometers):
        if self.check_fuel(kilometers):
            self.fuel -= self.fuel_consumption * kilometers

    def check_fuel(self, kilometers):
        return self.fuel_consumption * kilometers <= self.fuel


