import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth = 2)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_aspect("equal")
plt.show()