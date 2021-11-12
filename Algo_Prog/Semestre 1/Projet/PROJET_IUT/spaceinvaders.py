from typing import List, Dict
from random import randint, sample

def affichageDebugPlateau(lePlateau : Dict[str, int]) -> None:
    """!
    Cette fonction permet d'afficher le plateau de façon textuel le plateau

    Args:
        lePlateau (Dict[str, int]): les informations du jeu sous la forme d'un dictionnaire.
    """
    assert type(lePlateau) == dict ,"la variable `lePlateau` doit être un dictionnaire"
    assert set(lePlateau.keys()) == {"L","H","vie","score","level"} ,"le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"
    
    print(f'largeur : {lePlateau["L"]} cases, ',
          f'hauteur : {lePlateau["H"]} lignes,',
          f'score : {lePlateau["score"]},',
          f'vie : {lePlateau["vie"]}, ',
          f'level : {lePlateau["level"]}.')
    
    
    
def affichagePlateau(lePlateau : Dict[str, int], lesAliens : List[Dict[str, int]], leVaisseau : Dict[str,int]) -> None:
    """!
    Cette fonction permet d'afficher le plateau, avec l'ensemble des 
    informations relative au jeu (niveau, vie, score) puis
    le plateau de jeu avec les aliens et le vaisseau

    Args:
        lePlateau (Dict[str, int]): [description]
    """
    assert type(lePlateau) == dict ,"la variable `lePlateau` doit être un dictionnaire"
    assert type(leVaisseau) == dict ,"la variable `leVaisseau` doit être un dictionnaire"
    assert type(lesAliens) == list ,"la variable `lesAliens` doit être une liste"
    assert set(lePlateau.keys()) == {"L","H","vie","score","level"} ,"`Erreur -> lePlateau :`le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"
    assert len([i for i in lesAliens if type(i) != dict]) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"
    assert set(leVaisseau.keys()) == {"posx","tir"} ,"`Erreur -> leVaisseau :`le dictionnaire doit avoir comme clé : `posx;tir`"
    
    print("-" * 40)
    print(" " * 4 + "SCORE" + " " * 4 + "VIE" + " " * 4 + "NIVEAU")
    print(f'    {lePlateau["score"]:5}  {lePlateau["vie"] : 5}     {lePlateau["level"] : 5}')
    print("-" * 40)
    
    #code couleur : 
    couleur_alien : str = "\033[0;32;40m"
    couleur_vaisseau : str = "\033[0;31;40m"
    
    #affichage des aliens, du vaisseau
    affichage : str = ""
    for y in range(lePlateau["H"]):
        for x in range(lePlateau["L"]):
            caractere : str = " "
            for a in lesAliens:
                if a["posx"] == x and a["posy"] == y :
                    caractere = f'{couleur_alien}@'
            if y == lePlateau["H"] - 1 and x == leVaisseau["posx"]:
                caractere = f'{couleur_vaisseau}#'
            affichage += caractere
        print(affichage)
        affichage = ""
    print(f"\033[0;37;40m")
    print("-" * 40)

def generationAliens(
        lesAliens: List[Dict[str, int]], lePlateau: Dict[str, int]) -> None:
    """!
    Cette fonction permet de générer les aliens en fonction du niveau du jeu

    Args:
        lesAliens (List[Dict[str, int]]): la liste des Aliens (supposée vide)
        lePlateau (Dict[str, int]): le dictionnaire représentant les informations du plateau de jeu.
    """
    assert type(lePlateau) == dict ,"la variable `lePlateau` doit être un dictionnaire"
    assert type(lesAliens) == list ,"la variable `lesAliens` doit être une liste"
    assert set(lePlateau.keys()) == {"L","H","vie","score","level"} ,"`Erreur -> lePlateau :`le dictionnaire doit avoir comme clé : `L;H;vie;level;score`"
    assert len([i for i in lesAliens if type(i) != dict]) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"
    
    nbAliens: int = lePlateau["level"] * 10 + 20
    nbAliensParLigne: int = 10
    ligneCourante: int = -1
    nbAliensAvecTirs: int = 5
    i: int
    for i in range(nbAliens):
        alien: Dict[str, int] = {}

        if i % nbAliensParLigne == 0:
            ligneCourante += 1

        alien["posx"] = i % nbAliensParLigne + lePlateau["L"] // 2 - nbAliensParLigne //2
        alien["posy"] = ligneCourante
        alien["sens"] = 0
        alien["tir"] = 0

        lesAliens.append(alien)

    # sample est une fonction du module Random qui permet de tirer un sous ensemble aléatoire de taille k parmi une population
    # dans notre cas, la population c'est la liste lesAliens et la taille c'est nbAliensAvecTirs
    aliensAvecTirs: List[int] = sample(lesAliens, nbAliensAvecTirs)
    for alien in aliensAvecTirs:
        alien["tir"] = randint(2,3)

def affichageDebugAlien(lesAliens : List[Dict[str,int]]) -> None:
    """!
    Cette fonction permet d'afficher les aliens dans leur forme primaire (un dictionnaire) 

    Args:
        lesAliens (List[Dict[str,int]]): Une liste de dictionnaire représentant les aliens.
    """
    assert type(lesAliens) == list, "le paramètre `lesAliens` doit être une liste"
    assert len([i for i in lesAliens if type(i) != dict]) == 0, "le paramètre `lesAliens` doit être une liste de dictionnaires"
    a : Dict[str, int]
    for a in lesAliens:
        print(a)

if __name__ == "__main__":
    
    lePlateau : Dict[str, int] = {
    "L" : 25,
    "H" : 20,
    "score" : 0,
    "vie" : 3,
    "level" : 1
    }
    leVaisseau : Dict[str, int] = {
        "posx": lePlateau["L"] // 2,
        "tir" : 1
    }
    lesAliens : List[Dict[str, int]] = []
    
    generationAliens(lesAliens, lePlateau)
    # affichageDebugPlateau(lePlateau)
    affichagePlateau(lePlateau, lesAliens, leVaisseau)
    # affichageDebugAlien(lesAliens)