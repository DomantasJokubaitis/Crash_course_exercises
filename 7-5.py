while True:

    age = input("Enter your age: ")

    if age == "quit":
        break

    else:

        age = int(age)

        if age < 3:
            print("Ticket costs $0")

        elif age > 3 and age <= 12:
            print("Ticket costs $10")

        elif age > 12:
            print("Ticket costs $15")