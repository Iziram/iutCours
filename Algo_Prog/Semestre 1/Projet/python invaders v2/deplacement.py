from typing import List, Dict

def deplacerAliens(lesAliens: List[Dict[str,int]], lePlateau : Dict[str,int]) ->None:
    nbAliensLigne : int
    nbAliensLigne = 10
    for Alien in lesAliens:
        x : int = Alien["posx"]
        if Alien["sens"] == 0:
            x = (x + 1) % nbAliensLigne
            if x == 0 :
                Alien["posy"] += 1
            Alien["posx"] = x
        else :
            x = (x - 1) % nbAliensLigne
            if x == 0 :
                Alien["posy"] += 1
            Alien["posx"] = x

def actionVaisseau(entree : str , vaiseau: dict) -> None | bool:
    if entree == "k":
        if(vaiseau["posx"] > 0) : vaiseau["posx"] -=1
    elif entree == "m":
        if(vaiseau["posx"] < plateau["L"]-1) : vaiseau["posx"] +=1
    elif entree == "o":
        return True
    else:
        return False