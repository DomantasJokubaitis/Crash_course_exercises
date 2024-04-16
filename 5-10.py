current_users = ["john", "jack", "Jeremy", "James", "jones"]
new_users = ["Gerald", "Cleetus", "jeremy", "james", "Richard"]
lower_current_users = []

for user in current_users:
    lower_current_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_current_users:
        print("You need a new username")
    else:
        print("Your username is available")
