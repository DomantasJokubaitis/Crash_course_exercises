my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

friend_foods.append("cookies")

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)