"""
Ce module vérifie qu'un nombre est premier dans la fonction secondaire "isprime()" 
et teste cette dernière dans la fonction principale "main()" pour plusieurs nombres.
"""
#### Fonction secondaire


def isprime(p):
    """
    Vérifie que p est un nombre premier.
    """

    # votre code ici
    for i in range(1,p):
        while i != 1 and p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Vérifie le bon fonctionnement de la fonction "isprime()" 
    """

    # vos appels à la fonction secondaire ici

    for n in range(2,100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
