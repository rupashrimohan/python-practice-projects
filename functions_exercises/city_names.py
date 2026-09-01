def city_names(city, country):
    """This function formats the city and its country"""
    formatted_value = f'"{city}, {country}"'
    return formatted_value


city_one = city_names("Santiago", "Chile")
city_two = city_names("Annapolis", "USA")

print(city_one)
print(city_two)

