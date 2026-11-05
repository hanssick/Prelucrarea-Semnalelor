# Laboratorul 4 - Exercitiul 2: fenomenul de aliere la esantionare.

import numpy as np  # Importam functiile numerice pentru vectori si sinus.
import matplotlib.pyplot as plt  # Importam functiile pentru realizarea graficelor.

f0 = 13  # Alegem frecventa semnalului initial: 13 Hz.
fs = 10  # Alegem frecventa de esantionare: 10 Hz, mai mica decat 2*f0 = 26 Hz.
f1 = f0 - fs  # Prima alternativa are frecventa 3 Hz; diferenta fata de f0 este -fs.
f2 = f0 + fs  # A doua alternativa are frecventa 23 Hz; diferenta fata de f0 este +fs.
durata = 1  # Observam semnalele timp de o secunda.

t = np.linspace(0, durata, 5000)  # Folosim multe puncte doar pentru a desena curbele neted.
n = np.arange(int(fs * durata) + 1)  # Construim indicii de esantionare: 0, 1, ..., 10.
t_n = n / fs  # Momentele esantioanelor sunt t_n = n/fs: 0, 0.1, ..., 1 secunda.

x0 = np.sin(2 * np.pi * f0 * t)  # Semnalul initial: x0(t) = sin(2*pi*13*t), amplitudine 1, faza 0.
x1 = np.sin(2 * np.pi * f1 * t)  # Prima alternativa: x1(t) = sin(2*pi*3*t), amplitudine 1, faza 0.
x2 = np.sin(2 * np.pi * f2 * t)  # A doua alternativa: x2(t) = sin(2*pi*23*t), amplitudine 1, faza 0.

es0 = np.sin(2 * np.pi * f0 * t_n)  # Calculam esantioanele semnalului de 13 Hz.
es1 = np.sin(2 * np.pi * f1 * t_n)  # Calculam separat esantioanele semnalului de 3 Hz.
es2 = np.sin(2 * np.pi * f2 * t_n)  # Calculam separat esantioanele semnalului de 23 Hz.

aceleasi_1 = np.allclose(es0, es1, atol=1e-12)  # Verificam daca esantioanele de 13 Hz si 3 Hz coincid numeric.
aceleasi_2 = np.allclose(es0, es2, atol=1e-12)  # Verificam daca esantioanele de 13 Hz si 23 Hz coincid numeric.
print('Esantionare sub-Nyquist pentru semnalul initial:', fs < 2 * f0)  # Verificam 10 < 26.
print('Aceleasi esantioane pentru 13 Hz si 3 Hz:', aceleasi_1)  # Rezultatul trebuie sa fie True.
print('Aceleasi esantioane pentru 13 Hz si 23 Hz:', aceleasi_2)  # Rezultatul trebuie sa fie True.
print('Diferenta maxima intre es0 si es1:', np.max(np.abs(es0 - es1)))  # Masuram eroarea numerica.
print('Diferenta maxima intre es0 si es2:', np.max(np.abs(es0 - es2)))  # Masuram si a doua eroare.

fig, axe = plt.subplots(4, 1, figsize=(10, 9), sharex=True, constrained_layout=True)  # Cream patru grafice suprapuse.
fig.suptitle('Aliere: trei sinusoide diferite, aceleasi esantioane', fontsize=14)  # Adaugam titlul general.

axe[0].plot(t, x0, color='C0')  # Desenam semnalul initial fara marcajele de esantionare.
axe[0].set_title('Semnalul initial: f = 13 Hz')  # Precizam frecventa semnalului initial.

axe[1].plot(t, x0, color='C0')  # Redesenam semnalul initial, acum impreuna cu esantioanele.
axe[1].scatter(t_n, es0, color='gold', edgecolors='black', s=45, zorder=3, label='Esantioane la 10 Hz')  # Marcam valorile esantionate.
axe[1].set_title('Esantionare la fs = 10 Hz < 2 * 13 Hz')  # Evidentiem faptul ca rata de esantionare este insuficienta.
axe[1].legend(loc='upper right', fontsize=8)  # Explicam semnificatia punctelor galbene.

axe[2].plot(t, x1, color='C2')  # Desenam sinusoida alternativa de 3 Hz.
axe[2].scatter(t_n, es1, color='gold', edgecolors='black', s=45, zorder=3)  # Marcam esantioanele calculate pentru aceasta sinusoida.
axe[2].set_title('Alternativa: f = 3 Hz - aceleasi esantioane')  # Precizam ca esantioanele coincid.

axe[3].plot(t, x2, color='C3')  # Desenam sinusoida alternativa de 23 Hz.
axe[3].scatter(t_n, es2, color='gold', edgecolors='black', s=45, zorder=3)  # Marcam si esantioanele celei de-a doua alternative.
axe[3].set_title('Alternativa: f = 23 Hz - aceleasi esantioane')  # Precizam a doua frecventa alternativa.

for ax in axe:  # Configuram identic cele patru grafice, pentru a le compara usor.
    ax.set_xlim(-0.015, durata + 0.015)  # Lasam putin spatiu ca sa vedem complet punctele de la capete.
    ax.set_ylim(-1.25, 1.25)  # Folosim aceeasi scara pentru amplitudine.
    ax.set_ylabel('Amplitudine')  # Etichetam axa verticala.
    ax.grid(True, alpha=0.3)  # Adaugam o grila discreta.

axe[-1].set_xlabel('Timp (s)')  # Etichetam axa timpului, comuna tuturor graficelor.
fig.savefig('ex2.pdf')  # Salvam intreaga figura in format PDF vectorial.
plt.show()  # Afisam figura in Spyder sau intr-o fereastra Matplotlib.
