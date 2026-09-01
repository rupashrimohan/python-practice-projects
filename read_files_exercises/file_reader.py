from pathlib import Path

path = Path("files/pi_digits.txt")
contents = path.read_text()  # .rstrip()
# print(contents)

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
