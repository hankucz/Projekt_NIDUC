import random

def generuj_dane(ilosc_bitow):
    return [random.randint(0, 1) for i in range(0, ilosc_bitow)]      #zwracanie bitów w formie tablicy