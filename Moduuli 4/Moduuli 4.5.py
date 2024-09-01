käyttäjätunnus = "python"
salasana = "rules"
k_arvaus=input("Anna käyttäjätunnus:")
p_arvaus=input("Anna salasana:")
#toisto tarkistaa onko silmukka mennyt yli viisi kertaa. aluksi arvo 0 ja joka toistossa lisätään siihen 1
toisto=0
#tarkistetaan onko onko salasana TAI käyttäjätunnus väärin JA toistoja on alle 5
while (k_arvaus!=käyttäjätunnus or p_arvaus!=p_arvaus) and toisto<5:
    print("Salasana tai käyttäjätunnus on väärin")
    toisto=toisto+1
    k_arvaus=input("Anna käyttäjätunnus:")
    p_arvaus=input("Anna salasana:")
#silmukan päätyttyä tarkistetaan johtuiko se liian monesta toistosta vai oikeasta syötteestä
if toisto<5:
    print("Tervetuloa!")
else:
    print("Pääsy evätty.")