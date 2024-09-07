import math # piin arvoa varten
# Syötetään pizzojen koot ja hinnat
pizza1 = float(input("Anna ensimmäisen pizzan halkaisija metreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: " ))
pizza2 = float(input("Anna toisen pizzan halkaisija metreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: " ))

# Luodaan aliohjelma joka laskee pizzan pinta-alan A=πr2 ja jaetaan hinta sillä
def pizza_ala(pizza_halkaisija, hinta):
    pizza_r = pizza_halkaisija / 2
    a = math.pi * pizza_r ** 2 # A on pizzan pinta-ala
    hinta_per_ala = hinta / a
    return hinta_per_ala

# Tulostetaan eri pizzojen hinnat per neliömetri.
print(f"Ensimmäinen pizzan hinta per neliömetri on {pizza_ala(pizza1, hinta1): .2f}")
print(f"Toisen pizzan hinta per neliömetri on {pizza_ala(pizza2, hinta2): .2f}")

# Verrataan eri parametrien pinta-aloja.
if pizza_ala(pizza1, hinta1) <= pizza_ala(pizza2, hinta2):
    print("Ensimmäinen pizza on halvempi")
elif pizza_ala(pizza1, hinta1) >= pizza_ala(pizza2, hinta2):
    print("toinen pizza on halvempi")
else:
    print("Pizzat ovat saman hintaisia.")