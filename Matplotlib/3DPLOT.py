import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)

# ax.scatter(x,y,z)
# ax.set_title('3D')

# plt.show()

# x = np.arange(0, 50, 0.1)
# y = np.sin(x)
# z = np.cos(x)

# ax.plot(x,y,z)
# ax.set_title('3D')
# plt.show()

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x,y)
Z = np.sin(X) * np.sin(Y)

ax.plot_surface(X,Y,Z, cmap='Spectral')
ax.view_init(azim=0,elev=90)

plt.show()