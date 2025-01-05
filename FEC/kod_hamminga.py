from typing import List
import numpy as np
import kanaly

# Stałe dla kodu Hamminga(31,26)
BITY_WIADOMOSCI = 0 # Całkowita liczba bitów w wiadomości
BITY_DANYCH = 0      # Liczba bitów danych
BITY_PARZYSTOSCI = BITY_WIADOMOSCI - BITY_DANYCH # Liczba bitów parzystości
BITY_KODU = BITY_DANYCH + BITY_PARZYSTOSCI  # Całkowita liczba bitów w jednym bloku kodowym

# Funkcja kodująca wiadomość przy użyciu kodu Hamminga(7,4)
def koduj(wiadomosc: List[int], n:int  , k:int) -> List[int]:
    BITY_WIADOMOSCI = n
    BITY_DANYCH =k
    while len(wiadomosc) % BITY_DANYCH != 0:
        wiadomosc.append(0)  # Dodajemy 0 na końcu, żeby wiadomość miała odpowiednią długość

    fragmenty_wiadomosci = [wiadomosc[i:i + BITY_DANYCH] for i in range(0, len(wiadomosc), BITY_DANYCH)]

    macierz_przejscia = generowanie_macierz_przejscia(BITY_WIADOMOSCI, BITY_DANYCH)

    wynik = []
    for fragment in fragmenty_wiadomosci:
        fragment_array = fragment
        zakodowany_fragment = [0] * BITY_WIADOMOSCI
        for i in range(BITY_DANYCH):
            for j in range(BITY_WIADOMOSCI):
                zakodowany_fragment[j] += fragment_array[i] * macierz_przejscia[i][j]

        zakodowany_fragment = [bit % 2 for bit in zakodowany_fragment]
        wynik.extend(zakodowany_fragment)

    return wynik

# Funkcja obliczająca syndrom błędu
def syndrom(wiadomosc,n:int, k:int):
    BITY_WIADOMOSCI = n
    BITY_DANYCH = k
    fragmenty_wiadomosci = [wiadomosc[i:i + BITY_WIADOMOSCI] for i in range(0, len(wiadomosc), BITY_WIADOMOSCI)]

    macierz_przejscia = generowanie_macierzy_syndromu(BITY_WIADOMOSCI, BITY_DANYCH)

    wynik = []
    for fragment in fragmenty_wiadomosci:
        fragment_array = list(map(int,fragment))
        syndrom_fragmentu = [0] * BITY_DANYCH
        for i in range(BITY_DANYCH):
            for j in range(BITY_WIADOMOSCI):
                syndrom_fragmentu[i] += fragment_array[j] * macierz_przejscia[i][j]

        syndrom_fragmentu = [x % 2 for x in syndrom_fragmentu]
        wynik.extend(syndrom_fragmentu)

    return wynik

# Funkcja poprawiająca błędy w wiadomości
def popraw(syndrom_bledow, wiadomosc, n:int, k:int):
    BITY_WIADOMOSCI = n
    BITY_DANYCH = k
    fragmenty_wiadomosci = [wiadomosc[i:i + BITY_WIADOMOSCI] for i in range(0, len(wiadomosc), BITY_WIADOMOSCI)]
    fragmenty_syndromu = [syndrom_bledow[i:i + BITY_DANYCH] for i in range(0, len(syndrom_bledow), BITY_DANYCH)]

    macierz_przejscia = generowanie_macierzy_syndromu(BITY_WIADOMOSCI, BITY_DANYCH)

    for x, fragment_syndromu in enumerate(fragmenty_syndromu):
        for y in range(BITY_WIADOMOSCI):
            if all(macierz_przejscia[z][y] == fragment_syndromu[z] for z in range(BITY_DANYCH)):
                fragmenty_wiadomosci[x][y] ^= 1  # Korekta błędu

    return [bit for fragment in fragmenty_wiadomosci for bit in fragment]

# Funkcja dekodująca wiadomość
def dekoduj(wiadomosc: List[int], n:int, k:int) -> List[int]:
    BITY_WIADOMOSCI = n
    BITY_DANYCH = k
    fragmenty_wiadomosci = [wiadomosc[i:i + BITY_WIADOMOSCI] for i in range(0, len(wiadomosc), BITY_WIADOMOSCI)]

    macierz_r = macierz_dekodowania(n, k)

    wynik = []
    for fragment in fragmenty_wiadomosci:
        wynik_fragmentu = np.array(fragment).reshape(-1, 1)
        res_array = np.dot(macierz_r, wynik_fragmentu)
        res_array=[int(x%2)for x in res_array.flatten()]


        wynik.extend(res_array[:k])

    return wynik

def sprawdz_bledy(wiadomosc_po, wiadomosc_przed) -> int:
    if np.array_equal(wiadomosc_po, wiadomosc_przed):
        return 0  # brak błędu
    return 1


def generowanie_macierz_przejscia(n, k):
    if n <= k or n <= 0 or k <= 0:
        raise ValueError("n musi być większe od k")

        # Obliczanie liczby bitów parzystości
    r = n - k

    # Tworzenie macierzy tożsamości dla bitów danych
    I_k = np.eye(k, dtype=int)

    # Tworzenie macierzy parzystości H
    H = []
    for i in range(r):
        row = []
        for j in range(1, n + 1):
            if (j >> i) & 1:
                row.append(1)
            else:
                row.append(0)
        H.append(row)

    # H jest macierzą parzystości (r x n)
    H = np.array(H, dtype=int)

    # Macierz przejścia G dla kodu Hamminga
    G = np.hstack((I_k, H[:, :k].T))  # Łączymy macierz tożsamości z odpowiednią częścią H

    return G


