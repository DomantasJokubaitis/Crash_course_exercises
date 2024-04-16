while True:

    try:
        first = input("input a number: ")
        second = input("input a second number: ")
        answer = int(first) + int(second)

    except ValueError:
        print("inputed character is not a number")

    else:
        print(answer)
        break