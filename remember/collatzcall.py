from collatz import collatz

number = int(input("Enter any integer: "))
while number != 1:
    number = collatz(number)
    print(number)