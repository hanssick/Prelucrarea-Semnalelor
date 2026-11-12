from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
x = np.genfromtxt(folder / 'Train.csv', delimiter=',',
                  skip_header=1, usecols=2)

N = len(x)
Fs = 1 / 3600

X = np.fft.fft(x)
M = np.abs(X) / N
f = np.arange(N // 2) * Fs / N

plt.figure(figsize=(10, 4.5))
plt.plot(f, M[:N // 2], linewidth=0.8)
plt.title('Laboratorul 5 - Exercitiul 1 d): modulul transformatei Fourier')
plt.xlabel('Frecventa (Hz)')
plt.ylabel('|FFT(x)| / N')
plt.ylim(bottom=0)
plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(folder / 'lab5_ex1_d.pdf')
plt.show()
