import math
#ensin kysytään ympyrän sädettä
r_str = input("Anna ympyrän säde senttimetreinä: ")
#muutetaan liukuluvuksi
r = float(r_str)
#lasketaan pinta-ala
ala = (r**2)*math.pi
#potenssiin 2 merkki unicodista
squared = "\u00b2"
#tulostetaan vastaus merkkijonona
print("Ympyrän pinta-ala on: "+str(ala)+("cm")+squared)
