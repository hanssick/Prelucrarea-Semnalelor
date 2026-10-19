import numpy as np
import matplotlib.pyplot as plt

f = 5
fs = 1000
t = np.arange(0, 1, 1 / fs)

faze = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
etichete = ["0", "pi/2", "pi", "3pi/2"]

plt.figure(figsize=(9, 5))

for i in range(len(faze)):
    x = np.sin(2 * np.pi * f * t + faze[i])
    plt.plot(t, x, label="phi = " + etichete[i])

plt.title("Sinusoide de 5 Hz cu patru faze diferite")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("ex2_faze.pdf")

x = np.sin(2 * np.pi * f * t)

np.random.seed(0)
z = np.random.normal(0, 1, len(t))

valori_snr = [0.1, 1, 10, 100]
fig, axs = plt.subplots(4, figsize=(9, 11))
fig.suptitle("Sinusoida cu zgomot gaussian")

for i in range(len(valori_snr)):
    snr = valori_snr[i]
    gamma = np.linalg.norm(x) / (
        np.sqrt(snr) * np.linalg.norm(z)
    )
    y = x + gamma * z

    axs[i].plot(t, y, label="Cu zgomot", linewidth=0.8)
    axs[i].plot(t, x, label="Fara zgomot", linewidth=1.5)
    axs[i].set_title("SNR = " + str(snr))
    axs[i].set_xlabel("Timp (s)")
    axs[i].set_ylabel("Amplitudine")
    axs[i].grid(True)
    axs[i].legend(loc="upper right")

fig.tight_layout()
fig.savefig("ex2_zgomot.pdf")
plt.show()
