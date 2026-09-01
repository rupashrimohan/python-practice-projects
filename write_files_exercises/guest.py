from pathlib import Path

path = Path("files/guests.txt")
name = input("Enter your name: ")
path.write_text(name)
