
def dodaj_bity_parzystosci(dane):
    """Dodaje bity parzystości do danych wejściowych."""
    n = len(dane)
    r = 0

    while (2 ** r < n + r + 1):                        # Oblicz liczbę bitów parzystości potrzebnych do zakodowania danych
        r += 1

    hamming_code = [0] * (n + r)                       # Tworzenie tablicy z bitami parzystości

    j = 0                                              # Wstawianie danych wejściowych do odpowiednich pozycji w hamming_code
    for i in range( len(hamming_code), 0, -1):
        if (i & (i - 1) == 0):                                # Pozycje bitów parzystości
            continue
        else:
            hamming_code[i - 1] = dane[j]
            j += 1

    for i in range(r):                                  # Obliczanie bitów parzystości
        parity_pos = 2 ** i
        parity_bit = 0


        for j in range(1, len(hamming_code) + 1):      # Obliczanie bitu parzystości dla pozycji parity_pos
            if (j & parity_pos) == parity_pos:         # Sprawdzenie, czy pozycja jest kontrolowana przez bit parzystości
                parity_bit ^= hamming_code[j - 1]      # Użyj wartości bitu zamiast sumy

        hamming_code[parity_pos - 1] = parity_bit

    return hamming_code[::-1]


def popraw_bity_hamminga(dane):
    """Poprawia bity w zakodowanych danych przy użyciu kodu Hamminga."""
    dane = dane[::-1]
    n = len(dane)
    r = 0

    while (2 ** r < n + 1):                            # Oblicz liczbę bitów parzystości
        r += 1

    error_position = 0

    for i in range(r):                                 # Sprawdzenie bitów parzystości
        parity_pos = 2 ** i
        parity_bit = 0
        for j in range(1, n + 1):
            if (j & parity_pos) == parity_pos:         # Sprawdzenie pozycji kontrolowanej przez bit parzystości
                parity_bit ^= dane[j - 1]

        if parity_bit != 0:
            error_position += parity_pos

    if 0 < error_position <= n:
        dane[error_position - 1] ^= 1
                                                       # Popraw błąd, jeśli został znaleziony

    corrected_data = []                                # Usunięcie bitów parzystości i zwrócenie poprawionych danych
    corrected_data = corrected_data[::-1]
    j = 0
    for i in range(1, n + 1):
        if i != (2 ** j):                              # Pomijaj bity parzystości
            corrected_data.append(dane[i - 1])
        else:
            j += 1

    return corrected_data[::-1], 1 if error_position else 0