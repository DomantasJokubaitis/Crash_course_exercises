from matplotlib import pyplot as plt
from datetime import datetime as dt
from pathlib import Path
import csv

path = Path("C:/Users/doman/Desktop/Crash_course_exercises/weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)

index = 0

for item in header:
    print(f"{index} {item}")
    index += 1

precipitation, dates = [], []

for object in reader:
    precipitate = float(object[5])
    date = dt.strptime(object[2], "%Y-%m-%d")
    precipitation.append(precipitate)
    dates.append(date)



plt.style.use('seaborn-v0_8-poster')
fig, ax = plt.subplots()
ax.plot(dates, precipitation)
ax.set_ylabel("Precipitation (mm)")
ax.tick_params(labelsize = 13)

fig.autofmt_xdate()

plt.show()