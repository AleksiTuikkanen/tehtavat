import random
summa = 0
noppaluku=int(input("Kuinka montaa arpakuutiota haluat heittää?:"))
for _ in range(noppaluku): #_ tarkoittaa ettei kyseistä arvoa tarvita/ haluta käyttää
    noppa =random.randint(1, 6)
    summa += noppa
print(f"Silmälukujen summa on: {summa}")
