from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

folder = Path(__file__).resolve().parent
t = np.linspace(-3, 3, 2001)
frecvente = [1, 1.5, 2, 4]

with PdfPages(folder / 'lab6_ex1.pdf') as pdf:
    for B in [1, 2]:
        x = np.sinc(B * t) ** 2
        fig, axe = plt.subplots(2, 2, figsize=(11, 7),
                                sharex=True, sharey=True)

        for ax, Fs in zip(axe.flat, frecvente):
            Ts = 1 / Fs
            n = np.arange(int(np.ceil(-3 * Fs)),
                          int(np.floor(3 * Fs)) + 1)
            tn = n * Ts
            xn = np.sinc(B * tn) ** 2
            xr = np.sinc((t[:, None] - tn) / Ts) @ xn

            ax.plot(t, x, color='#2463a0', lw=2, label='Original')
            ax.plot(t, xr, '--', color='#d2691e', lw=1.8,
                    label='Reconstruit')
            ax.scatter(tn, xn, color='#202020', s=28, zorder=3,
                       label='Eșantioane')
            ax.set_title(f'Fs = {Fs:g} Hz; Ts = {Ts:g} s')
            ax.set_xlabel('t [s]')
            ax.set_ylabel('Amplitudine')
            ax.set_xlim(-3, 3)
            ax.set_ylim(-0.3, 1.15)
            ax.set_xticks(np.arange(-3, 4))
            ax.grid(alpha=0.25)

        fig.suptitle(f'Eșantionare și reconstrucție sinc | B = {B}',
                     fontsize=16, y=0.98)
        fig.legend(*axe[0, 0].get_legend_handles_labels(),
                   loc='upper center', bbox_to_anchor=(0.5, 0.93),
                   ncol=3, frameon=False)
        fig.tight_layout(rect=(0, 0.035, 1, 0.86))
        fig.text(0.5, 0.015,
                 'Reconstrucție din eșantioanele disponibile în [-3, 3].',
                 ha='center', fontsize=10, color='#555555')
        pdf.savefig(fig)
        fig.savefig(folder / f'lab6_ex1_B{B}.png', dpi=180)

plt.show()
