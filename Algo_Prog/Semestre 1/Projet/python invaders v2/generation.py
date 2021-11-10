from random import randint
from typing import List, Dict


def generationAliens(
        lesAliens: List[Dict[str, int]], lePlateau: Dict[str, int]) -> None:
    nbAliens: int = lePlateau["level"] * 10 + 20
    nbAliensParLigne: int = 10
    ligneCourante: int = -1
    nbAliensAvecTirs: int = 5
    i: int
    for i in range(nbAliens):
        alien: Dict[str, int] = {}

        if i % nbAliensParLigne == 0:
            ligneCourante += 1

        alien["posx"] = i % nbAliensParLigne
        alien["posy"] = ligneCourante
        alien["sens"] = 0
        alien["tir"] = 0

        lesAliens.append(alien)

    aliensAvecTirs: List[int] = []
    while len(aliensAvecTirs) < nbAliensAvecTirs:
        alien: int = randint(0, len(lesAliens) - 1)
        if alien not in aliensAvecTirs:
            lesAliens[alien]["tir"] = randint(2, 3)
            aliensAvecTirs.append(alien)
