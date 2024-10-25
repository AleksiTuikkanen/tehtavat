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

# Luokka talo-olioiden luontia varten
class Talo:
    def __init__(self,alin_kerros, ylin_kerros, hissien_maara):
    # Aluksi luokka luo halutun määrän hissiejä käyttäen aiempaa hissi luokkaa
        hissit = []
        for hissi_alkio in range(1, hissien_maara + 1):
            hissi_alkio = Hissi(alin_kerros, ylin_kerros)
            hissit.append(hissi_alkio)

        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = hissit # luodut hissit tallennetaan ominaisuutena

    # Metodi, jolla tietty hissi siirtyy kutsumalla Hissi-luokan siirry_kerrokseen metodia
    def aja_hissia(self, hissin_numero, toivottu_kerros):
        hissin_numero = self.hissit[hissin_numero]
        Hissi.siirry_kerrokseen(hissin_numero,toivottu_kerros)
        return

    def palohalytys(self):
        hissin_numero=0
        for hissi in self.hissit:
            Talo.aja_hissia(self,hissin_numero,self.alin_kerros)
            hissin_numero+=1
        print("PII! PII! PALOHÄLYTYS! PII! PII!")
        return

talo1 = Talo(1,13,5) # hissien numero on 0-4
talo1.aja_hissia(2,5)
talo1.aja_hissia(4,7)
talo1.aja_hissia(0,3)
Talo.palohalytys(talo1)