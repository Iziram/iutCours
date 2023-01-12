#  -*- coding: utf-8 -*-
"""
THEORIE des GRAPHES
TP3 : Parcours en largeur
NOM PRENOM : HARTMANN Matthias
DATE : 03/01/2023
"""


import numpy as np


# Graphe Question 1 TP3
M1 = np.array(
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]
)


def chemin_arbre_rec(Pred: list, x: int) -> int:
    # Renvoie le chemin de la racine à x à partir du tableau PRED
    # Version récursive (correction du TP précédent)
    T = []
    if Pred[x] != -1:
        T = chemin_arbre_rec(Pred, Pred[x]) + [x]
    else:
        T = [x]
    return T


# Renvoie les successeurs d'un sommet à partir de la matrice d'adjacence
# par ordre croissant si ordre=1, par ordre décroissant si ordre=0
def successeurs(M, x: int, ordre: int) -> list:
    ligne = M[x]

    sucs: list[int] = [i for i, val in enumerate(ligne) if val]

    if not ordre:
        sucs.reverse()

    return sucs


assert successeurs(M1, 7, 1) == [2, 3, 4]
assert successeurs(M1, 7, 0) == [4, 3, 2]


def largeur(M, r: int, ordre: int) -> list:

    file = []
    marque = [0 for _ in range(len(M))]

    file.append(r)
    marque[r] = 1

    pred = [None for _ in range(len(M))]

    pred[r] = -1

    while len(file) > 0:
        noeud = file[0]
        file.remove(noeud)
        for suc in successeurs(M, noeud, ordre):
            if not marque[suc]:
                marque[suc] = 1
                file.append(suc)
                pred[suc] = noeud

    return pred


assert largeur(M1, 0, 1) == [-1, 6, 0, 7, 2, 1, 3, 0, 1]
assert largeur(M1, 0, 0) == [-1, 6, 0, 7, 7, 1, 3, 0, 1]


def plus_court_chemin(M, x: int, y: int) -> list:
    pred = largeur(M, x, 1)
    if pred[y] != None:
        return chemin_arbre_rec(pred, y)
    else:
        return []


assert plus_court_chemin(M1, 0, 8) == [0, 7, 3, 6, 1, 8]
assert plus_court_chemin(M1, 0, 4) == [0, 2, 4]


def est_connexe(M):
    return None not in largeur(M, 0, 1)


M2 = np.array(
    [
        [2, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 2, 1],
        [1, 1, 1, 2],
    ]
)
M3 = np.array(
    [
        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
    ]
)
assert est_connexe(M2) == True
assert est_connexe(M3) == False


def profondeur(M, r, ordre, marque=[], pred=[]):
    marque.append(r)
    if len(pred) == 0:
        pred = [None for _ in range(len(M))]
        pred[r] = -1

    for suc in successeurs(M, r, ordre):
        if suc not in marque:
            pred[suc] = r
            profondeur(M, suc, ordre, marque, pred)

    return pred


M4 = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
    ]
)


assert profondeur(M4, 8, 1) == [2, 0, 5, 6, 5, 8, 8, None, -1]
