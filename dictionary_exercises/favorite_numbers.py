person_num = {
    "Zara": [3, 4, 5],
    "Alice": [0, 2],
    "Bob": [9],
    "Charcles": [6, 23, 65],
    "Micheal": [4],
}

for name, numbers in person_num.items():
    if len(numbers) == 1:
        print(f"\n{name}'s favorite number is {numbers[0]}\n")
    else:
        print(f"\n{name}'s favorite numbers are:")
        for num in numbers:
            print(num)


# sorted()

for name in sorted(person_num.keys()):
    print(f"{name.title()}, thank you for participating in the poll.")
