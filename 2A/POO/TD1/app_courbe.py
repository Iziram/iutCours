"""! @brief [description du fichier]
 @file app_courbe.py
 @section libs Librairies/Modules
  - typing (lien)
  - matplotlib.pyplot (lien)
 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 02/09/2022 .
"""
from typing import List
import matplotlib.pyplot as plt


class Point:
    """!
    @brief [Description de la classe]


    """

    def __init__(self, pos_x: float, pos_y: float):
        self.__x = pos_x
        self.__y = pos_y

    def get_x(self):
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]

        """
        return self.__x

    def get_y(self):
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]

        """
        return self.__y


class Courbe:
    """!
    @brief [Description de la classe]


    """

    def __init__(self):
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]

        """
        self.__liste_points: List[Point] = []

    def ajouter_point(self, point: Point):
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]
            @param point : Point => [description]

        """
        self.__liste_points.append(point)

    def affiche(self):
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => [description]

        """
        liste_x, liste_y = [], []
        for point in self.__liste_points:
            liste_x.append(point.get_x())
            liste_y.append(point.get_y())

        plt.plot(liste_x, liste_y)
        plt.show()


if __name__ == "__main__":
    crb: Courbe = Courbe()
    crb.ajouter_point(Point(1, 1))
    crb.ajouter_point(Point(2, 1))
    crb.ajouter_point(Point(3, 2))
    crb.affiche()
