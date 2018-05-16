import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from scipy import linalg as la

#import quantum computing fuctions
from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_state

quantum = QuantumProgram()
qubit = quantum.create_quantum_register("qubit", 7)
classic = quantum.create_classical_register("classic", 7)
qCircuit = quantum.create_circuit("linear_solver", [qubit], [classic])

qCircuit.h(qubit[0])
qCircuit.x(qubit[2])
qCircuit.cx(qubit[0], qubit[4])
qCircuit.measure(qubit[4], classic[4])
qCircuit.reset(qubit[4])

if (classic[4] == 0):
    qCircuit.cx(qubit[1], qubit[2])
    qCircuit.cx(qubit[2], qubit[1])
    qCircuit.cx(qubit[1], qubit[2])

qCircuit.cx(qubit[1], qubit[5])
qCircuit.cx(qubit[2], qubit[6])
qCircuit.measure(qubit[5], classic[5])
qCircuit.measure(qubit[6], classic[6])

if (classic[6] == 1):
    qCircuit.u3(pi/3,0,0, qubit[3])

if (classic[5] == 1):
    qCircuit.u3(pi,0,0, qubit[3])

if (classic[4] == 0):
    qCircuit.cx(qubit[1], qubit[2])
    qCircuit.cx(qubit[2], qubit[1])
    qCircuit.cx(qubit[1], qubit[2])

qCircuit.h(qubit[0])
qCircuit.measure(qubit[3], classic[3])
result = quantum.execute(["linear_solver"], backend='local_qasm_simulator', shots=8192)

plot_histogram(result.get_counts('linear_solver'))