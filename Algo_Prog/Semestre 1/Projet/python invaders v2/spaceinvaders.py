from generation import *
from affichage import *
from deplacement import *
from time import sleep
from typing import List, Dict

def fin_jeu (vaisseau: dict, liste_Aliens: list, plateau: dict)-> bool:  
    return (len(liste_Aliens) == 0 or len([x for x in liste_Aliens if x["posy"] == plateau["H"]-1]) >= 1)

if __name__ == "__main__":
    lePlateau : Dict[str, int] = {
    "H":12,
    "L": 25,
    "score": 0,
    "level": 1,
    "vie": 3
    }

    leVaisseau : Dict[str, int] = {
        "posx" : lePlateau["L"]//2,
        "tir" : 1
    }

    lesAliens : List[Dict[str,int]] = []
    generationAliens(lesAliens, lePlateau)

    
    i = 0
    fin = False
    while i < 10 and not fin :
        fin = fin_jeu(leVaisseau, lesAliens, lePlateau)
        affichagePlateau(lePlateau, lesAliens, leVaisseau)
        deplacerAliens(lesAliens, lePlateau)
        sleep(0.01)