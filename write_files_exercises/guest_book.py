from pathlib import Path

path = Path("files/guest_book.txt")
active_state = True
name = ""
while active_state:
    guest_name = input("Enter the Guest name: ")
    name += guest_name + "\n"
    path.write_text(name)
    active = input("Do you have more Guest type('yes'/'no')? ")
    if active.lower() == "no":
        active_state = False
