import numpy as np

#converter bit 2 float
def bits_to_float(bits: str) -> float:
    if len(bits) == 0:
        return 0.0
    val = int(bits, 2)
    return val / (2 ** len(bits))

#generate 2 paramater of theta and phi
def sample_theta_phi_from_bits(b1: str, b2: str):
    u1 = bits_to_float(b1)  
    u2 = bits_to_float(b2)
    theta = np.arccos(1 - 2*u1)  # cdf sampling
    phi = 2 * np.pi * u2  
    return theta, phi, u1, u2
