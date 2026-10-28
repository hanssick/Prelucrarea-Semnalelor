# Laboratorul 3 - Exercitiul 2: infasurarea unui semnal in planul complex.
# Fisierele sunt salvate in directorul de lucru din care rulezi programul.
# In Spyder, pentru ferestre animate: executa %matplotlib qt in consola IPython.

import numpy as np  # Importam operatiile numerice si numerele complexe.
import matplotlib.pyplot as plt  # Importam functiile pentru desenarea figurilor.
from matplotlib.animation import FuncAnimation, PillowWriter  # Importam animatia si salvarea GIF.

fs = 1000  # Alegem frecventa de esantionare: 1000 de esantioane pe secunda.
t = np.arange(fs + 1) / fs  # Construim timpul de la 0 la 1 secunda, inclusiv capetele.
f = 3  # Alegem frecventa semnalului: 3 Hz, diferita de cei 5 Hz din indrumar.
x = np.sin(2 * np.pi * f * t)  # Generam sinusul de amplitudine 1 si faza initiala 0.
raza = np.abs(x)  # Modulul semnalului va fi distanta punctelor complexe fata de origine.
frecvente = [1, 2, 3, 5]  # Alegem patru frecvente de infasurare; una este egala cu f.
y = x * np.exp(-2j * np.pi * t)  # Pentru Figura 1, infasuram cu frecventa de 1 Hz.
z = [x * np.exp(-2j * np.pi * omega * t) for omega in frecvente]  # Calculam cele patru infasurari.
scala = plt.Normalize(0, 1)  # Fixam aceeasi corespondenta distanta-culoare pentru toate graficele.
cerc = np.exp(1j * np.linspace(0, 2 * np.pi, 400))  # Construim cercul unitate ca reper vizual.
indice_fix = 620  # Alegem esantionul evidentiat cu rosu in figurile statice.
cadre = np.arange(0, len(t), 10)  # La fiecare cadru mai desenam 10 intervale de esantionare.
interval_ms = 40  # Intervalul tinta dintre cadre este de 40 milisecunde.
salveaza_gif = False  # Pune True daca vrei sa generezi din nou si fisierele GIF.


def plan_complex(ax, titlu):  # Definim o functie pentru configurarea fiecarui plan complex.
    ax.plot(cerc.real, cerc.imag, '--', color='0.75', linewidth=1)  # Desenam cercul unitate.
    ax.axhline(0, color='0.75', linewidth=0.7)  # Marcam axa reala.
    ax.axvline(0, color='0.75', linewidth=0.7)  # Marcam axa imaginara.
    ax.set_xlim(-1.1, 1.1)  # Stabilim limitele orizontale.
    ax.set_ylim(-1.1, 1.1)  # Stabilim aceleasi limite pe verticala.
    ax.set_aspect('equal', adjustable='box')  # Pastram aceeasi scara pe cele doua axe.
    ax.set_xlabel('Partea reala')  # Etichetam axa orizontala.
    ax.set_ylabel('Partea imaginara')  # Etichetam axa verticala.
    ax.set_title(titlu)  # Adaugam titlul planului complex.
    ax.grid(True, alpha=0.2)  # Adaugam o grila discreta.


fig1, axe1 = plt.subplots(1, 2, figsize=(11, 4.5), constrained_layout=True)  # Cream Figura 1.
fig1.suptitle('Semnalul in timp si infasurarea lui in planul complex')  # Punem titlul general.
graf_timp = axe1[0].scatter(t, x, c=raza, cmap='viridis', norm=scala, s=6)  # Coloram dupa |x(t)|.
axe1[0].set_xlim(0, 1)  # Afisam o secunda din semnal.
axe1[0].set_ylim(-1.15, 1.15)  # Lasam putin spatiu in jurul amplitudinii [-1, 1].
axe1[0].set_xlabel('Timp (s)')  # Etichetam timpul in secunde.
axe1[0].set_ylabel('Amplitudine')  # Etichetam amplitudinea semnalului.
axe1[0].set_title('Semnal sinusoidal: f = 3 Hz')  # Precizam frecventa semnalului.
axe1[0].grid(True, alpha=0.2)  # Adaugam grila in graficul temporal.
plan_complex(axe1[1], 'Frecventa de infasurare: 1 Hz')  # Configuram graficul din dreapta.
graf_y = axe1[1].scatter(y.real, y.imag, c=raza, cmap='viridis', norm=scala, s=6)  # Desenam y(t).
punct_timp, = axe1[0].plot([t[indice_fix]], [x[indice_fix]], 'ro', markersize=7)  # Marcam esantionul.
verticala, = axe1[0].plot([t[indice_fix]] * 2, [0, x[indice_fix]], 'r-', linewidth=1.5)  # Aratam amplitudinea.
punct_y, = axe1[1].plot([y[indice_fix].real], [y[indice_fix].imag], 'ro', markersize=7)  # Marcam punctul complex.
raza_y, = axe1[1].plot([0, y[indice_fix].real], [0, y[indice_fix].imag], 'r-', linewidth=1.5)  # Desenam raza.
text1 = axe1[0].text(0.02, 0.95, '', transform=axe1[0].transAxes, va='top', color='red')  # Pregatim indicatorul de timp.
text1.set_text(f'n = {indice_fix}, t = {t[indice_fix]:.3f} s')  # Afisam indicele si timpul punctului rosu.
fig1.colorbar(graf_y, ax=axe1.tolist(), label=r'$|z(t)| = |x(t)|$')  # Explicam semnificatia culorilor.
fig1.savefig('ex2_figura1.pdf')  # Salvam figura completa, inainte sa incepem animatia.
fig1.set_layout_engine(None)  # Fixam aranjarea deja calculata, pentru actualizari mai rapide.


