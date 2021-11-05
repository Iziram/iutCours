from random import randint
from typing import List, Dict

def affichageInfoJeu(infoJeu : Dict[str, int]) -> None:

    print(f'largeur : {infoJeu["L"]} cases, hauteur : {infoJeu["H"]} lignes, score : {infoJeu["score"]}, vie : {infoJeu["vie"]}, level : {infoJeu["level"]}.')

def affichagePlateau(infoJeu : Dict[str, int], lesAliens : List[Dict[str, int]], leVaisseau : Dict[str, int]) -> None:

    #affichage infoJeu
    print("-"*infoJeu["L"])
    print(" "*4 + "SCORE" + " "*4 + "VIE" + " "*4 + "NIVEAU")
    print(" "*8 + str(infoJeu["score"]) + " "*6 + str(infoJeu["vie"]) + " "*9 + str(infoJeu["level"]))
    print("-"*infoJeu["L"])

    #création plateau
    plateau : List[List[str]]
    plateau = [ [ " " for j in range(infoJeu["L"])] for i in range(infoJeu["H"])]

    #placement des aliens
    alien : Dict[str, int]
    for alien in lesAliens:
        plateau[alien["posy"]][alien["posx"]] = "@"

    #placement vaisseau

    plateau[infoJeu["H"]-1][leVaisseau["posx"]] = "#"

    #affichage plateau

    for ligne in plateau:
        for caractere in ligne:
            print(caractere, end="")
        print("")
    print("-"*infoJeu["L"])

      
def generationAliens(lesAliens : List[Dict[str, int]], infoJeu : Dict[str, int]) -> None:
    nbAliens : int = infoJeu["level"] * 10 + 20
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
    infoJeu : Dict[str, int]
    leVaisseau : Dict[str, int]
    lesAliens : List[Dict[str, int]]


    #assignation des variables
    infoJeu = {"L":25, "H":20, "score":0, "vie":3, "level":1}
    leVaisseau = {"posx": infoJeu["L"]//2, "tir":1}
    lesAliens = []

    affichageInfoJeu(infoJeu)
    generationAliens(lesAliens, infoJeu)
    affichageAliens(lesAliens)
    affichagePlateau(infoJeu, lesAliens, leVaisseau)