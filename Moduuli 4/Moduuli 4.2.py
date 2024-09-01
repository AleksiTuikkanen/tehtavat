#Määritellään tuuma
tuuma=float(input("Anna tuumat: "))
#toistetaan tuuman ollessa yli 0
while tuuma>0:
    sentti=tuuma*2.54
    print(str(sentti)+("cm"))
    #annetaan tuumalle uusi arvo
    tuuma = float(input("Anna tuumat: "))