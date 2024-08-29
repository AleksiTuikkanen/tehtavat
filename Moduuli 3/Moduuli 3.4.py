#mikä vuosi inputiksi
vuosi=int(input("Anna vuosiluku: "))
#jaetaan vuosi 4
jako=vuosi/4
#jaetaan vuosi 4 josta jää vain kokonaisluvut
jakokokonais=vuosi//4
#jos 4:llä jakamisesta jää jäännöstä niin kyseessä ei ole karkausvuosi
tarkistus=jako-jakokokonais
if tarkistus!=0:
    print("Vuosi ei ole karkausvuosi")
#jos kyseessä on vuosi joka on jaollinen 100:lla JA ei jaollinen 400:lla vuosi ei ole karkausvuosi
elif vuosi/100-vuosi//100==0 and vuosi/400-vuosi//400!=0:
    print("Vuosi ei ole karkausvuosi")
else:
    print("Vuosi on karkausvuosi")