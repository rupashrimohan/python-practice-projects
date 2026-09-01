peoples = ["Alice", "Mark", "Micheal", "Jadon"]

person_num = {"Zara": 3, "Alice": 2, "Bob": 9, "Charcles": 6, "Micheal": 4}

if peoples:
    for people in peoples:
        if people in person_num:
            print(f"{people}, thank you for participating in the poll")
        else:
            print(f"We like to invite {people} to take the poll asap.")
else:
    print("Provide the list of people who should take the poll.")
