# A List in a Dictionary

favorite_places = {
    "alice": ["egypt", "columbia"],
    "mark": ["spain", "paris", "London"],
    "Micheal": ["usa"],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name}'s favorite place is {places[0]}")
    else:
        print(f"\n{name}'s favorite places are:")
        for place in places:
            print(place)
