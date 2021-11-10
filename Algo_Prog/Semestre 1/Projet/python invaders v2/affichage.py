from typing import List, Dict
from os import system
def affichagelePlateau(lePlateau : Dict[str, int]) -> None:

    print(f'largeur : {lePlateau["L"]} cases, hauteur : {lePlateau["H"]} lignes, score : {lePlateau["score"]}, vie : {lePlateau["vie"]}, level : {lePlateau["level"]}.')

def affichagePlateau(lePlateau : Dict[str, int], lesAliens : List[Dict[str, int]], leVaisseau : Dict[str, int]) -> None:
    system("clear")
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

def affichageAliens(lesAliens : List[Dict[str, int]]) -> None:
    alien : Dict[str, int]
    for alien in lesAliens:
        print("\t",alien)