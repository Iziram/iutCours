"""! @brief Programme Python concernant le TP n°3 du module Maths 3
 @file tp.py
 @section libs Librairies/Modules
  - Numpy
  - typing

 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 17/03/2022 .
"""
import numpy as np
from typing import List, Tuple

print("-- Partie 1 --")
#Création d'une matrice M
M = np.array([[2,3,1],[0,1,5],[0,0,2]])
#Affichage de l'inverse de la matrice M pour vérifier le calcul papier
print(np.linalg.inv(M))

print("-- Partie 2 --")
def is_symetrique(M: np.ndarray) -> bool:
    """!
    @brief Cette fonction verifie si une matrice donnée est symétrique, c'est à dire que la matrice est égale à sa transposée

    Paramètres : 
        @param M : np.ndarray => Une matrice carrée M
    Retour de la fonction : 
        @return bool => Un booléen, Vrai si la matrice est symétrique, Faux sinon

    """
    if M.shape[0] == M.shape[1]:
        tM = np.transpose(M)
        sym = True 
        col = 0
        line = 0
        while sym == True and line < M.shape[0]:
            while sym == True and col < M.shape[0]:
                sym = M[line,col] == tM[line,col]
                col += 1
            line += 1
        return sym        
    else:
        return False  
    
def is_positive(M:np.ndarray) -> bool or List[Tuple[float,float]]:
    """!
    @brief Cette fonction vérifie si une matrice contient uniquement des valeurs positives. 

    Paramètres : 
        @param M : np.ndarray => Une matrice M
    Retour de la fonction : 
        @return bool or List[Tuple[float,float]] => Renvoie Vrai si la matrice ne possède que des valeurs positives, sinon renvoie la liste des coordonnées des valeurs négatives

    """
    cases = []
    ttLine, ttCol = M.shape
    for line in range(ttLine):
        for col in range(ttCol):
            if M[line,col] < 0:
                cases.append((line,col))
    return cases if len(cases) > 0 else True

#Test des fonctions
print(is_symetrique(np.zeros((3,3))))
print(is_positive(np.zeros((3,3)) * -1))

print("-- Partie 3 --")

#Création d'une matrice A et d'une matrice T calculée à la main
A = np.array([[4,2],[2,10]])

T = np.array([[2,1],[0,3]])

print(A)
#Vérification du calcul papier
print(np.dot(np.transpose(T), T))
print("-- Partie 3.8 --")
def factorisation_cholesky(M: np.ndarray) -> np.ndarray:
    """!
    @brief Cette fonction retourne une matrice T telle que M = transposée(T) * T

    Paramètres : 
        @param M : np.ndarray => Une matrice carrée de rang 2
    Retour de la fonction : 
        @return np.ndarray => La matrice T

    """
    if M.shape == (2,2):
        [[w,x],[y,z]] = M
        a = w**0.5
        b = x/a
        c = (z - b**2)**0.5
        return np.array([[a,b],[0, c]])
    else:
        return False
#Vérification de la véracité de la fonction 'factorisation_cholesky'
print("Cholesky: \n",factorisation_cholesky(A))
Test = factorisation_cholesky(A)
print("A:\n",A)
print("A (Cholesky): \n",np.dot(np.transpose(T), T))