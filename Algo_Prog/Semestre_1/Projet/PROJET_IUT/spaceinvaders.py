"""! @brief Implémentation en python du jeu SpaceInvaders
 @file spaceinvaders.py
 @section libs Librairies/Modules
  - List et Dict du module typing
  - sample et randint du module Random
  - system du module os
  - sleep du module time
  - SaisiCar du module saisiCar

 @section authors Author(s)
  - Créé par Matthias Hartmann le 15/11/2021 .
"""
from typing import List, Dict, Tuple
from random import randint, sample
from os import system
from time import sleep
from saisiCar import SaisiCar


def affichageDebugPlateau(lePlateau: Dict[str, int]):
    """!
    @brief Cette fonction affiche le plateau en une ligne pour débug

    Paramètre(s) :
        @param lePlateau : Dict[str, int] => Un dictionnaire qui représente le plateau

    """
    assert isinstance(
        lePlateau, dict), "le paramètre `lePlateau` doit être un dictionnaire"
    assert set(lePlateau.keys()) == {
        "L", "H", "vie", "score", "level","tirS"}, "le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"

    print(f'largeur : {lePlateau["L"]} cases, ',
          f'hauteur : {lePlateau["H"]} lignes,',
          f'score : {lePlateau["score"]},',
          f'vie : {lePlateau["vie"]}, ',
          f'level : {lePlateau["level"]}.')


def affichagePlateau(
        lePlateau: Dict[str, int], lesAliens: List[Dict[str, int]], leVaisseau: Dict[str, int], tir_y : int or None = None):
    """!
    @brief Cette fonction gère l'affichage du plateau de jeu, des aliens, du vaisseau et des tirs

    Paramètre(s) :
        @param lePlateau : Dict[str, int] => Un dictionnaire qui représente le plateau
        @param lesAliens : List[Dict[str, int]] => Une liste de dictionnaire représentant une liste d'aliens
        @param leVaisseau : Dict[str,int] => Un dictionnaire représentant le vaisseau
        @param tir_y : int or None = None => La coordonnée y de l'alien à tuer avec le tir
        

    """
    assert isinstance(
        lePlateau, dict), "le paramètre `lePlateau` doit être un dictionnaire"
    assert isinstance(
        leVaisseau, dict), "le paramètre `leVaisseau` doit être un dictionnaire"
    assert isinstance(
        lesAliens, list), "le paramètre `lesAliens` doit être une liste"
    assert set(lePlateau.keys()) == {
        "L", "H", "vie", "score", "level","tirS"}, "`Erreur -> lePlateau :`le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"
    assert len([i for i in lesAliens if not isinstance(i, dict)]
               ) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"
    assert set(leVaisseau.keys()) == {
        "posx", "tir"}, "`Erreur -> leVaisseau :`le dictionnaire doit avoir comme clé : `posx;tir`"

    #Remise à zero de l'affichage de la console / du terminal.
    # system("clear") #linux
    system("cls") #windows

    #Affichage du bandeau d'informations
    print("-" * lePlateau["L"])
    print(" " * 2 + "SCORE" + " " * 4 + "VIE" + " " * 4 + "NIVEAU")
    print(
        f'  {lePlateau["score"]:5}  {lePlateau["vie"] : 5}     {lePlateau["level"] : 5}')
    print("-" * lePlateau["L"])

    # code couleur :
    couleur_alien: str = "\033[0;32;40m"
    couleur_vaisseau: str = "\033[0;31;40m"

    # affichage des aliens, du vaisseau
    affichage: str = ""
    for y in range(lePlateau["H"]):
        for x in range(lePlateau["L"]):
            #initialisation du caractère à afficher (par défaut un espace)
            caractere: str = " "

            #Gestion du tir spécial
            if lePlateau["tirS"] != None and x == lePlateau["tirS"][0] and y == lePlateau["tirS"][1]:

                #Si les coordonnées du tir spécial correspondent avec les coordonnées du caractère courant,
                #on change le caractère par un '2' si le tir est de niveau 2 et un '3' pour le tir de niveau 3
                caractere = str(lePlateau["tirS"][2]) 

                #On vérifie si le tir spécial a atteint le bas du plateau
                if y == lePlateau["H"] -1:
                    if x == leVaisseau["posx"]:
                        #Si le vaisseau ce trouve au même endroit que le tir spécial on assigne le tir spécial au vaisseau
                        #/!\ Uniquement si le tir spécial est supérieur au tir du vaisseau 
                        leVaisseau["tir"] = max(leVaisseau["tir"], lePlateau["tirS"][2])
                    #Puisque le tir a atteint le bas du plateau on le détruit
                    lePlateau["tirS"] = None

            #On vérifie si les coordonnées du caractère courant sont associées aux coordonnées d'un alien
            for a in lesAliens:
                if a["posx"] == x and a["posy"] == y:
                    #Si les deux paires de coordonnées sont égales on change le caractère par un '@' (coloré en vert grâce au code couleur)
                    caractere = f'{couleur_alien}@'

            #On vérifie si les coordonnées du caractère courant sont associées aux coordonnées du vaisseau
            if y == lePlateau["H"] - 1 and x == leVaisseau["posx"]:
                #Si on est bien à la dernière ligne du plateau et que les positions X correspondent
                #Alors on change le caractère par un '#' (coloré en Rouge grâce au code couleur) 
                caractere = f'{couleur_vaisseau}#'
            
            #On vérifie si un tir a été initié
            if tir_y != None :
                if x == leVaisseau["posx"]:
                    #Si c'est le cas on doit afficher une trainée reliant l'alien touché et le vaisseau
                    if tir_y < y < lePlateau["H"]:
                        #On change le caractère en fonction du niveau du tir.
                        if leVaisseau["tir"] == 1:
                            caractere = ":"
                        if leVaisseau["tir"] == 2:
                            caractere = "§"
                        if leVaisseau["tir"] == 3:
                            caractere = "|"
            #On ajoute le caractère à la ligne courante
            affichage += caractere

        #Lorsque la ligne est finie on l'affiche et remet la variable d'affichage à ""
        print(affichage, end="")
        affichage = ""

        #On réinitialise l'affichage des couleurs afin de ne pas avoir de débordement de couleur
        print(f"\033[0;37;40m")
        
    print("-" * lePlateau["L"])

