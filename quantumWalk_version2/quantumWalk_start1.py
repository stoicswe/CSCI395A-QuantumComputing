#Nathan Bunch - Quantum Walk, 10-10-2017

#import functions from python
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from scipy import linalg as la

#import quantum computing fuctions
from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_state

################## ABOUT THE PROGRAM ################
# In this program we compute a quantum walk.
#
# Interesting things to note:
#
# The reason we have 9 qubits and 5 classical bits is
# becuase in order to correctly measure the states
# of the qubits, we need to copy the values of the
# quantum walk bits to alternate bits that will be
# measured. The reason for this is because when we
# measure the bit state, the qubit state decomposes
# to |0>.
#
# The reason we only have 5 classical bit states is
# becuase there is one for the coin that is flipped
# and four for the qubits involed in the walk.

Q_Program = QuantumProgram()

#initialize the registers
qr = Q_Program.create_quantum_register("qr", 9)
cr = Q_Program.create_classical_register("cr", 5)
qc = Q_Program.create_circuit("quantumWalk", [qr], [cr])

#begin the quantum walk
for x in range (0, 5):
    
    #flip the coin
    qc.x(qr[0])
    qc.h(qr[0])
    qc.measure(qr[0], cr[0])

    #if coin value is 1, step forward in the walk:
    qc.ccx(qr[0], qr[3], qr[4]).c_if(cr, 1)
    qc.ccx(qr[0], qr[2], qr[1]).c_if(cr, 1)

    qc.ccx(qr[0], qr[1], qr[2]).c_if(cr, 1)
    qc.cx(qr[0], qr[1]).c_if(cr, 1)
    qc.x(qr[0]).c_if(cr, 1)

    #copy the values from the quantum walk qubits 
    #to the measurable qubits, to prevent walk interference
    qc.cx(qr[1], qr[5])
    qc.cx(qr[2], qr[6])
    qc.cx(qr[3], qr[7])
    qc.cx(qr[4], qr[8])

    #measure the values
    qc.measure(qr[5], cr[1])
    qc.measure(qr[6], cr[2])
    qc.measure(qr[7], cr[3])
    qc.measure(qr[8], cr[4])

#run the complete circuit and gather the result
result = Q_Program.execute(["quantumWalk"], backend='local_qasm_simulator', shots=1024)

#return the result to console: bits and bit states that were counted
print(result)
print(result.get_data("quantumWalk"))

#plot the counts, determine probability of each state
plot_histogram(result.get_counts('quantumWalk'))