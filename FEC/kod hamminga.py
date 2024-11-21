import numpy as np

from FEC.generator import generuj_dane
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

    print("Zmienione dane (z bitami parzystości '0'):", res)  # Debug
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

def detectError(arr, after_BSC, nr):
    n = len(arr)
    res = 0

    # Wykonujemy obliczenia XOR dla wszystkich bitów parzystości
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i)) == (2 ** i):  # Jeśli pozycja w danych ma być sprawdzona
                # Porównanie bitów w arr i after_BSC
                if arr[-j] != after_BSC[-j]:
                    val = 1  # Bit różni się, ustawiamy wynik XOR na 1
        res += val * (2 ** i)  # Zbieramy wyniki XOR w reprezentacji binarnej

    return res

data = generuj_dane(4)
data = np.array(data)
print("Dane wejściowe", data)

m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)

arr = np.array(arr, dtype=int)

arr = calcParityBits(arr, r)

print("Dane po przejściu przez kod Hamminga", arr)

after_BSC = BSC(arr, 0.2)
print("Dane po przejściu przez kanał BSC", after_BSC)

correction = detectError(arr, after_BSC, r)
if correction == 0:
    print("Nie ma żadnego błędu")
elif correction > len(arr):
    print("Błędów jest więcej niż 1")
else:
    print("Pozycja błędu jest nr ", len(arr) - correction + 1, "od lewej, ", correction)