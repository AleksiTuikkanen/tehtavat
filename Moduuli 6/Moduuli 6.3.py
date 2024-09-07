galloona = float(input("Kuinka monta yhdysvaltalaista galloonaa? "))

def litroiksi (galloona):
    litra = galloona * 3.785
    return litra

while galloona > 0:
    print(f"Joka on litroissa {litroiksi(galloona):.2f}l")
    galloona = float(input("Kuinka monta yhdysvaltalaista galloonaa? "))

print("Ohjelma loppunut, syötit negatiivisen arvon.")