import plotly.express as px

from rolling_dice import Die

die_1 = Die(8)
die_2 = Die(8)

results = []

for number in range(100000000):
    result = die_1.roll_dice() + die_2.roll_dice()
    results.append(result)

frequencies = []
max_result = die_1.sides + die_2.sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling two dice"
labels = {"x": "result", "y": "frequency of result"}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels=labels)
fig.show()