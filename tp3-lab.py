import graph
import math
import random


def noir(haut, larg):
    """
    Creation d'une fenetre __noire__ 400x600
    """
    for y in range(haut):  # parcourt les lignes y
        for x in range(larg):  # parcourt les colonnes x
            graph.plot(y, x)
    return


def bande_noire_gauche(haut, larg, larg_bande):
    """
    Colorie une bande noire de largeur larg_band a gauche de la fenetre
    """
    for y in range(haut):
        for x in range(larg):
            if x < larg_bande:
                graph.plot(y, x)
    return


def rectangle_noir(haut, larg, ymin, ymax, xmin, xmax):
    """
    Colorie un rectangle noir compris entre (xmin, xmax) horizontalement
    et (ymin, ymax) verticalement (fond blanc)
   """
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x)
    return


def rectangle_blanc(haut, larg, ymin, ymax, xmin, xmax):
    """
    Colorie un rectangle blanc compris entre (xmin, xmax) horizontalement
    et (ymin, ymax) verticalement sur fond noir
   """
    for y in range(haut):
        for x in range(larg):
            if not (x >= xmin and x < xmax
                    and y >= ymin and y < ymax):
                graph.plot(y, x)
    return


def numero_bande(x, larg_bande):
    """
    Trouver le numero de la bande sur lequel se trouve x
    si le graph est compose de bandes verticales et que
    elles sont numerotees de 0, au N. Avec N = numero de
    bandes total.
    """
    return int(x / larg_bande)


def bande_est_noire(nv):
    """
    Determine si une bande est noire ou blanche a partir de
    son numero
    """
    return nv % 2 == 1


def rayures_verticales_naif(hauteur, largeur, larg_bande):
    """
    Dessine des rayures verticales de largeur larg_bande
    alternant blanc et noir sur une fenetre de taille
    hauteur x largeur.
    Il n'y a aucune condition necessaire pour larg_bande.

    **Algorithme naif**
    """
    for x in range(largeur):
        if bande_est_noire(numero_bande(x, larg_bande)):
            for y in range(hauteur):
                graph.plot(y, x)
    return


def rayures_verticales(hauteur, largeur, larg_bande):
    """
    Dessine des rayures verticales de largeur larg_bande
    alternant blanc et noir sur une fenetre de taille
    hauteur x largeur.
    Il n'y a aucune condition necessaire pour larg_bande
    """
    # on calcule le nombre de bandes total
    nb_total_bandes = math.ceil(largeur / larg_bande)

    # on dessine les bandes (<=> rectangles) NOIRES
    for ind in range(1, nb_total_bandes, 2):
        rectangle_noir(hauteur, largeur, 0, hauteur,
                       larg_bande*ind, min(larg_bande*ind + larg_bande,
                                           largeur))

    return


def numero_case(x, y, cote):
    """
    Trouver le numero de la case du pixel (x,y)
    si le graph est en forme de damier noir et blanc et que
    les cases sont numerotees par leur numero vertical et horizontal
    en commencant par 0
    """
    nv = int(x / cote)
    nh = int(y / cote)
    return nv, nh


def case_est_noire(nv, nh):
    """
    Determine si une case est noire ou blanche a partir de
    ses numeros nv et nh
    """
    return (nv % 2 == 1 and nh % 2 == 0) or (nv % 2 == 0 and nh % 2 == 1)


def damier_naif(hauteur, largeur, cote):
    """
    Dessine un damier de case carees de largeur cote
    alternant blanc et noir sur une fenetre de taille
    hauteur x largeur.
    Il n'y a aucune condition necessaire pour cote et la premiere case
    est blanche.

    **Algorithme naif**
    """
    for x in range(largeur):
        for y in range(hauteur):
            nv, nh = numero_case(x, y, cote)
            if case_est_noire(nv, nh):
                graph.plot(y, x)
    return


def damier(hauteur, largeur, cote):
    """
    Dessine un damier de case carees de largeur cote
    alternant blanc et noir sur une fenetre de taille
    hauteur x largeur.
    Il n'y a aucune condition necessaire pour cote et la premiere case
    est blanche.
    """
    # on calcule le nombre cases horizontal
    nb_hor = math.ceil(largeur / cote)
    # on calcule le nombre cases vertical
    nb_ver = math.ceil(hauteur / cote)

    # on dessine les cases (<=> rectangles) NOIRES
    for indv in range(nb_ver):
        for indh in range(nb_hor):
            if case_est_noire(indv, indh):
                rectangle_noir(hauteur, largeur,
                               indv*cote, min(indv*cote+cote, hauteur),
                               indh*cote, min(indh*cote+cote, largeur))

    return


