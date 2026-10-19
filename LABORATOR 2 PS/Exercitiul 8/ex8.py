import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1001)

sinus = np.sin(alpha)
taylor = alpha
pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)

eroare_taylor = np.abs(sinus - taylor)
eroare_pade = np.abs(sinus - pade)

plt.figure(figsize=(9, 5))
plt.plot(alpha, sinus, color="black", label="sin(alpha)")
plt.plot(alpha, taylor, "--", color="C1", label="Taylor: alpha")
plt.plot(alpha, pade, ":", color="C0", label="Pade", linewidth=2)
plt.title("Compararea aproximarilor pe [-pi/2, pi/2]")
plt.xlabel("alpha (rad)")
plt.ylabel("Valoare")
plt.xlim(-np.pi / 2, np.pi / 2)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("ex8_functii.pdf")

plt.figure(figsize=(9, 5))
plt.plot(alpha, eroare_taylor, color="C1", label="Eroare Taylor")
plt.plot(alpha, eroare_pade, color="C0", label="Eroare Pade")
plt.title("Erorile absolute - scara liniara")
plt.xlabel("alpha (rad)")
plt.ylabel("Eroare absoluta")
plt.xlim(-np.pi / 2, np.pi / 2)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("ex8_erori.pdf")

# Valorile zero sunt omise doar din graficul logaritmic.
eroare_taylor_log = np.where(eroare_taylor > 0, eroare_taylor, np.nan)
eroare_pade_log = np.where(eroare_pade > 0, eroare_pade, np.nan)

plt.figure(figsize=(9, 5))
plt.semilogy(alpha, eroare_taylor_log, color="C1", label="Eroare Taylor")
plt.semilogy(alpha, eroare_pade_log, color="C0", label="Eroare Pade")
plt.title("Erorile absolute - scara logaritmica")
plt.xlabel("alpha (rad)")
plt.ylabel("Eroare absoluta")
plt.xlim(-np.pi / 2, np.pi / 2)
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("ex8_erori_log.pdf")

plt.show()
