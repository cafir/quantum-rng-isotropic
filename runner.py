import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from circuit import build_qrng
from rejection_sampling import angle_to_int, unbiased_index_from_int
from converter import sample_theta_phi_from_bits


def run_qrng(num_outcomes: int, shots: int = 1, isotropic: bool = False, unique: bool = False):
    qc, k_bits, total_qubits = build_qrng(num_outcomes)
    sim = AerSimulator()

    if not isotropic:
        k = k_bits
        results = []
        while len(results) < shots:
            res = sim.run(qc, shots=1).result()
            b = list(res.get_counts().keys())[0][:k]  # take top k bits
            v = int(b, 2)
            idx = unbiased_index_from_int(v, k, num_outcomes)
            if idx is None:
                continue
            results.append(idx)
        if shots == 1:
            return results[0]
        return results

    else:
        # base on Monte Carlo, resolution 2^-16
        r = 16
        results = []
        seen = set()
        while len(results) < shots:
            res = sim.run(qc, shots=1).result()
            b_full = list(res.get_counts().keys())[0]
            # adding 0 for so it form 32 bits
            if len(b_full) < 2*r:
                b_full = b_full.ljust(2*r, '0')
            b1 = b_full[:r]
            b2 = b_full[r:2*r]
            theta, phi, u1, u2 = sample_theta_phi_from_bits(b1, b2)
            # use theta and phi to produce angle that being convert for rejection sampling
            idx = angle_to_int(theta, phi, num_outcomes)
            if idx is None:
                continue
            if unique:
                if idx in seen:
                    continue
                seen.add(idx)
            results.append(idx)
        if shots == 1:
            return results[0]
        return results
