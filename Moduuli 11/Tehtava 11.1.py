class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__ (self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Kirjan {self.nimi} kirjoittaja on {self.kirjoittaja} ja siinä on {self.sivumaara}"
              f" sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Lehden {self.nimi} päätoimittaja on {self.paatoimittaja}")

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

Lehti.tulosta_tiedot(lehti1)
Kirja.tulosta_tiedot(kirja1)
