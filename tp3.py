import random


def sapin_decore(hauteur):
    """
    Creation d'un sapin compose de `*` decore de `O`.
    Les decorations apparaissent avec une probabilité de 20%
    au lieu des branches *
    """
    for ind_ligne in range(hauteur - 1):
        # la ligne consiste d'abord en espaces vides
        ligne_sapin = (hauteur - 2 - ind_ligne)*" "
        # puis soit de boules soit de branches
        for etoile in range(2*ind_ligne-1):
            if random.random() <= 0.2:
                # On affiche une decoration avec 20% de chance
                ligne_sapin += "0"
            else:
                # sinon une branche normale
                ligne_sapin += "*"
        print(ligne_sapin)
    print()
    return


# On affiche notre sapin decore :
print("******* Bonnes fetes **********")
sapin_decore(11)


def myst():
    """
    Cette fonction choisi au hasard un nombre entre 0 et 99.
    L'utilisateur doit le deviner, le programme lui indique
    si le nombre qu'ielle a choisi est trop grand ou trop petit
    """
    nombre_myst = int(random.random()*100)
    nombre_util = -1
    print("===========================================")
    print("        Bienvenue au jeu Mystere !! ")
    print("===========================================")
    print("L'ordinateur a choisi un nombre entre 0 et 99.")
    print("A vous de le trouver !\n")
    while not nombre_myst == nombre_util:
        nombre_util = int(input("Choissisez un nombre entre 0 et 99 : "))
        if nombre_util > nombre_myst:
            print("Trop grand !")
        if nombre_util < nombre_myst:
            print("Trop petit !")
    print("\n        Felicitations !! Vous avez trouve le bon nombre ")
    return


myst()
