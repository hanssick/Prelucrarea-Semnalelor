# Laboratorul 4 - Exercitiul 1: comparatie intre DFT propriu, FFT propriu si NumPy FFT.
# FFT-ul implementat aici este radix-2: dimensiunea N trebuie sa fie o putere a lui 2.

import numpy as np  # Importam operatiile numerice pentru vectori si numere complexe.
import matplotlib.pyplot as plt  # Importam functiile pentru realizarea graficului.
import time  # Importam cronometrul pentru masurarea duratelor de executie.


def dft(x):  # Definim transformata Fourier discreta calculata direct din formula.
    N = len(x)  # Aflam numarul de esantioane.
    n = np.arange(N)  # Construim indicii n = 0, 1, ..., N-1.
    X = np.zeros(N, dtype=complex)  # Pregatim vectorul coeficientilor complecsi.
    for k in range(N):  # Calculam pe rand coeficientul asociat fiecarui indice k.
        X[k] = np.sum(x * np.exp(-2j * np.pi * k * n / N))  # X[k] = suma x[n]*exp(-2*pi*j*k*n/N).
    return X  # Intoarcem cei N coeficienti Fourier.


def fft(x):  # Definim propriul algoritm FFT, prin impartire in pozitii pare si impare.
    N = len(x)  # Aflam dimensiunea subproblemei curente.
    if N == 1:  # O singura valoare este egala cu propria transformata Fourier.
        return np.array(x, dtype=complex)  # Intoarcem acea valoare ca vector complex.
    pare = fft(x[::2])  # Calculam FFT pentru pozitiile 0, 2, 4, ... din vectorul curent.
    impare = fft(x[1::2])  # Calculam FFT pentru pozitiile 1, 3, 5, ... din vectorul curent.
    X = np.zeros(N, dtype=complex)  # Pregatim rezultatul de dimensiune N.
    for k in range(N // 2):  # Combinam cele doua transformate, fiecare de dimensiune N/2.
        termen = np.exp(-2j * np.pi * k / N) * impare[k]  # Calculam W_N^k * O[k], cu W_N = exp(-2*pi*j/N).
        X[k] = pare[k] + termen  # Prima jumatate: X[k] = E[k] + W_N^k*O[k].
        X[k + N // 2] = pare[k] - termen  # A doua jumatate: X[k+N/2] = E[k] - W_N^k*O[k].
    return X  # Intoarcem transformata obtinuta prin combinare.


def cronometreaza(functie, x):  # Masuram durata unei functii pe acelasi vector, de trei ori.
    durate = []  # Vom pastra cele trei durate masurate.
    for repetare in range(3):  # Repetam calculul pentru a reduce influenta unei singure masuratori.
        inceput = time.perf_counter()  # Citim cronometrul imediat inaintea calculului.
        rezultat = functie(x)  # Executam transformata pe vectorul primit.
        durata = time.perf_counter() - inceput  # Calculam timpul scurs, in secunde.
        durate.append(durata)  # Retinem durata masurata.
    return float(np.median(durate)), rezultat  # Intoarcem mediana celor trei durate si rezultatul ultimei rulari.


dimensiuni = [128, 256, 512, 1024, 2048, 4096, 8192]  # Folosim toate dimensiunile cerute.
timpi_dft = []  # Vom retine cate un timp pentru DFT la fiecare N.
timpi_fft = []  # Vom retine cate un timp pentru FFT-ul nostru.
timpi_numpy = []  # Vom retine cate un timp pentru FFT-ul NumPy.
verificari = []  # Vom retine verificarile numerice pentru fiecare dimensiune.

test = np.arange(8, dtype=float)  # Pregatim un vector mic pentru apelurile de incalzire.
dft(test)  # Apelam DFT inainte de masuratori.
fft(test)  # Apelam FFT-ul nostru inainte de masuratori.
np.fft.fft(test)  # Apelam si NumPy FFT, evitand includerea initializarii primului apel in timpi.

print('N       DFT (s)       FFT propriu (s)   NumPy FFT (s)   Corecte: DFT / FFT')  # Antetul tabelului.

for N in dimensiuni:  # Repetam comparatia pentru fiecare dimensiune ceruta.
    n = np.arange(N)  # Construim indicii vectorului curent.
    x = np.sin(2 * np.pi * 7 * n / N) + 0.5 * np.cos(2 * np.pi * 19 * n / N)  # Alegem acelasi semnal pentru cele trei metode.
    timp_dft, X_dft = cronometreaza(dft, x)  # Cronometram implementarea directa.
    timp_fft, X_fft = cronometreaza(fft, x)  # Cronometram FFT-ul implementat de noi.
    timp_numpy, X_numpy = cronometreaza(np.fft.fft, x)  # Cronometram functia FFT a bibliotecii NumPy.
    timpi_dft.append(timp_dft)  # Pastram durata DFT.
    timpi_fft.append(timp_fft)  # Pastram durata FFT propriu.
    timpi_numpy.append(timp_numpy)  # Pastram durata NumPy FFT.
    corect_dft = np.allclose(X_dft, X_numpy, atol=1e-7)  # Comparam DFT-ul nostru cu rezultatul de referinta.
    corect_fft = np.allclose(X_fft, X_numpy, atol=1e-7)  # Comparam FFT-ul nostru cu acelasi rezultat.
    verificari.append((corect_dft, corect_fft))  # Retinem cele doua verificari.
    print(f'{N:<6} {timp_dft:.6e}   {timp_fft:.6e}      {timp_numpy:.6e}   {corect_dft} / {corect_fft}')  # Afisam timpii in secunde.

with open('ex1_timpi.txt', 'w', encoding='utf-8') as fisier:  # Deschidem un fisier pentru timpii masurati la rularea curenta.
    fisier.write('Timpi in secunde: mediana a 3 rulari; valorile depind de calculator.\n')  # Precizam metodologia si unitatea.
    fisier.write('N DFT_s FFT_propriu_s NumPy_FFT_s\n')  # Scriem antetul coloanelor.
    for i, N in enumerate(dimensiuni):  # Asociem fiecare dimensiune cu pozitia ei in liste.
        fisier.write(f'{N} {timpi_dft[i]:.9e} {timpi_fft[i]:.9e} {timpi_numpy[i]:.9e}\n')  # Salvam valorile reale masurate.

fig, ax = plt.subplots(figsize=(9.5, 5.5), constrained_layout=True)  # Cream figura pentru comparatie.
ax.semilogy(dimensiuni, timpi_dft, 'o-', label='DFT propriu - suma directa')  # Desenam timpul DFT pe scara logaritmica Oy.
ax.semilogy(dimensiuni, timpi_fft, 's-', label='FFT propriu - radix-2')  # Adaugam timpul FFT-ului nostru.
ax.semilogy(dimensiuni, timpi_numpy, '^-', label='NumPy FFT')  # Adaugam timpul functiei NumPy.
ax.set_xscale('log', base=2)  # Dublarile succesive ale lui N vor fi egal distantate pe axa Ox.
ax.set_xticks(dimensiuni)  # Marcam exact cele sapte dimensiuni cerute.
ax.set_xticklabels([str(N) for N in dimensiuni])  # Afisam dimensiunile ca numere obisnuite.
ax.set_xlabel('Dimensiunea vectorului N')  # Etichetam axa dimensiunilor.
ax.set_ylabel('Timp de executie (s) - scara logaritmica')  # Precizam unitatea timpului si scara Oy.
ax.set_title('Comparatie DFT si FFT - mediana a 3 rulari')  # Adaugam titlul graficului.
ax.grid(True, which='both', alpha=0.3)  # Afisam grila pentru ambele tipuri de diviziuni.
ax.legend()  # Afisam legenda celor trei metode.
fig.savefig('ex1.pdf')  # Salvam graficul in format PDF vectorial.
plt.show()  # Afisam figura in Spyder sau intr-o fereastra Matplotlib.
