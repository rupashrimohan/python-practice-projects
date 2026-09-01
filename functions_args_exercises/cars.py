def car_print(manufacturer, model, **cars):
    """Print the car info"""
    cars["manufacturer"] = manufacturer
    cars["model"] = model
    print(cars)


car_print("subaru", "outback", color="blue", tow_package=True)
