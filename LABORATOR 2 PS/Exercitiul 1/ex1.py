import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
phi = np.pi / 6
fs = 1000

t = np.arange(0, 1, 1 / fs)

x = A * np.sin(2 * np.pi * f * t + phi)
y = A * np.cos(2 * np.pi * f * t + phi - np.pi / 2)

fig, axs = plt.subplots(2, figsize=(8, 6))
fig.suptitle("Laboratorul 2 - Exercitiul 1")

axs[0].plot(t, x)
axs[0].set_title("Semnal sinus")

axs[1].plot(t, y)
axs[1].set_title("Semnal cosinus")

for ax in axs:
    ax.set_xlabel("Timp (s)")
    ax.set_ylabel("Amplitudine")
    ax.set_xlim(0, 1)
    ax.set_ylim(-2.2, 2.2)
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex1.pdf")
plt.show()
