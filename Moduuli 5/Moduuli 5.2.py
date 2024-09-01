luvut = []
luku=input("Anna luku tai paina enteriä lopettaaksesi: ")
while luku!="":#jos luku on eri kuin tyhjä toistetaan
    luvut.append(int(luku))
    luku = input("Anna luku tai paina enteriä lopettaaksesi: ")
luvut.sort(reverse=True)
print(luvut)