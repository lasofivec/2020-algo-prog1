import graph
def ligne_horiz(y, larg):
    for x in range(larg):
        graph.plot(y, x)

def segment_horiz(y, xmin, xmax):
    for x in range(xmin, xmax):
        graph.plot(y, x)

def rectangle(ymin, ymax, xmin, xmax):
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            graph.plot(y, x)

def rayures_vertic(haut, larg, epaisseur):
    for i in range(1, larg//epaisseur, 2):
        rectangle(0, haut, i*epaisseur, (i+1)*epaisseur)

def damier(haut, larg, cote):
    for j in range(1, haut//cote, 2):
        for i in range(0, larg//cote, 2):
            rectangle(j*cote, (j+1)*cote, i*cote, (i+1)*cote)
    for j in range(0, haut//cote, 2):
        for i in range(1, larg//cote, 2):
            rectangle(j*cote, (j+1)*cote, i*cote, (i+1)*cote)

def sapin(haut, larg):
    graph.ouvre_fenetre(haut, 200)
    print((haut*9)//10)
    for i in range(0, (haut*9)//10):
        debut = larg//2 + 1 - i
        fin = debut + 2*i - 1
        segment_horiz(i, debut, fin)

    rectangle(9*haut//10, haut, larg//2-20,larg//2+20)
    graph.attend_fenetre()


# graph.ouvre_fenetre(120, 160)
# # ligne_horiz(40, 160)
# # segment_horiz(80, 40, 100)
# # rectangle(20,60,40,60)
# # rayures_vertic(120,160,20)
# damier(120,160,20)
# graph.attend_fenetre()

sapin(110, 200)
