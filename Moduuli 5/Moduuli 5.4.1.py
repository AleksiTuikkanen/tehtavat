#Tein tehtävän myös "väärin" eli toteutin saman eri funktioilla

kaupungit = []
kaupunki = input("Anna kaupungin nimi:")
kaupungit.append(kaupunki)
while len(kaupungit) <=4:
    kaupunki = input("Anna kaupungin nimi:")
    kaupungit.append(kaupunki)
print(kaupungit)