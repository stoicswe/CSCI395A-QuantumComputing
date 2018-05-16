import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from scipy import linalg as la

#import quantum computing fuctions
from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_state

qp = QuantumProgram()
qc = None
qubit = None
classic = Non

def initialize(qp_name, qubits, classicals){
    qubit = qp.create_quantum_register("qubit", qubits)
    classic = qp.create_classical_register("classic", classicals)
    qc = qp.create_circuit(qp_name, [qubit], [classic])
    print("Quantum Circuit ['" + qp_name + "'] generated: Qubits['" + qubits + "'] Classic Bits['" + classicals + "']")
}