def generowanie_macierzy_syndromu(n, k):
    r = n - k

    # Tworzymy macierz jednostkową (I_k) o wymiarze k x k
    G = np.zeros((k, n), dtype=int)

    # Kolumny odpowiadające bitom danych są jednostkowymi wektorami
    for i in range(k):
        G[i, i] = 1

    # Tworzymy macierz do bitów parzystości
    parity_bits = np.zeros((k, r), dtype=int)
    for i in range(k):
        num = i + 1
        for j in range(r):
            if num % 2 == 1:
                parity_bits[i, j] = 1
            num //= 2

    # Łączymy te dwie macierze, aby uzyskać pełną macierz przejścia
    G[:, k:] = parity_bits

    return G

def macierz_dekodowania(n, k):
    # Tworzymy macierz o wymiarach k x n wypełnioną zerami
    matrix = np.zeros((k, n), dtype=int)

    # Wstawiamy 1 na przekątnej
    for i in range(min(k, n)):
        matrix[i, i] = 1

    return matrix

def simulacja(przypadek,wejscie, n, k):

    zakodowany_hamming = koduj(wejscie, n, k)

    # Symulacja kanału BSC z zastosowaniem korekcji poprzez kod Hamminga(n, k)
    wynik_bsc_hamming = kanaly.BSC(zakodowany_hamming, przypadek['prawdopodobienstwo_BSC']).tolist()

    czy_blad_bsc_hamming = sprawdz_bledy(zakodowany_hamming, wynik_bsc_hamming)

    syndrom_bledu_bsc = syndrom(wynik_bsc_hamming, n, k)
    korygowanie_dane_hamming_bsc = popraw(syndrom_bledu_bsc, wynik_bsc_hamming, n, k)
    dekodowane_dane_hamming_bsc = dekoduj(korygowanie_dane_hamming_bsc, n, k)

    czy_naprawiony_hamming_bsc = sprawdz_bledy(wejscie, dekodowane_dane_hamming_bsc)

    if czy_naprawiony_hamming_bsc == 1:
        czy_naprawiony_hamming_bsc = 0
    else: czy_naprawiony_hamming_bsc = 1


    # Symulacja kanału GE z zastosowaniem korekcji poprzez kod Hamminga(n, k)
    wynik_ge_hamming = kanaly.gilbert_elliott(zakodowany_hamming, przypadek['q'], przypadek['p'])
    print(list(map(int, zakodowany_hamming)))
    print(wynik_ge_hamming)

    czy_blad_ge_hamming = sprawdz_bledy(zakodowany_hamming, wynik_ge_hamming)

    syndrom_bledu_ge = syndrom(wynik_ge_hamming, n, k)
    korygowanie_dane_hamming_ge = popraw(syndrom_bledu_ge, wynik_ge_hamming, n, k)
    dekodowane_dane_hamming_ge = dekoduj(korygowanie_dane_hamming_ge, n, k)

    czy_naprawiony_hamming_ge = sprawdz_bledy(wejscie, dekodowane_dane_hamming_ge)

    if czy_naprawiony_hamming_ge == 1:
        czy_naprawiony_hamming_ge = 0
    else: czy_naprawiony_hamming_ge = 1

    # Wyswietlanie danych po zastosowaniu korekcji przez kod Haminga
    print("*" * 20)
    print(f"Zakodowane dane Hamminga({n}, {k}):", list(map(int, zakodowany_hamming)))

    print("*" * 10)
    print("Symulacja za pomocą kanału BSC: ")
    if czy_blad_bsc_hamming == 1:
        print("Wykryto błąd")
        print("Wiadomość po przejściu przez kod Hamminga i kanał BSC: ", wynik_bsc_hamming)

        if czy_naprawiony_hamming_bsc == 1:
            print("Wiadomość została w pełni poprawiona: ", dekodowane_dane_hamming_bsc)
        else:
            print("Wiadomość nie została w pełni poprawiona: ", dekodowane_dane_hamming_bsc)
    else:
        print("Wiadomość po przejściu przez kod Hamminga i kanał BSC: ", wynik_bsc_hamming)
        print("Nie wykryto błędu w wiadomości: ", dekodowane_dane_hamming_bsc)


    print("*" * 10)
    print()
    print("Symulacja za pomocą kanału GE: ")
    if czy_blad_ge_hamming == 1:
        print("Wykryto błąd")
        print("Wiadomość po przejściu przez kod Hamminga i kanał GE: ", wynik_ge_hamming)

        if czy_naprawiony_hamming_ge == 1:
            print("Wiadomość została w pełni poprawiona: ", dekodowane_dane_hamming_ge)
        else:
            print("Wiadomość nie została w pełni poprawiona: ", dekodowane_dane_hamming_ge)
    else:
        print("Wiadomość po przejściu przez kod Hamminga i kanał GE: ", wynik_ge_hamming)
        print("Nie wykryto błędu w wiadomości: ", dekodowane_dane_hamming_ge)

    return czy_blad_bsc_hamming, czy_naprawiony_hamming_bsc, czy_blad_ge_hamming, czy_naprawiony_hamming_ge