from typing import List, Dict


def recuperationAliensSurX(
        lesAliens: List[Dict[str, int]], lePlateau: Dict[str, int], posx: int) -> List[Dict[str, int]]:
    alienOnX: list = [
        x for x in lesAliens if x["posx"] +
        lePlateau["L"] //
        2 -
        5 == posx]
    return sorted(
        alienOnX,
        key=lambda k: k['posy'],
        reverse=True)


def alienAtteignable(lesAliens: List[Dict[str, int]],
                     posx: int,
                     lePlateau: Dict[str, int]) -> None or int:
    lowestAliens: List[Dict[str, int]] = recuperationAliensSurX(
        lesAliens, lePlateau, posx)
    if len(lowestAliens) >= 1:
        return lowestAliens[0]["posy"]


def gestionTir(leVaisseau: Dict[str,
                                int],
               alienAtteignable: int or None,
               lesAliens: List[Dict[str,
                                    int]],
               lePlateau: Dict[str,
                               int]) -> int:

    nbAliensTues: int = 0
    if alienAtteignable is not None:
        for ignored in range(leVaisseau["tir"]):
            aTuer: List[Dict[str, int]] = recuperationAliensSurX(
                lesAliens, lePlateau, leVaisseau["posx"])
            if(len(aTuer) > 0 and aTuer[0] in lesAliens):
                lesAliens.remove(aTuer[0])
                aTuer.pop(0)
                nbAliensTues += 1
        aliensSurX: list = [
            x for x in lesAliens if x["posx"] == leVaisseau["posx"]]

    return nbAliensTues
