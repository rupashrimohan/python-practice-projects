def get_formatted_name(first, last, middle=""):
    """Return the formatted full name"""
    if middle:
        formatted_name = f"{first} {middle} {last}"
    else:
        formatted_name = f"{first} {last}"
    return formatted_name.title()
