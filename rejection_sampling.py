import numpy as np

# rejection sampling
def unbiased_index_from_int(v: int, k: int, N: int):
    M = 1 << k # bias if 2^k
    t = (M // N) * N   # largest multiple of N <= M
    if v >= t:
        return None 
    return v % N

# rejection sampling for theta and phi
def angle_to_int(theta, phi, N):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    #deterministic hashing
    h = abs(
        int((x + 1) * 1e6) * 73856093 ^
        int((y + 1) * 1e6) * 19349663 ^
        int((z + 1) * 1e6) * 83492791
    )
    return h % N