def generationAliens(
        lesAliens: List[Dict[str, int]], lePlateau: Dict[str, int]):
    """!
    @brief Cette fonction permet de generer la liste d'aliens

    Paramètre(s) :
        @param lePlateau : Dict[str, int] => Un dictionnaire qui représente le plateau
        @param lesAliens : List[Dict[str, int]] => Une liste de dictionnaire représentant une liste d'aliens

    """
    assert isinstance(
        lePlateau, dict), "le paramètre `lePlateau` doit être un dictionnaire"
    assert isinstance(
        lesAliens, list), "le paramètre `lesAliens` doit être une liste"
    assert set(lePlateau.keys()) == {
        "L", "H", "vie", "score", "level","tirS"}, "`Erreur -> lePlateau :`le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"
    assert len([i for i in lesAliens if not isinstance(i, dict)]
               ) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"

    nbAliens: int = lePlateau["level"] * 10 + 20
    nbAliensParLigne: int = 10
    ligneCourante: int = -1
    nbAliensAvecTirs: int = 5
    i: int
    for i in range(nbAliens):
        
        alien: Dict[str, int] = {}
        if i % nbAliensParLigne == 0:
            ligneCourante += 1

        alien["posx"] = i % nbAliensParLigne + \
            lePlateau["L"] // 2 - nbAliensParLigne // 2
        alien["posy"] = ligneCourante
        alien["sens"] = 0
        alien["tir"] = 0

        lesAliens.append(alien)

    # sample est une fonction du module Random qui permet de tirer un sous ensemble aléatoire de taille k parmi une population
    # dans notre cas, la population c'est la liste lesAliens et la taille
    # c'est nbAliensAvecTirs
    aliensAvecTirs: List[int] = sample(lesAliens, nbAliensAvecTirs)
    for alien in aliensAvecTirs:
        alien["tir"] = randint(2, 3)


