responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb someday? ")

    responses[name] = mountain
    state = input("Would like to continue the poll?(yes/no) : ")
    if state.lower() == "no":
        polling_active = False

print(responses)
