pizza_toppings = ["Cheese", "Pepparoni", "Olives"]
if pizza_toppings:
    for topping in pizza_toppings:
        print(f"Adding {topping}")
    print("Finishes making Pizza.")
else:
    print("Are you trying to order plain pizza.")

# emply version
print("\nEmpty topping list version")
pizza_toppings = []
if pizza_toppings:
    for topping in pizza_toppings:
        print(f"Adding {topping}")
    print("Finishes making Pizza.")
else:
    print("Are you trying to order plain pizza.")

# two list version
print("\nTwo List version")
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
print(f"Available Toppings = {available_toppings}")
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
print(f"Requested Toppings = {requested_toppings} ")

if requested_toppings:
    for each_topping in requested_toppings:
        if each_topping in available_toppings:
            print(f"Adding {each_topping}")
        else:
            print(f"Sorry, this {each_topping} is not available at the store.")
    print("Finished building the pizza.")
else:
    print("Are you trying to build the plain pizza.")
