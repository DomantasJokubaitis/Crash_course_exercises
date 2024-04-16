cities = {

"vilnius" : {

    "functionis" : "capital",
    "population" : "600000",
    "tier" : "b"
}
,
"kaunas" : {

"functionis" : "culture",
"population" : "300000",
"tier" : "c"

}
}

for city, city_info in cities.items():
    print(f"{city} function is {city_info["functionis"]},
          it has a population of {city_info["population"]},
          and scores an {city_info["tier"]} in the baseness tier")