def get_formatted_city_country(city, country, population=None):
    """Get a formatted city, country like Santiago, Chile"""
    if population:
        formatted_city_name = f"{city}, {country} - population {population}"
    else:
        formatted_city_name = f"{city}, {country}"
    return formatted_city_name.title()
