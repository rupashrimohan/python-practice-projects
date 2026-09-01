print("Please enter two numbers for division calculator as per the below prompt.")
print("you can enter 'q' if you want to quit at any time of the program")

while True:
    first_num = input("Enter the first number: ")
    if first_num.lower() == "q":
        break
    second_num = input("Enter the second number: ")
    if second_num.lower() == "q":
        break

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("you can't divide by zero.")
    else:
        print(answer)
4
