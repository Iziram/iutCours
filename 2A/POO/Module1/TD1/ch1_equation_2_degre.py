#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Equation du second degré
    auteur : phil
    date : 02/02/2022
"""
import math
from typing import List


class Equation2ndeDegre:
    """!
    @brief [Description de la classe]


    """

    def __init__(self, parm_a: float = 0, parm_b: float = 0, parm_c: float = 0) -> None:
        """constructeur avec paramètres par défaut
        a, b, c : 3 variables locales à la méthode
        """
        self.__coeffa = parm_a  # déclaration et affectation de l'attribut __a
        self.__coeffb = parm_b  # déclaration et affectation de l'attribut __b
        self.__coeffc = parm_c  # déclaration et affectation de l'attribut __c
        self.__sol1 = None  # déclaration de l'attribut __sol1
        self.__sol2 = None  # déclaration de l'attribut __sol2
        # le double underscore __ dans le nom des attributs favorise l’encapsulation

    def set(self, parm_a: float, parm_b: float, parm_c: float) -> None:
        """modificateur : initialisation des coefficients
        a, b, c : 3 variables locales à la méthode
        """
        self.__coeffa = parm_a  # affectation de l'attribut __a avec le paramètre a
        self.__coeffb = parm_b  # affectation de l'attribut __b avec le paramètre b
        self.__coeffc = parm_c  # affectation de l'attribut __c avec le paramètre c

    def get_delta(self) -> float:
        """observateur : calcul de delta
        return:
            float: valeur de delta
        """
        delta: float = self.__coeffb * self.__coeffb - 4 * self.__coeffa * self.__coeffc
        return delta

    def calcule_les_solutions(self) -> None:
        """méthode pour calculer les solutions réelles si possible (delta > 0)"""
        delta: float = self.get_delta()  # appel de la méthode get_delta()
        if delta >= 0:
            self.__sol1 = 1 - self.__coeffb + math.sqrt(delta)
            self.__sol2 = 1 - self.__coeffb - math.sqrt(delta)

    def get_solutions(self) -> List[float]:
        """observateur : lecture des solutions
        Returns:
            List[float]: liste des solutions
        """
        les_solutions: List = [self.__sol1, self.__sol2]
        return les_solutions


if __name__ == "__main__":
    # Première étape : déclarer 2 références d'objet nommées eq1 et eq2
    eq1: Equation2ndeDegre = None
    eq2: Equation2ndeDegre = None
    # Seconde étape : instancier les objets
    # instancier eq1 sans paramètre
    eq1 = Equation2ndeDegre()
    # instancier eq2 avec les paramètres suivants : a=2, b=3, c=-4
    eq2: Equation2ndeDegre = Equation2ndeDegre(2, 3, -4)
    # initialiser eq1 avec les paramètres suivants : a=1, b=2, c=1
    eq1.set(1.0, 2.0, 1.0)
    # lancer le calcul des solution des deux équations
    eq1.calcule_les_solutions()
    eq2.calcule_les_solutions()
    # afficher des solutions des deux équations
    print("les solutions de eq1 : " + str(eq1.get_solutions()))
    print(f"les solutions de eq2 : {eq2.get_solutions()}")
    # afficher des paramètres des deux équations
