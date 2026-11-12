from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
x = np.genfromtxt(folder / 'Train.csv', delimiter=',',
                  skip_header=1, usecols=2)

start = 5256
nr_ore = 30 * 24
luna = x[start:start + nr_ore]
zile = np.arange(len(luna)) / 24

print('Indice initial:', start, '- luni, 01.04.2013, ora 00:00')
print('Numar de esantioane:', len(luna))

plt.figure(figsize=(11, 4.5))
plt.plot(zile, luna, linewidth=0.8)
plt.xticks([0, 7, 14, 21, 28],
           ['01.04', '08.04', '15.04', '22.04', '29.04'])
plt.xlim(0, 30)
plt.ylim(bottom=0)
plt.xlabel('Data (2013) - marcajele indica zile de luni')
plt.ylabel('Numar de masini')
plt.title('Laboratorul 5 - Exercitiul 1 g): traficul din aprilie 2013')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(folder / 'lab5_ex1_g.pdf')
plt.show()