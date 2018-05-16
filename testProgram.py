from qiskit import QuantumProgram

Q_Program = QuantumProgram()

#initialize the registers
qr = Q_Program.create_quantum_register("qr", 1)
cr = Q_Program.create_classical_register("cr", 1)
qc = Q_Program.create_circuit("test", [qr], [cr])

qc.h(qr[0])
coin = qc.measure(qr[0], cr[0])

print(coin)

result = Q_Program.execute(["test"], backend='local_qasm_simulator', shots=1024)

print(result)
print(result.get_data("quantumWalk"))