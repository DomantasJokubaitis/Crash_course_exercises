

# Attempt to show temperature differences in Tampa in years 1980, 2000 and 2020.

from matplotlib import pyplot as plt, dates
from datetime import datetime as dt
import csv
from pathlib import Path

path = Path("tampa_temperature_change/3666826.csv")

lines = path.read_text().splitlines()
reader = csv.reader(lines)

dates_str, temps_1980, temps_2000, temps_2020 = [], [], [], []

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

    except FileNotFoundError:
        print("File doesn't exist!")
        break


plt.style.use("dark_background")

fig, ax = plt.subplots()

ax = plt.gca()                       # Gets current axis
xaxis = dates.date2num(dates_str)    # Converts to maplotlib format
hfmt = dates.DateFormatter('%m\n%d') # Formats date line mm-dd
ax.xaxis.set_major_formatter(hfmt)   # Axis uses newly formatted dates

plt.xlabel('Date')
plt.ylabel('Temperature, F')

ax.plot(xaxis, temps_2020, color="red")
ax.plot(xaxis, temps_2000, color="yellow")
ax.plot(xaxis, temps_1980, color="green")

ax.set_aspect(1.3)
#fig.autofmt_xdate() if you want the dates to be slightly tilted for readability purposes

plt.show()




