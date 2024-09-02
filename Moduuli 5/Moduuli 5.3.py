luku = int(input("Anna kokonaisluku: "))
tekijöitä = 0 # Aloitetaan 0 tekijällä
# Käydään läpi kaikki luvut välillä 2 ja luku-1
for i in range(2, luku, 1):
    if luku % i == 0:
        tekijöitä += 1  # Kasvatetaan tekijöiden määrää
# Jos tekijöitä on tasan 1, luku on alkuluku
if tekijöitä == 0:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")