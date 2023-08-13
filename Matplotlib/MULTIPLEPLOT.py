import matplotlib.pyplot as plt
import numpy as np

# x1, y1 = np.random.random(100), np.random.random(100)
# x2, y2 = np.random.random(100), np.random.random(100)

# plt.figure(1)
# plt.scatter(x1,y1)

# plt.figure(2)
# plt.plot(x2,y2)

# plt.show()

x = np.arange(100)
fig, axs = plt.subplots(2, 2)

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title('Sine Wave')

axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title('Cos Wave')

axs[1,0].plot(x, np.random.random(100))
axs[1,0].set_title('Random Function')

axs[1,1].plot(x, np.log(x))
axs[1,1].set_title('Log Function')
axs[1,1].set_xlabel('TEST')

fig.suptitle('Four Graph')
plt.tight_layout()
# plt.show()

plt.savefig('fourplot.png', dpi=300)