# Määritellään monikko jonka alkioina on vuodenaikojen nimet ja niiden kk järjestysnumerot jotka niihin kuuluu.
vuodenajat = ("talvi",(12,1,2)), ("kevät",(3,4,5)), ("kesä",(6,7,8)), ("syksy",(9,10,11))

monesko = int(input("Anna kuukauden järjestysnumero (1-12): ")) # Kysytään kuukauden järjestysnumeroa
# Käydään monikko-vuodenajat läpi alkio alkiolta
for vuodenaika, kuukaudet in vuodenajat: # Kaksi muuttujaa viittavaat mini-monikkoihin "vuodenajat"-monikon sisällä
    if monesko in kuukaudet: # Jos "monesko" on alkion minialkiossa
        print(f"Vuoden {monesko}. kuukausi on {vuodenaika}kuukausi")
        break