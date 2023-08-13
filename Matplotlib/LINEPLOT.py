import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weight = [80,83,83,85,86,82,81,79,83,80,82,82,83,81,80,79]

plt.plot(years, weight, c='r', lw=3, linestyle='--')
plt.show()