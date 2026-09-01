def build_profile(first, last, **user_info):
    """Build the user profile"""
    user_info["first"] = first
    user_info["last"] = last
    print(user_info)


build_profile("Rupashri", "Mohan", location="Maryland", Field="Software")


def build_profile(first, last, **info):
    """Build the user profile"""
    user_info = {}
    user_info["first"] = first
    user_info["last"] = last
    print(user_info)


build_profile("Rupashri", "Mohan", location="Maryland", Field="Software")
