import datetime as dt

def time_calc(future):


    today = dt.date.today()
    future = future.split("-")
    year = int(future[0])
    month = int(future[1])
    day = int(future[2])
    future = dt.date(year, month, day)
    today = dt.date.today()
    diff = (future - today).days
    return diff

while True:
    try:

        future = input("Enter future date as yyyy-mm-dd: ")
        left = time_calc(future)
        print(f"There are {left} days left till {future}")
        break

    except ValueError:
        print("Invalid date, try again. ")