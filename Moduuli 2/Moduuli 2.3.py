#ensin kysytään tietoja
kanta_srt = input("Anna suorakulmion kanta senttimetreinä:")
korkeus_srt=input("Anna suorakulmion korkeus senttimetreinä:")
#muutetaan tiedot liukuluvuiksi
kanta=float(kanta_srt)
korkeus=float(korkeus_srt)
squared = "\u00b2"
#lasketaan
ala = kanta * korkeus
piiri=kanta*2+korkeus*2
#tulostetaan merkkijonona
print("Suorakulmion pinta-ala on:"+str(ala) +("cm")+squared)
print ("Suorakulmion piiri on: "+str(piiri)+("cm"))