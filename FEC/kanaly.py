import komm
import numpy as np

def BSC(dane_wejsciowe, prawdopodobienstwo):

    kanal = komm.BinarySymmetricChannel(prawdopodobienstwo)  # Tworzenie kanału

    dane_wejsciowe = np.array(dane_wejsciowe)                  # Konwertuje na tablice NumPy

    return kanal(dane_wejsciowe)                             # Zwraca dane wejściowe po przejściu przez kanał BSC

def gilbert_elliott(dane_wejsciowe, p_dobry_do_zlego, p_zly_do_dobrego, p_bledu_dobryStan, p_bledu_zlyStan):
    state = "dobry"                                          # Inicjalizacja stanu
    dane_wyjsciowe = []                                      # Inicjalizacja tablicy przechowującej dane wyjsciowe

    for bit in dane_wejsciowe:
        if state == "dobry":                                 # Stan dobry
            if np.random.rand() < p_bledu_dobryStan:
                dane_wyjsciowe.append(0)                 # Dodanie bitu do tablicy danych wyjsciowych z dodaniem błędu
            else:
                dane_wyjsciowe.append(bit)                 # Dodanie bitu do tablicy danych wyjsciowych
            if np.random.rand() < p_dobry_do_zlego:          # Losowanie czy przejść do stanu złego
                state = "zly"
        else:                                                # Stan zły
            if np.random.rand() < p_bledu_zlyStan:
                dane_wyjsciowe.append(0)                 # Dodanie bitu do tablicy danych wyjsciowych z dodaniem błędu
            else:
                dane_wyjsciowe.append(bit)                 # Dodanie bitu do tablicy danych wyjsciowych
            if np.random.rand() < p_zly_do_dobrego:          # Losujemy, czy przejść do stanu dobrego
                state = "dobry"

    return dane_wyjsciowe                                    # Zwracanie tablicy danych wyjsciowych
