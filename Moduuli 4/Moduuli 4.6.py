import random
# Kysytään käyttäjältä arvottavien pisteiden määrä
N = int(input("Anna arvottavien pisteiden määrä: "))
# Alustetaan muuttujat
n = 0  # ympyrän sisälle osuvat pisteet
i = 0  # laskuri toistojen määrää varten
# Arvotaan N pistettä neliön sisällä
while i < N:
    x = random.uniform(-1, 1)  # Arvotaan x-koordinaatti välillä -1 ja 1
    y = random.uniform(-1, 1)  # Arvotaan y-koordinaatti välillä -1 ja 1
    # Testataan, jääkö piste (x, y) yksikköympyrän sisään
    if x * x + y * y < 1:
        n += 1  # Jos piste on ympyrän sisällä, kasvatetaan n-arvoa yhdellä
    # Kasvatetaan laskuria yhdellä
    i += 1
# Lasketaan piin likiarvo kaavalla π ≈ 4n/N
pi_likiarvo = 4 * n / N
# Tulostetaan piin likiarvo
print(f"Piin likiarvo arvottujen pisteiden perusteella on noin: {pi_likiarvo:.6f}")