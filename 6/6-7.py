albert = {"name" : "albert", "surname" : "einstein", "city" : "vilnius"}
nicola = {"name" : "nicola", "surname" : "tesla", "city" : "kaunas"}
nauseda = {"name" : "gitanas", "surname" : "nauseda", "city" : "klaipeda"}

people = [albert, nicola, nauseda]

for person in people:
    print(f"{person["name"]}'s full name is {person["name"]} {person["surname"]}, they live in {person["city"]}")