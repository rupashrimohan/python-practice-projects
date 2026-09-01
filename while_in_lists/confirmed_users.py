unconfirmed_users = ["alice", "Mark", "peter"]
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)
    print(f"{user} has been added into the confirmed users list")

print(confirmed_users)
