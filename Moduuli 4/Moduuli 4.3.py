#määritellään aloituksen luku
luku=input("Anna luku tai paina enteriä lopettaaksesi: ")
#määritellään pienin ja suurin aloituksen luvuksi
suurin=luku
pienin=luku
#jos luku on eri kuin tyhjä toistetaan
while luku!="":
    #uusi määritelmä luvulle, jonka jälkeen testataan onko se suurempi tai pienempi kuin aiemmin annetut
    luku = input("Anna luku: ")
    if luku>suurin:
        suurin=luku
    #pienin tarvitsee lisäfunktion, jotta tyhjä ei tulkittaisi pienimmäksi
    if luku<pienin and luku!="":
        pienin=luku
print("suurin luku on: "+str(suurin))
print("pienin luku on: "+str(pienin))