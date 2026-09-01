usernames = ["Jadon", "Alice", "Admin", "Mark"]
if usernames:
    for name in usernames:
        if name.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("Sorry I donot see any names in the liust specified")

# Empty list version
print("\nTesting empty list version")
usernames = []
if usernames:
    for name in usernames:
        if name.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("Sorry I donot see any names in the liust specified")
