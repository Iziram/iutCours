from threading import Thread
import GLOBALES
from typing import List
from time import sleep
from random import randint
import os


class Point:
    def __init__(self, x: int, y: int, car: str) -> None:
        self.__x = x
        self.__y = y
        self.__car = car

    def affiche_car(self, x: int, y: int, car: str) -> None:
        # méthode générique
        # utilisation des codes d'échappement ANSI pour l'affichage dans la console
        # print("\033[y;xHchaine") Using ANSI escape sequence, moves curser to row y, col x:
        chaine: str = f"\033[{y};{x}H{car}"
        print(chaine)

    def affiche(self) -> None:
        # affiche le caractère à la position (x,y)
        self.affiche_car(self.__x, self.__y, self.__car)
        self.derniere_ligne()

    def efface(self) -> None:
        # affiche un espace à la position (x,y)
        self.affiche_car(self.__x, self.__y, " ")
        self.derniere_ligne()

    def derniere_ligne(self) -> None:
        # affiche un espace au debut de la dernière ligne
        self.affiche_car(GLOBALES.LARGEUR, GLOBALES.HAUTEUR, " ")


class Etoile(Thread, Point):
    def __init__(self, x: int, y: int, t_sommeil: float, t_visible: float):
        Thread.__init__(self)
        Point.__init__(self, x, y, '*')
        self.__visible: bool = False
        self.__t_sommeil: float = t_sommeil
        self.__t_visible: float = t_visible

    def run(self):
        sleep(self.__t_sommeil)
        self.__visible = True
        Point.affiche(self)
        sleep(self.__t_visible)
        self.__visible = False
        Point.efface(self)

    def get_visible(self) -> bool:
        return self.__visible


def afficheEffacePoints(points: List[Point], sleep_time: int = .5):
    for point in points:
        point.affiche()
        sleep(sleep_time)
        point.efface()


def affiche_derniere_ligne(msg: str) -> None:
    p = Point()
    for i in range(len(msg)):
        p.affiche_car(i+1, GLOBALES .HAUTEUR+1, msg[i])
    # pour compléter la ligne avec des espaces
    for i in range(len(str(msg))+1, GLOBALES .LARGEUR):
        p.affiche_car(i, GLOBALES .HAUTEUR+1, " ")


def compte_etoile(tpl):
    cnt: int = 0
    for i in tpl:
        if i.is_alive():
            cnt += 1
    return cnt


if __name__ == '__main__':
    # declaration des variables
    liste_etoiles: List[Etoile]
    nb_etoiles: int
    x: int  # compris entre 0 et LARGEUR
    y: int  # compris entre 0 et HAUTEUR
    duree: float  # duree = temps maxi
    temps_sommeil: float
    temps_visible: float
    # initialisation et instanciation
    liste_etoiles = []
    nb_etoiles = 100
    duree = 5.0
    os.system("cls")
    # boucle pour générer les etoiles et les ajouter à la liste
    for nb in range(nb_etoiles):
        # generer aléatoirement x, y, temps_sommeil, temps_visible
        x = randint(0, GLOBALES.LARGEUR)
        y = randint(0, GLOBALES.HAUTEUR)
        temps_visible = randint(2, 4)*0.5
        temps_sommeil = randint(2, 4)*0.1
        liste_etoiles.append(Etoile(x, y, temps_sommeil, temps_visible))
    # boucle pour lancer les threads
    for etoile in liste_etoiles:
        etoile.run()
    # compter le nombre d'étoiles toutes les 30 ms
    while nb_etoiles > 0:
        sleep(0.03)
        nb_etoiles = compte_etoile(liste_etoiles)
        affiche_derniere_ligne(f"nb etoiles : {nb_etoiles}")
