from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Janis Joplin' work"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_middlenames():
    """do names like Janis Amanda Joplin works"""
    formatted_name = get_formatted_name("janis", "joplin", "amanda")
    assert formatted_name == "Janis Amanda Joplin"
