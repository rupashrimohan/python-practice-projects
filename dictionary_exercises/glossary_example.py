glossary = {
    "sort()": "sorts the actual list in an ascending order.",
    "del": "remove an item from the list or dictionary.",
    "append()": "add an item in the list at the end.",
    "pop()": "remove an item from list at the end or using index.",
}

for keyword, definition in glossary.items():
    print(f"{keyword}:")
    print(f"\t{definition}\n")


# keys()
for keyword in glossary.keys():
    print(keyword)
