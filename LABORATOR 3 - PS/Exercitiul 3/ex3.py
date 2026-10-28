# Laboratorul 3 - Exercitiul 3: transformata Fourier a unui semnal compus.
# Calculam direct suma DFT si apoi folosim matricea Fourier; nu apelam functii FFT.

import numpy as np  # Importam NumPy pentru vectori, matrice si calcule complexe.
import matplotlib.pyplot as plt  # Importam functiile pentru reprezentarea grafica.

fs = 1000  # Alegem frecventa de esantionare: 1000 Hz.
N = 1000  # Luam 1000 de esantioane, corespunzatoare unei durate N/fs = 1 secunda.
n = np.arange(N)  # Construim indicii esantioanelor: 0, 1, ..., 999.
t = n / fs  # Transformam indicii in momente de timp, exprimate in secunde.

f1 = 7  # Alegem frecventa primei componente: 7 Hz.
f2 = 23  # Alegem frecventa celei de-a doua componente: 23 Hz.
f3 = 61  # Alegem frecventa celei de-a treia componente: 61 Hz.
x1 = np.cos(2 * np.pi * f1 * t)  # Generam prima componenta, de amplitudine 1.
x2 = 2 * np.cos(2 * np.pi * f2 * t)  # Generam a doua componenta, de amplitudine 2.
x3 = 0.5 * np.cos(2 * np.pi * f3 * t)  # Generam a treia componenta, de amplitudine 0.5.
x = x1 + x2 + x3  # Adunam componentele pentru a obtine semnalul compus.

X_bucle = np.zeros(N, dtype=complex)  # Pregatim cei N coeficienti Fourier, initial egali cu zero.

for k in range(N):  # Alegem pe rand fiecare indice de frecventa al transformatei.
    for m in range(N):  # Parcurgem toate esantioanele pentru coeficientul curent.
        X_bucle[k] += x[m] * np.exp(-2j * np.pi * k * m / N)  # Adunam termenii din formula DFT.

F = np.zeros((N, N), dtype=complex)  # Pregatim matricea Fourier de dimensiune N x N.

for k in range(N):  # Parcurgem liniile matricei, asociate indicilor de frecventa.
    for m in range(N):  # Parcurgem coloanele, asociate esantioanelor semnalului.
        F[k, m] = np.exp(-2j * np.pi * k * m / N)  # Completam elementul de pe linia k si coloana m.

X_matrice = F @ x  # Obtinem aceiasi coeficienti prin produsul matrice-vector.
coincid = np.allclose(X_bucle, X_matrice)  # Verificam daca rezultatele sunt numeric apropiate.
eroare = np.max(np.abs(X_bucle - X_matrice))  # Calculam cea mai mare diferenta in modul.

print('Cele doua metode dau acelasi rezultat:', coincid)  # Rezultatul trebuie sa fie True.
print('Diferenta maxima intre metode:', eroare)  # Afisam abaterea numerica dintre metode.
print('Rezolutia in frecventa:', fs / N, 'Hz')  # Afisam distanta dintre frecventele DFT consecutive.

frecvente = n * fs / N  # Asociem indicelui k frecventa fizica f_k = k*fs/N, in Hz.
modul = np.abs(X_matrice)  # Calculam modulul coeficientilor Fourier, cerut in exercitiu.
masca = (frecvente >= 0) & (frecvente <= 100)  # Selectam pentru desen intervalul 0-100 Hz.

fig, axe = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)  # Cream doua grafice alaturate.
fig.suptitle('Transformata Fourier a unui semnal cu trei componente')  # Adaugam titlul general.

axe[0].plot(t, x, color='C0', linewidth=1)  # Desenam semnalul compus in domeniul timp.
axe[0].set_title('Semnalul compus x(t)')  # Punem titlul graficului temporal.
axe[0].set_xlabel('Timp (s)')  # Etichetam timpul in secunde.
axe[0].set_ylabel('Amplitudine')  # Etichetam amplitudinea semnalului.
axe[0].set_xlim(0, N / fs)  # Afisam intervalul de observatie de o secunda.
axe[0].grid(True, alpha=0.3)  # Adaugam grila pentru citirea graficului.

axe[1].stem(frecvente[masca], modul[masca], linefmt='C1-', markerfmt='C1o', basefmt='k-')  # Desenam modulul DFT.
axe[1].set_title('Modulul transformatei Fourier')  # Punem titlul spectrului.
axe[1].set_xlabel('Frecventa (Hz)')  # Etichetam axa frecventelor fizice.
axe[1].set_ylabel(r'$|X[k]|$')  # Precizam ca afisam modulul nenormalizat al coeficientilor.
axe[1].set_xlim(0, 100)  # Fixam plaja de frecvente afisate.
axe[1].set_ylim(0, 1.15 * np.max(modul[masca]))  # Lasam spatiu deasupra varfului cel mai inalt.
axe[1].grid(True, alpha=0.3)  # Adaugam grila si in spectru.

for frecventa in [f1, f2, f3]:  # Marcam cele trei frecvente alese pentru semnal.
    k = int(round(frecventa * N / fs))  # Gasim indicele DFT corespunzator fiecarei frecvente alese.
    axe[1].annotate(f'{frecventa} Hz', (frecvente[k], modul[k]), xytext=(0, 8), textcoords='offset points', ha='center')  # Etichetam varful.
    print(f'La {frecventa} Hz: |X[k]| = {modul[k]:.6f}')  # Afisam si valoarea calculata a modulului.

fig.savefig('ex3.pdf')  # Salvam ambele grafice intr-un PDF vectorial.
plt.show()  # Afisam figura pe ecran.
