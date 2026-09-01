from pathlib import Path

path = Path("files/pi_1_million_decimals.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday details as mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first milliom digits of pi!")
else:
    print("Your birthday doesnot appear in the first million digits of pi!.")
