class Car:
    """A Simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print the statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the guven amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Prints a statement to fill the gas tank"""
        print("The gas tank has to be filled befire start.")


# inheritance
class Battery:
    """This represents Battery"""

    def __init__(self, battery_size=40):
        """Initializes attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing a battery size"""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print the statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225

        print(f"This car range is {range}")


class ElectricCar(Car):
    """Represents aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initializes attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Overriding the parent class method to match the child class description"""
        print("Electric cars donot have gas tank.")


# inistantiation
my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.battery_size = 60
my_leaf.battery.get_range()
my_leaf.fill_gas_tank()