def affichageDebugAlien(lesAliens: List[Dict[str, int]]):
    """!
    @brief Cette fonction permet d'afficher les aliens dans leur forme primaire (un dictionnaire)

    Paramètre(s) :
        @param lesAliens : List[Dict[str,int]] => Une liste de dictionnaire représentant les aliens.

    """

    assert isinstance(
        lesAliens, list), "le paramètre `lesAliens` doit être une liste"
    assert len([i for i in lesAliens if not isinstance(i, dict)]
               ) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"
    a: Dict[str, int]
    for a in lesAliens:
        print(a)


def deplacementAliens(
        lesAliens: List[Dict[str, int]], lePlateau: Dict[str, int]):
    """!
    @brief Cette fonction effectuer le déplacement des aliens d'une case

    Paramètre(s) :
        @param lesAliens : List[Dict[str, int]] => La liste des aliens
        @param lePlateau : Dict[str, int] => Un dictionnaire qui représente le plateau
    """
    sens = lesAliens[0]["sens"]
    bord: bool = False
    if sens:
        for a in lesAliens:
            if a["posx"] <= 0:
                bord = True
    else:
        for a in lesAliens:
            if a["posx"] >= lePlateau["L"] - 1:
                bord = True

    for alien in lesAliens:
        if bord:
            alien["posy"] += 1
            alien["sens"] = not(alien["sens"])
        else:
            if sens:
                alien["posx"] -= 1
            else:
                alien["posx"] += 1


def actionVaisseau(action: str, leVaisseau: dict,
                   lePlateau: Dict[str, int]) -> bool:
    """!
    @brief Cette fonction permet de bouger le vaisseau ou d'activer un tir en fonction d'une action utilisateur passée en paramètre

    Paramètre(s) :
        @param action : str => Une chaine de caractère représentant l'action de l'utilisateur
        @param leVaisseau : dict => Un Dictionnaire représentant le vaisseau
        @param lePlateau : Dict[str, int] => Un Dictionnaire représentant le plateau de jeu
    Retour de la fonction :
        @return bool True si un tir est actionné, False sinon

    """
    retour : bool = False

    if action == "k":
        if(leVaisseau["posx"] > 0):
            leVaisseau["posx"] -= 1
    elif action == "m":
        if(leVaisseau["posx"] < lePlateau["L"] - 1):
            leVaisseau["posx"] += 1
    elif action == "o":
        retour = True

    return retour


def finJeu(lePlateau: Dict[str,
                           int],
           lesAliens: List[Dict[str,
                                int]],
           leVaisseau: Dict[str,
                            int]) -> bool:
    """!
    @brief Cette fonction vérifie les conditions de fin de jeu

    Paramètre(s) :
        @param lePlateau : Dict[str, int] => Un dictionnaire qui représente le plateau
        @param lesAliens : List[Dict[str, int]] => Une liste de dictionnaire représentant une liste d'aliens
        @param leVaisseau : Dict[str,int] => Un dictionnaire représentant le vaisseau
    Retour de la fonction :
        @return bool Vrai si la partie doit s'arrêter, Faux sinon

    """
    return (len(lesAliens) == 0 or len(
        [x for x in lesAliens if x["posy"] == lePlateau["H"] - 1]) >= 1)


def alienAtteint(lesAliens : List[Dict[str,int]], posx) -> int or None:
    """!
    @brief Cette fonction retourne la coordonnée y de l'alien le plus bas étant sur la même coordonnée x que posx 

    Paramètre(s) : 
        @param lesAliens : List[Dict[str,int]] => Une liste de dictionnaire représentant une liste d'aliens
        @param posx => La coordonnée x du vaisseau
    Retour de la fonction : 
        @return int or None La coordonnée y de l'alien le plus bas sur la même colonne que posx ou None si aucun n'a été trouvé

    """
    ymax : int  = -1 
    for alien in lesAliens :
        if alien["posx"] == posx:
            ymax = max(alien["posy"], ymax)
    return ymax if ymax != -1 else None

