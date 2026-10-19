import numpy as np
import sounddevice as sd
from scipy.io import wavfile

fs = 8000

t_a = np.arange(1600) / fs
x_a = np.sin(2 * np.pi * 400 * t_a)

t_b = np.arange(3 * fs) / fs
x_b = np.sin(2 * np.pi * 800 * t_b)

t_c = np.arange(0, 0.02, 1 / fs)
x_c = 2 * np.mod(240 * t_c, 1) - 1

t_d = np.arange(0, 0.02, 1 / fs)
x_d = np.sign(np.sin(2 * np.pi * 300 * t_d))
x_d[x_d == 0] = 1

date = np.round(32767 * x_b).astype(np.int16)
wavfile.write("ex3.wav", fs, date)

rate, reincarcat = wavfile.read("ex3.wav")
print("Frecventa de esantionare:", rate, "Hz")
print("Numarul de esantioane:", len(reincarcat))
print("Reincarcare corecta:", rate == fs and np.array_equal(date, reincarcat))

semnale = [x_a, x_b, x_c, x_d]
nume = ["Sinus 400 Hz", "Sinus 800 Hz", "Sawtooth 240 Hz", "Square 300 Hz"]

for i in range(len(semnale)):
    print("Se reda:", nume[i])
    sd.play(semnale[i], fs)
    sd.wait()
