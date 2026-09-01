from pathlib import Path
import json


def get_stored_userinfo(path):
    """Returns the stored user's information from the parameter path"""
    path = Path("files/userinfo.json")
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        if user_info:
            return user_info
        else:
            return None
    else:
        return None


def register_userinfo(path):
    """Register the user's information"""
    user_info = {}
    user_info["username"] = input("Enter your username:")
    user_info["fav_num"] = input("Enter your fav number:")
    user_info["city"] = input("Enter your city:")
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def users_info():
    """Get the User's Information"""
    path = Path("files/userinfo.json")
    user_info = get_stored_userinfo(path)
    if user_info:
        print(f"Welcome back! {user_info}")
    else:
        user_info = register_userinfo(path)
        print(f"We will remember you whe you come back, {user_info['username']}")
        print(user_info)


users_info()
