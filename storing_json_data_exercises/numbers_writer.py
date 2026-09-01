from pathlib import Path
import json

numbers = [1, 2, 6, 3, 9, 8]

path = Path("files/numbers.json")
contents = json.dumps(numbers)

path.write_text(contents)
