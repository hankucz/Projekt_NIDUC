import numpy as np

import kanaly
import generator
import korekcja_powielania_bitow
import kod_hamminga

def main():
    ilosc_bitow = 4                                             # Ustalanie ilości bitów w danych wejsciowych

    stopien_powielenia_bitow = 15

    dane_wejsciowe = generator.generuj_dane(ilosc_bitow)         # Generowanie losowych bitów uzytych potem do obu modeli

    dane_wejscioewe_powielone = korekcja_powielania_bitow.powielanie(dane_wejsciowe, stopien_powielenia_bitow)

    #BSC
    prawdopodobienstwo_BSC = 0.10                                    # Prawdopodobieństwo z jakim bit zostanie zmieniony na przeciwny
    wynik_bsc = kanaly.BSC(dane_wejsciowe, prawdopodobienstwo_BSC)   # Symulacja kanału BSC
    wynik_bsc_powielanie = kanaly.BSC(dane_wejscioewe_powielone, prawdopodobienstwo_BSC)  # Symulacja kanału BSC z zastosowaniem korekcji poprzez powielanie

    zakodowany_kod_hamminga = kod_hamminga.dodaj_bity_parzystosci(dane_wejsciowe)
    wynik_bsc_hamming = kanaly.BSC(zakodowany_kod_hamminga, prawdopodobienstwo_BSC)
    (odkodowany_kod_hamminga_bsc, czy_ma_blad_bsc) = kod_hamminga.popraw_bity_hamminga(wynik_bsc_hamming)
    odkodowany_kod_hamminga_bsc = np.array(odkodowany_kod_hamminga_bsc)

    #Gilberta Elliotta
    q = 0.5
    p = 0.5
    wynik_g_e = kanaly.gilbert_elliott(dane_wejsciowe, q, p)                       # Symulacja kanału G-E
    wynik_g_e_powielanie = kanaly.gilbert_elliott(dane_wejscioewe_powielone, q, p) # Symulacja kanału G-E z zastosowaniem korekcji poprzez powielanie
    wynik_g_e_hamming = kanaly.gilbert_elliott(zakodowany_kod_hamminga, q, p)              # Symulacja kanału G-E z zastosowaniem korekcji poprzez kod Hamminga
    odkodowany_kod_hamminga_ge, czy_ma_blad_ge = kod_hamminga.popraw_bity_hamminga(wynik_g_e_hamming)
    odkodowany_kod_hamminga_ge = np.array(odkodowany_kod_hamminga_ge)

    print("Dane wejściowe:", dane_wejsciowe)                     # Wyświetlenie wyników
    print("Dane po przejściu przez kanał BSC:", wynik_bsc)
    print("Dane po przejściu przez kanał Gilberta Elliotta:", wynik_g_e)

    print("*************************************************")
    print("Dane po przejściu przez kanał BSC z zastosowanym powieleniem:", wynik_bsc_powielanie)
    print("Dane po przejściu przez kanał Gilberta Elliotta z zastosowanym powieleniem:", wynik_g_e_powielanie)
    print("Skorygowane dane po BSC (powielanie): ", korekcja_powielania_bitow.korektor(wynik_bsc_powielanie, stopien_powielenia_bitow))
    print("Skorygowane dane po G-E (powielanie): ", korekcja_powielania_bitow.korektor(wynik_g_e_powielanie, stopien_powielenia_bitow))

    print("*************************************************")
    print("Zakodowane dane Hamminga:", zakodowany_kod_hamminga)

    print("Dane po przejściu przez kanał BSC (Hamming):", wynik_bsc_hamming)
    print("Dane po przejściu przez kanał G-E (Hamming):", wynik_g_e_hamming)

    if czy_ma_blad_bsc:
        print("Błąd został wykryty i poprawiony.")

    print("Skorygowane dane po BSC (Hamming):", odkodowany_kod_hamminga_bsc)



    if czy_ma_blad_ge:
        print("Błąd został wykryty i poprawiony.")

    print("Skorygowane dane po G-E (Hamming):", odkodowany_kod_hamminga_ge)

if __name__ == "__main__":
    main()

