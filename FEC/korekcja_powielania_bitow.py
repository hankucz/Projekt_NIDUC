def powielanie(dane, poziom_powielania):
    dane_powielone = []
    for x in dane:
        for _ in range(0,poziom_powielania):
            dane_powielone.append(x)
    return dane_powielone

def korektor(dane, poziom_powielenia):
    skorygowane_dane = []
    for i in range(0, len(dane), poziom_powielenia):
        suma_bitow = sum(dane[i:i+poziom_powielenia])
        if suma_bitow/poziom_powielenia < 0.5:
            skorygowane_dane.append(0)
        else:
            skorygowane_dane.append(1)
    return skorygowane_dane