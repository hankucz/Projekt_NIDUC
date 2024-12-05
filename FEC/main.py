import numpy as np

import kanaly
import generator
import korekcja_powielania_bitow
import kod_hamminga
import dane

def main():

    # Import przypadków testowych
    przypadki = dane.przypadki()

    # Przygotowanie pliku wyjściowego z wynikami
    plik_wyniki = open("wyjscie.csv", "w")

    # Zapis nagłówków do pliku z wynikami
    for klucz in przypadki[0]:
        plik_wyniki.write(f"{klucz};")

    # Iteracja przez przypadki
    for przypadek in przypadki:

        print('\n' + '-'*20)
        print(przypadek['opis'])
        print('-'*20 + '\n')

        # Generowanie losowych bitów uzytych potem do obydwu modeli
        dane_wejsciowe = generator.generuj_dane(przypadek['ilosc_bitow'])

        #Powielanie danych
        dane_wejscioewe_powielone = korekcja_powielania_bitow.powielanie(dane_wejsciowe, przypadek['stopien_powielenia_bitow'])

        # --------------------
        #BSC
        # --------------------
         
        # Symulacja kanału BSC
        wynik_bsc = kanaly.BSC(dane_wejsciowe, przypadek['prawdopodobienstwo_BSC'])
        # Symulacja kanału BSC z zastosowaniem korekcji poprzez powielanie
        wynik_bsc_powielanie = kanaly.BSC(dane_wejscioewe_powielone, przypadek['prawdopodobienstwo_BSC'])
        # Korekcja po transmisji przez kanał BSC z zastosowaniem korekcji poprzez powielanie
        wynik_korekcja_bsc_powielanie = korekcja_powielania_bitow.korektor(wynik_bsc_powielanie, przypadek['stopien_powielenia_bitow'])

        # Symulacja kanału BSC z zastosowaniem korekcji poprzez kod Hamminga
        zakodowany_hamming = kod_hamminga.dodaj_bity_parzystosci(dane_wejsciowe)
        wynik_bsc_hamming = kanaly.BSC(zakodowany_hamming, przypadek['prawdopodobienstwo_BSC'])
        (skorygowane_dane_hamming_bsc, przypadek['czy_blad_bsc_hamming']) = kod_hamminga.popraw_bity_hamminga(wynik_bsc_hamming)
        skorygowane_dane_hamming_bsc = np.array(skorygowane_dane_hamming_bsc)
        
        
        # --------------------
        #Gilberta Elliotta
        # --------------------

        # Symulacja kanału G-E
        wynik_g_e = kanaly.gilbert_elliott(dane_wejsciowe, przypadek['q'], przypadek['p'])
        # Symulacja kanału G-E z zastosowaniem korekcji poprzez powielanie
        wynik_g_e_powielanie = kanaly.gilbert_elliott(dane_wejscioewe_powielone, przypadek['q'], przypadek['p']) 
        # Korekcja po transmisji przez kanał G-E z zastosowaniem korekcji poprzez powielanie
        wynik_korekcja_g_e_powielanie = korekcja_powielania_bitow.korektor(wynik_g_e_powielanie, przypadek['stopien_powielenia_bitow'])

        # Symulacja kanału G-E z zastosowaniem korekcji poprzez kod Hamminga
        wynik_g_e_hamming = kanaly.gilbert_elliott(zakodowany_hamming, przypadek['q'], przypadek['p']) 
        (skorygowane_dane_hamming_ge, przypadek['czy_blad_ge_hamming']) = kod_hamminga.popraw_bity_hamminga(wynik_g_e_hamming)
        skorygowane_dane_hamming_ge = np.array(skorygowane_dane_hamming_ge)


        # --------------------
        # Wyświetlenie przebiegu i wyników symulacji
        # --------------------

        # Wyswietalnie danych wejsciowych
        print("Dane wejściowe:", dane_wejsciowe)                     
        print("Dane po przejściu przez kanał BSC:", wynik_bsc)
        print("Dane po przejściu przez kanał Gilberta Elliotta:", wynik_g_e)
        
        # --------------------
        
        # Wyswietlanie danych po zastosowaniu korekcji przez powielanie bitow
        print("*"*20)
        print("Dane po przejściu przez kanał BSC z zastosowanym powieleniem:", wynik_bsc_powielanie)
        print("Dane po przejściu przez kanał Gilberta Elliotta z zastosowanym powieleniem:", wynik_g_e_powielanie)
        print("Skorygowane dane po BSC (powielanie): ", wynik_korekcja_bsc_powielanie)
        print("Skorygowane dane po G-E (powielanie): ", wynik_korekcja_g_e_powielanie)

        #Zliczanie blednych bitow w kanale BSC po korekcji przez powielanie
        licz_ile_zlych_bsc_powielanie = 0
        for i in range(przypadek['ilosc_bitow']):
            if not(dane_wejsciowe[i] == wynik_korekcja_bsc_powielanie[i]):
                licz_ile_zlych_bsc_powielanie +=1
        przypadek['ile_zlych_bsc_powielanie'] = licz_ile_zlych_bsc_powielanie
        
        print("*"*10)
        print(f"Korekcja przez powielanie w kanele BSC miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_bsc_powielanie}/{przypadek['ilosc_bitow']}")
        
        # Zliczanie blednych bitow w kanale G-E po korekcji przez powielanie
        licz_ile_zlych_g_e_powielanie = 0
        for i in range(przypadek['ilosc_bitow']):
            if not(dane_wejsciowe[i] == wynik_korekcja_g_e_powielanie[i]):
                licz_ile_zlych_g_e_powielanie +=1
        przypadek['ile_zlych_g_e_powielanie'] = licz_ile_zlych_g_e_powielanie
        print(f"Korekcja przez powielanie w kanele G-E miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_g_e_powielanie}/{przypadek['ilosc_bitow']}")

        # --------------------

        # Wyswietlanie danych po zastosowaniu korekcji przez kod Haminga
        print("*"*20)
        print("Zakodowane dane Hamminga:", zakodowany_hamming)

        print("Dane po przejściu przez kanał BSC (Hamming):", wynik_bsc_hamming)
        print("Dane po przejściu przez kanał G-E (Hamming):", wynik_g_e_hamming)

        print("*"*10)
        # Weryfikacja czy korekta się udała
        if przypadek['czy_blad_bsc_hamming']:
            print("Błąd w kanale BSC został wykryty i poprawiony.")
        # Zliczanie blednych bitow w kanale BSC po korekcji kodem Hamminga
        licz_ile_zlych_bsc_hamming = 0
        for i in range(przypadek['ilosc_bitow']):
            if not(dane_wejsciowe[i] == wynik_bsc_hamming[i]):
                licz_ile_zlych_bsc_hamming +=1
        przypadek['ile_zlych_bsc_hamming'] = licz_ile_zlych_bsc_hamming

        print(f"Korekcja kodem Hamminga w kanele BSC miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_bsc_hamming}/{przypadek['ilosc_bitow']}")

        print("Skorygowane dane po BSC (Hamming):", skorygowane_dane_hamming_bsc)

        print("*"*10)
        # Weryfikacja czy korekta się udała
        if przypadek['czy_blad_ge_hamming']:
            print("Błąd w kanale G-E został wykryty i poprawiony.")
        # Zliczanie blednych bitow w kanale G-E po korekcji kodem Hamminga
        licz_ile_zlych_g_e_hamming = 0
        for i in range(przypadek['ilosc_bitow']):
            if not(dane_wejsciowe[i] == wynik_g_e_hamming[i]):
                licz_ile_zlych_g_e_hamming +=1
        przypadek['ile_zlych_g_e_hamming'] = licz_ile_zlych_g_e_hamming
        print(f"Korekcja kodem Hamminga w kanele G-E miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_g_e_hamming}/{przypadek['ilosc_bitow']}")

        print("Skorygowane dane po G-E (Hamming):", skorygowane_dane_hamming_ge)

        # Zapis wartości przypadku do pliku
        plik_wyniki.write('\n')
        for wartosc in przypadek.values():
            plik_wyniki.write(f"{wartosc};")
    
    # Zamknięcie pliku
    plik_wyniki.close()

if __name__ == "__main__":
    main()

