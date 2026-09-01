from city_functions import get_formatted_city_country


def test_city_country_names():
    """Test function if this formatting works - 'Santiago, Chile"""
    formatted_city_name = get_formatted_city_country("santiago", "chile")
    assert formatted_city_name == "Santiago, Chile"


def test_city_country_names_with_population():
    """Test function if this formatting works - 'Santiago, Chile - population 4000"""
    formatted_city_name = get_formatted_city_country("santiago", "chile", 4000)
    assert formatted_city_name == "Santiago, Chile - Population 4000"
