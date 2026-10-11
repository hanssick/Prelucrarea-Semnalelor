import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.03, 0.0005)

x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

fig, axs = plt.subplots(3, figsize=(8, 7))
fig.suptitle("Semnale continue")

axs[0].plot(t, x)
axs[0].set_title("x(t)")
axs[1].plot(t, y)
axs[1].set_title("y(t)")
axs[2].plot(t, z)
axs[2].set_title("z(t)")

for ax in axs:
    ax.set_xlabel("Timp (s)")
    ax.set_ylabel("Amplitudine")
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex1_continuu.pdf")

fs = 200
ts = np.arange(0, 0.03, 1 / fs)

xn = np.cos(520 * np.pi * ts + np.pi / 3)
yn = np.cos(280 * np.pi * ts - np.pi / 3)
zn = np.cos(120 * np.pi * ts + np.pi / 3)

fig, axs = plt.subplots(3, figsize=(8, 7))
fig.suptitle("Semnale esantionate la 200 Hz")

axs[0].stem(ts, xn)
axs[0].set_title("x[n]")
axs[1].stem(ts, yn)
axs[1].set_title("y[n]")
axs[2].stem(ts, zn)
axs[2].set_title("z[n]")

for ax in axs:
    ax.set_xlabel("Timp (s)")
    ax.set_ylabel("Amplitudine")
    ax.grid(True)

fig.tight_layout()
fig.savefig("ex1_esantionat.pdf")

plt.show()
