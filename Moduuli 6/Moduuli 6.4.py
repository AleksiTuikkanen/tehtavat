# Luodaan aliohjelma joka saa arvoksi luvut (nimi on vain määrittelyä varten)
def summaaja(luvut):
    summa = 0 # alustetaan summa-arvo 0
    for luku in luvut: # käydään läpi jokainen listan "luvut" alkio, jotka on nimetty nimellä "luku".
        summa += luku # Lisätään alkio yksi kerrallaan summaan
    return summa

lista = [4, 19, 9090, 2]

summaaja(lista) # Annetaan aliohjelmalle parametriksi lista (aiemman parametrin "luvut" sijaan)
print(summaaja(lista))