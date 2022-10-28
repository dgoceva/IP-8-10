import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
points = ax.plot(x, y)
ax.set_xlabel('X', loc='right')
ax.set_ylabel('Y', loc='top')
ax.set_title('SIN(X)')
ax.set_facecolor('yellow')
plt.setp(points, color='green', linestyle='dashdot', linewidth=3)
plt.show()
