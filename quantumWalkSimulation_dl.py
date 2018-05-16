#the following source code was downloaded from:
#http://susan-stepney.blogspot.com/2014/02/mathjax.html
#somewhat useful?
#http://etheses.whiterose.ac.uk/4975/1/kbarrfinalthesis.pdf

from numpy import *
from matplotlib.pyplot import *

N = 100      # number of random steps
P = 2*N+1    # number of positions

#coin 0, and coin 1
coin0 = array([1, 0])  # |0>
coin1 = array([0, 1])  # |1>

#We will see terms like |0⟩c⟨0| in what follows.  
#This is the outer product of the relevant vectors, resulting in a matrix.  
#We can use NumPy to calculate these:
C00 = outer(coin0, coin0)  # |0><0| 
C01 = outer(coin0, coin1)  # |0><1| 
C10 = outer(coin1, coin0)  # |1><0| 
C11 = outer(coin1, coin1)  # |1><1| 

#perform Hadamard on coin:
C_hat = (C00 + C01 + C10 - C11)/sqrt(2.)

#take a step
ShiftPlus = roll(eye(P), 1, axis=0)
ShiftMinus = roll(eye(P), -1, axis=0)
S_hat = kron(ShiftPlus, C00) + kron(ShiftMinus, C11)

#the walk operator?
U = S_hat.dot(kron(eye(P), C_hat))

#initial state?
posn0 = zeros(P)
posn0[N] = 1     # array indexing starts from 0, so index N is the central posn
psi0 = kron(posn0,(coin0+coin1*1j)/sqrt(2.))

#state after N steps
psiN = linalg.matrix_power(U, N).dot(psi0)

#measure
prob = empty(P)
for k in range(P):
    posn = zeros(P)
    posn[k] = 1     
    M_hat_k = kron( outer(posn,posn), eye(2))
    proj = M_hat_k.dot(psiN)
    prob[k] = proj.dot(proj.conjugate()).real

#lets plot the result
fig = figure()
ax = fig.add_subplot(111)

plot(arange(P), prob)
plot(arange(P), prob, 'o')
loc = range (0, P, P // 10) #Location of ticks
xticks(loc)
xlim(0, P)
ax.set_xticklabels(range (-N, N+1, P // 10))

show()