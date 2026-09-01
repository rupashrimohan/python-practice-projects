rivers = {"nile": "egypt", "amazon": "brazil", "misissippi": "usa", "patapsco": "usa"}


# loop
for river, country in rivers.items():
    print(f"The {river} runs throught {country}.")
print("\n")
# river
for river in sorted(rivers.keys()):
    print(river)
print("\n")
# country
for country in rivers.values():
    print(country)
print("\n")

for country in set(rivers.values()):
    print(country)
