from pathlib import Path

path = Path("files/learning.python.txt")
contents = path.read_text()

print(contents)

print("\n This the another version using lines")
lines = contents.splitlines()
learning_python = ""
for line in lines:
    learning_python += line.strip()


print(learning_python.replace("Python", "C"))
