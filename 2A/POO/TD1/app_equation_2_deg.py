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

    def __init__(self, coeff_a: float, coeff_b: float, coeff_c: float) -> None:
        self.__a: float = coeff_a
        self.__b: float = coeff_b
        self.__c: float = coeff_c
        self.__sol_1: float = None
        self.__sol_2: float = None

    def get_delta(self) -> float:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]
        Retour de la fonction :
            @return float => [description]

        """
        _delta: float = self.__b**2 - 4 * self.__a * self.__c
        return _delta

    def get_coeff(self) -> Tuple[float]:
        coeff: Tuple[float] = (self.__a, self.__b, self.__c)
        return coeff

    def calcule_les_solutions(self) -> Tuple[float]:
        delta: float = self.get_delta()
        if delta > 0:
            coeff_a, coeff_b, _ = self.get_coeff()
            self.__sol_1 = (coeff_b + delta**2) / (2 * coeff_a)
            self.__sol_2 = (coeff_b - delta**2) / (2 * coeff_a)

    def get_solutions(self) -> Tuple[float]:
        return self.__sol_1, self.__sol_2


if __name__ == "__main__":
    mathematitien: Equation2ndDeg = Equation2ndDeg(5, 8, 3)
    mathematitien.calcule_les_solutions()
    print(mathematitien.get_solutions())