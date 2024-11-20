import kanaly
import Generator
import numpy as np


def main():
    ilosc_bitow = 6                                              # ustalanie ilości bitów w danych wejsciowych

    dane_wejsciowe = Generator.generuj_dane(ilosc_bitow)         # Generowanie losowych bitów uzytych potem do obu modeli

    #BSC
    prawdopodobienstwo = 0.5                                     # Prawdopodobieństwo z jakim bit zostanie zmieniony na przeciwny
    wynik_bsc = kanaly.BSC(dane_wejsciowe, prawdopodobienstwo)  # Symulacja kanału BSC z prawdopodobieństwem błędu 0.1

    #Gilberta Elliotta
    p_dobry_do_zlego = 0.5
    p_zly_do_dobrego = 0.5
    wynik_g_e = kanaly.gilbert_elliott_model(p_dobry_do_zlego, p_zly_do_dobrego, dane_wejsciowe)

    print("Dane wejściowe:", dane_wejsciowe)                     # Wyświetlenie wyników
    print("Dane po przejściu przez kanał BSC:", wynik_bsc)
    print("Dane po przejściu przez kanał Gilberta Elliotta:", wynik_g_e)

if __name__ == "__main__":
    main()



# przy okazji znalazlam jak kodować za pomoca ej biblioteki:
    # Kodowanie danych wejściowych przy użyciu kodera binarnego z komm
    #encoder = komm.BinEncoder()
    #encoded_bits = encoder.encode(input_bits)