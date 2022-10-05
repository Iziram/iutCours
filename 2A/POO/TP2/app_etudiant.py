from typing import List, Dict
import json


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

    def get_nom(self) -> str:
        return self.__nom

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

        if isinstance(self, Etudiant_BUT):

            ects = Etudiant_BUT.calcul_credit(self)

        elif isinstance(self, EtudiantLP):

            ects = EtudiantLP.calcul_credit(self)

        representation[f"_{Etudiant.__name__}__ECTS"] = ects

        representation["classe"] = self.__class__.__name__

        return representation


class Etudiant_BUT(Etudiant):

    def __init__(self, nom) -> None:

        Etudiant.__init__(self, nom)

    def calcul_credit(self) -> int:

        credit: int = 0

        if len(self.get_liste_notes()) > 0 and self.get_moyenne() > 10:

            credit = Etudiant.MAX_CREDITS
        return credit


class Etudiant_LP(Etudiant):

    def __init__(self, nom) -> None:

        Etudiant.__init__(self, nom)

    def calcul_credit(self) -> int:

        credit = 0

        if len(self.get_liste_notes()) > 0:

            good_notes: List[float] = [

                note for note in self.get_liste_notes() if note > 10

            ]

            credit: int = int(

                len(good_notes) / len(self.get_liste_notes()) *

                Etudiant.MAX_CREDITS
            )
        return credit


def init() -> List[Etudiant]:

    liste_etu: List[Etudiant] = []

    liste_etu.append(Etudiant_BUT("BOB"))

    liste_etu[-1].ajouter_notes((10.0, 15.0, 9.0,))

    liste_etu.append(Etudiant_LP("BILL"))

    liste_etu[-1].ajouter_notes((12.0, 15.0, 18.0,))

    liste_etu.append(Etudiant_LP("CHUCK"))

    liste_etu[-1].ajouter_notes((7.0, 12.0, 15.0,))
    return liste_etu


def sauvegarder(liste_etudiants: List[Etudiant], chemin) -> str:
    liste_dico = [etu.get_dict() for etu in liste_etudiants]
    return json.dumps(liste_dico)


def charger(json_str: str) -> List[Etudiant]:
    liste_dico = json.loads(json_str)
    liste_etu = []
    for dico in liste_dico:
        if dico["classe"] == "Etudiant_LP":
            etu = Etudiant_LP(dico["_Etudiant__nom"])
        elif dico["classe"] == "Etudiant_BUT":
            etu = Etudiant_LP(dico["_Etudiant__nom"])
        etu.ajouter_notes(dico["__liste_notes"])
        liste_etu.append(etu)
    return liste_etu


if __name__ == "__main__":

    # TP 2

    # # Déclarer une variable de type liste d'étudiants appelée liste_etudiants

    # liste_etudiants: List[Etudiant]

    # # Instancier le liste

    # liste_etudiants = []

    # # Ajouter 3 étudiants à la liste

    # # BOB, étudiant en BUT, "BILL" étudiant en LP et CHUCK étudiant en LP

    # liste_etudiants.append(EtudiantBUT("BOB"))

    # liste_etudiants.append(EtudiantLP("BILL"))

    # liste_etudiants.append(EtudiantLP("CHUCK"))

    # # afficher les étudiants

    # for etu in liste_etudiants:

    #     print(etu.get())

    # # Ajouter 3 notes à BOB : 10, 15 et 9

    # liste_etudiants[0].ajouter_notes([10, 15, 9])

    # # Ajouter 3 notes à BIL : 12, 15, 18

    # liste_etudiants[1].ajouter_notes([12, 15, 18])

    # # Ajouter 3 note également à CHUCK : 7, 12 et 15

    # liste_etudiants[2].ajouter_notes([7, 12, 15])

    # # afficher les résultats de tous les étudiants en utilisant la méthode get()

    # for etu in liste_etudiants:

    #     print(etu.get())

    # # afficher le dictionnaire associé à chaque étudiant

    # for etu in liste_etudiants:

    #     print(etu.get_dict())

    # TP 6

    liste_etudiants: List[Etudiant] = []

    choix: int = 0

    while choix != -1:

        print("-1 : quiter")

        print(" 0 : initialisation")

        print(" 1 : afficher toutes les informations")

        print(" 2 : ajouter un étudiant")

        print(" 3 : ajouter une note")

        print(" 4 : sauvegarder les donnees au format json (une liste de dictionnaires)")

        print(" 5: lire les donnees depuis un fichier au format json(une liste de dictionnaires)")

        choix = int(input("votre choix : "))

        if choix == 0:

            liste_etudiants = init()

        elif choix == 1:  # 1 : afficher toutes les informations

            print("--Affichage de toutes les informations : --")
            for e in liste_etudiants:
                print(e.get())
            print('-'*8)

        elif choix == 2:  # ajouter un étudiant

            nom = input("nom de l'etudiant : ")

            formation = input("quelle formation (BUT ou LP) ? ")
            if formation == "BUT":
                liste_etudiants.append(Etudiant_BUT(nom))
                print(f"L'étudiant {nom} a été inscrit en {formation}")

            elif formation == "LP":
                liste_etudiants.append(Etudiant_LP(nom))
                print(f"L'étudiant {nom} a été inscrit en {formation}")
            else:
                print("La formation n'est pas reconnue.")

        elif choix == 3:  # ajouter une note
            nom: str = input("Entrez le nom de l'étudiant : ")
            etu = None
            i = 0
            while etu == None and i < len(liste_etudiants):
                if liste_etudiants[i].get_nom() == nom:
                    etu = liste_etudiants[i]
                    i = len(liste_etudiants)
                else:
                    i += 1

            if i == len(liste_etudiants) and etu == None:
                print("Le nom n'existe pas dans la liste d'étudiants")
            else:
                note: int = int(input("Entrez la note (/20): "))
                etu.ajouter_note(note)
                print("La noté a été ajoutée.")

        elif choix == 4:  # sauvegarder les donnees au format json

            # vous définirez une fonction

            pass

        elif choix == 5:  # lire les donnees depuis un fichier au format json

            # vous définirez une fonction

            pass
