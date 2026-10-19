import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1 / fs)

x = np.sin(2 * np.pi * 5 * t)
y = 2 * np.mod(3 * t, 1) - 1
z = x + y

fig, axs = plt.subplots(3, figsize=(8, 8))
fig.suptitle("Laboratorul 2 - Exercitiul 4")

axs[0].plot(t, x)
axs[0].set_title("Semnal sinusoidal de 5 Hz")

axs[1].plot(t, y)
axs[1].set_title("Semnal sawtooth de 3 Hz")

axs[2].plot(t, z)
axs[2].set_title("Suma celor doua semnale")

for ax in axs:
    ax.set_xlabel("Timp (s)")
    ax.set_ylabel("Amplitudine")
    ax.set_xlim(0, 1)
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex4.pdf")
plt.show()
