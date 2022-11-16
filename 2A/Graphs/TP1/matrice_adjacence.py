"""! @brief Fichier python contenant les fonctions du TP 1 Matrice d'adjacence
 @file matrice_adjacence.py
 @section libs Librairies/Modules
    - Numpy
 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 16/11/2022 .
"""
import numpy as np

array: list[list[int]] = [
    [1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
]
MATRICE: np.ndarray = np.array(array)
ZEROS: np.ndarray = np.zeros((5, 5))
ONES: np.ndarray = np.ones((5, 5))
IDENTITE: np.ndarray = np.eye(5)


def ordre(matrice: np.ndarray) -> int:
    """!
    @brief Renvoie l'ordre d'une matrice

    Explication:
        len(matrice) renvoie la taille de la première ligne de `matrice`
        la matrice étant carrée, la taille des lignes == la taille des colonnes
        On peut alors renvoyer cette taille

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return int => un entier représentant l'ordre de la matrice

    """
    size: int = len(matrice)
    return size

assert ordre(MATRICE) == 5, "La fonction ordre ne retourne pas le bon  ordre"
"""
>>> ordre(MATRICE)
>>> 5
"""

def taille(matrice: np.ndarray) -> int:
    """!
    @brief Renvoie la taille d'une matrice

    Explication:
        La taille d'un graph représenté par une matrice correspond au nombre de 1 qui se trouvent dans la matrice
        en utilisant la fonction `sum` de python, nous pouvons calculer la somme d'une liste de nombre
        On aplatie la matrice dans une seule et même liste et on fait la somme des 1


    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return int => un entier représentant la taille de la matrice

    """
    return sum(matrice.flatten())

assert taille(MATRICE) == 10, "La fonction taille ne retourne pas le bon  ordre"
"""
>>> taille(MATRICE)
>>> 10
"""

def voisin(matrice: np.ndarray, a: int, b: int) -> bool:
    """!
    @brief Retourne vrai si les deux sommets a et b sont voisins

    Explication:
        A et B sont voisins si on retrouve:
            1 en position Matrice[A,B]
            ou
            1 en postion Matrice[B,A]

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
        @param a : int => un sommet A
        @param b : int => un sommet B
    Retour de la fonction :
        @return bool => un booléen Vrai si les sommets sont voisins

    """
    return matrice[b,a] or matrice[a,b]

assert voisin(MATRICE, 1, 4) == False, "La fonction voisin ne fonctionne pas"
assert voisin(MATRICE, 0, 4) == True, "La fonction voisin ne fonctionne pas"
"""
>>> voisin(MATRICE, 1, 4)
>>> False

>>> voisin(MATRICE, 0, 4)
>>> True
"""

def predecesseurs(matrice: np.ndarray, sommet: int) -> list[int]:
    """!
    @brief renvoie la liste des prédécesseurs d'un sommet

    Explication:
        On peut savoir la liste des prédécesseurs en regardant la matrice et en prenant la colonne d'indice sommet
        On retient l'indice de chaque 1 qui se trouve dans la colonne.

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
        @param sommet : int => un sommet de la matrice
    Retour de la fonction :
        @return list[int] => la liste des sommets étant prédécesseurs au sommet donné

    """
    col: np.ndarray = matrice[:, sommet]
    pred: list[int] = []
    for i, boo in enumerate(col):
        if boo:
            pred.append(i)

    return pred

assert predecesseurs(MATRICE, 0) == [
    0,
    1,
], "La fonction prédécesseur ne fonctionne pas"
assert predecesseurs(MATRICE, 3) == [], "La fonction prédécesseur ne fonctionne pas"
"""
>>> predecesseurs(MATRICE, 0)
>>> [0, 1]
>>> predecesseurs(MATRICE, 4)
>>> []
"""

def successeurs(matrice: np.ndarray, sommet: int) -> list[int]:
    """!
    @brief renvoie la liste des successeurs d'un sommet

    Explication:
        On peut savoir la liste des successeurs en regardant la matrice et en prenant la ligne d'indice sommet
        On retient l'indice de chaque 1 qui se trouve dans la colonne.

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
        @param sommet : int => un sommet de la matrice
    Retour de la fonction :
        @return list[int] => la liste des successeurs du sommet

    """
    lig: np.ndarray = matrice[sommet, :]
    suc: list[int] = []
    for i, boo in enumerate(lig):
        if boo:
            suc.append(i)

    return suc

assert successeurs(MATRICE, 0) == [
    0,
    1,
    4,
], "La fonction successeurs ne fonctionne pas"
assert successeurs(MATRICE, 3) == [
    1,
    2,
], "La fonction successeurs ne fonctionne pas"
assert successeurs(MATRICE, 2) == [], "La fonction successeurs ne fonctionne pas"
"""
>>> successeurs(MATRICE, 0)
>>> [0, 1, 4]
>>> successeurs(MATRICE, 3)
>>> [1, 2]
>>> successeurs(MATRICE, 2)
>>> []
"""

def sans_predecesseurs(matrice: np.ndarray) -> list[int]:
    """!
    @brief Renvoie la liste des sommets sans prédécesseurs

    Explication:
        Pour obtenir la liste des sommets sans prédécesseurs, on parcourt les colonnes de la matrices
            Si la somme de la colonne est égale à 0
            Alors on ajoute l'indice dans la liste des sommets

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return list[int] => la liste des sommets sans prédécesseurs

    """
    ss_pred: list[int] = []
    for i in range(ordre(matrice)):
        col: np.ndarray = matrice[:, i]
        if sum(col) == 0:
            ss_pred.append(i)
    return ss_pred

assert sans_predecesseurs(MATRICE) == [
    3
], "La fonction sans predecesseurs ne fonctionne pas"
assert sans_predecesseurs(ZEROS) == [
    0,
    1,
    2,
    3,
    4,
], "La fonction sans predecesseurs ne fonctionne pas"
assert (
    sans_predecesseurs(ONES) == []
), "La fonction sans predecesseurs ne fonctionne pas"
"""
>>> sans_predecesseurs(MATRICE)
>>>  [3]
>>> sans_predecesseurs(ZEROS)
>>>  [0,1,2,3,4]
>>> sans_predecesseurs(ONES)
>>>  []
"""

def sans_successeurs(matrice: np.ndarray) -> list[int]:
    """!
    @brief Renvoie la liste des sommets dans successeurs

    Explication:
        Pour obtenir la liste des sommets sans successeurs, on parcourt les lignes de la matrices
            Si la somme de la ligne est égale à 0
            Alors on ajoute l'indice dans la liste des sommets

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return list[int] => la liste des sommets sans successeurs

    """
    ss_suc: list[int] = []
    for i, lig in enumerate(matrice):
        if sum(lig) == 0:
            ss_suc.append(i)

    return ss_suc

assert sans_successeurs(MATRICE) == [
    2
], "La fonction sans successeurs ne fonctionne pas"
assert sans_successeurs(ZEROS) == [
    0,
    1,
    2,
    3,
    4,
], "La fonction sans successeurs ne fonctionne pas"
assert (
    sans_successeurs(ONES) == []
), "La fonction sans successeurs ne fonctionne pas"
"""
>>> sans_successeurs(MATRICE)
>>>  [2]
>>> sans_successeurs(ZEROS)
>>>  [0,1,2,3,4]
>>> sans_successeurs(ONES)
>>>  []
"""

def reflexif(matrice: np.ndarray) -> bool:
    """!
    @brief Renvoie Vrai si la matrice est reflexive

    Explication:
        Pour savoir si une matrice est réflexive, il faut regarder si la diagonale contient que des 1
        On parcourt la matrice en diagonale et on s'arrête si on tombe sur un 0

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return bool => un booléan Vrai si la matrice est reflexive

    """
    ordr: int = ordre(matrice)
    i: int = 0
    fin: bool = False
    while i < ordr and not fin:
        fin = matrice[i, i] == 0
        i += 1

    return not fin

assert reflexif(MATRICE) == False, "La fonction réflexif ne fonctionne pas"
assert reflexif(ZEROS) == False, "La fonction réflexif ne fonctionne pas"
assert reflexif(ONES) == True, "La fonction réflexif ne fonctionne pas"
assert reflexif(IDENTITE) == True, "La fonction réflexif ne fonctionne pas"
"""
>>> reflexif(MATRICE)
>>> False
>>> reflexif(ZEROS)
>>> False
>>> reflexif(ONES)
>>> True
>>> reflexif(IDENTITE)
>>> True
"""

def symetrique_v1(matrice: np.ndarray) -> bool:
    """!
    @brief Renvoie Vrai si la matrice est symétrique

    Explication:
        On parcourt chaque case de la matrice et on vérifie si les cases M[i,j] et M[j,i] sont égales
        Sinon on quitte et on renvoie Faux 

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return bool => un booléen Vrai si la matrice est symétrique

    """

    ordr: int = ordre(matrice)
    i: int = 0
    j: int = 0

    fin: bool = False
    while i < ordr and not fin:
        while j < ordr and not fin:
            fin = matrice[i, j] != matrice[j, i]
            j += 1
        i += 1
    return not fin

assert symetrique_v1(MATRICE) == False, "La fonction symétrique ne fonctionne pas"
assert symetrique_v1(ZEROS) == True, "La fonction symétrique ne fonctionne pas"
assert symetrique_v1(ONES) == True, "La fonction symétrique ne fonctionne pas"
assert symetrique_v1(IDENTITE) == True, "La fonction symétrique ne fonctionne pas"

"""
>>> symetrique_v1(MATRICE)
>>> False
>>> symetrique_v1(ZEROS)
>>> True
>>> symetrique_v1(ONES)
>>> True
>>> symetrique_v1(IDENTITE)
>>> True
"""

def symetrique_v2(matrice: np.ndarray) -> bool:
    """!
    @brief Renvoie Vrai si la matrice est symétrique

    Explication:
        Une matrice est symétrique si elle est égale à sa transposée

    Paramètres :
        @param matrice : np.ndarray => une matrice numpy
    Retour de la fonction :
        @return bool => un booléen Vrai si la matrice est symétrique

    """
    transpo: np.ndarray = np.transpose(matrice)
    return np.array_equal(transpo, matrice)

assert symetrique_v2(MATRICE) == False, "La fonction symétrique ne fonctionne pas"
assert symetrique_v2(ZEROS) == True, "La fonction symétrique ne fonctionne pas"
assert symetrique_v2(ONES) == True, "La fonction symétrique ne fonctionne pas"
assert symetrique_v2(IDENTITE) == True, "La fonction symétrique ne fonctionne pas"

"""
>>> symetrique_v2(MATRICE)
>>> False
>>> symetrique_v2(ZEROS)
>>> True
>>> symetrique_v2(ONES)
>>> True
>>> symetrique_v2(IDENTITE)
>>> True
"""




# Taille


# Voisin



# Successeurs



# Prédécesseurs



# Sans Successeurs



# Sans Prédécesseur



# Réflexif



# Symétrique



    