# Laboratorul 6 - Exercițiul 3

import numpy as np

N = 4
rng = np.random.default_rng(42)
p = rng.integers(-5, 6, size=N + 1)
q = rng.integers(-5, 6, size=N + 1)

L = 2 * N + 1
r_direct = np.zeros(L, dtype=int)
for i in range(N + 1):
    for j in range(N + 1):
        r_direct[i + j] += p[i] * q[j]

P = np.fft.fft(p, n=L)
Q = np.fft.fft(q, n=L)
r_fft = np.rint(np.fft.ifft(P * Q).real).astype(int)

print('p:', p)
print('q:', q)
print('Produs direct:', r_direct)
print('Produs prin FFT:', r_fft)
print('Rezultate identice:', np.array_equal(r_direct, r_fft))
