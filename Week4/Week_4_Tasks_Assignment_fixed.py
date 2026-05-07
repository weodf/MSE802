# Qiskit Assignment - Fixed display version

from math import pi

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere, plot_histogram
from qiskit_aer import AerSimulator
from IPython.display import display

import matplotlib.pyplot as plt


# Task 1
print("=" * 60)
print("Task 1: 2-qubit circuit with 90 degree phase shift")
print("=" * 60)

qc_phase = QuantumCircuit(2)
qc_phase.h(0)
qc_phase.p(pi / 2, 0)

print("Circuit text:")
print(qc_phase.draw(output="text"))

phase_circuit_fig = qc_phase.draw(output="mpl")
display(phase_circuit_fig)
plt.close(phase_circuit_fig)

state_phase = Statevector.from_instruction(qc_phase)

print("Statevector:")
print(state_phase)

qsphere_fig = plot_state_qsphere(state_phase)
display(qsphere_fig)
plt.close(qsphere_fig)


# Task 2
print("\n" + "=" * 60)
print("Task 2: QASM circuit imported and run in Qiskit")
print("=" * 60)

qasm_code = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
"""

qc_qasm = QuantumCircuit.from_qasm_str(qasm_code)

print("Imported QASM circuit:")
print(qc_qasm.draw(output="text"))

qasm_circuit_fig = qc_qasm.draw(output="mpl")
display(qasm_circuit_fig)
plt.close(qasm_circuit_fig)

simulator = AerSimulator()
job = simulator.run(qc_qasm, shots=1024)
result = job.result()
counts = result.get_counts()

print("Measurement result:")
print(counts)

hist_fig = plot_histogram(counts)
display(hist_fig)
plt.close(hist_fig)


# Task 3
print("\n" + "=" * 60)
print("Task 3: Random circuit drawing without dump method")
print("=" * 60)

qc_random = QuantumCircuit(3, 3)

qc_random.h(0)
qc_random.x(1)
qc_random.cx(0, 2)
qc_random.s(2)
qc_random.t(1)
qc_random.z(0)
qc_random.measure([0, 1, 2], [0, 1, 2])

print("Random circuit text:")
print(qc_random.draw(output="text"))

random_circuit_fig = qc_random.draw(output="mpl")
display(random_circuit_fig)
plt.close(random_circuit_fig)


# Simple checks
assert qc_phase.num_qubits == 2
assert qc_qasm.num_qubits == 2
assert qc_random.num_qubits == 3

print("\nAll tasks completed successfully.")
