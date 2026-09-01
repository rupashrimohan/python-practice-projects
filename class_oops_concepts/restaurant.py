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


# Instantiation
korean_restaurant = Restaurant("KAWA Sushi Restaurant", "Korean")
print(korean_restaurant.restaurant_name)
print(korean_restaurant.cuisine_type)
korean_restaurant.describe_restaurant()
korean_restaurant.open_restaurant()
korean_restaurant.number_served(4)


# three more instances
print("\n")
indian_restaurant = Restaurant("Biriyani Grill", "Indian")
indian_restaurant.describe_restaurant()

print("\n")
chinese_restaurant = Restaurant("Bon Chon", "Chinese")
chinese_restaurant.describe_restaurant()
