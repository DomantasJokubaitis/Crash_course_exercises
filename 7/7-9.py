sandwich_orders = ["poboy", "pastrami", "cheeseburger", "pastrami", "avocado_toast", "pastrami"]
finished_sandwiches = []

print("pastrami sandwiches are temporarily not available. ")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"\nI made your {finished}")
    finished_sandwiches.append(finished)

for sandwich in finished_sandwiches:
    print(f"\n{sandwich} is finished. ")