#ensin luodaan inputit sukupuolelle ja hemoglobiinille
suku=input("Mikä sukupuolesi on?(mies/nainen): ")
#pakotetaan valitsemaan jompikumpi
if suku!="mies" and suku != "nainen":
    print("virhesyöte, kirjoita joko mies tai nainen")
hemo=int(input("Mikä on hemoglobiiniarvosi?: "))
#jos mies ja arvot ovat alle, yli tai sisällä sekä oikeat printit
if suku=="mies"and hemo<=134:
    print("hemoglobiinisi on alhainen")
if suku=="mies" and hemo>=195:
    print("Hemoglobiinisi on korkea")
#hemoglobiiniarvojen pitää olla sekä yli 134 että alle 195
if suku=="mies" and (hemo>=134 and hemo<=195):
    print("Hemoglobiinisi on normaali")
#jos nainen ja arvot ovat alle, yli tai sisällä sekä oikeat printit
if suku=="nainen"and hemo<=117:
    print("hemoglobiinisi on alhainen")
elif suku=="nainen" and hemo>=175:
    print("Hemoglobiinisi on korkea")
else:
    print("Hemoglobiinisi on normaali")
