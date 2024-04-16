def city_country(city, country):
    location = f"{city}, {country}"
    return location

precise_location = city_country("Santiago", "Chile")
print(precise_location)
precise_location = city_country("Kaunas", "Lithuania")
print(precise_location)
precise_location = city_country("Stockholm", "Sweden")
print(precise_location)