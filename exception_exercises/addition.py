print("Addition:\n")
active = True

while active:
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    try:
        answer = int(num_1) + int(num_2)
    except ValueError:
        print("Please enter a valid number")
    else:
        print(f"Answer: {answer}")
    state = input("Do you want to continue type ('y'/'n')? ")
    if state.lower() == "n":
        active = False
        print("Thank for trying our addition program")
    elif state.lower() == "y":
        active = True
    else:
        active = False
        print("Thank for trying our addition program")
