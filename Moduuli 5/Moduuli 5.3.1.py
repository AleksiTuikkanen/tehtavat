#Tein tehtävän myös "väärin" eli toteutin saman eri funktioilla

luku = int(input("Anna kokonaisluku:"))
jakaja = luku-1 # Määritellään jakajaksi luku joka on 1 pienempi kuin annettu luku
while luku % jakaja !=0 and jakaja !=1: # Niin kauan kuin jakojäännös ei ole 0 ja jakaja ei ole 1 jatketaan
    jakaja -= 1 # Vähennetään jakajasta 1
if jakaja == 1: # Jos toistorakenne sulkeutuu siksi, että jakaja on 1 niin kyseessä on alkuluku
    print(f"{luku} on alkuluku.")
else: # Jos toistorakenne sulkeutuu siksi, että jakojäännös oli 0 niin kyseessä ei ole alkuluku
    print(f"{luku} ei ole alkuluku.")