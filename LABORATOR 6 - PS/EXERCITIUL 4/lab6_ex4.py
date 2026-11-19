# Laboratorul 6 - Exercițiul 4: Deplasarea circulară

import numpy as np

N = 20
d = 7
n = np.arange(N)
rng = np.random.default_rng(42)

x = np.sin(2 * np.pi * 3 * n / N) + 0.3 * rng.standard_normal(N)
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

corelatie = np.fft.ifft(np.conj(X) * Y).real
print("Deplasarea aleasă:", d)
print("Deplasarea prin corelație:", np.argmax(corelatie))

if np.min(np.abs(X)) <= 1e-12 * np.max(np.abs(X)):
    raise ValueError("Împărțirea nu este sigură: FFT(x) are valori aproape de zero.")

impuls = np.fft.ifft(Y / X).real
print("Deplasarea prin împărțire:", np.argmax(impuls))
