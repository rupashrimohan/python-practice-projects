from pathlib import Path

path = Path("/Users/rupashrimohan/Desktop/python_work/files/pi_1_million_decimals.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line

print(f"{pi_string[:52]}")
print(len(pi_string))
