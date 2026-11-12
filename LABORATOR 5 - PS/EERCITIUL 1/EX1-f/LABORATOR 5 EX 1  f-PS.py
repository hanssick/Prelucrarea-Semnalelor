from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
x = np.genfromtxt(folder / 'Train.csv', delimiter=',',
                  skip_header=1, usecols=2)
y = x - np.mean(x)
N = len(y)
Fs = 1 / 3600

M = np.abs(np.fft.fft(y))[:N // 2] / N
f = np.arange(N // 2) * Fs / N
indici = np.argsort(M[1:])[::-1][:4] + 1

print('  k       Modul        Frecventa (Hz)     Perioada (zile)')
for k in indici:
    print(f'{k:4d}  {M[k]:12.6f}  {f[k]:18.10e}  {1 / (f[k] * 86400):12.6f}')

plt.figure(figsize=(10, 5.4))
plt.bar(range(4), M[indici], color='C0', width=0.6)

etichete = [
    f'k = {k}\n{f[k]:.6e} Hz\nT (zile): {1 / (f[k] * 86400):g}'
    for k in indici
]
plt.xticks(range(4), etichete)

for j, k in enumerate(indici):
    plt.text(j, M[k] + 1, f'{M[k]:.4f}', ha='center')

plt.ylim(0, 1.15 * np.max(M[indici]))
plt.ylabel('Modul FFT / N')
plt.xlabel('Componente Fourier selectate')
plt.title('Laboratorul 5 - Exercitiul 1 f): cele mai mari patru module, fara DC')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(folder / 'lab5_ex1_f.pdf')
plt.show()