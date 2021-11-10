from generation import *
from affichage import *
from deplacement import *
from tir import *
from time import sleep
from typing import List, Dict
from saisiCar import SaisiCar


def finJeu(lesAliens: list, lePlateau: dict,
           leVaisseau: Dict[str, int]) -> bool:
    return (len(lesAliens) == 0 or len(
        [x for x in lesAliens if x["posy"] == lePlateau["H"] - 1]) >= 1)


lePlateau: Dict[str, int] = {
    "H": 12,
    "L": 25,
    "score": 0,
    "level": 1,
    "vie": 3
}

leVaisseau: Dict[str, int] = {
    "posx": lePlateau["L"] // 2,
    "tir": 3
}
lesAliens: List[Dict[str, int]] = []
generationAliens(lesAliens, lePlateau)

if __name__ == "__main__":
    partieFinie: bool = False
    action = "x"
    kb = SaisiCar()

    while not partieFinie and action != "q":
        partieFinie = finJeu(lesAliens, lePlateau, leVaisseau)

        action = kb.recupCar(["m", "k", "o", "q"])
        aTir = actionVaisseau(action, leVaisseau, lePlateau)
        alienAtteint: int or None = alienAtteignable(
            lesAliens, leVaisseau["posx"], lePlateau)
        if aTir:
            lePlateau["score"] += gestionTir(
                leVaisseau,
                alienAtteint,
                lesAliens,
                lePlateau)
            affichagePlateau(lePlateau, lesAliens, leVaisseau, alienAtteint)
        affichagePlateau(lePlateau, lesAliens, leVaisseau)

        deplacerAliens(lesAliens, lePlateau)

        sleep(0.05)
