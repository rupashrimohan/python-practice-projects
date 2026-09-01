pet_0 = {"dog": "marie"}
pet_1 = {"cat": "alandra"}
pet_2 = {"mouse": "charles"}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    for petty, owner in pet.items():
        print(f"{petty} is owned by {owner}.")
