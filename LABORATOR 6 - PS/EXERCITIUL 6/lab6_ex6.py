# Laboratorul 6 - Exercițiul 6 (a–f): Filtrarea traficului

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, sosfiltfilt, sosfreqz

cale = Path(__file__).resolve()
date = np.loadtxt(cale.with_name('Train.csv'), delimiter=',',
                 skiprows=1, usecols=2)
start = 5256
x = date[start:start + 72]
if len(x) != 72:
    raise ValueError('Folosește fișierul Train.csv complet.')
ore = np.arange(len(x))

Fs = 1 / 3600
fc = 1 / (12 * 3600)
Wn = fc / (Fs / 2)
print(f'Frecvența de tăiere: {fc:.6e} Hz; Wn = {Wn:.6f}')

ordine = (3, 5, 7)
ondulatii = (0.5, 1, 5)
filtre = {}
for ordin in ordine:
    filtre['Butterworth', ordin, None] = butter(ordin, Wn, output='sos')
    for rp in ondulatii:
        filtre['Chebyshev', ordin, rp] = cheby1(ordin, rp, Wn, output='sos')


def eticheta(cheie):
    tip, ordin, rp = cheie
    text = f'{tip} {ordin}'
    return text if rp is None else f'{text}, rp={rp:g} dB'


y = {}
atenuari = {}
for cheie, sos in filtre.items():
    y[cheie] = sosfiltfilt(sos, x)
    _, h = sosfreqz(sos, worN=2 * np.pi / np.array([24, 6]))
    a24, a6 = -40 * np.log10(np.abs(h))
    atenuari[cheie] = a24, a6
    print(f'{eticheta(cheie)}: 24 h = {a24:.3f} dB, 6 h = {a6:.2f} dB')

acceptate = [k for k, (a24, a6) in atenuari.items() if a24 <= 1 and a6 >= 30]
ales = min(acceptate, key=lambda k: (k[1], atenuari[k][0]))
print('Filtrul ales:', eticheta(ales))

fig, axe = plt.subplots(2, 2, figsize=(13, 7.5), sharex=True,
                        sharey=True, layout='constrained')
ma, baza, ordini, ripple = axe.flat
for ax in axe.flat:
    ax.plot(ore, x, color='0.7', label='Date brute')
    ax.grid(alpha=0.25)

for w in (5, 9, 13, 17):
    medie = np.convolve(x, np.ones(w), 'valid') / w
    ma.plot((w - 1) // 2 + np.arange(len(medie)), medie, label=f'w = {w}')

for k in [('Butterworth', 5, None), ('Chebyshev', 5, 5)]:
    baza.plot(ore, y[k], label=eticheta(k))

for tip, rp, culoare in [('Butterworth', None, 'tab:blue'),
                        ('Chebyshev', 5, 'tab:orange')]:
    for ordin, stil in [(3, '-'), (7, '--')]:
        k = tip, ordin, rp
        ordini.plot(ore, y[k], stil, color=culoare, label=f'{tip} {ordin}')

for rp in ondulatii:
    ripple.plot(ore, y['Chebyshev', 5, rp], label=f'rp = {rp:g} dB')

ma.set_title('(a–b) Medii mobile centrate')
baza.set_title('(d–e) Filtre de ordin 5')
ordini.set_title('(f) Ordinele 3 și 7 | Chebyshev cu rp = 5 dB')
ripple.set_title('(f) Efectul lui rp | Chebyshev de ordin 5')

for ax in axe.flat:
    ax.legend(loc='upper right', ncol=2, fontsize=8)
for ax in axe[:, 0]:
    ax.set_ylabel('Valoarea semnalului')
for ax in axe[1]:
    ax.set_xlabel('Ore de la începutul intervalului')

ma.set_xticks(np.arange(0, 73, 12))
ma.set_xlim(0, 72)
fig.suptitle('Filtrarea datelor din Train.csv | 1–3 aprilie 2013')
fig.savefig(cale.with_suffix('.png'), dpi=160)
plt.show()
