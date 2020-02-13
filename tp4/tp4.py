########################################
#          Partie numero 1
########################################

def fonctions_partie1():
    print("\n######################################")
    print("                Partie 1")
    print("######################################")

    # question 1
    print("\n------------- question 1 ------------------")
    lst=[5,0,50,200]
    print("Liste avant boucle for : ", lst)
    for i in range(len(lst)):
        lst[i] *= 2
    print("Liste apres boucle for : ", lst)

    # question 2
    print("\n------------- question 2 ------------------")
    li = []
    for ele in range(1, 100):
        if ele % 2 == 0 or ele % 3 == 0:
            li.append(ele)
    print("10 premiers entiers (<100) divisibles par 2 ou 3 : ",
          li[:10])

    # question 3
    print("\n------------- question 3 ------------------")
    print(">>> premiere version")
    lst=[5,0,50,200]
    lst2 = lst[:]
    for i in range(len(lst)):
        lst2[i] *= 2
    print("Liste lst : ", lst)
    print("Liste lst2 : ", lst2)

    print(">>> deuxieme version")
    lst=[5,0,50,200]
    lst2 = []
    for ele in lst:
        lst2.append(2 * ele)
    print("Liste lst : ", lst)
    print("Liste lst2 : ", lst2)

    # question 4
    print("\n------------- question 4 ------------------")
    y = 5
    x = -3
    print("Pixels voisins de ", y, x, " : ", pixels_voisins(y, x))

def pixels_voisins(y, x):
    """
    Calcul les 4 voisins du point aux coordonnees (y,x)
    Retourne les voisins a droite gauche bas haut
    """
    vecteur = [(0,1), (0,-1), (1,0), (-1,0)]
    voisins = []
    for v in vecteur:
        voisins.append((v[0] + y, v[1] + x))
    return voisins


########################################
#          Partie numero 2
########################################
import graph


def fonctions_partie2():
    print("\n######################################")
    print("                Partie 2")
    print("######################################")

    # question 1
    print("\n------------- question 1 ------------------")
    lst = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
    print("largeur de l'image : ", largeur_image(lst, 20))

    import time

    # strategie 1
    print("\n------------- strategie 1 ------------------")
    dessine_bandes1(lst, 50, 20)
    graph.attend_fenetre()

    # strategie 2
    print("\n------------- strategie 2 ------------------")
    dessine_bandes2(lst, 50, 20)
    graph.attend_fenetre()

    # Temps de calcul
    start_time = time.time()
    dessine_bandes1(lst, 50, 20)
    print("Temps premiere strategie = ", time.time() - start_time)
    graph.fengra.ferme()
    graph.fengra = None
    start_time = time.time()
    dessine_bandes2(lst, 50, 20)
    print("Temps deuxieme strategie = ", time.time() - start_time)
    graph.fengra.ferme()
    graph.fengra = None


def largeur_image(lst, largeur_bande):
    """
    Calcul la largeur de l'image composee de bandes de largeur
    largeur_bande, noires ou blanches definies par lst
    """
    return len(lst)*largeur_bande


def num_bande(x, y, largeur_bande):
    return x // largeur_bande


def dessine_bandes1(lst, hauteur, largeur_bandes):
    largeur = largeur_image(lst, largeur_bandes)
    graph.ouvre_fenetre(hauteur, largeur)

    # parcour pixels
    for y in range(hauteur):
        for x in range(largeur):
            nb = num_bande(x, y, largeur_bandes)
            if lst[nb] == 0:
                graph.plot(y,x)

    #graph.attend_fenetre()
    return


def rectangle(ymin, ymax, xmin, xmax):
    """
    Colorie un rectangle noir compris entre (xmin, xmax) horizontalement
    et (ymin, ymax) verticalement (fond blanc)
   """
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x)
    return


def dessine_bandes2(lst, hauteur, largeur_bandes):
    largeur = largeur_image(lst, largeur_bandes)
    graph.ouvre_fenetre(hauteur, largeur)

    # parcours bandes
    for i in range(len(lst)):
        if lst[i] == 0:
            rectangle(0, hauteur, largeur_bandes*i, largeur_bandes*(i+1))

    #graph.attend_fenetre()
    return


########################################
#          Partie numero 3
########################################
def fonctions_partie3():
    print("\n######################################")
    print("                Partie 3")
    print("######################################")

    lstlst = [[0, 1, 1, 0, 1, 1, 1, 0],
              [1, 0, 0, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1, 1, 0],
              [1, 1, 0, 0, 0, 1, 0, 1]]

    # question 1
    print("\n------------- question 1 ------------------")
    print("Nombre de lignes de lstlst : ", nb_lignes(lstlst))

    # question 2
    print("\n------------- question 2 ------------------")
    print("Nombre de lignes de lstlst : ", nb_colonnes(lstlst))

    # question 3
    print("\n------------- question 3 ------------------")
    print("Nombre de lignes de lstlst : ", taille_image(lstlst, 40))

    # question 4
    print("\n------------- question 4 ------------------")
    dessine_grille(lstlst, 40)
    graph.attend_fenetre()

def nb_lignes(liste_de_liste):
    return len(liste_de_liste)


def nb_colonnes(liste_de_liste):
    return len(liste_de_liste[0])


def taille_image(lstlst, taille):
    nl = nb_lignes(lstlst)
    nc = nb_colonnes(lstlst)
    hauteur = nl * taille
    largeur = nc * taille
    return hauteur, largeur

def dessine_grille(lstlst, taille):
    h, l = taille_image(lstlst, taille)
    graph.ouvre_fenetre(h, l)

    nl = nb_lignes(lstlst)
    nc = nb_colonnes(lstlst)
    for il in range(nl):
        ligne = lstlst[il]
        for ic in range(nc):
            if ligne[ic] == 0:
                rectangle(taille*il, taille*(il+1), taille*ic, taille*(ic+1))


########################################
#                 MAIN
########################################
if __name__ == "__main__":

    # Appel aux fonctions de la premiere partie
    fonctions_partie1()

    # Appel aux fonctions de la 2e partie
    # fonctions_partie2()

    # Appel aux fonctions de la 3e partie
    fonctions_partie3()
