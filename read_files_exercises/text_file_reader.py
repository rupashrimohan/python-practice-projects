from pathlib import Path

path = Path("files/text.txt")
content = path.read_text().rstrip()

lines = content.splitlines()
print(lines)