fig2, axe2 = plt.subplots(2, 2, figsize=(8, 7.5), constrained_layout=True)  # Cream cele patru planuri complexe.
titlu2 = fig2.suptitle(f'Frecvente de infasurare - t = {t[indice_fix]:.3f} s (punct rosu)')  # Precizam timpul comun.
grafice_z = []  # Vom pastra reprezentarile colorate, pentru a le actualiza in animatie.
puncte_z = []  # Vom pastra cei patru indicatori rosii.
raze_z = []  # Vom pastra cele patru segmente de la origine la indicator.

for ax, omega, semnal_z in zip(axe2.flat, frecvente, z):  # Asociem fiecare axa cu o frecventa si o infasurare.
    titlu = f'Infasurare: {omega} Hz'  # Construim titlul graficului curent.
    if omega == f:  # Verificam daca frecventa de infasurare coincide cu frecventa semnalului.
        titlu += ' = f'  # Evidentiem cazul in care cele doua frecvente sunt egale.
    plan_complex(ax, titlu)  # Configuram axele si cercul unitate.
    graf = ax.scatter(semnal_z.real, semnal_z.imag, c=raza, cmap='viridis', norm=scala, s=6)  # Desenam infasurarea.
    punct, = ax.plot([semnal_z[indice_fix].real], [semnal_z[indice_fix].imag], 'ro', markersize=7)  # Marcam punctul curent.
    linie, = ax.plot([0, semnal_z[indice_fix].real], [0, semnal_z[indice_fix].imag], 'r-', linewidth=1.3)  # Desenam raza sa.
    grafice_z.append(graf)  # Retinem graficul colorat.
    puncte_z.append(punct)  # Retinem indicatorul rosu.
    raze_z.append(linie)  # Retinem segmentul rosu.

fig2.colorbar(grafice_z[0], ax=axe2.ravel().tolist(), label=r'$|z(t)| = |x(t)|$')  # Adaugam scala comuna de culori.
fig2.savefig('ex2_figura2.pdf')  # Salvam cele patru grafice complete intr-un PDF vectorial.
fig2.set_layout_engine(None)  # Pastram pozitiile axelor fara sa le recalculam la fiecare cadru.


def actualizeaza1(i):  # Descriem ce se schimba la un cadru din prima animatie.
    graf_timp.set_offsets(np.column_stack((t[:i + 1], x[:i + 1])))  # Aratam semnalul numai pana la esantionul i.
    graf_timp.set_array(raza[:i + 1])  # Actualizam culorile punctelor deja desenate.
    graf_y.set_offsets(np.column_stack((y[:i + 1].real, y[:i + 1].imag)))  # Aratam infasurarea pana la acelasi esantion.
    graf_y.set_array(raza[:i + 1])  # Folosim aceleasi distante pentru culoarea infasurarii.
    punct_timp.set_data([t[i]], [x[i]])  # Mutam indicatorul din graficul temporal.
    verticala.set_data([t[i]] * 2, [0, x[i]])  # Mutam segmentul care arata amplitudinea.
    punct_y.set_data([y[i].real], [y[i].imag])  # Mutam indicatorul din planul complex.
    raza_y.set_data([0, y[i].real], [0, y[i].imag])  # Actualizam raza punctului complex.
    text1.set_text(f'n = {i}, t = {t[i]:.3f} s')  # Afisam indicele si timpul cadrului curent.


def actualizeaza2(i):  # Descriem un cadru din animatia cu patru frecvente.
    for j, semnal_z in enumerate(z):  # Parcurgem cele patru infasurari.
        grafice_z[j].set_offsets(np.column_stack((semnal_z[:i + 1].real, semnal_z[:i + 1].imag)))  # Desenam progresiv.
        grafice_z[j].set_array(raza[:i + 1])  # Actualizam culorile dupa distanta fata de origine.
        puncte_z[j].set_data([semnal_z[i].real], [semnal_z[i].imag])  # Mutam indicatorul rosu.
        raze_z[j].set_data([0, semnal_z[i].real], [0, semnal_z[i].imag])  # Actualizam segmentul radial.
    titlu2.set_text(f'Frecvente de infasurare - t = {t[i]:.3f} s (punct rosu)')  # Actualizam timpul comun.


animatie1 = FuncAnimation(fig1, actualizeaza1, frames=cadre, interval=interval_ms, repeat=True, cache_frame_data=False)  # Animam Figura 1.
animatie2 = FuncAnimation(fig2, actualizeaza2, frames=cadre, interval=interval_ms, repeat=True, cache_frame_data=False)  # Animam Figura 2.

if salveaza_gif:  # Salvam animatiile si ca fisiere care pot fi deschise separat.
    print('Salvez cele doua animatii GIF...')  # Anuntam exportul, care poate dura mai mult.
    animatie1.save('ex2_animatie1.gif', writer=PillowWriter(fps=25), dpi=85)  # Exportam prima animatie.
    animatie2.save('ex2_animatie2.gif', writer=PillowWriter(fps=25), dpi=85)  # Exportam a doua animatie.

actualizeaza1(0)  # Pregatim prima fereastra sa porneasca de la primul esantion.
actualizeaza2(0)  # Pregatim si a doua fereastra de la acelasi moment.
print('PDF-urile sunt salvate. Punctele rosii indica esantionul curent.')  # Confirmam rezultatele.
plt.show()  # Deschidem ferestrele grafice si lasam animatiile sa ruleze.
