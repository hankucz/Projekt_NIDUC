import kanaly
import generator
import korekcja_powielania_bitow
import kod_hamminga
import dane
import numpy as np

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


           # --------------------
           #Gilberta Elliotta
           # --------------------

           # Symulacja kanału G-E
           wynik_g_e = kanaly.gilbert_elliott(dane_wejsciowe, przypadek['q'], przypadek['p'])
           # Symulacja kanału G-E z zastosowaniem korekcji poprzez powielanie
           wynik_g_e_powielanie = kanaly.gilbert_elliott(dane_wejscioewe_powielone, przypadek['q'], przypadek['p'])
           # Korekcja po transmisji przez kanał G-E z zastosowaniem korekcji poprzez powielanie
           wynik_korekcja_g_e_powielanie = korekcja_powielania_bitow.korektor(wynik_g_e_powielanie, przypadek['stopien_powielenia_bitow'])



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
           przypadek['skutecznosc_bsc_powielanie'] = (przypadek['ilosc_bitow'] - licz_ile_zlych_bsc_powielanie) / przypadek['ilosc_bitow']
           print("*"*10)
           print(f"Korekcja przez powielanie w kanele BSC miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_bsc_powielanie}/{przypadek['ilosc_bitow']}")

           # Zliczanie blednych bitow w kanale G-E po korekcji przez powielanie
           licz_ile_zlych_g_e_powielanie = 0
           for i in range(przypadek['ilosc_bitow']):
               if not(dane_wejsciowe[i] == wynik_korekcja_g_e_powielanie[i]):
                   licz_ile_zlych_g_e_powielanie +=1
           przypadek['ile_zlych_g_e_powielanie'] = licz_ile_zlych_g_e_powielanie
           przypadek['skutecznosc_g_e_powielanie'] = (przypadek['ilosc_bitow']-licz_ile_zlych_g_e_powielanie)/przypadek['ilosc_bitow']
           print(f"Korekcja przez powielanie w kanele G-E miała skuteczność: {przypadek['ilosc_bitow']-licz_ile_zlych_g_e_powielanie}/{przypadek['ilosc_bitow']}")




           # --------------------
           #Symulacja dla kodów Hamminga
           #Symulacja dla kodu Hamminga(7,4) ----------------------------------------
           czy_blad_hamming_bsc_7_4, czy_naprawiony_hamming_bsc_7_4, czy_blad_ge_hamming_7_4, czy_naprawiony_hamming_ge_7_4 = kod_hamminga.simulacja(
               przypadek, dane_wejsciowe, 7, 4)

           przypadek['czy_blad_bsc_hamming_7_4'] = czy_blad_hamming_bsc_7_4
           przypadek['czy_naprawiony_hamming_7_4_bsc'] = czy_naprawiony_hamming_bsc_7_4
           przypadek['czy_blad_ge_hamming_7_4'] = czy_blad_ge_hamming_7_4
           przypadek['czy_naprawiony_hamming_ge_7_4'] = czy_naprawiony_hamming_ge_7_4

           # Symulacja dla kodu Hamminga(15,11) ----------------------------------------
           czy_blad_hamming_bsc_15_11, czy_naprawiony_hamming_bsc_15_11, czy_blad_ge_hamming_15_11, czy_naprawiony_hamming_15_11_ge = kod_hamminga.simulacja(przypadek, dane_wejsciowe, 15, 11)

           przypadek['czy_blad_bsc_hamming_15_11'] = czy_blad_hamming_bsc_15_11
           przypadek['czy_naprawiony_hamming_15_11_bsc'] = czy_naprawiony_hamming_bsc_15_11
           przypadek['czy_blad_ge_hamming_15_11'] = czy_blad_ge_hamming_15_11
           przypadek['czy_naprawiony_hamming_15_11_ge'] = czy_naprawiony_hamming_15_11_ge

           # Symulacja dla kodu Hamminga(31,26) ----------------------------------------
           czy_blad_hamming_bsc_31_26, czy_naprawiony_hamming_bsc_31_26, czy_blad_ge_hamming_31_26, czy_naprawiony_hamming_31_26_ge = kod_hamminga.simulacja(przypadek, dane_wejsciowe, 31, 26)

           przypadek['czy_blad_bsc_hamming_31_26'] = czy_blad_hamming_bsc_31_26
           przypadek['czy_naprawiony_hamming_31_26_bsc'] = czy_naprawiony_hamming_bsc_31_26
           przypadek['czy_naprawiony_hamming_31_26_ge'] = czy_naprawiony_hamming_31_26_ge
           przypadek['czy_blad_ge_hamming_31_26'] = czy_blad_ge_hamming_31_26

           # Symulacja dla kodu Hamminga(63,57) ----------------------------------------
           czy_blad_hamming_bsc_63_57, czy_naprawiony_hamming_bsc_63_57, czy_blad_ge_hamming_63_57, czy_naprawiony_hamming_63_57_ge = kod_hamminga.simulacja(przypadek, dane_wejsciowe, 63, 57)

           przypadek['czy_blad_bsc_hamming_63_57'] = czy_blad_hamming_bsc_63_57
           przypadek['czy_naprawiony_hamming_63_57_bsc'] = czy_naprawiony_hamming_bsc_63_57
           przypadek['czy_naprawiony_hamming_63_57_ge'] = czy_naprawiony_hamming_63_57_ge
           przypadek['czy_blad_ge_hamming_63_57'] = czy_blad_ge_hamming_63_57

           # Zapis wartości przypadku do pliku
           plik_wyniki.write('\n')
           for wartosc in przypadek.values():
               plik_wyniki.write(f"{wartosc};")

       # Zamknięcie pliku
       plik_wyniki.close()

if __name__ == "__main__":
    main()