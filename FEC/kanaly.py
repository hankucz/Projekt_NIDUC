import komm
import numpy as np
import random

def BSC(dane_wejsciowe, prawdopodobienstwo):

    kanal = komm.BinarySymmetricChannel(prawdopodobienstwo)  # Tworzenie kanału

    dane_wejsciowe=np.array(dane_wejsciowe)                  # Konwertuje na tablice NumPy

    return kanal(dane_wejsciowe)                             # Zwraca dane wejściowe po przejściu przez kanał BSC

