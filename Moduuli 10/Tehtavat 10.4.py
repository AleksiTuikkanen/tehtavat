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

class Kilpailu:

    def __init__(self, kilpailun_nimi, kilpailu_km, kilpailevat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailu_km = kilpailu_km
        self.kilpailevat_autot = kilpailevat_autot
        self.kisan_kesto = 0

    def tunti_kuluu(self):

        for osallistuja in self.kilpailevat_autot:
            osallistuja.kiihdyta(random.randint(-10, 15))
            osallistuja.kulje(1)
        self.kisan_kesto += 1
        return

    def tulosta_tilanne(self):

        table = PrettyTable()
        table.field_names = ["Rekisterinumero", "Huippunopeus (km/h)", "Kuljettu matka (km)", "Nykyinen nopeus (km/h)"]

        for osallistuja in self.kilpailevat_autot:
            table.add_row([osallistuja.rekisteritunnus, osallistuja.huippunopeus, osallistuja.kuljettu_matka, osallistuja.nopeus_nyt])

        return print(table.get_string(sortby="Kuljettu matka (km)", reversesort=True))

    def kilpailu_ohi(self):
        ohi_on = False
        for osallistuja in self.kilpailevat_autot:
            if osallistuja.kuljettu_matka ==  self.kilpailu_km or osallistuja.kuljettu_matka >= self.kilpailu_km:
                ohi_on = True
        return ohi_on


# Aliohjelma,   jossa luodaan autot kisaa varten
def autotehdas(autojen_maara):
    auto_lista = []  # Tyhjä lista autoille
    for i in range(1, autojen_maara + 1):
        rekisteritunnus = "ABC-" + str(i)  # Rekisterinumero luodaan vakio-osasta ABC ja järjestysnumerosta
        huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus 100 ja 200 välillä
        auto = Auto(rekisteritunnus, huippunopeus)  # Luodaan alkiosta olio
        auto_lista.append(auto)  # Lisätään alkio listaan
    return auto_lista

# Pääohjelma alkaa

autot=(autotehdas(10)) # Kutsutaan aliohjelmaa

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot) # Luodaan kilpailu

while Kilpailu.kilpailu_ohi(kilpailu1) == False:
    Kilpailu.tunti_kuluu(kilpailu1)
    if kilpailu1.kisan_kesto % 10 == 0: # kesto / 10 ei tuota jakojäännöstä ainoastaan K10 välein
        Kilpailu.tulosta_tilanne(kilpailu1)
        print(f"Kilpailu on kestänyt {kilpailu1.kisan_kesto}h.")

if Kilpailu.kilpailu_ohi(kilpailu1) == True:
    kilpailu1.tulosta_tilanne()
    print(f"Kilpailu kesti {kilpailu1.kisan_kesto}h.")