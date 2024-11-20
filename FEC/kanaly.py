import komm
import numpy as np

def BSC(dane_wejsciowe, prawdopodobienstwo):

    kanal = komm.BinarySymmetricChannel(prawdopodobienstwo)  # Tworzenie kanału

    dane_wejsciowe=np.array(dane_wejsciowe)                  # Konwertuje na tablice NumPy

    return kanal(dane_wejsciowe)                             # Zwraca dane wejściowe po przejściu przez kanał BSC

def gilbert_elliott(p_dobry_do_zlego, p_zly_do_dobrego, input_data):
    state = "dobry"                                          # Inicjalizacja stanu
    dane_wyjsciowe = []                                      # Inicjalizacja tablicy przechowującej dane wyjsciowe

    for bit in input_data:
        if state == "dobry":                                 # Stan dobry
            bit_po_przejsciu = bit
            if np.random.rand() < p_dobry_do_zlego:          # Losowanie czy przejść do stanu złego
                state = 0
        else:                                                # Stan zły
            bit_po_przejsciu = 0
            if np.random.rand() < p_zly_do_dobrego:          # Losujemy, czy przejść do stanu dobrego
                state = 1

        dane_wyjsciowe.append(bit_po_przejsciu)              # Dodanie bitu do tablicy danych wyjsciowych

    return dane_wyjsciowe                                    # Zwracanie tablicy danych wyjsciowych
