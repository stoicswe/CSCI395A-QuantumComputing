import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

width = 1
dx = 0.1
X = np.arange(-width, width, dx)
Y = np.arange(-width, width, dx)
X, Y = np.meshgrid(X, Y)
Z = []
for i in range(len(X)):
    Z.append(np.zeros(len(X[i])))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z)

plt.show()