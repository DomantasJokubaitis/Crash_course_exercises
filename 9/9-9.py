class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            print(f'{self.battery_size}')
        elif self.battery_size == 65:
            print(f'{self.battery_size}')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

my_elec = ElectricCar("merc", "eq", 2023)
my_elec.battery.get_range()
my_elec.battery.upgrade_battery()
my_elec.battery.get_range()
    