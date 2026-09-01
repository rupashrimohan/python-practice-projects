def sandwiches(*items):
    """Making Sandwiches"""
    print(items)
    for topping in items:
        print(topping)


sandwiches("Bread", "butter", "Chicken")
print("\n")
sandwiches("Panini", "Avacado")
