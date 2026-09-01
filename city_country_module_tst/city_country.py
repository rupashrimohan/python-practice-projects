from city_functions import get_formatted_city_country

print(
    "Enter your city and country to get a formatted string\n Press 'q' to quite anytime"
)

while True:
    city = input("Enter your City: ")
    if city.lower() == "q":
        break
    country = input("Enter your Country: ")
    if country.lower() == "q":
        break
    formatted_city_name = get_formatted_city_country(city, country)
    print(formatted_city_name)
