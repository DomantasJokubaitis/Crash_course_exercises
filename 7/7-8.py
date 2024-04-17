sandwich_orders = ["poboy", "cheeseburger", "avocado_toast"]
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"\nI made your {finished}")
    finished_sandwiches.append(finished)

for sandwich in finished_sandwiches:
    print(f"\n{sandwich} is finished. ")