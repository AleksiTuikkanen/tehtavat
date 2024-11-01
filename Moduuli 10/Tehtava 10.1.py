class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_alas(self): # metodi jolla mennään yksi kerros alas
        self.nykyinen_kerros -= 1
        print(self.nykyinen_kerros)
        return

    def kerros_ylos(self): # metodi jolla mennään yksi kerros ylös
        self.nykyinen_kerros += 1
        print(self.nykyinen_kerros)
        return

    def siirry_kerrokseen(self, toivottu_kerros):
        # Tarkistetaan onko kerrostoiveet mahdollisia
        if (toivottu_kerros > self.alin_kerros - 1) and (toivottu_kerros < self.ylin_kerros + 1):
            kerros_muutos =  toivottu_kerros - self.nykyinen_kerros # montako kertaa ohjelma pitää kutsua
            if kerros_muutos > 0:
                for i in range(1,kerros_muutos + 1):
                    Hissi.kerros_ylos(self)
            if kerros_muutos < 0:
                for i in range(1, abs(kerros_muutos) + 1): # kerroksen muutoksen itseisarvo antaa oikean määrän kutsuja
                    Hissi.kerros_alas(self)
        else:
            print("Toivottua kerrosta ei ole olemassa tai sinne ei pääse tällä hissillä.")
        return

hissi1 = Hissi(1, 13)

hissi1.siirry_kerrokseen(10)

hissi1.siirry_kerrokseen(1)