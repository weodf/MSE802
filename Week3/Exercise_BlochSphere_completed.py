# Exercise: Understanding Qubit States

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from IPython.display import display
import matplotlib.pyplot as plt
import math


def show_state(title, circuit):
   
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    state = Statevector.from_instruction(circuit)

    print("Statevector:")
    print(state)

    print("\nCircuit text:")
    print(circuit.draw(output="text"))

    circuit_fig = circuit.draw(output="mpl")
    display(circuit_fig)
    plt.close(circuit_fig)

    bloch_fig = plot_bloch_multivector(state)
    display(bloch_fig)
    plt.close(bloch_fig)

    return state


# Part 1: Initialize a Qubit in the |0> State
qc_0 = QuantumCircuit(1)
state_0 = show_state("Part 1: Qubit initialized in |0> state", qc_0)

# Part 2: Change to |1> State using X gate
qc_1 = QuantumCircuit(1)
qc_1.x(0)
state_1 = show_state("Part 2: Apply X gate to create |1> state", qc_1)

# Part 3: Create a Superposition using Hadamard gate
qc_h = QuantumCircuit(1)
qc_h.h(0)
state_h = show_state("Part 3: Apply Hadamard gate to create superposition", qc_h)

assert abs(state_0.data[0] - 1) < 1e-9
assert abs(state_0.data[1] - 0) < 1e-9

assert abs(state_1.data[0] - 0) < 1e-9
assert abs(state_1.data[1] - 1) < 1e-9

expected = 1 / math.sqrt(2)
assert abs(state_h.data[0] - expected) < 1e-9
assert abs(state_h.data[1] - expected) < 1e-9

print("All tests passed.")
