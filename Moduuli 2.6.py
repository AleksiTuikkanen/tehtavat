import random
# Arvotaan koodi, jossa numerot ovat välillä 0–9
#luodaan koodi johon lisätään 3 numeroa
code1 =""
code1 += str(random.randint(0, 9))
code1 += str(random.randint(0, 9))
code1 += str(random.randint(0, 9))
# Arvotaan nelinumeroinen koodi, jossa numerot ovat välillä 1–6
code2 = ""
#sama funktio pitää tehdä 4 kertaa, ja se on helpompi toteuttaa for _ in funktiolla (vaatii sisennyksen)
for _ in range(4):
    code2 += str(random.randint(1, 6))

# Tulostetaan koodit
print(f"Kolmenumeroinen koodi: {code1}")
print(f"Nelinumeroinen koodi: {code2}")

