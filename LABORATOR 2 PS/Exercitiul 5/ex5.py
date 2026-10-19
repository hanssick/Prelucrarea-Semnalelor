import numpy as np
import sounddevice as sd
from scipy.io import wavfile

fs = 44100
durata = 2
t = np.arange(fs * durata) / fs

x1 = 0.5 * np.sin(2 * np.pi * 440 * t)
x2 = 0.5 * np.sin(2 * np.pi * 880 * t)

x = np.concatenate((x1, x2))

date = np.round(32767 * x).astype(np.int16)
wavfile.write("ex5.wav", fs, date)

print("Primele 2 secunde: sinus de 440 Hz.")
print("Urmatoarele 2 secunde: sinus de 880 Hz.")
print("Al doilea ton este mai inalt, cu o octava.")

sd.play(x, fs)
sd.wait()
