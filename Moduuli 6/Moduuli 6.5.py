# Luodaan aliohjelma joka palauttaa listan, johon kuuluu ainoastaan parilliset luvut niistä jotka sille syötetään
def parittomat(luvut):
    pari_lista = [] # Luodaan tyhjä lista parillisille
    for luku in luvut: # Käydään annettu lista läpi alkio alkiolta
        if luku % 2 == 0: # Jos kahdella jakamisesta ei jää jakojäännöstä kyseessä on parillinen luku
            pari_lista.append(luku) # lisätään ne luvut jotka olivat parillisia listaan
    return pari_lista # Palautetaan lista parillisia lukuja

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Lista ilman parittomia: {parittomat(lista)}")
print(f"Alkuperäinen lista: {lista}")
