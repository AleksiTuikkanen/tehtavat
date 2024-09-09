nimi = input("Syötä nimi tai paina enter lopettaaksesi:") # Syötetään 1. nimi

nimet = set() # Luodaan tyhjä joukko

while nimi !="": # Niin kauan kuin nimi ei ole tyhjä niin toistetaan
    # Tarkistetaan onko nimi jo joukossa
    if nimi not in nimet:
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")
    nimet.add(nimi) # Lisätään nimi joukkoon
    nimi = input("Syötä nimi tai paina enter lopettaaksesi:") # Kysytään uusi nimi

print(nimet)