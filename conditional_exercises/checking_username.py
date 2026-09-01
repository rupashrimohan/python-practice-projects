current_users = ["Alice", "Mark", "Jane", "Alandra"]
new_users = ["Kaylie", "Jane", "Losli", "Mark"]

existing_users = [user.lower() for user in current_users]
print(existing_users)

for new_user in new_users:
    if new_user.lower() not in existing_users:
        print(f"{new_user} username is available to use in our website.")
    else:
        print("you have to choose a different username")
