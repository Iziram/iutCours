from typing import List, Dict


class Etudiant:
    MAX_CREDITS: int = 60

    def __init__(self, nom) -> None:
        self.__nom: str = nom
        self.__liste_notes: List[float] = []

    def ajouter_note(self, note: float) -> None:
        self.__liste_notes.append(note)

    def ajouter_notes(self, notes: List[float]) -> None:
        self.__liste_notes += notes

    def calcul_credit(self) -> int:
        pass

    def get_liste_notes(self) -> List[float]:
        return self.__liste_notes

    def get_moyenne(self) -> float:
        if len(self.__liste_notes) > 0:
            return sum(self.__liste_notes) / len(self.__liste_notes)
        return 0.0

    def get(self) -> str:
        base: str = f"{self.__nom}({type(self).__name__})"
        average: str = ""
        notes: str = ""
        credit: str = ""
        if len(self.__liste_notes) > 0:
            notes = f" notes : {self.__liste_notes}"
            average = f" moyenne : {self.get_moyenne():.4}"
        credit = f" ECTS : {self.calcul_credit()}"
        return base + notes + average + credit

    def get_dict(self) -> Dict[str, any]:
        representation: Dict[str, any] = self.__dict__
        ects: int = 0
        if isinstance(self, EtudiantBUT):
            ects = EtudiantBUT.calcul_credit(self)
        elif isinstance(self, EtudiantLP):
            ects = EtudiantLP.calcul_credit(self)

        representation[f"_{Etudiant.__name__}__ECTS"] = ects
        return representation


class EtudiantBUT(Etudiant):
    def __init__(self, nom) -> None:
        Etudiant.__init__(self, nom)

    def calcul_credit(self) -> int:
        credit: int = 0
        if len(self.get_liste_notes()) > 0 and self.get_moyenne() > 10:
            credit = Etudiant.MAX_CREDITS
        return credit


class EtudiantLP(Etudiant):
    def __init__(self, nom) -> None:
        Etudiant.__init__(self, nom)

    def calcul_credit(self) -> int:
        credit = 0
        if len(self.get_liste_notes()) > 0:
            good_notes: List[float] = [
                note for note in self.get_liste_notes() if note > 10
            ]
            credit: int = int(
                len(good_notes) / len(self.get_liste_notes()) * Etudiant.MAX_CREDITS
            )
        return credit


if __name__ == "__main__":
    # Déclarer une variable de type liste d'étudiants appelée liste_etudiants
    liste_etudiants: List[Etudiant]
    # Instancier le liste
    liste_etudiants = []
    # Ajouter 3 étudiants à la liste
    # BOB, étudiant en BUT, "BILL" étudiant en LP et CHUCK étudiant en LP
    liste_etudiants.append(EtudiantBUT("BOB"))
    liste_etudiants.append(EtudiantLP("BILL"))
    liste_etudiants.append(EtudiantLP("CHUCK"))
    # afficher les étudiants
    for etu in liste_etudiants:
        print(etu.get())
    # Ajouter 3 notes à BOB : 10, 15 et 9
    liste_etudiants[0].ajouter_notes([10, 15, 9])
    # Ajouter 3 notes à BIL : 12, 15, 18
    liste_etudiants[1].ajouter_notes([12, 15, 18])

    # Ajouter 3 note également à CHUCK : 7, 12 et 15
    liste_etudiants[2].ajouter_notes([7, 12, 15])
    # afficher les résultats de tous les étudiants en utilisant la méthode get()
    for etu in liste_etudiants:
        print(etu.get())
    # afficher le dictionnaire associé à chaque étudiant
    for etu in liste_etudiants:
        print(etu.get_dict())
