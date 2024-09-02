luvut = [] # Luodaan tyhjä lista
luku=input("Anna luku tai paina enteriä lopettaaksesi: ")
while luku!="": # Jos luku on eri kuin tyhjä toistetaan
    luvut.append(int(luku))
    luku = input("Anna luku tai paina enteriä lopettaaksesi: ")
luvut.sort(reverse=True) # Lajitellaan luvut suurimmasta pienimpään
print(luvut)