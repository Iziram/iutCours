from random import randint
from typing import List, Dict

def affichagelePlateau(lePlateau : Dict[str, int]) -> None:

    print(f'largeur : {lePlateau["L"]} cases, hauteur : {lePlateau["H"]} lignes, score : {lePlateau["score"]}, vie : {lePlateau["vie"]}, level : {lePlateau["level"]}.')

def affichagePlateau(lePlateau : Dict[str, int], lesAliens : List[Dict[str, int]], leVaisseau : Dict[str, int]) -> None:

    #affichage lePlateau
    print("-"*lePlateau["L"])
    print(" "*4 + "SCORE" + " "*4 + "VIE" + " "*4 + "NIVEAU")
    print(" "*8 + str(lePlateau["score"]) + " "*6 + str(lePlateau["vie"]) + " "*9 + str(lePlateau["level"]))
    print("-"*lePlateau["L"])

    #création plateau
    plateau : List[List[str]]
    plateau = [ [ " " for j in range(lePlateau["L"])] for i in range(lePlateau["H"])]

    #placement des aliens
    alien : Dict[str, int]
    for alien in lesAliens:
        plateau[alien["posy"]][alien["posx"] + lePlateau["L"]//2 - 5 ] = "@"

    #placement vaisseau

    plateau[lePlateau["H"]-1][leVaisseau["posx"]] = "#"

    #affichage plateau

    for ligne in plateau:
        for caractere in ligne:
            print(caractere, end="")
        print("")
    print("-"*lePlateau["L"])

      
def generationAliens(lesAliens : List[Dict[str, int]], lePlateau : Dict[str, int]) -> None:
    nbAliens : int = lePlateau["level"] * 10 + 20
    nbAliensParLigne : int = 10
    ligneCourante : int = -1
    nbAliensAvecTirs : int = 5
    i:int
    for i in range(nbAliens):
        alien : Dict[str, int] = {}

        if i % nbAliensParLigne == 0:
            ligneCourante += 1

        alien["posx"] = i % nbAliensParLigne
        alien["posy"] = ligneCourante
        alien["sens"] = 0
        alien["tir"] = 0

        lesAliens.append(alien)
    
    aliensAvecTirs : List[int] = []
    while len(aliensAvecTirs) <5:
        alien : int = randint(0, len(lesAliens)-1)
        if alien not in aliensAvecTirs:
            lesAliens[alien]["tir"] = randint(2, 3)
            aliensAvecTirs.append(alien)
    
def affichageAliens(lesAliens : List[Dict[str, int]]) -> None:
    alien : Dict[str, int]
    for alien in lesAliens:
        print("\t",alien)

if __name__ == "__main__":

    #déclaration des variables
    lePlateau : Dict[str, int]
    leVaisseau : Dict[str, int]
    lesAliens : List[Dict[str, int]]


    #assignation des variables
    lePlateau = {"L":25, "H":20, "score":0, "vie":3, "level":1}
    leVaisseau = {"posx": lePlateau["L"]//2, "tir":1}
    lesAliens = []

    affichagelePlateau(lePlateau)
    generationAliens(lesAliens, lePlateau)
    affichageAliens(lesAliens)
    affichagePlateau(lePlateau, lesAliens, leVaisseau)