"""! @brief [description du fichier]
 @file app_equation_2_deg.py
 @section libs Librairies/Modules
 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 02/09/2022 .
"""
from typing import Tuple


class Equation2ndDeg:
    """!
    @brief Classe Equation du second degré

    """

    def __init__(
        self, coeff_a: float = None, coeff_b: float = None, coeff_c: float = None
    ) -> None:
        self.__sol_1: float = None
        self.__sol_2: float = None
        if coeff_a and coeff_b and coeff_c:
            self.set(coeff_a, coeff_b, coeff_c)

    def set(self, coeff_a: float, coeff_b: float, coeff_c: float) -> None:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
            @param coeff_a : float => [description]
            @param coeff_b : float => [description]
            @param coeff_c : float => [description]
        Retour de la fonction :
            @return None => [description]

        """
        self.__a: float = coeff_a
        self.__b: float = coeff_b
        self.__c: float = coeff_c
        self.calcule_les_solutions()

    def get_delta(self) -> float:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return float => [description]

        """
        _delta: float = self.__b**2 - 4 * self.__a * self.__c
        return _delta

    def solutions_reelles(self) -> bool:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return bool => [description]

        """
        return self.get_delta() >= 0

    def get_coeff(self) -> Tuple[float]:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return Tuple[float] => [description]

        """
        coeff: Tuple[float] = (self.__a, self.__b, self.__c)
        return coeff

    def calcule_les_solutions(self) -> Tuple[float]:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return Tuple[float] => [description]

        """
        delta: float = self.get_delta()
        if self.solutions_reelles():
            coeff_a, coeff_b, _ = self.get_coeff()
            self.__sol_1 = (coeff_b + delta**2) / (2 * coeff_a)
            self.__sol_2 = (coeff_b - delta**2) / (2 * coeff_a)

    def get_solutions(self) -> Tuple[float]:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return Tuple[float] => [description]

        """
        return self.__sol_1, self.__sol_2

    def get(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Equation2ndDeg
        Retour de la fonction :
            @return str => [description]

        """
        message: str = f"l'équation {self.__a}x² + {self.__b}x + {self.__c : } = 0 "
        if self.solutions_reelles():
            message += f"a pour solutions : {self.__sol_1 : .3} et {self.__sol_2 : .3}"
        else:
            message += "n'a pas de solution réelle"

        return message


if __name__ == "__main__":
    # Première étape : déclarez 2 références d'objet nommées eq1 et eq2
    eq1: Equation2ndDeg = None
    eq2: Equation2ndDeg = None
    # Seconde étape : instanciez les objets
    #   instanciez eq1 sans paramètre
    eq1 = Equation2ndDeg()

    #   instanciez eq2 avec les paramètres suivants : a=1,0 ; b=2,0 ; c=3,0
    eq2 = Equation2ndDeg(1.0, 2.0, 3.0)
    # initialisez eq1 avec les paramètres suivants : a=1,0 ; b=2,2 ; c=1,0
    eq1.set(1.0, 2.2, 1.0)
    # affichez des solutions des deux équations
    print(eq1.get_solutions())
    print(eq2.get_solutions())
    # affichez des paramètres des deux équations
    print(eq1.get_coeff())
    print(eq2.get_coeff())
    # afficher toutes les informations de chaque équation
    print(eq1.get())
    print(eq2.get())
