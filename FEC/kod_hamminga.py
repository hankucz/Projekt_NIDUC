
def dodaj_bity_parzystosci(dane):
    """Dodaje bity parzystości do danych wejściowych."""
    n = len(dane)
    r = 0

    # Oblicz liczbę bitów parzystości potrzebnych do zakodowania danych
    while (2 ** r < n + r + 1):
        r += 1

    # Tworzenie tablicy z bitami parzystości
    hamming_code = [0] * (n + r)

    # Wstawianie danych wejściowych do odpowiednich pozycji w hamming_code
    j = 0
    for i in range(1, n + r + 1):
        if i == 2 ** j:  # Pozycje bitów parzystości
            j += 1
        else:
            hamming_code[i - 1] = dane[i - j - 1]

    # Obliczanie bitów parzystości
    for i in range(r):
        parity_pos = 2 ** i
        parity_bit = 0

        # Obliczanie bitu parzystości dla pozycji parity_pos
        for j in range(1, len(hamming_code) + 1):
            if (j & parity_pos) == parity_pos:  # Sprawdzenie, czy pozycja jest kontrolowana przez bit parzystości
                parity_bit ^= hamming_code[j - 1]  # Użyj wartości bitu zamiast sumy

        hamming_code[parity_pos - 1] = parity_bit

    return hamming_code


def popraw_bity_hamminga(dane):
    """Poprawia bity w zakodowanych danych przy użyciu kodu Hamminga."""
    n = len(dane)
    r = 0

    # Oblicz liczbę bitów parzystości
    while (2 ** r < n + 1):
        r += 1

    error_position = 0

    # Sprawdzenie bitów parzystości
    for i in range(r):
        parity_pos = 2 ** i
        parity_bit = 0
        for j in range(1, n + 1):
            if (j & parity_pos) == parity_pos:  # Sprawdzenie pozycji kontrolowanej przez bit parzystości
                parity_bit ^= sum(dane[j - 1:j + (parity_pos - 1) * 2 + 1:parity_pos])

        if parity_bit != 0:
            error_position += parity_pos

    # Popraw błąd, jeśli został znaleziony
    if error_position > 0 and error_position <= n:  # Upewnij się, że indeks jest w zakresie
        dane[error_position - 1] ^= 1

    # Usunięcie bitów parzystości i zwrócenie poprawionych danych
    corrected_data = []
    j = 0
    for i in range(1, n + 1):
        if i != (2 ** j):  # Pomijaj bity parzystości
            corrected_data.append(dane[i - 1])
        else:
            j += 1

    return corrected_data, error_position > 0