#kysytään aluksi kuinka iso kala on
pituus=float(input("Kuinka pitkä kuha on?"))
#nyt jos pituus on liian pieni niin lasketaan paljonko liian pieni
if pituus <=37:
    puuttuva=37-pituus
    print("Kuha on alimittainen, pituudesta puuttuu "+str(puuttuva)+("cm"))

