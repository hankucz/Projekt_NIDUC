import random

def przypadki():
    
    # Ustalanie danych wejsciowych
    # ilosc_bitow : Ustalanie ilości bitów w danych wejsciowych
    # stopien_powielenia_bitow : Ustalenie ile razy dany bit zostanie powielony
    # q : Prawdopodobieństwo przejścia ze stanu dobrego do stanu złego
    # p : Prawdopodobieństwo przejścia ze stanu złego do stanu dobrego
    # prawdopodobienstwo_BSC : Prawdopodobieństwo z jakim bit zostanie zmieniony na przeciwny
    
    # Ustalanie danych pomiarowych
    # 'ile_zlych_bsc_powielanie' : Ilość błędnie skorygowanych bitów po przejściu przez kanał BSC i korekcji przez powielanie
    # 'ile_zlych_g_e_powielanie' : Ilość błędnie skorygowanych bitów po przejściu przez kanał G-E i korekcji przez powielanie
    # 'ile_zlych_bsc_hamming' : Ilość błędnie skorygowanych bitów po przejściu przez kanał BSC i korekcji kodem Hamminga
    # 'ile_zlych_g_e_hamming' : Ilość błędnie skorygowanych bitów po przejściu przez kanał G-E i korekcji kodem Hamminga
    # 'czy_blad_bsc_hamming' : Zmienna 0/1 czy bity uległy korekcji po przejściu przez kanał BSC i korekcji kodem Hamminga
    # 'czy_blad_ge_hamming' : Zmienna 0/1 czy bity uległy korekcji po przejściu przez kanał G-E i korekcji kodem Hamminga

    przypadki = [ 
        # {
        #     'opis': 'Przypadek 1',
        #     'id_przypadku' : 1, 

        #     'ilosc_bitow' : 4, 
        #     'stopien_powielenia_bitow' : 15, 
        #     'q' : 0.5, 
        #     'p' : 0.5,
        #     'prawdopodobienstwo_BSC' : 0.15,

        #     'ile_zlych_bsc_powielanie' : None,
        #     'ile_zlych_g_e_powielanie' : None,
        #     'ile_zlych_bsc_hamming' : None,
        #     'ile_zlych_g_e_hamming' : None,
        #     'czy_blad_bsc_hamming' : None,
        #     'czy_blad_ge_hamming' : None,
        # },
        
        # Losowe przypadki
        {
            'opis': f'Przypadek {i+1}', 
            'id_przypadku' : (i+1),
            
            'ilosc_bitow' : random.randint(1, 150), 
            'stopien_powielenia_bitow' : random.randint(1, 50), 
            'q' : round(random.uniform(0.01, 0.99), 2), 
            'p' : round(random.uniform(0.01, 0.99), 2),
            'prawdopodobienstwo_BSC' : round(random.uniform(0.01, 0.99), 2),

            'ile_zlych_bsc_powielanie' : None,
            'ile_zlych_g_e_powielanie' : None,
            'ile_zlych_bsc_hamming' : None,
            'ile_zlych_g_e_hamming' : None,
            'czy_blad_bsc_hamming' : None,
            'czy_blad_ge_hamming' : None,
        } for i in range(1500)
    ]

    return przypadki