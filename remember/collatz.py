def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    if number % 2 == 1:
        number = number * 3 + 1
        return number
    



