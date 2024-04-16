try:
    first = int(input("input a number: "))
    second = int(input("input a second number: "))
    print(first + second)

except ValueError:
    print("inputed character is not a number")
