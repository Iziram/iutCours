"""! @brief TD 1 du module Prog 2
 @file td1.py
 @section libs Librairies/Modules
  - typing

 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 20/01/2022 .
"""
from typing import Dict, Tuple

def p1():
    d : Dict[str, str] = {'blanc':'white', 'noir':'noir','rouge':'red'}
    couleur : str = input("Saisissez une couleur : ")
    try:
        color : str = d[couleur]
        print(f"la couleur '{couleur}' se dit : '{color}'")
    except KeyError:
        print(f"La couleur '{couleur}' n'est pas présente dans le dictionnaire d")

def p2():
    # t : Tuple[int, int, int] = (1, 1, 0)
    # t[2] = 1 -> TypeError -> tuple non mutable
    v : int = None
    while type(v) != int :
        i : str = input('entrez une information: ')
        try:
            v = int(i)
            print("v est dorénavant un entier")
        except ValueError:
            print('La valeur ne peut pas être convertie en Entier')

def p3():
    entierUn, entierDeux = 0, 0
    try:
        entierUn : int = int(input("Entrez le premier entier: "))
        entierDeux : int = int(input("Entrez le second entier: "))
        div : int = 0
        try:
            div = entierUn / entierDeux
            print(f"le résultat de {entierUn}/{entierDeux} est : {div}")
        except ZeroDivisionError:
            print(f"L'entier deux ({entierDeux}) ne peut pas être égal à 0 !")
    except ValueError:
        print("La saisie ne permet pas d'obtenir un entier")

def p4():
    d: dict = dict()
    try:
        d[(3,4)] = 'v1'
        d[{5,6}] = 'v2'
    except TypeError:
        print("La clé doit être immuable")
