lentokentat = {} # Luodaan kirjasto lentokentille ja koodeille

# Kysytään mitä halutaan tehdä

teko = input("Lisätäksesi uuden lentoaseman syötä 'uusi', \nhakeaksesi lentoasemaa syötä 'haku' \ntai paina enter lopettaaksesi: ")

while teko != "": # While silmukka niin kauan kunnes syöte on tyhjä

    if teko == "uusi": # Jos valittiin uuden syöttö niin kysytään ensin ICAO ja kentän nimi sitten lisätään kirjastoon
        icao = input("Syötä lentokentän ICAO-koodi: ")
        lentokentan_nimi = input("Syötä lentokentän nimi: ")
        lentokentat[icao] = lentokentan_nimi

    elif teko == "haku": # Jos valittiin haku niin kysytään koodia
        haku = input("Syötä lentokentän ICAO-koodi: ")
        if haku in lentokentat: # Jos 'avain'-koodi on kirjastossa niin tulostetaan sen nimi
            print(f"Antamasi ICAO-koodi viittaa lentokenttään nimeltä {lentokentat[haku]}.")
        else: # Jos 'avain'-koodia ei löydy kirjastosta niin tulostetaan ettei sitä löydy.
            print("Antamaasi ICAO-koodia ei ole kirjastossa.")

    # Lopuksi toistetaan alkuperäinen kysymys silmukan sisällä ja aloitetaan alusta
    teko = input("Lisätäksesi uuden lentoaseman syötä 'uusi', \nhakeaksesi lentoasemaa syötä 'haku' \ntai paina enter lopettaaksesi: ")

print("Ohjelma lopetettu.") # Kun syötteeksi tulee tyhjä niin while silmukka sulkeutuu ja ohjelma loppuu.