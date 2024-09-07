import random

heitto = 0 # alustetaan heitoille arvo, joka on eri kuin 6, tämä ensin

# luodaan aliohjelma joka arpoo satunnaisen numeron 1 ja 6 väliltä ja palauttaa sen arvon.
def noppa(): # neljäs
    heitto = random.randint(1, 6) # viides
    return heitto # kuudes

while heitto != 6: # jos heitto ei ole 6 niin toistetaan. toinen.
    heitto = noppa() # heitto = noppa kutsuu aliohjelmaa sillä siinä tarvitaan sen arvo. kolmas
    print(f"{heitto}") # seitsemäs, jonka jälkeen while silmukka toistaa vaiheita 2.-7.