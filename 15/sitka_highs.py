from pathlib import Path
import csv
from matplotlib import pyplot as plt

path = Path("C:/Users/doman/Desktop/Crash_course_exercises/weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, title in enumerate(header_row):
    print(index, title)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

number = 0

for item in highs:
    number += 1

t_av_max = []

while number > 0:
    t_av_max.append(59)
    number -= 1

print(highs)

plt.style.use("fast")
fig, ax = plt.subplots()
ax.plot(highs, color = "red")
ax.plot(t_av_max, color = "blue")

plt.show()