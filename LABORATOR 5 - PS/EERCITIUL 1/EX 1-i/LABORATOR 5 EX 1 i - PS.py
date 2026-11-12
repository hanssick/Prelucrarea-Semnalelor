from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
x = np.genfromtxt(folder / 'Train.csv', delimiter=',',
                  skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600

X = np.fft.fft(x)
f = np.fft.fftfreq(N) * Fs
fc = 1 / (12 * 3600)

X[np.abs(f) > fc] = 0
x_filtrat = np.fft.ifft(X).real

start = 5256
nr_ore = 30 * 24
zile = np.arange(nr_ore) / 24

plt.figure(figsize=(11, 5))
plt.plot(zile, x[start:start + nr_ore],
         color='C0', alpha=0.55, label='Trafic initial')
plt.plot(zile, x_filtrat[start:start + nr_ore],
         color='C1', linewidth=2, label='Trafic filtrat')

plt.xticks([0, 7, 14, 21, 28],
           ['01.04', '08.04', '15.04', '22.04', '29.04'])
plt.xlim(0, 30)
plt.xlabel('Data (2013) - aprilie')
plt.ylabel('Numar de masini / valoare filtrata')
plt.title('Laboratorul 5 - Exercitiul 1 i): filtrare trece-jos, prag de 12 ore')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(folder / 'lab5_ex1_i.pdf')
plt.show()