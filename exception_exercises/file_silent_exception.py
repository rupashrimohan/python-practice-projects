from pathlib import Path


def count_words(filenames):
    """count the number of words in the file and print"""
    for each_path in filenames:
        path = Path(f"files/{each_path}")
        try:
            contents = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            pass
        else:
            lines = contents.split()
            num_words = len(lines)
            print(f"The file {path.name} contains {num_words} words.")


filenames = ["alice.txt", "syu.txt", "programming.txt"]
count_words(filenames)
