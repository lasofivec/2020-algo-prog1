import graph
import math


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


def bande_est_noire(numero_bande):
    """
    Determine si une bande est noire ou blanche a partir de
    son numero
    """
    return numero_bande % 2 == 1


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
                       larg_bande*ind, min(larg_bande*ind + larg_bande, largeur))

    return

# ..............................................................................
# Tests de nos fonctions

if __name__=="__main__":

    print(" ==== TP3 ex 3 ====")
    print(" Questions: ")
    print("    0. fentre noire")
    print("    1. bande noire a gauche")
    print("    2. rectangle noir sur blanc")
    print("    3. rectangle blanc sur noir")
    print("    4. numero bande")
    print("    5. condition noire")
    print("    6. rayures verticales")
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
        print("2.5 se trouve a la " + str(numero_bande(2.5, 2)) + "e bande de grosseur 2")
        print("0.5 se trouve a la " + str(numero_bande(0.5, 2)) + "e bande de grosseur 2")
        print("5.1 se trouve a la " + str(numero_bande(5.1, 2)) + "e bande de grosseur 2")
    if reponse == 5 or reponse == 100:
        print("Le numero de bande doit etre impair :)")
    if reponse == 6 or reponse == 100:
        graph.ouvre_fenetre(500, 800)
        rayures_verticales(500, 800, 150)
        graph.attend_fenetre()
    if reponse < 0 or (reponse > 6 and not reponse == 100):
        print("Mauvais choix. Bye bye")
