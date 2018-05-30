import os
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np



def get_notes_from(id):
    path = os.path.abspath("./fma_small_wav/%03d/%06d.wav" % (id // 1000, id))
    rate, data = wav.read(path)
    data = data.T[0]
    aSecond = int(len(data) / 30)
    notes = []
    for i in range(0,30):
        normalized = [ ele / (2**16) for ele in data[i * aSecond : i * aSecond + aSecond]]
        fftout = fft(normalized)
        limitx = int(len(fftout) / 2)
        notes.append(( [ i / 30 for i in range(0, (limitx-1))], np.abs(fftout[:limitx-1])))
    freqnotes = []
    for note in notes:
        avgFreq = 0;
        totalAmp = 0;
        for i in range(0, len(note[0])):
            frequency = note[0][i]
            amplitude = note[1][i]
            avgFreq = frequency * amplitude
            totalAmp = totalAmp + amplitude
        freqnotes.append(avgFreq)
    return freqnotes