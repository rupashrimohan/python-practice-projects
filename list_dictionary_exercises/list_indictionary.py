pizza = {"crust": "thin", "toppings": ["mushroom", "cheese"]}

# summarize the order
print(f"you ordered a {pizza['crust']}- crust pizza with the toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")


# example 2
favorite_lang = {"jane": ["sql", "c"], "mark": ["python"], "vena": ["c++", "vb.net"]}

for name, fav in favorite_lang.items():
    if len(fav) == 1:
        print(f"{name}'s favorite language is:{fav[0]}")
    else:
        print(f"\n{name}'s favorite languages are:")
        for lan in fav:
            print(lan)
