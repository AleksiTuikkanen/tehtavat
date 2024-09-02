#Tein tehtävän myös "väärin" eli toteutin saman eri funktioilla

luku = int(input("Anna kokonaisluku:"))
jakaja = 1 # Määritellään jakajaksi 1
while luku % jakaja !=0 and jakaja == luku: # Niin kauan kuin jakojäännös ei ole 0 JA jakaja ei ole sama kuin luku
    jakaja += 1 # lisätään jakajaan 1
if jakaja == luku: # Jos toistorakenne sulkeutuu siksi, että jakaja on sama kuin luku kyseessä on alkuluku
    print(f"{luku} on alkuluku.")
else: # Jos toistorakenne sulkeutuu siksi, että jakojäännös oli 0 niin kyseessä ei ole alkuluku
    print(f"{luku} ei ole alkuluku.")