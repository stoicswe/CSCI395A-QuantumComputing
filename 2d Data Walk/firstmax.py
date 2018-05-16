#!/usr/bin/env python
"""
Usage: python firstmax.py L

Simulate search on the LxL grid with a self-loop of weight 4/N at each vertex
using a discrete-time coined quantum walk with the Grover oracle.

Prints the first max in success probability and the time it occurs.

Written by Tom Wong, www.thomaswong.net.
Last modified: 2017-06-21 (YYYY-MM-DD).
"""

# Import modules.
from sys import argv
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Check the number of arguments.
assert(len(argv) == 2), "Missing command-line argument. Usage: python firstmax.py L"

# Get the arguments.
L = int(argv[1])

# Calculate the number of vertices.
N = L*L

# Calculate the weight of the self-loop.
l = 4/N

# Define the indices of the coin.
up = 0
down = 1
left = 2
right = 3
stay = 4

# Define the initial state. The first two indices are the (x,y)
# coordinate and the last is the coin.
psi = np.tile(np.array([
    1 / sqrt(N*(4+l)),
    1 / sqrt(N*(4+l)),
    1 / sqrt(N*(4+l)),
    1 / sqrt(N*(4+l)),
    sqrt(l) / sqrt(N*(4+l))
    ]),(L,L,1))

# Without loss of generality, let the marked vertex be floor(L/2,L/2).
wx = L // 2
wy = L // 2

# Keep track of the success probability and time.
last_prob = 0
t = 0

# Simulate the quantum walk.
while True:
    # Oracle query.
    psi[wx][wy] *= -1

    # Allocate temporary space for the state after the Grover coin is applied.
    tmp = np.empty((L,L,5))

    # Weighted Grover coin.
    for x in range(L):
        for y in range(L):
            # Calculate the funny "average."
            bar = (psi[x][y][up] + psi[x][y][down] + psi[x][y][left] + psi[x][y][right] + sqrt(l)*psi[x][y][stay]) / (4 + l)

            # Do the inversions.
            tmp[x][y][up] = 2*bar - psi[x][y][up]
            tmp[x][y][down] = 2*bar - psi[x][y][down]
            tmp[x][y][left] = 2*bar - psi[x][y][left]
            tmp[x][y][right] = 2*bar - psi[x][y][right]
            tmp[x][y][stay] = 2*bar*sqrt(l) - psi[x][y][stay]

    # Flip-flop shift.
    for x in range(L):
        for y in range(L):
            psi[x][y][up] = tmp[x][(y+1) % L][down]
            psi[x][y][down] = tmp[x][y-1][up]
            psi[x][y][left] = tmp[x-1][y][right]
            psi[x][y][right] = tmp[(x+1) % L][y][left]
            psi[x][y][stay] = tmp[x][y][stay]

    # See if we've found the peak.
    if last_prob > (psi[wx][wy]**2).sum():
        # We've found the peak. Stop simulating.
        break
    else:
        # Iterate the number of steps taken.
        t += 1

        # Save the current success probability for the next iteration.
        last_prob = (psi[wx][wy]**2).sum()

# Calculate and print the total probability.
print("%d\t%d\t%f\t%d" % (L, N, last_prob, t))
