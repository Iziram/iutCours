from typing import List, Dict


def deplacerAliens(lesAliens: List[Dict[str, int]],
                   lePlateau: Dict[str, int]) -> None:
    nbAliensLigne: int
    nbAliensLigne = 10
    for Alien in lesAliens:
        x: int = Alien["posx"]
        if Alien["sens"] == 0:
            x = (x + 1) % nbAliensLigne
            if x == 0:
                Alien["posy"] += 1
            Alien["posx"] = x
        else:
            x = (x - 1) % nbAliensLigne
            if x == 0:
                Alien["posy"] += 1
            Alien["posx"] = x


def actionVaisseau(action: str, leVaisseau: dict,
                   lePlateau: Dict[str, int]) -> bool:
    if action == "k":
        if(leVaisseau["posx"] > 0):
            leVaisseau["posx"] -= 1
    elif action == "m":
        if(leVaisseau["posx"] < lePlateau["L"] - 1):
            leVaisseau["posx"] += 1
    elif action == "o":
        return True

    return False
