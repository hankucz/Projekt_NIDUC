import komm
import numpy as np

def BSC(dane, p):

    kanal = komm.BinarySymmetricChannel(p)  # Tworzenie kanału

    dane_wejsciowe = np.array(dane)                # Konwertowanie na tablice NumPy

    return kanal(dane_wejsciowe)                             # Zwracanie danych wejściowych po przejściu przez kanał BSC

def gilbert_elliott(dane, q, p):
    p_G = 1 - q
    p_B = 1 - p
    dane_wejsciowe = np.array(dane)               # Konwertowanie na tablice NumPy
    stan = "dobry"
    dane_wyjsciowe = []                                     # Inicjalizowanie pustej listy danych wyjsciowych

    for bit in dane_wejsciowe:
        if stan == "dobry":                                 #Sprawdzanie, czy stan dobry
            if np.random.rand() < p_G:        # Sprawdzanie, czy błąd w stanie dobrym
                dane_wyjsciowe.append(1 - bit)              # Jeśli błąd wystąpił, odwracanie bitu i dodanie do listy
            else:
                dane_wyjsciowe.append(bit)                  # Jeśli błąd nie wystąpił, dodanie oryginalnego bitu
            if np.random.rand() < q:         # Losujemy, czy zmiana stanu
                stan = "zly"
        else:                                               # Sprawdzanie, czy stan zły
            if np.random.rand() < p_B:          # Sprawdzanie, czy błąd w stanie złym
                dane_wyjsciowe.append(1 - bit)              # Jeśli błąd wystąpił, odwracanie bitu i dodanie do listy
            else:
                dane_wyjsciowe.append(bit)                  # Jeśli błąd nie wystąpił, dodanie oryginalnego bitu
            if np.random.rand() < p:         # Losujemy, czy zmiana stanu
                stan = "dobry"

    return np.array(dane_wyjsciowe)                         # Zwracanie danych wyjściowych jako NumPy array

