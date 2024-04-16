import matplotlib.pyplot as plt


input_numbers = range(1, 5001)
squares = [x**3 for x in input_numbers]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(input_numbers, squares, c = squares, cmap = plt.cm.Reds, s=5)

ax.set_title("Squares of the first 10 numbers", fontsize = 26)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)
ax.tick_params(labelsize = 14)
ax.ticklabel_format(style = "plain")

ax.axis([1, 5000, 1, 125_000_000_000])
plt.show()