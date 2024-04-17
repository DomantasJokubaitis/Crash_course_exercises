def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("Domantas", "Jokubaitis", faceit_level = 3, health = "poor", money = "poor2")

print(user_profile)
