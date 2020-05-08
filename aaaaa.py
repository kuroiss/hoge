import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
right_x = np.outer(np.cos(u), np.sin(v)) + 1
left_x = np.outer(np.cos(u), np.sin(v)) - 1
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

r = 0.5
theta = np.linspace(0, 2 * np.pi, 100)
stick_x = np.cos(theta) * r
stick_y = np.sin(theta) * r
stick_z = np.array([[0] * 100, [5] * 100])

ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([-6, 6])

ax.plot_surface(right_x, y, z, color = 'bisque')
ax.plot_surface(left_x, y, z, color = 'bisque')
ax.plot_surface(stick_x, stick_y, stick_z, color = 'bisque')

plt.show()

