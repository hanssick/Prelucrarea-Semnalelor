# Laboratorul 4 - Exercitiul 3: esantionare suficienta pentru cele trei semnale.

import numpy as np  # Importam operatiile numerice pentru vectori si functia sinus.
import matplotlib.pyplot as plt  # Importam functiile pentru desenarea graficelor.

f0 = 13  # Pastram frecventa semnalului initial de la exercitiul 2: 13 Hz.
f1 = 3  # Pastram prima frecventa alternativa: 3 Hz.
f2 = 23  # Pastram a doua frecventa alternativa: 23 Hz.
fs = 64  # Alegem noua frecventa de esantionare: 64 Hz.
B = max(f0, f1, f2)  # Frecventa maxima a celor trei semnale este B = 23 Hz.
durata = 1  # Observam semnalele pe un interval de o secunda.

t = np.linspace(0, durata, 5000)  # Construim o grila deasa numai pentru desenarea curbelor.
n = np.arange(int(fs * durata) + 1)  # Construim indicii n = 0, 1, ..., 64, incluzand ambele capete.
t_n = n / fs  # Momentele de esantionare sunt t_n = n/64, la distanta 1/64 secunde.

x0 = np.sin(2 * np.pi * f0 * t)  # Semnalul initial: x0(t) = sin(2*pi*13*t).
x1 = np.sin(2 * np.pi * f1 * t)  # Prima alternativa: x1(t) = sin(2*pi*3*t).
x2 = np.sin(2 * np.pi * f2 * t)  # A doua alternativa: x2(t) = sin(2*pi*23*t).

es0 = np.sin(2 * np.pi * f0 * t_n)  # Esantionam sinusoida de 13 Hz la noua frecventa fs.
es1 = np.sin(2 * np.pi * f1 * t_n)  # Esantionam separat sinusoida de 3 Hz, la aceleasi momente.
es2 = np.sin(2 * np.pi * f2 * t_n)  # Esantionam separat sinusoida de 23 Hz.

aceleasi_1 = np.allclose(es0, es1, atol=1e-12)  # Comparam sirurile de esantioane pentru 13 Hz si 3 Hz.
aceleasi_2 = np.allclose(es0, es2, atol=1e-12)  # Comparam sirurile de esantioane pentru 13 Hz si 23 Hz.
aceleasi_3 = np.allclose(es1, es2, atol=1e-12)  # Comparam si sirurile de esantioane pentru 3 Hz si 23 Hz.

print('Conditia fs > 2*B este indeplinita:', fs > 2 * B)  # Verificam 64 > 2*23 = 46.
print('Limita Nyquist a esantionarii:', fs / 2, 'Hz')  # Afisam limita fs/2 = 32 Hz.
print('Aceleasi esantioane pentru 13 Hz si 3 Hz:', aceleasi_1)  # Acum rezultatul trebuie sa fie False.
print('Aceleasi esantioane pentru 13 Hz si 23 Hz:', aceleasi_2)  # Si aceasta comparatie trebuie sa dea False.
print('Aceleasi esantioane pentru 3 Hz si 23 Hz:', aceleasi_3)  # Verificam ca toate cele trei siruri sunt distincte.
print('La t = 1/64 s, valorile sunt:', es0[1], es1[1], es2[1])  # Afisam un moment la care valorile sunt diferite.

fig, axe = plt.subplots(4, 1, figsize=(10, 9), sharex=True, constrained_layout=True)  # Cream patru grafice suprapuse.
fig.suptitle('Esantionare la 64 Hz: cele trei sinusoide au esantioane diferite', fontsize=14)  # Adaugam titlul general.

axe[0].plot(t, x0, color='C0')  # Desenam semnalul initial fara marcajele de esantionare.
axe[0].set_title('Semnalul initial: f = 13 Hz')  # Precizam frecventa lui.

axe[1].plot(t, x0, color='C0')  # Desenam semnalul initial impreuna cu esantioanele noi.
axe[1].scatter(t_n, es0, color='gold', edgecolors='black', s=25, zorder=3, label='Esantioane la 64 Hz')  # Marcam esantioanele.
axe[1].set_title('Esantionare la fs = 64 Hz > 2 * 23 Hz')  # Precizam conditia suficienta pentru toate cele trei semnale.
axe[1].legend(loc='upper right', fontsize=8)  # Explicam semnificatia punctelor galbene.

axe[2].plot(t, x1, color='C2')  # Desenam sinusoida de 3 Hz.
axe[2].scatter(t_n, es1, color='gold', edgecolors='black', s=25, zorder=3)  # Marcam propriile ei esantioane.
axe[2].set_title('Semnalul de 3 Hz - sir de esantioane diferit de cel initial')  # Evidentiem schimbarea fata de exercitiul 2.

axe[3].plot(t, x2, color='C3')  # Desenam sinusoida de 23 Hz.
axe[3].scatter(t_n, es2, color='gold', edgecolors='black', s=25, zorder=3)  # Marcam si esantioanele acestei sinusoide.
axe[3].set_title('Semnalul de 23 Hz - sir de esantioane diferit de cel initial')  # Precizam ca nici aceasta alternativa nu mai coincide.

for ax in axe:  # Pastram aceleasi limite si aceeasi grila in toate graficele.
    ax.set_xlim(-0.015, durata + 0.015)  # Lasam loc pentru punctele situate la capetele intervalului.
    ax.set_ylim(-1.25, 1.25)  # Folosim o scara verticala comuna.
    ax.set_ylabel('Amplitudine')  # Etichetam axa verticala.
    ax.grid(True, alpha=0.3)  # Adaugam o grila discreta.

axe[-1].set_xlabel('Timp (s)')  # Etichetam axa timpului, comuna celor patru grafice.
fig.savefig('ex3.pdf')  # Salvam figura in format PDF vectorial.
plt.show()  # Afisam figura in Spyder sau intr-o fereastra Matplotlib.
