prompt = "Enter the toppings for the pizza, Enter 'quit' if you are done.: "


active = True
while active:
    message = input(prompt)
    if message.lower() != "quit":
        print(f"We will add {message} to your pizza")
    else:
        active = False
