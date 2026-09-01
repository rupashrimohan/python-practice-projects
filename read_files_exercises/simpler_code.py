from pathlib import Path

path = Path("files/learning.python.txt")
contents = path.read_text()

print(contents)
print(len(contents))

print("\n This the another version using lines")
learning_python = ""
for line in contents.splitlines():
    learning_python += line.strip()

print(len(learning_python))
print(learning_python.replace("Python", "C"))
