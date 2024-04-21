#show temperature differences in Tampa between 1980-2000-2020

from matplotlib import pyplot as plt, dates
from datetime import datetime as dt
import csv
from pathlib import Path

path = Path("tampa_temperature_change/3666826.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)


#for title in header:
    #print(f"{header.index(title)} {title}")



dates_str = []
temps_1980 = []
temps_2000 = []
temps_2020 = []

for line in reader:
    try:
        date = line[2]
        temp = line[8]

        if "2020" in date:
            temps_2020.append(int(temp))
            dates_str.append(date)

        elif "1980" in date:
            temps_1980.append(int(temp))

        elif "2000" in date:
            temps_2000.append(int(temp))

        else:
            continue

    except ValueError:
        print("skipping...")
        continue


plt.style.use("dark_background")

fig, ax = plt.subplots()

ax = plt.gca()
xaxis = dates.date2num(dates_str)    # Convert to maplotlib format
hfmt = dates.DateFormatter('%m\n%d')
ax.xaxis.set_major_formatter(hfmt)

print(xaxis)

plt.xlabel('Date')
plt.ylabel('Temperature, F')

ax.plot(xaxis, temps_2020, color="red")
ax.plot(xaxis, temps_2000, color="yellow")
ax.plot(xaxis, temps_1980, color="green")
plt.tight_layout()
fig.autofmt_xdate()

plt.show()




