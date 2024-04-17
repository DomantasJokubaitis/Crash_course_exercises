def city_adding(city_name, country_name, population = None):

    if population:
        sentence = f"{city_name}, {country_name} - {population}"
    else:
        sentence = f"{city_name}, {country_name}"
    return sentence