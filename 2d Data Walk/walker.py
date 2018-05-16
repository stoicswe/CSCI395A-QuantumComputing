"""
Requires matplotlib for plotting. Tested with python 27. If you want to try this
without plotting, remove the final two lines and the pylab import. The guts only
depends on math and will work with vanilla python.
"""
import math
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *


def probabilities(posn): #calculate probabilities
    """Returns a list of the probabilies for each place."""
    return [sum([abs(amp) ** 2 for amp in place]) for place in posn]


def normalise(posn): #normalize the data
    """Normalise function to normalise an input 1D line."""
    N = math.sqrt(sum(probabilities(posn)))
    return [[amp / N for amp in place] for place in posn]


def timestep(posn): #flip the coin
	"""Defines action of a timestep, i.e. a Hadamard gate on each element."""
	return normalise([[x[0]*1j + x[1], x[0] + x[1]*1j, x[0]*1j - x[1], x[0] - x[1]*1j] for x in posn])


#return normalise([[x[0] + x[1], x[0] - x[1]] for x in posn])


def shift(coin):
    """Shift the up elements leftwards and the down elements rightwards."""
    newposn = [[0, 0, 0, 0] for i in range(len(coin))]
    for j in range(1, len(posn) - 1):
        newposn[j + 1][0] += coin[j][0] #up
        newposn[j - 1][1] += coin[j][1] #down
        #------------------------------
        newposn[j + 1][2] += coin[j][2] #left
        newposn[j - 1][3] += coin[j][3] #right
        #------------------------------
        #print(newposn)
    return normalise(newposn)


# Initialise lists.
min, max = -500, 501
posn = [[0, 0, 0, 0] for i in range(min, max)]
#posn[-min] = [1 / math.sqrt(2), 1j / math.sqrt(2)]
posn[-min] = [1 / math.sqrt(2), 1 / math.sqrt(2), -1 / math.sqrt(2), -1 / math.sqrt(2)]

# Run for some steps...
for time in range(-min):
    posn = shift(timestep(posn))

# Plot.
#pylab.plot(range(min, max), probabilities(posn))
#pylab.show()
#fig = plt.figure()
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes.set_xlabel('time')
#axes.set_ylabel('direction')
#axes.set_title('2D Walk')
#axes.plot(range(min,max), probabilities(posn), 'r')
#axes.show()
fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(min, max, probabilities(posn), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)