def rectangle_random(haut, larg, ymin, ymax, xmin, xmax):
    """
    Colorie un rectangle de couleur aleatoire compris entre (xmin, xmax)
    horizontalement et (ymin, ymax) verticalement (fond blanc)
    """
    couleurs = ["black", "white", "red", "green", "blue", "yellow",
                "cyan", "magenta", "orange", "darkgrey"]
    # on choisit une couleur au hasard
    c = couleurs[int(random.random()*len(couleurs))]
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x, c)
    return


def damier_colore(hauteur, largeur, cote):
    """
    Dessine un damier colore de case carees de largeur cote
    alternant blanc et noir sur une fenetre de taille
    hauteur x largeur.
    Il n'y a aucune condition necessaire pour cote et la premiere case
    est blanche.
    """
    # on calcule le nombre cases horizontal
    nb_hor = math.ceil(largeur / cote)
    # on calcule le nombre cases vertical
    nb_ver = math.ceil(hauteur / cote)

    # on dessine les cases (<=> rectangles) NOIRES
    for indv in range(nb_ver):
        for indh in range(nb_hor):
            if case_est_noire(indv, indh):
                rectangle_random(hauteur, largeur,
                                 indv*cote, min(indv*cote+cote, hauteur),
                                 indh*cote, min(indh*cote+cote, largeur))

    return


# ..............................................................................
# Tests de nos fonctions
if __name__ == "__main__":

    print(" ==== TP3 ex 3 ====")
    print(" Questions: ")
    print("    0. fentre noire")
    print("    1. bande noire a gauche")
    print("    2. rectangle noir sur blanc")
    print("    3. rectangle blanc sur noir")
    print("    4. numero bande")
    print("    5. condition noire")
    print("    6. rayures verticales")
    print("    7. damier")
    print("    8. damier colore")
    print("  100. Tout afficher")
    print("")
    reponse = int(input("Choisissez quelle reponse voir : "))
    print("")

    if reponse == 0 or reponse == 100:
        # Exemple
        graph.ouvre_fenetre(400, 600)
        noir(400, 600)
        graph.attend_fenetre()
    if reponse == 1 or reponse == 100:
        # Question 1
        graph.ouvre_fenetre(500, 800)
        bande_noire_gauche(500, 800, 100)
        graph.attend_fenetre()
    if reponse == 2 or reponse == 100:
        # Question 2
        graph.ouvre_fenetre(500, 800)
        rectangle_noir(500, 800, 50, 200, 150, 450)
        graph.attend_fenetre()
    if reponse == 3 or reponse == 100:
        # Question 3
        graph.ouvre_fenetre(500, 800)
        rectangle_blanc(500, 800, 50, 200, 150, 450)
        graph.attend_fenetre()
    if reponse == 4 or reponse == 100:
        # Question 4
        print("Quelques exemples:")
        for ii in range(5):
            x = random.random() * 20  # nombre entre 0 et 20
            larg_bande = random.random() * 5 + 1  # nombre entre 1 et 6
            nb = numero_bande(x, larg_bande)
            print(str(x) + " se trouve a la " + str(nb) + "e bande de largeur"
                  + str(larg_bande))
        print()
    if reponse == 5 or reponse == 100:
        print("Le numero de bande doit etre impair :)")
        print("")
    if reponse == 6 or reponse == 100:
        graph.ouvre_fenetre(500, 800)
        # rayures_verticales(500, 800, 150)
        rayures_verticales_naif(500, 800, 150)
        graph.attend_fenetre()
    if reponse == 7 or reponse == 100:
        graph.ouvre_fenetre(500, 800)
        # damier_naif(500, 800, 75)
        damier(500, 800, 75)
        graph.attend_fenetre()
    if reponse == 8 or reponse == 100:
        graph.ouvre_fenetre(500, 800)
        damier_colore(500, 800, 75)
        graph.attend_fenetre()

    if reponse < 0 or (reponse > 8 and not reponse == 100):
        print("Mauvais choix. Bye bye")
