name = "Rupashri"
if name == "Rupashri":
    print(f"The given name is {name} and result == evaluates to {name=="Rupashri"}")
if name != "Rupashri":
    print(f"The given name is {name} and result != evaluates to {name=="Rupashri"}")
if name.lower() == "rupashri":
    print(
        f"The given name is {name.lower()} and result == evaluates to {name.lower()=="rupashri"}"
    )

# and AND or operator
age_0 = 21
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)


things_lists = ["apple", "banana", "orange"]
if "apple" in things_lists:
    print("yes, apple is in the list")
if "apricot" not in things_lists:
    print("no, apricot is not in the list")
