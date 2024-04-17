pizzas = ["Cheesy", "Meaty", "Mixed"]
friend_pizzas = pizzas[:]

pizzas.append("Mushroomy")
friend_pizzas.append("Vegetabley")

print(f"\nMy favorite pizzas are: ", end = "")
for pizza in pizzas:
    print(pizza.lower(), end=" ")

print(f"\n\nMy friends favorite pizzas are: ", end = "")
for pizza in friend_pizzas:
    print(pizza.lower(), end=" ")