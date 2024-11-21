import numpy as np

import kanaly
import generator
import korekcja_powielania_bitow
import kod_hamminga

def main():
    ilosc_bitow = 10                                             # ustalanie ilości bitów w danych wejsciowych

    stopien_powielenia_bitow = 15

    dane_wejsciowe = generator.generuj_dane(ilosc_bitow)         # Generowanie losowych bitów uzytych potem do obu modeli

    dane_wejscioewe_powielone = korekcja_powielania_bitow.powielanie(dane_wejsciowe, stopien_powielenia_bitow)

    #BSC
    prawdopodobienstwo_BSC = 0.5                                     # Prawdopodobieństwo z jakim bit zostanie zmieniony na przeciwny
    wynik_bsc = kanaly.BSC(dane_wejsciowe, prawdopodobienstwo_BSC)   # Symulacja kanału BSC
    wynik_bsc_powielanie = kanaly.BSC(dane_wejscioewe_powielone, prawdopodobienstwo_BSC)  # Symulacja kanału BSC z zastosowaniem korekcji poprzez powielanie

    encoded_hamming = kod_hamminga.dodaj_bity_parzystosci(dane_wejsciowe)
    wynik_bsc_hamming = kanaly.BSC(encoded_hamming, prawdopodobienstwo_BSC)
    corrected_data, has_error = kod_hamminga.popraw_bity_hamminga(wynik_bsc_hamming)
    corrected_data = np.array(corrected_data)

    #Gilberta Elliotta
    p_dobry_do_zlego = 0.5
    p_zly_do_dobrego = 0.5
    p_bledu_dobryStan = 0.5
    p_bledu_zlyStan = 0.5
    wynik_g_e = kanaly.gilbert_elliott(dane_wejsciowe, p_dobry_do_zlego, p_zly_do_dobrego, p_bledu_dobryStan, p_bledu_zlyStan) # Symulacja kanału G-E
    wynik_g_e_powielanie = kanaly.gilbert_elliott(dane_wejscioewe_powielone, p_dobry_do_zlego, p_zly_do_dobrego, p_bledu_dobryStan, p_bledu_zlyStan) # Symulacja kanału G-E z zastosowaniem korekcji poprzez powielanie
    wynik_g_e_hamming = kanaly.gilbert_elliott(encoded_hamming, p_dobry_do_zlego, p_zly_do_dobrego, p_bledu_dobryStan, p_bledu_zlyStan) # Symulacja kanału G-E z zastosowaniem korekcji poprzez kod Hamminga

    print("Dane wejściowe:", dane_wejsciowe)                     # Wyświetlenie wyników
    print("Dane po przejściu przez kanał BSC:", wynik_bsc)
    print("Dane po przejściu przez kanał Gilberta Elliotta:", wynik_g_e)
    print("Dane po przejściu przez kanał BSC z zastosowanym powieleniem:", wynik_bsc_powielanie)
    print("Dane po przejściu przez kanał Gilberta Elliotta z zastosowanym powieleniem:", wynik_g_e_powielanie)
    print("Skorygowane dane po BSC: ", korekcja_powielania_bitow.korektor(wynik_bsc_powielanie, stopien_powielenia_bitow))
    print("Skorygowane dane po G-E: ", korekcja_powielania_bitow.korektor(wynik_g_e_powielanie, stopien_powielenia_bitow))

    print("*************************************************")
    print("Zakodowane dane Hamminga:", encoded_hamming)

    print("Dane po przejściu przez kanał BSC (Hamming):", wynik_bsc_hamming)
    print("Dane po przejściu przez kanał G-E (Hamming):", wynik_g_e_hamming)

    if has_error:
        print("Błąd został wykryty i poprawiony.")

    print("Skorygowane dane po BSC (Hamming):", corrected_data)

if __name__ == "__main__":
    main()

# przy okazji znalazlam jak kodować za pomoca ej biblioteki:
    # Kodowanie danych wejściowych przy użyciu kodera binarnego z komm
    #encoder = komm.BinEncoder()
    #encoded_bits = encoder.encode(input_bits)
