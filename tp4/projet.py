import Labyrinthe
import graph
# importation des fonctions definies dans les parties 1 a 3 du TP4
import tp4

# -- Question 1 ----------------------------------------------------------------
laby = Labyrinthe.creer(11,15)
for ligne in laby:
    print(ligne)


# -- Question 2 ----------------------------------------------------------------
taille_carre = 20
tp4.dessine_grille(laby, taille_carre)
graph.attend_fenetre()


# -- Question 3 ----------------------------------------------------------------
def entree(laby):
    """
    Cette fonction calcule l'indice de la ligne et de la conne
    de la liste de listes laby qui contiennent un 2.
    S'il n'y en a pas, elle retourne None et affiche un message d'erreur
    """
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == 2:
                return i, j # pas besoin de continuer, on renvoit le resultat
    print("Erreur: pas de 2 dans la liste de listes laby. \n laby = \n ", laby)
    return None

def sortie(laby):
    """
    Cette fonction calcule l'indice de la ligne et de la conne
    de la liste de listes laby qui contiennent un 3.
    S'il n'y en a pas, elle retourne None et affiche un message d'erreur
    """
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == 3:
                return i, j # pas besoin de continuer, on renvoit le resultat
    print("Erreur: pas de 3 dans la liste de listes laby. \n laby = \n ", laby)
    return None

print("La case contenant 2 se trouve a la position: ", entree(laby))
print("La case contenant 3 se trouve a la position: ", sortie(laby))

# -- Question 4 ----------------------------------------------------------------
def color_rectangle(ymin, ymax, xmin, xmax, c):
    """
    Colorie un rectangle de couleur c compris entre (xmin, xmax) horizontalement
    et (ymin, ymax) verticalement (fond blanc)
    """
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x, couleur=c)
    return

def dessine_labyrinthe(laby, taille):
    """
    Dessine un labyrinthe avec son entree en bleu et sa sortie en rouge
    """
    # On dessine toute la grille (avec l'entree et la sortie en noire)
    tp4.dessine_grille(laby, taille)

    # puis on dessine par dessus l'entree en bleu
    je, ie = entree(laby)
    color_rectangle(je*taille, (je+1)*taille, ie*taille, (ie+1)*taille, "blue")

    # puis on dessine par dessus la sortie en rouge
    je, ie = sortie(laby)
    color_rectangle(je*taille, (je+1)*taille, ie*taille, (ie+1)*taille, "red")
    return

dessine_labyrinthe(laby, 20)
graph.attend_fenetre()
