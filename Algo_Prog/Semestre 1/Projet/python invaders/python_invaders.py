from random import randint, sample
from os import system
from time import sleep
from saisiCar import SaisiCar

def displayDictLiteral(plateau: dict ) -> None:
    print(f'largeur: {plateau["L"]} cases, hauteur: {plateau["H"]} lignes'+
    f'score: {plateau["score"]}, vie: {plateau["vie"]}, level: {plateau["level"]} ')

def displayDictGame(plateau: dict, vaisseau: dict, liste_Aliens: list, tir: None or int = None) -> None:
    #affichage bandeau score
    print("-"*plateau["L"])
    print("SCORE      VIE    NIVEAU   ")
    print(" "*3, str(plateau["score"]), " "*6, str(plateau["vie"]), " "*6, str(plateau["level"]))
    print("-"*plateau["L"])

    #generation du plateau
    plat : list = [[" " for j in range(plateau["L"])] for i in range(plateau["H"])]
    
    #affichage aliens
    for alien in liste_Aliens:
        plat[alien["posy"]][alien["posx"]] = "@"
    
    
    #affichage vaiseau
    plat[plateau["H"]-1][vaiseau["posx"]] = "#"

    #affichage tir
    if(tir != None):
        for y in range(tir, plateau["H"]-1):
            if(vaiseau["tir"] == 1) : plat[y][vaiseau["posx"]] = ":" 
            elif(vaiseau["tir"] == 2) : plat[y][vaiseau["posx"]] = "§" 
            elif(vaiseau["tir"] == 3) : plat[y][vaiseau["posx"]] = "|" 

    #affichage du plateau
    for i in plat:
        ligne : str = ""
        for j in i : ligne += j
        print(ligne)
    print("-"*plateau["L"])

def initAliens(plateau : dict, lst_Alienne: list()) -> None:
    y : int = plateau["H"]//2 - 3
    x : int = 0
    for i in range (30):
        alien_temp : dict = alien.copy()
        x = i % 10 
        if i != 0 and i % 10 == 0:
            y += 1
        alien_temp["posx"] = x
        alien_temp["posy"] = y
        lst_Alienne.append(alien_temp)
    
    
    
    tirs_alien : list = sample(lst_Alienne, 5)
    a : dict
    for a in tirs_alien:
        a["tir"] = randint(2,4)
    

def moveAliens(liste_aliens: list) -> None:
    for alien in liste_aliens:
        x : int = ( alien["posx"] + 1 ) % 10
        alien["posx"] = x 
        if( x == 0) : 
            alien["posy"] += 1

def actionVaisseau(entree : str , vaiseau: dict) -> None | bool:
    if entree == "k":
        if(vaiseau["posx"] > 0) : vaiseau["posx"] -=1
    elif entree == "m":
        if(vaiseau["posx"] < plateau["L"]-1) : vaiseau["posx"] +=1
    elif entree == "o":
        return True
    else:
        return False

def fin_jeu (vaisseau: dict, liste_Aliens: list, plateau: dict)-> bool:  
    return (len(liste_Aliens) == 0 or len([x for x in liste_Aliens if x["posy"] == plateau["H"]-1]) >= 1)
    
def getLowestAlien(posx : int, liste_Aliens:list) -> None or int:
    aliens_on_x : list = [x for x in liste_aliens if x["posx"] == posx]
    lowest_list : list  = sorted(aliens_on_x, key=lambda k: k['posy'], reverse=True)
    if len(lowest_list) >=1 :
        return lowest_list[0]["posy"]
    else : return None

def gestionTir(vaisseau: dict, liste_aliens: list) -> int:
    aliens_on_x : list = [x for x in liste_aliens if x["posx"] == vaiseau["posx"]]
    lowest_list : list  = sorted(aliens_on_x, key=lambda k: k['posy'], reverse=True)
    counter : int = 0
    for ignored in range(vaiseau["tir"]):
        if(len(lowest_list)> 0 and lowest_list[0] in liste_aliens):
            liste_aliens.remove(lowest_list[0])
            lowest_list.pop(0)
            counter +=1
    return counter

def looseLife(vaisseau:dict, plateau:dict, liste_Aliens:list):
    vaiseau["tir"] = 1
    plateau["vie"] -=1
    liste_Aliens.clear()
    initAliens(plateau, liste_Aliens)

plateau : dict = {"L": 25, "H": 20, "score": 0, "vie": 3, "level": 1}
vaiseau : dict = {"posx": plateau["L"]//2, "tir": 3}
alien : dict = {"posx":0, "posy": 0, "tir": 0, "sens": 0}
liste_aliens : list() = []

initAliens(plateau, liste_aliens)
#displayDictGame(plateau, vaiseau, liste_aliens)

if __name__ == "__main__":
    partie_finie :bool = False
    action : str = "x"
    kb : SaisiCar= SaisiCar()
    wait : int = 0
    while action != "q" and plateau["vie"] >0:
        action = kb.recupCar(["m","k","o","q"])
        aTire = actionVaisseau(action, vaiseau)
        
        wait +=1
        if(wait == 3): 
            moveAliens(liste_aliens)
            wait = 0
        if(aTire == True):
            displayDictGame(plateau, vaiseau, liste_aliens, getLowestAlien(vaiseau["posx"], liste_aliens))
            plateau["score"] += 5*gestionTir(vaiseau, liste_aliens)
        else:
            displayDictGame(plateau, vaiseau, liste_aliens)
        
        partie_finie = fin_jeu(vaiseau, liste_aliens, plateau)
        if(partie_finie) : 
            looseLife(vaiseau, plateau, liste_aliens)
        sleep(0.05)
        system("clear")
        
        
