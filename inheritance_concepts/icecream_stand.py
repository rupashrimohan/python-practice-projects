class Restaurant:
    """This is simple info about a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the restaurant name and the cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers = 0

    def describe_restaurant(self):
        """A Simple description about the restaurant"""
        print(
            f"The restaurant {self.restaurant_name} is famous for {self.cuisine_type}."
        )
        print(f"{self.restaurant_name} is located in the downtown.")

    def open_restaurant(self):
        """Provides info about the open timings"""
        print(f"{self.restaurant_name} is open until midnight every day of the week.")

    def number_served(self, reserved_number):
        """Number of people served"""
        self.numbers += reserved_number
        print(f"Number of people served is: {self.numbers}")


class IceCreamStand(Restaurant):
    """A Simple info about an IceCreamShop"""

    def __init__(self, restaurant_name, cuisine_type="Icecream"):
        """Initialize the attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Display all the flavors"""
        for flavor in self.flavors:
            print(flavor)


my_flavor = IceCreamStand("ColdStone")
my_flavor.flavors.append("Chocolate")
my_flavor.flavors.append("Vanilla")
my_flavor.display_flavors()
my_flavor.describe_restaurant()
