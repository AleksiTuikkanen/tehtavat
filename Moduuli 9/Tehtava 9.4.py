import random
from prettytable import PrettyTable
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):  # parametreiksi vain rekisterinunmero ja huippunopeus
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # Alustetaan kuljettu_matka ja nopeus_nyt nollaksi
        self.kuljettu_matka = 0
        self.nopeus_nyt = 0

    # Luodaan nopeuden muutoksia varten kiihdyta funktio
    def kiihdyta(self, kiihdytys):
        # Jos nopeuden ja kiihdytyksen summa on vähemmän kuin huippunopeus ja nopeus ei laske alle nollan lisätään kiihdytys.
        if (self.nopeus_nyt + kiihdytys < self.huippunopeus) and (self.nopeus_nyt + kiihdytys > 0):
            self.nopeus_nyt += kiihdytys
        # Jos summa olisi yli huippunopeuden nopeus jää huippunopeuteen
        elif self.nopeus_nyt + kiihdytys > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus
        # Muissa tapauksissa nopeus jää 0
        else:
            self.nopeus_nyt = 0
        return self.nopeus_nyt

    # Luodaan kuljetun matkan muuttamiseksi kulje funktio
    def kulje(self, kauan):
        self.kuljettu_matka += kauan * self.nopeus_nyt  # Aika kertaa nopeus kertoo kuljetun matkan, se lisätään kokonaisuuteen
        return self.kuljettu_matka

# Aliohjelma,   jossa luodaan autot kisaa varten
def autotehdas (autojen_maara):
    auto_lista = [] # Tyhjä lista autoille
    for i in range(1,autojen_maara+1):
        rekisteritunnus = "ABC-" + str(i) # Rekisterinumero luodaan vakio-osasta ABC ja järjestysnumerosta
        huippunopeus = random.randint (100,200) # Arvotaan huippunopeus 100 ja 200 välillä
        auto = Auto(rekisteritunnus, huippunopeus) # Luodaan alkiosta olio
        auto_lista.append(auto) # Lisätään alkio listaan
    return auto_lista


autot=(autotehdas(10)) # Kutsutaan aliohjelmaa

kisan_kesto = 0 #
eka_maalissa = False
while not eka_maalissa:
    eka_maalissa = False
    for auto in autot:
        if  auto.kuljettu_matka > 10000:
            eka_maalissa = True
            break
        auto.kiihdyta(random.randint(-10,15))
        auto.kulje(1)
        kisan_kesto += 1

# Taulukon luominen ja tulostaminen
table = PrettyTable()
table.field_names = ["Rekisterinumero", "Huippunopeus (km/h)", "Kuljettu matka (km)", "Nykyinen nopeus (km/h)"]

for auto in autot:
    table.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.kuljettu_matka, auto.nopeus_nyt])

print(table)
print(f"Kisa kesti {kisan_kesto} tuntia.")