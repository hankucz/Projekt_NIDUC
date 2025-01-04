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

            'ilosc_bitow' : random.randint(1, 5),
            'stopien_powielenia_bitow' : random.randint(1, 5),
            'q' : 0.05,
            'p' : round(random.uniform(0.00, 0.99), 2),
            'prawdopodobienstwo_BSC' : round(random.uniform(0.00, 0.99), 2),

            'ile_zlych_bsc_powielanie' : None,
            'ile_zlych_g_e_powielanie' : None,
            'skutecznosc_bsc_powielanie' : None,
            'skutecznosc_g_e_powielanie' : None,

            'czy_blad_bsc_hamming_7_4': None,
            'czy_naprawiony_hamming_7_4_bsc': None,
            'czy_blad_ge_hamming_7_4': None,
            'czy_naprawiony_hamming_ge_7_4': None,

            'czy_blad_bsc_hamming_15_11': None,
            'czy_naprawiony_hamming_15_11_bsc': None,
            'czy_blad_ge_hamming_15_11': None,
            'czy_naprawiony_hamming_15_11_ge': None,

            'czy_naprawiony_hamming_31_26_bsc': None,
            'czy_blad_bsc_hamming_31_26': None,
            'czy_naprawiony_hamming_31_26_ge': None,
            'czy_blad_ge_hamming_31_26': None,

            'czy_blad_bsc_hamming_63_57': None,
            'czy_naprawiony_hamming_63_57_bsc': None,
            'czy_naprawiony_hamming_63_57_ge': None,
            'czy_blad_ge_hamming_63_57': None
        } for i in range(2000)
    ]

    return przypadki