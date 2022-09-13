"""! @brief [description du fichier]
 @file app_ville.py
 @section libs Librairies/Modules
  - typing (lien)
 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 13/09/2022 .
"""
from typing import Tuple, Dict, List


class Ville:
    def __init__(self, nom, habitants) -> None:
        self.__habitants = habitants
        self.__nom = nom

    def get_attributs(self) -> Tuple[str, int]:
        return (self.__nom, self.__habitants)

    def get(self) -> str:
        return f"Nom: {self.__nom} Habitants : {self.__habitants}"

    def get_dict(self) -> Dict[str, any]:
        return self.__dict__


class Capitale(Ville):
    def __init__(self, nom, habitants, pays) -> None:
        Ville.__init__(self, nom, habitants)
        self.__pays = pays

    def get_attributs(self) -> Tuple[str, int, str]:
        return (*Ville.get_attributs(self), self.__pays)

    def get(self) -> str:
        return Ville.get(self) + f" Pays : {self.__pays}"


if __name__ == "__main__":
    print("----------objets simples-----------")
    # déclarer les références de 2 villes et 1 capitale
    ville_1: Ville
    ville_2: Ville
    capitale: Capitale
    # instancier les 3 objets
    # ROSPEZ, 1681 habitants
    # PERROS_GUIREC, 7440 habitants
    # LANNION 19920, habitants, capitale du TREGOR
    ville_1 = Ville("ROSPEZ", 1681)
    ville_2 = Ville("PEROS_GUIREC", 7440)
    capitale = Capitale("Lannion", 19920, "TREGOR")
    # afficher tous les attributs des villes et des capitales
    print(ville_1.get_attributs())
    print(ville_2.get_attributs())
    print(capitale.get_attributs())
    # afficher les noms des villes et capitales
    print(ville_1.get_attributs()[0])
    print(ville_2.get_attributs()[0])
    print(capitale.get_attributs()[0])
    print("----------liste de villes et capitale------------")
    # déclarer la référence d'un liste de Ville appelée liste_Villes
    liste_Villes: List[Ville]
    # instanciez la liste des villes
    liste_Villes = []
    # ajouter les 3 villes déclarées individuellement à la liste des villes
    liste_Villes.append(ville_1)
    liste_Villes.append(ville_2)
    liste_Villes.append(capitale)
    # ajouter une ville à la liste
    # RENNES 220 488 habitants, capitale de la BRETAGNE
    liste_Villes.append(Capitale("RENNES", 220488, "BRETAGNE"))
    print("----------affichez attributs des villes et capitales : ")
    for ville in liste_Villes:
        print(ville.get_attributs())
    print("----------affichez les noms des villes et capitales : ")
    for ville in liste_Villes:
        print(ville.get_attributs()[0])
    print("----------affichez les attributs des villes uniquement: ")
    for ville in liste_Villes:
        if isinstance(ville, Ville):
            print(ville.get_attributs())
    print("----------affichez population complète-----------")
    print(sum([ville.get_attributs()[1] for ville in liste_Villes]))

    for ville in liste_Villes:
        print(ville.get())
