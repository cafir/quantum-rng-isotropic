import numpy as np
from qiskit import QuantumCircuit

#create circuit
def build_qrng(num_outcomes: int):
    # minimal bits to represent number outcomes
    k_bits = int(np.ceil(np.log2(num_outcomes)))

    total_qubits = max(k_bits, 2 * k_bits)
    qc = QuantumCircuit(total_qubits, total_qubits)
    qc.h(range(total_qubits))
    qc.measure(range(total_qubits), range(total_qubits))
    return qc, k_bits, total_qubits
