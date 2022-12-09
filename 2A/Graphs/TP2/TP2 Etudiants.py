#  -*- coding: utf-8 -*-
"""
THEORIE des GRAPHES
TP2 : Arborescence
NOM PRENOM : 
DATE : 
"""


import numpy as np

# Matrice adjacence Arbre TP2
M = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]
)

Pred = [3, 3, 4, -1, 3, 2, 2, 8, 2]

# Partie 2


def pere(M: np.ndarray, x: int) -> int:
    # M matrice d'adjacence d'un arbre
    col: np.ndarray = M[:, x]
    parent: int = -1
    ite: int = 0
    while ite < len(col):
        if col[ite] == 1:
            parent = ite
            ite = len(col)
        else:
            ite += 1
    return parent


assert pere(M, 0) == 3
assert pere(M, 3) == -1

# Partie 3


def mat2pred(M: np.ndarray) -> list:
    # M : Matrice d'adajcence d'un arbre
    pred: list[int] = []
    for i in range(len(M)):
        pred.append(pere(M, i))
    return pred


assert mat2pred(M) == [3, 3, 4, -1, 3, 2, 2, 8, 2]

PRED = mat2pred(M)


def fils(Pred: list, x: int) -> list:
    liste_fils: list[int] = []
    for i, val in enumerate(Pred):
        if val == x:
            liste_fils.append(i)
    return liste_fils


assert fils([3, 3, 4, -1, 3, 2, 2, 8, 2], 3) == [0, 1, 4]
assert fils([3, 3, 4, -1, 3, 2, 2, 8, 2], 0) == []


def feuilles(Pred: list) -> list:
    liste_feuilles: list[int] = [i for i in range(len(Pred)) if i not in Pred]
    return liste_feuilles


assert set(feuilles([3, 3, 4, -1, 3, 2, 2, 8, 2])) == set([0, 1, 6, 5, 7])


def freres(Pred: list, x: int, y: int) -> bool:
    return Pred[x] == Pred[y]


assert freres([3, 3, 4, -1, 3, 2, 2, 8, 2], 0, 1) == True
assert freres([3, 3, 4, -1, 3, 2, 2, 8, 2], 0, 2) == False


def chemin_arbre(Pred: list, x: int) -> list:

    chemin: list[int] = [x]
    pointeur: int = x
    while pointeur != -1:
        pointeur = Pred[pointeur]
        if pointeur != -1:
            chemin.insert(0, pointeur)
    return chemin


assert chemin_arbre([3, 3, 4, -1, 3, 2, 2, 8, 2], 7) == [3, 4, 2, 8, 7]
assert chemin_arbre([3, 3, 4, -1, 3, 2, 2, 8, 2], 1) == [3, 1]
assert chemin_arbre([3, 3, 4, -1, 3, 2, 2, 8, 2], 3) == [3]


def chemin_arbre_rec(Pred: list, x: int) -> list:
    retour: list = None
    if Pred[x] == -1:
        retour = [x]
    else:
        prec = Pred[x]
        retour = chemin_arbre(Pred, prec) + [x]
    return retour


assert chemin_arbre_rec([3, 3, 4, -1, 3, 2, 2, 8, 2], 7) == [3, 4, 2, 8, 7]
assert chemin_arbre_rec([3, 3, 4, -1, 3, 2, 2, 8, 2], 1) == [3, 1]
assert chemin_arbre_rec([3, 3, 4, -1, 3, 2, 2, 8, 2], 3) == [3]


def frere_de(Pred: list, x: int) -> list:
    freres: list = []
    parent: int = Pred[x]
    for i, val in enumerate(Pred):
        if val == parent and i != x:
            freres.append(i)

    return freres


assert frere_de([3, 3, 4, -1, 3, 2, 2, 8, 2], 0) == [1, 4]
assert frere_de([3, 3, 4, -1, 3, 2, 2, 8, 2], 7) == []
assert frere_de([3, 3, 4, -1, 3, 2, 2, 8, 2], 3) == []


def descendant(Pred: list, x: int) -> list:
    fils = [sommet for sommet, parent in enumerate(Pred) if parent == x]
    if len(fils) != 0:
        for x in fils:
            desc = descendant(Pred, x)
            if len(desc) != 0:
                fils.extend(desc)
    return fils


assert descendant([3, 3, 4, -1, 3, 2, 2, 8, 2], 8) == [7]
assert set(descendant([3, 3, 4, -1, 3, 2, 2, 8, 2], 2)) == set([6, 5, 8, 7])
assert set(descendant([3, 3, 4, -1, 3, 2, 2, 8, 2], 3)) == set([1, 2, 4, 5, 6, 7, 8, 0])


MATRICE = np.array(
    [
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
    ]
)

# Ne fonctionne pas
# def parcourt_pronf(M: np.ndarray, x: int, marque: list = []):
#     marque.append(x)
#     print(x, marque, M[x])
#     prochains: list = [i for i in range(len(M[x])) if M[x][i] == 1]
#     print(prochains)
#     for succ in prochains:
#         if succ not in marque:
#             marque = parcourt_pronf(M, succ, marque)
#     return marque
