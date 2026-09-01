from pathlib import Path

path = Path("files/alice.txt")
try:
    lines = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"The specified file {path.name} doesn't exists.")
else:
    count = lines.lower().count("the")
    print(f"The number of times the word 'the' appears in the file is {count}.")
