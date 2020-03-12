import Labyrinthe
import random


# -- Question 1 ----------------------------------------------------------------
# .. 1.1 Fonction indice .......................................................
def indice(lst, n):
    """
    Fonction indice qui, a partir d’une liste d’entiers lst et d’un
    entier n retourne None si aucun element de lst ne vaut n.
    Dans le cas contraire, l’entier retourne est l’indice du premier element de
    lst qui vaut n.
    """
    indx = None  # si n n'est pas dans la liste on retourne None
    for ii in range(len(lst)):  # on parcourt toute la liste
        if lst[ii] == n:
            indx = ii
            return indx  # pas besoin de continuer
    return indx


# .. Test de la fonction `indice` ..............................................
# Creation d'une liste de 20 elements au hasard entre 0 et 10
lst_tst = []
for ii in range(20):
    lst_tst.append(random.randint(0, 10))
# On choisit un nombre au hasard entre 0 et 10 a trouver
num = random.randint(0, 10)

print("* Question 1.1 *")
print("  Liste de 20 chiffres au hasard entre 0 et 10:\n   ", lst_tst)
print("  Le chiffre ", num, " apparait pour la premiere fois a l'indice: ",
      indice(lst_tst, num))
# Tourner plusieurs fois ce code pour effectuer plusieurs tests.................


# .. 1.2 Fonction coord ........................................................
def coord(mat, n):
    """
    fonction coord qui, a partir d’une liste de listes d’entiers, laby, et d’un
    entier n retourne None si aucun des entiers de laby ne vaut n.
    Dans le cas contraire, la valeur retournee est un couple d’entiers
    representant les coordonnees de l’element valant n
    """
    indi = None
    indj = None
    for ii in range(len(mat)):
        for jj in range(len(mat[ii])):
            if mat[ii][jj] == n:
                indi = ii
                indj = jj
                return indi, indj
    return indi, indj


# .. Test exemple de l'enonce ..................................................
lab_test = [[1, 2, 3], [4, 5, 6]]
print("")  # pour sauter une ligne, purement esthetique
print("* Question 1.2 *")
print("  Coordonnees de 3 dans lab_test = ", coord(lab_test, 3),
      " (ca devrait etre egale a (0, 2))")


# .. 1.3 Entree et sortie ......................................................
def entree(laby):
    return coord(laby, 2)


def sortie(laby):
    return coord(laby, 3)


# .. Test donne par l'enonce ...................................................
laby1 = [[0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 2, 0, 1, 1, 3, 0],
         [0, 0, 0, 0, 0, 0, 0]]
print("")
print("* Question 1.3 *")
print("  Entree du labyrinthe test =", entree(laby1), ".")
print("  Sortie du labyrinthe test =", sortie(laby1), ".")

# Creation d'un labyrinthe de taille 15x18
laby2 = Labyrinthe.creer(15, 18)
print("")
print("  Labyrinthe aleatoire 15x18 :")
for ligne in laby2:
    print("  ", ligne)
print("  Entree du labyrinthe aleatoire = ", entree(laby2))
print("  Entree du labyrinthe aleatoire = ", sortie(laby2))


# -- Question 2 ----------------------------------------------------------------
# .. 2.1 Taille labyrinthe .....................................................
# Fonctions du TP4:
def get_nb_lignes(liste_de_liste):
    return len(liste_de_liste)


def get_nb_colonnes(liste_de_liste):
    return len(liste_de_liste[0])


def taille_laby(laby):
    return get_nb_lignes(laby), get_nb_colonnes(laby)


print("")
print("* Question 2.1 *")
print("  Nombre de lignes et colonnes du laby aleatoire:", taille_laby(laby2))

print("")
print("* Question 2.2 *")
print("  Nombre de lignes et colonnes du laby enonce:", taille_laby(laby1))


# .. 2.3 Voisins labyrinthe ....................................................
def estDedans(coords, nb_lignes, nb_colonnes):
    if 0 <= coords[0] < nb_lignes and 0 <= coords[1] < nb_colonnes:
        return True
    return False


def voisins_laby_fin(lgn, col, nb_lignes, nb_colonnes):
    deplacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    liste_voisins = []
    for i in range(4):
        voisin = (lgn + deplacements[i][0], col + deplacements[i][1])
        if estDedans(voisin, nb_lignes, nb_colonnes):
            liste_voisins += [voisin]
    return liste_voisins


nbl, nbc = taille_laby(laby2)
print("")
print("* Question 2.3 *")
print("  Voisins milieu (3, 3)  =", voisins_laby_fin(3, 3, nbl, nbc))
print("  Voisins coin   (0, 0)  =", voisins_laby_fin(0, 0, nbl, nbc))
print("  Voisins bords (14, 10) =", voisins_laby_fin(14, 10, nbl, nbc))


# .. 2.4 Voisins accessibles ...................................................
def voisins_laby_acc_1(lgn, col, laby):
    nbl, nbc = taille_laby(laby)
    liste_voisins = voisins_laby_fin(lgn, col, nbl, nbc)
    voisins_acc = []
    for v in liste_voisins:
        if laby[v[0]][v[1]] != 0:
            voisins_acc.append(v)
    return voisins_acc


def voisins_laby_acc(coords, laby):
    return voisins_laby_acc_1(coords[0], coords[1], laby)


print("")
print("* Question 2.4 + 2.5 *")
print("  Voisins accessibles de (1,5) dans laby :",
      voisins_laby_acc((1, 5), laby1))

