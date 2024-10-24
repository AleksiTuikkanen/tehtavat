class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus): # parametreiksi vain rekisterinunmero ja huippunopeus
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0
auto1 = Auto("ABC-123",142)

print(f"Auton rekisterinumero on {auto1.rekisteritunnus}, huippunopeus {auto1.huippunopeus}."
      f"\nSen kulkema matka on {auto1.kuljettu_matka}km ja tämänhetkinen nopeus on {auto1.nopeus_nyt}km/h.")
