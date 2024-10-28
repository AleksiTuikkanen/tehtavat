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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__ (self,rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ABC-123", 165, 32.3)
Auto.kiihdyta(auto1,100)
Auto.kiihdyta(auto2,101)
Auto.kulje(auto1,3)
Auto.kulje(auto2,3)
print(auto1.kuljettu_matka)
print(auto2.kuljettu_matka)