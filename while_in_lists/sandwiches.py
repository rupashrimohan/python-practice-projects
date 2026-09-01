sandwich_orders = ["ChickenSandwich", "VeganSandwich", "BeefSandwich", "pastrami"]

finished_sandwiches = []

while sandwich_orders:
    while "pastrami" in sandwich_orders:
        print("Sorry we ran out of pastrami. Processing the next order.")
        sandwich_orders.remove("pastrami")
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}, enjoy your sandwich:)")
    finished_sandwiches.append(sandwich)

print("These are the list of sandwiches that are made today:")
for each in finished_sandwiches:
    print(each)
