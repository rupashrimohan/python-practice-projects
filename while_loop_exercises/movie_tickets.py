prompt = "Enter the age of a person, (Enter 'quit' when you're done):"

active = True
while active:
    message = input(prompt)
    if message.isdigit():
        age = int(message)
        if age < 3:
            print("The ticket is free.")
        elif age >= 3 and age <= 12:
            print("The ticket cost is $10.")
        elif age > 12:
            print("The ticket cost is $15.")
    elif message.lower() == "quit":
        break
    else:
        print("Invalid input.")
