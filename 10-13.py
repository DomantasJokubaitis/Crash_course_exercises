from pathlib import Path
import json

def greet_user():
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        my_dict = json.loads(contents)
        print(f"Welcome back, {my_dict["username"]}. Are you still {my_dict["age"]} years old and {my_dict["gender"]}? ")
    else:
        my_dict = {}
        username = input("Input your username: ")
        age = input("Input your age: ")
        gender = input("Input your gender: ")
        my_dict["username"] = username
        my_dict["age"] = age
        my_dict["gender"] = gender
        contents = json.dumps(my_dict)
        path.write_text(contents)
        print(f"We'll remember you, {username}")

greet_user()