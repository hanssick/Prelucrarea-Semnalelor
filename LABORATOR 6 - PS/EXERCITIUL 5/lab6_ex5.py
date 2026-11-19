# Laboratorul 6 - Exercițiul 5: Ferestre de semnal

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def dreptunghiulara(N):
    return np.ones(N)


def hanning(N):
    n = np.arange(N)
    return 0.5 * (1 - np.cos(2 * np.pi * n / N))


f, A, phi = 100, 1, 0
Nw, Fs = 200, 4000
t = np.arange(Nw) / Fs
x = A * np.sin(2 * np.pi * f * t + phi)
x_d = x * dreptunghiulara(Nw)
x_h = x * hanning(Nw)

fig, axe = plt.subplots(2, 1, figsize=(9, 5.4), sharex=True,
                        sharey=True, layout='constrained')
axe[0].plot(1000 * t, x_d, color='#2463a0')
axe[0].set_title('Fereastră dreptunghiulară')
axe[1].plot(1000 * t, x_h, color='#b95022')
axe[1].set_title('Fereastră Hanning')

for ax in axe:
    ax.set_ylabel('Amplitudine')
    ax.set_ylim(-1.1, 1.1)
    ax.grid(alpha=0.25)

axe[1].set_xlabel('Timp [ms]')
fig.suptitle('Sinusoidă de 100 Hz | Ferestre de 200 de eșantioane')
fig.savefig(Path(__file__).resolve().with_suffix('.png'), dpi=160)
plt.show()
