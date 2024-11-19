
import kanaly
import Generator
import numpy as np


def main():
    ilosc_bitow = 6                                              # ustalanie ilości bitów w danych wejsciowych

    dane_wejsciowe = Generator.generuj_dane(ilosc_bitow)         # Generowanie losowych bitów

    prawdopodobienstwo = 0.1                                     # Prawdopodobieństwo z jakim bit zostanie zmieniony na przeciwny

    wynik = kanaly.BSC(dane_wejsciowe, prawdopodobienstwo)    # Symulacja kanału BSC z prawdopodobieństwem błędu 0.1

    print("Dane wejściowe:", dane_wejsciowe)                     # Wyświetlenie wyników
    print("Dane po przejściu przez kanał BSC:", wynik)


if __name__ == "__main__":
    main()