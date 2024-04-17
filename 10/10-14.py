from pathlib import Path
import json

def get_username():
    path = Path("username.json")
    username = input("Input your username: ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you, {username}")

def greet_user():
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        answer = input(f"Is your username {username}? ")
        if answer == "yes":
            print(f"Welcome back, {username}! ")
        elif answer == "no":
            get_username()
        

greet_user()