import komm
import numpy as np

def BSC(dane, prawdopodobienstwo):

    kanal = komm.BinarySymmetricChannel(prawdopodobienstwo)  # Tworzenie kanału

    dane_wejsciowe = np.array(dane)                # Konwertowanie na tablice NumPy

    return kanal(dane_wejsciowe)                             # Zwracanie danych wejściowych po przejściu przez kanał BSC

def gilbert_elliott(dane, p_dobry_do_zlego, p_zly_do_dobrego, p_bledu_dobryStan, p_bledu_zlyStan):
    dane_wejsciowe = np.array(dane)               # Konwertowanie na tablice NumPy
    stan = "dobry"
    dane_wyjsciowe = []                                     # Inicjalizowanie pustej listy danych wyjsciowych

    for bit in dane_wejsciowe:
        if stan == "dobry":                                 #Sprawdzanie, czy stan dobry
            if np.random.rand() < p_bledu_dobryStan:        # Sprawdzanie, czy błąd w stanie dobrym
                dane_wyjsciowe.append(1 - bit)              # Jeśli błąd wystąpił, odwracanie bitu i dodanie do listy
            else:
                dane_wyjsciowe.append(bit)                  # Jeśli błąd nie wystąpił, dodanie oryginalnego bitu
            if np.random.rand() < p_dobry_do_zlego:         # Losujemy, czy zmiana stanu
                stan = "zly"
        else:                                               # Sprawdzanie, czy stan zły
            if np.random.rand() < p_bledu_zlyStan:          # Sprawdzanie, czy błąd w stanie złym
                dane_wyjsciowe.append(1 - bit)              # Jeśli błąd wystąpił, odwracanie bitu i dodanie do listy
            else:
                dane_wyjsciowe.append(bit)                  # Jeśli błąd nie wystąpił, dodanie oryginalnego bitu
            if np.random.rand() < p_zly_do_dobrego:         # Losujemy, czy zmiana stanu
                stan = "dobry"

    return np.array(dane_wyjsciowe)                         # Zwracanie danych wyjściowych jako NumPy array

