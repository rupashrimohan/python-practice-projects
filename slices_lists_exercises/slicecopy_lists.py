my_pizzas = ["Cheese", "chicken"]

friend_pizzas = my_pizzas[:]

# add new pizza to my_pizza
my_pizzas.append("Pepparoni")
# add new pizza to friend_pizza
friend_pizzas.append("mac&cheese")

print("My Favorite Pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy Friend's Favorite Pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

num = [9, 8, 7]
print(num)
