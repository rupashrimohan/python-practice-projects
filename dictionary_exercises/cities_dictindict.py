# A dictionary isnide the dictionary

cities = {
    "Maryland": {"capital": "Annapolis", "famous": "crab", "flag": "yellow"},
    "Virginia": {"capital": "Richmond", "famous": "indian food", "flag": "blue"},
}

for city, city_facts in cities.items():
    print(f"\n{city}'s interesting facts are:")
    for key, value in city_facts.items():
        print(f"{key}:{value}")
