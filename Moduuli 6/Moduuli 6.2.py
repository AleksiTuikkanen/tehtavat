import random

heitto = 0 # alustetaan heitoille arvo, joka ei ole nopille mahdollinen.

tahko = int(input("Montako tahkoinen noppasi on? "))

def noppa(tahko): # Annetaan noppa-funktiolle parametriksi tahkoje määrä
    heitto = random.randint(1, tahko) # heittojen arvo vaihtelee 1 ja annetun tahkomäärän välillä
    return heitto # noppa-funtio palauttaa heitto arvon

while heitto != tahko:
    heitto = noppa(tahko)
    print(f"{heitto}")