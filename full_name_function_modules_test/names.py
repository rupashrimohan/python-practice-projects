from name_function import get_formatted_name

print("Enter 'q' anytime to quit")
while True:
    first = input("enter the first name: ")
    if first.lower() == "q":
        break
    last = input("enter the last name: ")
    if last.lower() == "q":
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)
