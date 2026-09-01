dream_vacations = {}

polling = True

while polling:
    name = input("Enter your name: ")
    vacation = input("Enter your dream vacation: ")
    dream_vacations[name] = vacation
    message = input("Would you like continue polling?(yes/no): ")
    if message.lower() == "no":
        polling = False

for name, vacation in dream_vacations.items():
    print(f"{name}'s dream vacation is {vacation}.")
