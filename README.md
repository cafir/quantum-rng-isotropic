# Quantum Random Number Generator with Isotropic Model

This repository provides a **Quantum Random Number Generator (QRNG)** implemented using Qiskit, with support for **isotropic sampling**. The QRNG generates truly random numbers by exploiting quantum superposition, and can optionally map isotropic spherical coordinates to discrete integers.

---

## Features

- **Quantum-based randomness** using Qiskit's Aer simulator or real quantum backends.
- **Direct mode**: Uniform random integers without isotropic mapping.
- **Isotropic mode**: Uses spherical coordinates (θ, φ) for sampling on the unit sphere.
- **Unique mode**: Optionally generate non-repeating random numbers.
- **Rejection sampling**: Ensures uniform distribution without modulo bias.
- **Flexible shots**: Generate single or multiple random numbers.

---

## Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install qiskit numpy
pip install qiskit_aer
