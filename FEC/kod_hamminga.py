
def dodaj_bity_parzystosci(dane):
    """Dodaje bity parzystości do danych wejściowych."""
    n = len(dane)
    r = 0

    while (2 ** r < n + r + 1):                        # Oblicz liczbę bitów parzystości potrzebnych do zakodowania danych
        r += 1

    hamming_code = [0] * (n + r)                       # Tworzenie tablicy z bitami parzystości

    j = 0                                              # Wstawianie danych wejściowych do odpowiednich pozycji w hamming_code
    for i in range(1, n + r + 1):
        if i == 2 ** j:                                # Pozycje bitów parzystości
            j += 1
        else:
            hamming_code[i - 1] = dane[i - j - 1]
    for i in range(r):                                  # Obliczanie bitów parzystości
        parity_pos = 2 ** i
        parity_bit = 0


        for j in range(1, len(hamming_code) + 1):      # Obliczanie bitu parzystości dla pozycji parity_pos
            if (j & parity_pos) == parity_pos:         # Sprawdzenie, czy pozycja jest kontrolowana przez bit parzystości
                parity_bit ^= hamming_code[j - 1]      # Użyj wartości bitu zamiast sumy

        hamming_code[parity_pos - 1] = parity_bit

    return hamming_code


def popraw_bity_hamminga(dane):
    """Poprawia bity w zakodowanych danych przy użyciu kodu Hamminga."""
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
                parity_bit ^= sum(dane[j - 1:j + (parity_pos - 1) * 2 + 1:parity_pos])

        if parity_bit != 0:
            error_position += parity_pos

                                                       # Popraw błąd, jeśli został znaleziony
    if error_position > 0 and error_position <= n:     # Upewnij się, że indeks jest w zakresie
        dane[error_position - 1] ^= 1

    corrected_data = []                                # Usunięcie bitów parzystości i zwrócenie poprawionych danych
    j = 0
    for i in range(1, n + 1):
        if i != (2 ** j):                              # Pomijaj bity parzystości
            corrected_data.append(dane[i - 1])
        else:
            j += 1

    return corrected_data, error_position > 0