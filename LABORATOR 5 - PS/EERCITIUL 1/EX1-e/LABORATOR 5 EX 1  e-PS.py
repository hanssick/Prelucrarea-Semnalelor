from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
x = np.genfromtxt(folder / 'Train.csv', delimiter=',',
                  skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600

media = np.mean(x)
y = x - media

X = np.fft.fft(x)
Y = np.fft.fft(y)
f = np.arange(N // 2) * Fs / N

print('Media initiala:', media)
print('Media dupa centrare:', np.mean(y))

fig, axe = plt.subplots(2, 1, figsize=(10, 7),
                        sharex=True, sharey=True)

axe[0].plot(f, np.abs(X[:N // 2]) / N, linewidth=0.8)
axe[1].plot(f, np.abs(Y[:N // 2]) / N,
            color='C1', linewidth=0.8)

axe[0].scatter(0, np.abs(X[0]) / N, color='C0', zorder=3)
axe[1].scatter(0, np.abs(Y[0]) / N, color='C1', zorder=3)

axe[0].set_title('Inainte de eliminarea componentei continue')
axe[1].set_title('Dupa eliminarea componentei continue')

for ax in axe:
    ax.set_ylabel('Modul FFT / N')
    ax.set_ylim(bottom=0)
    ax.set_xlim(-Fs / N, 20 * Fs / N)
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))

axe[1].set_xlabel('Frecventa (Hz)')
fig.suptitle('Laboratorul 5 - Exercitiul 1 e): detaliu in jurul frecventei zero')
fig.tight_layout()
fig.savefig(folder / 'lab5_ex1_e.pdf')
plt.show()
