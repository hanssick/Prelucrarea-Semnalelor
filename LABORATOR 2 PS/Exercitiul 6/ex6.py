import numpy as np
import matplotlib.pyplot as plt

fs = 1000
A = 1
phi = 0
n = np.arange(20)
t = n / fs

x1 = A * np.sin(2 * np.pi * (fs / 2) * t + phi)
x2 = A * np.sin(2 * np.pi * (fs / 4) * t + phi)
x3 = A * np.sin(2 * np.pi * 0 * t + phi)

fig, axs = plt.subplots(3, figsize=(8, 8))
fig.suptitle("Laboratorul 2 - Exercitiul 6: fs = 1000 Hz")

axs[0].stem(n, x1)
axs[0].set_title("(a) f = fs/2 = 500 Hz")

axs[1].stem(n, x2)
axs[1].set_title("(b) f = fs/4 = 250 Hz")

axs[2].stem(n, x3)
axs[2].set_title("(c) f = 0 Hz")

for ax in axs:
    ax.set_xlabel("Indicele esantionului n")
    ax.set_ylabel("x[n]")
    ax.set_xticks(np.arange(0, 20, 2))
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex6.pdf")
plt.show()
