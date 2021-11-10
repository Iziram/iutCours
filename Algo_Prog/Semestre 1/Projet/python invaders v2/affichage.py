from typing import List, Dict
from os import system


def affichagelePlateau(lePlateau: Dict[str, int]) -> None:

    print(f'largeur : {lePlateau["L"]} cases, ',
          f'hauteur : {lePlateau["H"]} lignes,',
          f'score : {lePlateau["score"]},',
          f'vie : {lePlateau["vie"]}, ',
          f'level : {lePlateau["level"]}.')


def affichagePlateau(lePlateau: Dict[str,
                                     int],
                     lesAliens: List[Dict[str,
                                          int]],
                     leVaisseau: Dict[str,
                     int],
                     lowestAlien: int or None = None) -> None:
    system("clear")
    # affichage lePlateau
    print("-" * lePlateau["L"])
    print(" " * 4 + "SCORE" + " " * 4 + "VIE" + " " * 4 + "NIVEAU")
    print(" " *
          8 +
          str(lePlateau["score"]) +
          " " *
          6 +
          str(lePlateau["vie"]) +
          " " *
          9 +
          str(lePlateau["level"]))
    print("-" * lePlateau["L"])

    # création plateau
    plateau: List[List[str]]
    plateau = [[" " for j in range(lePlateau["L"])]
               for i in range(lePlateau["H"])]

    # placement des aliens
    alien: Dict[str, int]
    for alien in lesAliens:
        plateau[alien["posy"]][alien["posx"] + lePlateau["L"] // 2 - 5] = "@"

    # placement vaisseau

    plateau[lePlateau["H"] - 1][leVaisseau["posx"]] = "#"

    # affichage du tir

    if lowestAlien is not None:
        file = open("test.txt", "a")
        file.write("\n" + str(lowestAlien))
        for y in range(lowestAlien, lePlateau["H"] - 1):
            if(leVaisseau["tir"] == 1):
                plateau[y][leVaisseau["posx"]] = ":"
            elif(leVaisseau["tir"] == 2):
                plateau[y][leVaisseau["posx"]] = "§"
            elif(leVaisseau["tir"] == 3):
                plateau[y][leVaisseau["posx"]] = "|"

    # affichage plateau

    for ligne in plateau:
        for caractere in ligne:
            print(caractere, end="")
        print("")
    print("-" * lePlateau["L"])


def affichageAliens(lesAliens: List[Dict[str, int]]) -> None:
    alien: Dict[str, int]
    for alien in lesAliens:
        print("\t", alien)


if __name__ == "__main__":
    from generation import generationAliens
    lesAliens: List[Dict[str, int]] = []
    lePlateau: Dict[str, int] = {
        "H": 12,
        "L": 25,
        "score": 0,
        "level": 1,
        "vie": 3
    }

    leVaisseau: Dict[str, int] = {
        "posx": lePlateau["L"] // 2,
        "tir": 1
    }
    generationAliens(lesAliens, lePlateau)
    affichagePlateau(lePlateau, lesAliens, leVaisseau, 3)
