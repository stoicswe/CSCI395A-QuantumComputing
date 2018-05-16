import math
import pylab
import matplotlib.pyplot as plt, matplotlib as mpt 
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D as axes3d
from pylab import *

def p(complex_number):
    return complex_number*complex_number

def getProbs(posn):
    probs = [[0 for i in range(len(posn[j]))] for j in range(len(posn))]
    for i in range(len(posn)):
        for j in range(len(posn[i])):
            probs[i][j] = sum([p(a) for a in posn[i][j]])
    return probs

def timeStep(posn, newposn, a):
    for j in range(len(posn) - 1):
        for k in range(len(posn[j]) - 1):
            #for b in range(0,3):
                left, right = posn[j][k][0], posn[j][k][2]
                up, down = posn[j][k][1], posn[j][k][3]
                newposn[j+1][k][0] =- a*left+a*up+a*right+a*down
                newposn[j-1][k][1] = a*left-a*up+a*right+a*down
                newposn[j][k+1][2] = a*left+a*up-a*right+a*down
                newposn[j][k-1][3] = a*left+a*up+a*right-a*down
    return newposn

size = 25
posn = [[[0,0,0,0] for i in range(1,size)] for j in range(1,size)]
newposn = [[[0,0,0,0] for i in range(1,size)] for j in range(1,size)]

posn[int(size/2)][int(size/2)] = [0.5, 0.5j, 0.5, 0.5j]

for i in range(0,size):
    posn = timeStep(posn, newposn, 0.5)
generatedProbs = getProbs(posn)

#print(generatedProbs)

X = range(size - 1)
Y = range(size - 1)
X, Y = np.meshgrid(X, Y)
zx = len(generatedProbs)
zy = len(generatedProbs[0])
Z = [[0 for x in range(zx)] for y in range(zy)]
Z = generatedProbs

#print(X)
#print(Y)
#print(Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z)

plt.show()