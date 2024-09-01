#tuodaan random ja luodaan d10 noppa joka heittää kerran
import random
noppa= random.randint(1,10)
#ensimmäisen heiton jälkeen tehdään silmukka joka toistaa kunnes arvaus on oikein
arvaus= int(input("Arvaa nopan 1d10 silmäluku:"))
while noppa!=arvaus:
    if arvaus>noppa:
        print("Liian suuri arvaus")
    elif arvaus<noppa:
        print("Liian pieni arvaus")
    arvaus= int(input("Arvaa nopan 1d10 silmäluku:"))
print("Oikein")