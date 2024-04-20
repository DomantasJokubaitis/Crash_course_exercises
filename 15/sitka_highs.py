from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

path = Path("C:/Users/doman/Desktop/Crash_course_exercises/weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, title in enumerate(header_row):
    print(index, title)

highs = []
lows = []
dates = []

for row in reader:
    high = int(row[4])
    low = int(row[5])
    date = dt.strptime(row[2], "%Y-%m-%d")
    highs.append(high)
    lows.append(low)
    dates.append(date)



number = 0

for item in highs:
    number += 1


print(dates)

plt.style.use("fast")
fig, ax = plt.subplots()
ax.plot(dates, highs, color = "red", linewidth = 5)
ax.plot(dates, lows, color = "blue", linewidth = 5)
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.set_xlabel("", fontsize = 16)
ax.fill_between(dates, highs, lows, facecolor = "purple", alpha = 0.2)
fig.autofmt_xdate()

plt.show()