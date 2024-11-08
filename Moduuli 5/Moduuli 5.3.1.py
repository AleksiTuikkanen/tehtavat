def is_prime(luku):
    if luku == 1:
        print("1 ei ole alkuluku")
        return False
    elif luku == 2:
        print(f"{luku} on alkuluku")
        return True
    elif luku % 2 == 0:
        print(f"{luku} ei ole alkuluku")
        print(f"Se on jaollinen ainakin tällä luvulla: 2")
        return False
    else:
        jakaja = 3 # Määritellään jakajaksi 3
        while luku % jakaja !=0 and jakaja != luku: # Niin kauan kuin jakojäännös ei ole 0 JA jakaja ei ole sama kuin luku
            jakaja += 2 # lisätään jakajaan 2
        if jakaja == luku: # Jos toistorakenne sulkeutuu siksi, että jakaja on sama kuin luku kyseessä on alkuluku
            print(f"{luku} on alkuluku.")
            return True
        else: # Jos toistorakenne sulkeutuu siksi, että jakojäännös oli 0 niin kyseessä ei ole alkuluku
            print(f"{luku} ei ole alkuluku.")
            print(f"{luku} on jaollinen ainakin tällä luvulla: {jakaja}")
            return False