def tuerAliens(leVaisseau : Dict[str, int], lesAliens : List[Dict[str,int]]) -> Tuple[int, int] :
    """!
    @brief Cette fonction permet de supprimer de la liste des Aliens les aliens que le tir du vaisseau touche.

    Paramètre(s) : 
        @param leVaisseau : Dict[str, int] => Un dictionnaire représentant le vaisseau
        @param lesAliens : List[Dict[str,int]] => Une liste de dictionnaire représentant une liste d'aliens
    Retour de la fonction : 
        @return Tuple[int, int] (Le nombre d'aliens tués, tir spécial)

    """
    nbMort : int = 0
    alienMort : List[Dict[str,int]] = []
    i : int = len(lesAliens) -1
    while i > -1 and nbMort < leVaisseau["tir"]:
        alien : Dict[str, int] = lesAliens[i];
        if alien["posx"] == leVaisseau["posx"]:
            nbMort += 1
            alienMort.append(alien)
        i -= 1
    maxtir : int = 0
    for a in alienMort:
        maxtir = max(a["tir"], maxtir)
        lesAliens.remove(a)
    return (nbMort, maxtir)

if __name__ == "__main__":
    #Initialisation du plateau, du vaisseau et des aliens
    lePlateau: Dict[str, int] = {
        "L": 25,
        "H": 20,
        "score": 0,
        "vie": 3,
        "level": 1,
        "tirS" : None
    }
    leVaisseau: Dict[str, int] = {
        "posx": lePlateau["L"] // 2,
        "tir": 1
    }
    lesAliens: List[Dict[str, int]] = []
    generationAliens(lesAliens, lePlateau)

    #initialisation de la récupération des actions utilisateur
    action : str or None = "x"
    kb : SaisiCar = SaisiCar()

    #Boucle principale
    while lePlateau["vie"] > 0 and action != "q":

        #Vérification d'une possible fin de partie
        finj : bool = finJeu(lePlateau, lesAliens, leVaisseau)

        if finj:
            #Deux cas, 
            # 1: il n'y a plus d'aliens, il faut donc augmenter le niveau
            # 2: il reste des aliens, alors le joueur doit perdre une vie et le vaisseau doit perdre son tir spécial
            if len(lesAliens) > 0:
                lePlateau["vie"] -= 1
                leVaisseau["tir"] = 1
                lesAliens.clear()
            else:
                lePlateau["level"] += 1

            #On génère de nouveau aliens
            generationAliens(lesAliens, lePlateau)

        #On vérifie s'il existe un tir Spécial sur le plateau, si Oui on le fait tomber progressivement (1 ligne par frame)
        if lePlateau["tirS"] != None:
            lePlateau["tirS"] = (lePlateau["tirS"][0], lePlateau["tirS"][1]+1, lePlateau["tirS"][2]) 
        
        #On déplace les aliens d'un cran
        deplacementAliens(lesAliens, lePlateau)

        #On récuppère une possible action faite par l'utilisateur (une touche du clavier)
        action = kb.recupCar(["m", "k", "o", "q"])

        #En fonction de l'action de l'utilisateur, on déplace le vaisseau ou bien on tire
        aTir : bool = actionVaisseau(action, leVaisseau, lePlateau)
        
        #Si on tire 
        if aTir :
            #On récupère l'alien le plus bas étant sur la même colonne que le vaisseau
            alienTue : int or None = alienAtteint(lesAliens, leVaisseau["posx"])
            
            aliensMorts : int
            tirSpecial : int
            #On tue le ou les aliens en fonction de la position du tir on récupère alors le nombre d'alien tué et le tir spécial laché de plus haut niveau (0,2,3)
            aliensMorts,tirSpecial = tuerAliens(leVaisseau, lesAliens)
            
            #Si le tir spécial n'est pas 0
            if tirSpecial in [2,3]:
                #On place le tir spécial sur le plateau grace à un triplet (position X, position Y, Niveau du tir)
                lePlateau["tirS"] = (leVaisseau["posx"], alienTue, tirSpecial)
            #On actualise le score en fonction des aliens tués
            lePlateau["score"] += 5 * aliensMorts

            #On affiche le plateau avec un tir
            affichagePlateau(lePlateau, lesAliens, leVaisseau, alienTue)
        else:
            #On affiche le plateau sans tir
            affichagePlateau(lePlateau, lesAliens, leVaisseau)

        
        #On marque une pose dans l'affichage car sinon le jeu serait injouable
        sleep(0.05)
        