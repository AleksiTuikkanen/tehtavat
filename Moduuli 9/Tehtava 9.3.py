
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


auto1 = Auto("ABC-123",142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

auto1.kulje(1.5)
print(f"{auto1.nopeus_nyt}km/h")

auto1.kiihdyta(-200)

print(f"Auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h."
      f"\nSen kulkema matka on {auto1.kuljettu_matka}km ja tämänhetkinen nopeus on {auto1.nopeus_nyt}km/h.")