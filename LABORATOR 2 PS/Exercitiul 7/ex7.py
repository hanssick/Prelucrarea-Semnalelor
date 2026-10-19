import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f = 50
t = np.arange(0, 0.1, 1 / fs)
x = np.sin(2 * np.pi * f * t)

fs_nou = fs / 4

t_a = t[::4]
x_a = x[::4]

t_b = t[1::4]
x_b = x[1::4]

fig, axs = plt.subplots(3, figsize=(9, 9))
fig.suptitle("Laboratorul 2 - Exercitiul 7: sinus de 50 Hz")

axs[0].stem(t, x)
axs[0].set_title("Semnal initial: fs = 1000 Hz")

axs[1].stem(t_a, x_a)
axs[1].set_title(f"(a) x[::4], fs = {fs_nou:g} Hz")

axs[2].stem(t_b, x_b)
axs[2].set_title(f"(b) x[1::4], fs = {fs_nou:g} Hz")

for ax in axs:
    ax.set_xlabel("Timp (s)")
    ax.set_ylabel("Amplitudine")
    ax.set_xlim(0, 0.1)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex7.pdf")
plt.show()
