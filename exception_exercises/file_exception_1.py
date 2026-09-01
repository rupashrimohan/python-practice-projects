from pathlib import Path

try:
    cat_file_path = Path("/Users/rupashrimohan/Desktop/python_work/files/cat.txt")
    dog_file_path = Path("/Users/rupashrimohan/Desktop/python_work/files/dogs.txt")
    cat_names = cat_file_path.read_text().rstrip()
    dog_names = dog_file_path.read_text().rstrip()
    print(f"Cat Names are : {cat_names}")
    print(f"Dog Names are : {dog_names}")
except FileNotFoundError as e:
    pass
    # print(f"The given file {e.filename} is not found in the mentioned directory")
