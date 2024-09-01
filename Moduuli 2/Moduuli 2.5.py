leiviskä_srt=input("Anna leiviskät:")
naula_srt=input("Anna naulat:")
luoti_srt=input("Anna luodit:")
leiviskä=float(leiviskä_srt)
naula=float(naula_srt)
luoti=float(luoti_srt)
#lasketaan montako grammaa kaikki on yhteensä.
gramma=((((leiviskä*20)+naula)*32)+luoti)*13.3
#tarkistetaan onko vastaus sama samoilla arvoilla kuin githubin esimerkissä
print("Paino on grammoina:"+str(gramma)+("g"))
kilogrammat=(gramma//1000)
grammajäännös=(gramma%1000)
print("Paino on nyky-yksiköissä:"+str(kilogrammat)+("kg")+(" ja ")+str(grammajäännös)+("g"))
#muotoillaan kahden desimaalin tarkkuudelle
print((f"Paino on nyky-yksiköissä:{kilogrammat:.2f}kg ja {grammajäännös:.2f}g"))