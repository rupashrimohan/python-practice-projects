# list of dictonaries
people_0 = {"first_name": "Rupashri", "last_name": "Mohan", "city": "elkridge"}
people_1 = {"first_name": "Mithun", "last_name": "Ravi", "city": "columbia"}
people_2 = {"first_name": "Nyra", "last_name": "Mithun", "city": "ellicott city"}

peoples = [people_0, people_1, people_2]

for person in peoples:
    first = person["first_name"]
    last = person["last_name"]
    city = person["city"]
    print(f"{first} {last} lives in {city}")
