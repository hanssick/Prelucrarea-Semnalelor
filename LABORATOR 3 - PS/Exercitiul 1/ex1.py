# Laboratorul 3 - Exercitiul 1: matricea Fourier pentru N = 8.
# Formula folosita: F[k, n] = exp(-2*pi*j*k*n/N), fara normalizare.

import numpy as np  # Importam NumPy pentru matrice si calcule cu numere complexe.
import matplotlib.pyplot as plt  # Importam functiile pentru desenarea graficelor.

N = 8  # Matricea Fourier va avea 8 linii si 8 coloane.
F = np.zeros((N, N), dtype=complex)  # Cream o matrice 8 x 8 de zerouri complexe.

for k in range(N):  # Parcurgem liniile: k = 0, 1, ..., 7.
    for n in range(N):  # Pentru fiecare linie, parcurgem coloanele: n = 0, ..., 7.
        F[k, n] = np.exp(-2j * np.pi * k * n / N)  # Aplicam formula; 1j este unitatea imaginara.

print("Matricea Fourier F (rotunjita doar pentru afisare):")  # Anuntam ce afisam.
print(np.round(F, 3))  # Afisam F cu 3 zecimale; valorile folosite in calcule raman neschimbate.

F_H = F.conj().T  # Calculam F^H: conjugam elementele si apoi transpunem matricea.
produs = F_H @ F  # Calculam produsul de matrice F^H F; @ inseamna inmultire matriceala.
I = np.eye(N)  # Cream matricea identitate 8 x 8: 1 pe diagonala, 0 in rest.

verificare = np.allclose(produs, N * I)  # Verificam daca F^H F este aproximativ egal cu 8I.
eroare = np.linalg.norm(produs - N * I)  # Masuram abaterea prin norma Frobenius.
print("F^H @ F este aproximativ egal cu 8I:", verificare)  # Rezultatul trebuie sa fie True.
print("Norma diferentei F^H @ F - 8I:", eroare)  # Valoarea trebuie sa fie foarte aproape de 0.

U = F / np.sqrt(N)  # Impartim fiecare element la sqrt(8), obtinand matricea normalizata.
print("U^H @ U este aproximativ egal cu I:", np.allclose(U.conj().T @ U, I))  # U este unitara in sens strict.

n = np.arange(N)  # Cream indicii coloanelor: [0, 1, 2, 3, 4, 5, 6, 7].
fig, axe = plt.subplots(N, 2, figsize=(11, 17), sharex=True, sharey=True)  # Cream 8 randuri si 2 coloane de grafice.
fig.suptitle("Matricea Fourier pentru N = 8", fontsize=16)  # Adaugam titlul general.

for k in range(N):  # Desenam separat fiecare dintre cele 8 linii ale matricei.
    axe[k, 0].stem(n, F[k, :].real, linefmt="C0-", markerfmt="C0o", basefmt="k-")  # Reprezentam partea reala a liniei k.
    axe[k, 0].set_title(f"Linia k = {k} - partea reala")  # Titlul graficului din stanga.
    axe[k, 1].stem(n, F[k, :].imag, linefmt="C1-", markerfmt="C1o", basefmt="k-")  # Reprezentam partea imaginara a liniei k.
    axe[k, 1].set_title(f"Linia k = {k} - partea imaginara")  # Titlul graficului din dreapta.
    for ax in axe[k]:  # Configuram ambele grafice de pe randul curent.
        ax.set_xticks(n)  # Marcam pe axa orizontala indicii intregi de la 0 la 7.
        ax.set_ylim(-1.2, 1.2)  # Folosim aceeasi scara verticala pentru toate graficele.
        ax.set_ylabel("Valoare")  # Etichetam axa verticala.
        ax.grid(True, alpha=0.3)  # Adaugam o grila discreta, pentru citirea valorilor.

axe[-1, 0].set_xlabel("Indicele n")  # Etichetam axa orizontala a ultimei linii, in stanga.
axe[-1, 1].set_xlabel("Indicele n")  # Etichetam axa orizontala a ultimei linii, in dreapta.
fig.tight_layout(rect=[0, 0, 1, 0.97])  # Aranjam graficele si lasam loc pentru titlul general.
fig.savefig("ex1.pdf")  # Salvam toate cele 16 subplot-uri intr-un PDF vectorial.
plt.show()  # Afisam fereastra cu graficele.
