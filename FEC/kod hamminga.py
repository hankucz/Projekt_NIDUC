import numpy as np

from FEC.Generator import generuj_dane
from FEC.kanaly import BSC


def calcRedundantBits(m):
    for i in range(m):  # użycie wzoru 2 ^ r >= m + r + 1
        if (2 ** i >= m + i + 1):
            return i


def posRedundantBits(data, r):  # wstawanie "0" na miejsca o potęgach 2
    j = 0
    k = 0
    m = len(data)
    res = np.zeros(m + r, dtype=int)  # Tablica z miejscami na bity parzystości

    for i in range(m + r):
        if (i + 1 == 2 ** j):  # Jeśli indeks jest potęgą 2, wstawiamy 0
            j += 1
        else:
            res[i] = int(data[k])  # Wstawiamy dane w odpowiednie miejsca
            k += 1

    print("Zmienione dane (z bitami parzystości):", res)  # Debug
    return res


def calcParityBits(arr, r):
    arr = arr[::-1]
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i) == (2 ** i)):  # Jeśli pozycja w zmienionych danych ma 1, to nr pozycji
                val ^= arr[-j]  # Operacja XOR dla odpowiednich bitów

        arr[-(2 ** i)] = val  # Ustawienie bitu parzystości w odpowiedniej pozycji

    arr = arr[::-1]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    # Wykonujemy obliczenia XOR dla wszystkich bitów parzystości
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i)) == (2 ** i):  # Jeśli pozycja w danych ma być sprawdzona
                val ^= arr[-j]              # XOR dla odpowiednich bitów

        res += val * (2 ** i)               # Zbieramy wyniki XOR w reprezentacji binarnej

    return res

data = '1011'
print("Dane wejściowe", data)

m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)  # Działamy na tablicach NumPy

arr = np.array(arr, dtype=int)  # Tablica NumPy, jeśli jeszcze tego nie zrobiliśmy

arr = calcParityBits(arr, r)

print("Data transferred is", arr)

arr = BSC(arr, 0.1)

print("Error Data is", arr)

correction = detectError(arr, r)
if correction == 0:
    print("Nie ma żadnego błędu")
else:
    print("Pozycja błędu jest nr ", len(arr) - correction + 1, "od lewej")