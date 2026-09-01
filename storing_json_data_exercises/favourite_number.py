from pathlib import Path
import json


def favourite_number():
    """This function returns your favourite number"""
    path = Path("files/favorite_number.json")
    if path.exists():
        fav_num = get_favorite_number(path)
        print(f"Welcome back! you favourite number is: {fav_num}")
    else:
        fav_num = store_favorite_number(path)
        print(f"your favorite number is : {fav_num}")


def get_favorite_number(path):
    """Return the fav number"""
    contents = path.read_text()
    fav_num = json.loads(contents)
    return fav_num


def store_favorite_number(path):
    """Store the fav number"""
    fav_num = input("Enter your favorite number: ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    return fav_num


favourite_number()
