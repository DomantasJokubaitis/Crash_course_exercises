

def sandwich_toppings(*toppings):
    print(f"\nToppings summary: ")
    for topping in toppings:
        print(f"-{topping}")

sandwich_toppings("Lettuce", "Tomato")
sandwich_toppings("Ham", "Cheese")
sandwich_toppings("Mayo", "Egg")
