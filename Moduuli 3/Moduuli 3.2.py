#kysyy mikä hyttiluokka, onko LUX,A,B vai C
hyttiluokka=input("Mikä hyttiluokkanne on?:")
#jos se on joku näistä niin printtaa
if hyttiluokka=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C":
    print("C on ikkunaton hytti autokannen alapuolella.")
#jos jotain muuta niin
else:
    print("Virheellinen hyttiluokka")