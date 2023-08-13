import matplotlib.pyplot as plt

x = ['C++', 'C#', 'Java', 'Python', 'Go']
y = [20, 50, 1, 140, 45]

plt.bar(x, y, color='b', align='edge', width=0.5, edgecolor='green', lw=6)
plt.show()