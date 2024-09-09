# Ensin ajattelin näin, mutta se on tosi ruma. :(
vuodenajat = ("talvi", "talvi", "kevät", "kevät","kevät", "kesä", "kesä", "kesä", "syksy","syksy","syksy","talvi")

monesko = int(input("Anna kuukauden järjestysnumero (1-12): "))

kuukausi = vuodenajat[monesko-1]
print(kuukausi)