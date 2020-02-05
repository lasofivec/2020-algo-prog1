import graph


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
    et (ymin, ymax) verticalement
   """
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x)
    return


# ..............................................................................
# Tests de nos fonctions

# Exemple
graph.ouvre_fenetre(400, 600)
noir(400, 600)
graph.attend_fenetre()

# Question 1
graph.ouvre_fenetre(500, 800)
bande_noire_gauche(500, 800, 100)
graph.attend_fenetre()

# Question 1
graph.ouvre_fenetre(500, 800)
rectangle_noir(500, 800, 50, 200, 150, 450)
graph.attend_fenetre()
