# Laboratorul 6 - Exercițiul 2

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

folder = Path(__file__).resolve().parent
N = 100
rng = np.random.default_rng(42)
x_aleator = rng.random(N)
x_bloc = np.zeros(N)
x_bloc[40:60] = 1

with PdfPages(folder / 'lab6_ex2.pdf') as pdf:
    for nume, x in [('aleator', x_aleator), ('rectangular', x_bloc)]:
        semnale = [x]
        for _ in range(3):
            x = np.convolve(x, x, mode='full')
            semnale.append(x)

        fig, axe = plt.subplots(4, 1, figsize=(10, 10),
                                layout='constrained')
        for k, (ax, s) in enumerate(zip(axe, semnale)):
            n = np.arange(len(s))
            ax.plot(n, s, color='#2463a0', lw=1.5)
            ax.fill_between(n, s, color='#2463a0', alpha=0.15)
            titlu = 'Semnal inițial' if k == 0 else f'Iterația {k}'
            ax.set_title(f'{titlu} | Lungime: {len(s)}')
            ax.set_xlabel('n [indice de eșantion]')
            ax.set_ylabel('Amplitudine')
            ax.set_xlim(0, len(s) - 1)
            ax.grid(alpha=0.25)

        fig.suptitle(f'Laboratorul 6 - Exercițiul 2 | Semnal {nume}',
                     fontsize=15)
        pdf.savefig(fig)
        fig.savefig(folder / f'lab6_ex2_{nume}.png', dpi=160)

plt.show()
