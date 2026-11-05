# Laboratorul 4 - Exercitiul 6: spectrograma vocalelor dintr-un fisier WAV.
# Audio: Denelson83 / Wikimedia Commons, CC BY-SA 3.0; detalii in surse_audio.txt.

import numpy as np  # Importam operatiile numerice pentru vectori, matrice si FFT.
import matplotlib.pyplot as plt  # Importam functiile pentru desenarea spectrogramei.
from scipy.io import wavfile  # Importam functia care citeste un fisier WAV.
from pathlib import Path  # Folosim calea dosarului in care se afla acest program.

dosar = Path(__file__).resolve().parent  # Identificam dosarul fisierului ex6.py.
fs, semnal = wavfile.read(str(dosar / 'vocale.wav'))  # (a) Citim frecventa fs si esantioanele audio.
tip_initial = semnal.dtype  # Retinem tipul datelor, pentru cazul WAV pe 8 biti.
semnal = semnal.astype(float)  # Convertim esantioanele in numere reale pentru calcule.

if tip_initial == np.uint8:  # Verificam daca WAV-ul foloseste valori intre 0 si 255.
    semnal = semnal - 128  # In acest caz, mutam nivelul de liniste din 128 in 0.

if semnal.ndim == 2:  # Verificam daca inregistrarea are mai multe canale, de exemplu stereo.
    semnal = np.mean(semnal, axis=1)  # Obtinem un singur vector facand media canalelor.

N = len(semnal)  # N este numarul total de esantioane din fisier.
lungime = 2 * int(round(0.01 * N / 2))  # (b) Rotunjim 1% din N la cel mai apropiat numar par.

if lungime < 2:  # O fereastra trebuie sa contina cel putin doua esantioane.
    raise ValueError('Inregistrarea este prea scurta pentru ferestre de 1%.')  # Oprim calculul daca lipsesc date.

pas = lungime // 2  # Avansam cu jumatate de fereastra: suprapunerea este exact 50%.
inceputuri = np.arange(0, N - lungime + 1, pas)  # Selectam numai ferestrele care incap complet in semnal.
nr_ferestre = len(inceputuri)  # Numarul de ferestre va fi numarul de coloane din matrice.
spectrograma = np.zeros((lungime, nr_ferestre))  # (d) Pregatim matricea modulelor FFT, inclusiv frecventele negative.

for j in range(nr_ferestre):  # Parcurgem toate ferestrele, in ordinea timpului.
    inceput = inceputuri[j]  # Aflam indicele primului esantion din fereastra curenta.
    fereastra = semnal[inceput:inceput + lungime]  # Extragem grupul de aproximativ 1% din semnal.
    transformata = np.fft.fft(fereastra)  # (c) Calculam FFT: X_j[k] = suma x_j[n] * exp(-2*pi*i*k*n/L).
    spectrograma[:, j] = np.abs(transformata)  # (d) Punem |X_j[k]| pe coloana j, pentru toate valorile k.

nr_frecvente = lungime // 2 + 1  # Pentru desen pastram frecventele de la 0 pana la fs/2, inclusiv.
frecvente = np.arange(nr_frecvente) * fs / lungime  # Frecventele afisate sunt f_k = k*fs/L, in Hz.
timpuri = (inceputuri + (lungime - 1) / 2) / fs  # Asociem fiecarei coloane timpul din centrul ferestrei.
referinta = np.max(spectrograma)  # Alegem drept referinta cel mai mare modul FFT din intreaga inregistrare.

if referinta == 0:  # Daca fisierul contine numai liniste, evitam impartirea la zero.
    referinta = 1  # Valorile spectrogramei raman nule inainte de conversia pentru afisare.

raport = spectrograma[:nr_frecvente, :] / referinta  # Normalizam modulele folosite in imagine.
spectrograma_db = 20 * np.log10(np.maximum(raport, 0.0001))  # Pentru culori: 20*log10(|X|/referinta), cu prag la -80 dB.

fig, ax = plt.subplots(figsize=(11, 5.5), constrained_layout=True)  # Cream figura in care vom afisa matricea.
imagine = ax.pcolormesh(timpuri, frecvente, spectrograma_db, shading='auto', cmap='magma', vmin=-80, vmax=0, rasterized=True)  # (e) Desenam spectrograma.
ax.set_title('Spectrograma vocalelor a, e, i, o, u - in aceasta ordine')  # Precizam ordinea sunetelor din WAV-ul inclus.
ax.set_xlabel('Timp (s)')  # Coloanele corespund momentelor succesive de timp.
ax.set_ylabel('Frecventa (Hz)')  # Randurile corespund frecventelor analizate.
ax.set_xlim(0, N / fs)  # Afisam durata intregului fisier audio.
ax.set_ylim(0, fs / 2)  # Afisam numai jumatatea spectrului necesara pentru un semnal real.
fig.colorbar(imagine, ax=ax, label='Modul FFT relativ (dB; 0 = maximul global)')  # Explicam scara culorilor.
fig.savefig(dosar / 'ex6.pdf', dpi=300)  # Salvam graficul in PDF, cu imagine clara si etichete vectoriale.

print('Frecventa de esantionare:', fs, 'Hz')  # Afisam frecventa citita din fisier.
print('Numar total de esantioane:', N)  # Afisam dimensiunea vectorului audio.
print('Lungimea ferestrei:', lungime, 'esantioane; pasul:', pas)  # Verificam lungimea si suprapunerea.
print('Dimensiunea matricei:', spectrograma.shape)  # Afisam numarul de frecvente FFT si numarul de ferestre.
plt.show()  # Afisam spectrograma in Spyder sau intr-o fereastra Matplotlib.
