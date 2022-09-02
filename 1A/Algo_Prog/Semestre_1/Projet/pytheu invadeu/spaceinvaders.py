from typing import Dict, List, Tuple
from random import randint
from os import system
from time import sleep

def affichagePlateu(lePlateu : Dict[str,int]) -> None:
    print(f'largeur : {lePlateu["L"]} cases, hauteur : {lePlateu["H"]} lignes, score : {lePlateu["score"]}, vie : {lePlateu["vie"]}, level: {lePlateu["level"]}')

def affichagePlateuJeu(lePlateu : Dict[str,int], lesAlieu : List[Dict[str,int]], leVaisseu : Dict[str,int])-> None:
    system("clear")
    print("-" * 87)
    print(" "*4 + "SCORE" + " "*4 + "VIE"+" "*4 + "NIVEAU")
    print(" "*8 + f'{lePlateu["score"]}' + " "*6 + f'{lePlateu["vie"]}'+" "*9 + f'{lePlateu["level"]}')
    print("-" * 87)
    
    #createon plateu de jeu

    plateu : List[List[str]]
    plateu = [ [ " " for j in range(lePlateu["L"])] for i in range(lePlateu["H"])]

    #placement des alieu
    nbAlieuLigne = parametreAlieu(lePlateu)[2]
    for alieu in lesAlieu:
        plateu[alieu["posy"]][alieu["posx"]+ lePlateu["L"]//2 - nbAlieuLigne//2] = "@"

    #placement du vaiseu

    plateu[lePlateu["H"]-1][leVaisseu["posx"]] = "#"

    #affichage plateu

    for linge in plateu:
        for caractere in linge:
            print(caractere, end="")
        print("")

    print("-" * 87)

def parametreAlieu(lePlateu : Dict[str,int]) -> Tuple[int, int, int]:
    nbAlieu : int = lePlateu["level"]*10 + 20
    nbAlieuLigne : int = 10
    nbAlieuTir : int = 5
    return (nbAlieu, nbAlieuLigne, nbAlieuTir)
    
def creationAlieu(lesAlieu : List[Dict[str,int]], lePlateu : Dict[str, int]) -> None:
    nbAlieu : int
    nbAlieuLigne : int
    nbAlieuTir: int
    nbAlieu, nbAlieuLigne, nbAlieuTir = parametreAlieu(lePlateu)
    lingeCourante: int = -1
    i : int
    for i in range(nbAlieu):
        alieu : Dict[str,int] = {}
        if i % nbAlieuLigne == 0:
            lingeCourante += 1
        alieu["posx"] = i % nbAlieuLigne 
        alieu["posy"] = lingeCourante
        alieu["sens"] = 0
        alieu["tir"] = 0
        lesAlieu.append(alieu)

    LstieAlieuTir : List[Dict[str,int]] = []
    while len(LstieAlieuTir) < nbAlieuTir :
        alieu : int = randint(0, len(lesAlieu)-1)
        if alieu not in LstieAlieuTir:
            lesAlieu[alieu]["tir"] = randint(2,3)
            LstieAlieuTir.append(alieu)

def deplacerAlieu(lesAlieu: List[Dict[str,int]], lePlateu : Dict[str,int]) ->None:
    nbAlieuLigne : int
    nbAlieuTir: int
    nbAlieuLigne, nbAlieuTir = parametreAlieu(lePlateu)[1:]
    const : int = lePlateu["L"]//2 - nbAlieuLigne//2
    for alieu in lesAlieu:
        x : int = alieu["posx"]
        if alieu["sens"] == 0:
            x = (x + 1) % nbAlieuLigne
            if x == 0 :
                alieu["posy"] += 1
            alieu["posx"] = x
        else :
            x = (x - 1) % nbAlieuLigne
            if x == 0 :
                alieu["posy"] += 1
            alieu["posx"] = x


def affichageAlieu(lesAlieu : List[Dict[str,int]]) -> None:
    alieu : Dict[str,int]
    for alieu in lesAlieu:
        print("\t", alieu)
    
if __name__ == "__main__":
    lePlateu : Dict[str, int] = {
    "H":12,
    "L": 25,
    "score": 0,
    "level": 1,
    "vie": 3
    }

    leVaisseu : Dict[str, int] = {
        "posx" : lePlateu["L"]//2,
        "tir" : 1
    }

    lesAlieu : List[Dict[str,int]] = []
    creationAlieu(lesAlieu, lePlateu)
    # affichageAlieu(lesAlieu)
    affichagePlateuJeu(lePlateu, lesAlieu, leVaisseu)

    
    i = 0
    while i < 10:
        deplacerAlieu(lesAlieu, lePlateu)
        affichagePlateuJeu(lePlateu, lesAlieu, leVaisseu)
        sleep(0.5)

    