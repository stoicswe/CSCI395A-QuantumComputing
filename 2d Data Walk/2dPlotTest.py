import math
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *

fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(5, 5, 8, rstride=4, cstride=4, linewidth=0)
pylab.plot(p)