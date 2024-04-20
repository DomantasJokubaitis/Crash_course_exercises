#show temperature differences in Tampa between 1980-2000-2020

from matplotlib import pyplot as plt, dates
from datetime import datetime as dt
import csv
from pathlib import Path

path = Path("C:/Users/doman/Desktop/Crash_course_exercises/weather_data/3666826.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)


for title in header:
    print(f"{header.index(title)} {title}")


dates_1980 = []
temps_1980 = []
dates_2000 = []
temps_2000 = []
dates_2020 = []
temps_2020 = []
for line in reader:
    try:
        date = line[2]
        temp = line[8]
        if "1980" in date:
            temps_1980.append(int(temp))
            dates_1980.append(dt.strptime(date, "%Y-%m-%d"))
        elif "2000" in date:
            temps_2000.append(int(temp))
            dates_2000.append(dt.strptime(date, "%Y-%m-%d"))
        elif "2020" in date:
            temps_2020.append(int(temp))
            dates_2020.append(dt.strptime(date, "%Y-%m-%d"))
        else:
            continue
    except ValueError:
        print("skipping...")
        continue

plt.style.use("dark_background")

fig, ax = plt.subplots()

ax = plt.gca()
xaxis = dates.date2num(dates_1980)    # Convert to maplotlib format
hfmt = dates.DateFormatter('%m\n%d')
ax.xaxis.set_major_formatter(hfmt)

plt.xlabel('Date')
plt.ylabel('Value')

ax.plot(dates_1980, temps_1980, color="green")
ax.plot(dates_2000, temps_2000, color="yellow")
ax.plot(dates_2020, temps_2020, color="red")
#ax.get_xaxis().set_visible(False)
plt.tight_layout()
fig.autofmt_xdate()

plt.show()
