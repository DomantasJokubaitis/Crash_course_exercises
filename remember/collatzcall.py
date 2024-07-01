from collatz import collatz
import sys

try:
    number = int(input("Enter any integer: "))
except ValueError:
    print("Invalid value")
    sys.exit()

while number != 1:
    number = collatz(number)
    print(number)