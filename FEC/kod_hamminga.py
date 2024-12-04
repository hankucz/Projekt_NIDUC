
def dodaj_bity_parzystosci(dane):
    """Dodaje bity parzystości do danych wejściowych."""
    n = len(dane)
    r = 0

    while (2 ** r < n + r + 1):                        # Oblicz liczbę bitów parzystości potrzebnych do zakodowania danych
        r += 1

    kod_hamminga = [0] * (n + r)                       # Tworzenie tablicy z bitami parzystości

    indeks_danych = 0                                              # Wstawianie danych wejściowych do odpowiednich pozycji w kod_hamminga
    for i in range( len(kod_hamminga), 0, -1):
        if (i & (i - 1) == 0):                                # Pozycje bitów parzystości
            continue
        else:
            kod_hamminga[i - 1] = dane[indeks_danych]
            indeks_danych += 1

    for i in range(r):                                  # Obliczanie bitów parzystości
        pozycja_parzystosci = 2 ** i
        bit_parzystosci = 0


        for j in range(1, len(kod_hamminga) + 1):      # Obliczanie bitu parzystości dla pozycji pozycja_parzystosci
            if (j & pozycja_parzystosci) == pozycja_parzystosci:         # Sprawdzenie, czy pozycja jest kontrolowana przez bit parzystości
                bit_parzystosci ^= kod_hamminga[j - 1]      # Użyj wartości bitu zamiast sumy

        kod_hamminga[pozycja_parzystosci - 1] = bit_parzystosci

    return kod_hamminga[::-1]


def popraw_bity_hamminga(dane):
    """Poprawia bity w zakodowanych danych przy użyciu kodu Hamminga."""
    dane = dane[::-1]
    n = len(dane)
    r = 0

    while (2 ** r < n + 1):                            # Oblicz liczbę bitów parzystości
        r += 1

    pozycja_bledu = 0

    for i in range(r):                                 # Sprawdzenie bitów parzystości
        pozycja_parzystosci = 2 ** i
        bit_parzystości = 0
        for j in range(1, n + 1):
            if (j & pozycja_parzystosci) == pozycja_parzystosci:         # Sprawdzenie pozycji kontrolowanej przez bit parzystości
                bit_parzystości ^= dane[j - 1]

        if bit_parzystości != 0:
            pozycja_bledu += pozycja_parzystosci

    if 0 < pozycja_bledu <= n:
        dane[pozycja_bledu - 1] ^= 1
                                                       # Popraw błąd, jeśli został znaleziony

    poprawione_dane = []                                # Usunięcie bitów parzystości i zwrócenie poprawionych danych
    indeks_parzystosci = 0
    for i in range(1, n + 1):
        if i != (2 ** indeks_parzystosci):                              # Pomijaj bity parzystości
            poprawione_dane.append(dane[i - 1])
        else:
            indeks_parzystosci += 1

    return poprawione_dane[::-1], 1 if pozycja_bledu else 0