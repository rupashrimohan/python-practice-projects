from pathlib import Path
import json


def get_stored_username(path):
    """Returns the stored username in the parameter path"""
    path = Path("files/username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        if username:
            return username
        else:
            return None
    else:
        return None


def register_username(path):
    """Register the username"""
    username = input("Enter your username:")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greeting the user by their username"""
    path = Path("files/username.json")
    username = get_stored_username(path)
    if username:
        verify = input(f"Is {username} is the correct username? Type('y'/'n'): ")
        if verify.lower() == "y":
            print(f"Welcome back! {username}")
        elif verify.lower() == "n":
            username = register_username(path)
            print(f"Welcome back! {username}")
        else:
            print(f"Welcome back! {username}")
    else:
        username = register_username(path)
        print(f"We will remember you whe you come back, {username}")


greet_user()
