import numpy as np
import matplotlib.pyplot as plt

fs = 8000

# a)
n = np.arange(1600)
t_a = n / fs
x_a = np.sin(2 * np.pi * 400 * t_a)

plt.figure(figsize=(9, 4))
plt.plot(t_a, x_a)
plt.title("2(a): Sinusoida de 400 Hz, 1600 de esantioane")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.tight_layout()
plt.savefig("ex2_a.pdf")

# b)
t_b = np.arange(3 * fs) / fs
x_b = np.sin(2 * np.pi * 800 * t_b)

plt.figure(figsize=(9, 4))
plt.plot(t_b, x_b)
plt.xlim(0, 0.01)
plt.title("2(b): Sinusoida de 800 Hz, durata 3 s\nDetaliu: primele 0.01 s")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.tight_layout()
plt.savefig("ex2_b.pdf")

# c)
t_c = np.arange(0, 0.02, 1 / fs)
x_c = 2 * np.mod(240 * t_c, 1) - 1

plt.figure(figsize=(9, 4))
plt.plot(t_c, x_c)
plt.title("2(c): Semnal sawtooth de 240 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.tight_layout()
plt.savefig("ex2_c.pdf")

# d)
t_d = np.arange(0, 0.02, 1 / fs)
x_d = np.sign(np.sin(2 * np.pi * 300 * t_d))
x_d[x_d == 0] = 1

plt.figure(figsize=(9, 4))
plt.step(t_d, x_d, where="post")
plt.title("2(d): Semnal square de 300 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.ylim(-1.2, 1.2)
plt.grid(True)
plt.tight_layout()
plt.savefig("ex2_d.pdf")

# e)
imagine_e = np.random.rand(128, 128)

plt.figure(figsize=(5, 5))
plt.imshow(imagine_e, cmap="gray", vmin=0, vmax=1)
plt.title("2(e): Semnal 2D aleator, 128 x 128")
plt.xlabel("Coloana")
plt.ylabel("Linia")
plt.tight_layout()
plt.savefig("ex2_e.pdf")

# f)
imagine_f = np.zeros((128, 128))
imagine_f[32:96, 32:96] = 1

plt.figure(figsize=(5, 5))
plt.imshow(imagine_f, cmap="gray", vmin=0, vmax=1)
plt.title("2(f): Patrat alb pe fundal negru, 128 x 128")
plt.xlabel("Coloana")
plt.ylabel("Linia")
plt.tight_layout()
plt.savefig("ex2_f.pdf")

plt.show()
