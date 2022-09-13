from typing import Dict


class Courrier:
    def __init__(self, poids: int, adresse: str) -> None:
        self.__poids: int = poids
        self.__adresse: str = adresse

    def valide(self) -> bool:
        return self.__adresse != ""

    def affranchir(self) -> float:
        pass

    def __str__(self) -> str:
        valide = "" if self.valide() else "\n\t(Courrier Invalide)"
        return f"""{type(self).__name__}{valide}
        Poids: {self.__poids} grammes
        Destination: {self.__adresse}
        Prix: {self.affranchir()}€
    """

    def get_poids(self) -> int:
        return self.__poids


class Lettre(Courrier):
    def __init__(self, poids, adresse, _format):
        Courrier.__init__(self, poids, adresse)
        self.__format = _format

    def affranchir(self) -> float:
        crits: Dict[str, int] = {
            "A4": 1,
            "A3": 2,
        }
        return crits[self.__format] + self.get_poids() / 1000

    def __str__(self) -> str:
        message: str = Courrier.__str__(self)
        message += f"\tFormat : {self.__format}"
        return message


class Colis(Courrier):
    def __init__(self, poids, adresse, volume):
        Courrier.__init__(self, poids, adresse)
        self.__volume = volume

    def valide(self) -> bool:
        return Courrier.valide(self) and self.__volume < 50

    def affranchir(self) -> float:
        return self.__volume * 0.25 + self.get_poids() / 1000

    def __str__(self) -> str:
        message: str = Courrier.__str__(self)
        message += f"\tVolume : {self.__volume} Litres"
        return message


class Boite:
    def __init__(self) -> None:
        self.__courriers = []

    def ajouter_courrier(self, *courrier: Courrier) -> None:
        self.__courriers += list(courrier)

    def affranchissement(self) -> float:
        return sum([courr.affranchir() for courr in self.__courriers])

    def courriers_invalides(self) -> int:
        return len([courr for courr in self.__courriers if not courr.valide()])

    def __str__(self) -> str:
        message: str = ""
        for courr in self.__courriers:
            message += courr.__str__() + "\n"
        return message


if __name__ == "__main__":
    # declarer trois références d'objets de type Courrier
    lettre: Courrier
    colis_1: Courrier
    colis_2: Courrier
    # instancier les trois courriers :
    # Lettre de 800 grammes sans adresse au format A4
    # Colis de 5 kg dont l'adresse est "IUT de Lannion" avec un volume de 30 litres
    # Colis de 3 kg dont l'adresse est "Place des Mouettes" avec un volume est 70 litres
    lettre = Lettre(800, "", "A4")
    colis_1 = Colis(5000, "IUT de Lannion", 30)
    colis_2 = Colis(3000, "Place des Mouettes", 70)
    # afficher les caractéristiques des trois courriers
    print(lettre)
    print(colis_1)
    print(colis_2)
    # seconde partie
    print("-------------gestion d'un boite------------------------")
    # déclarer une référence de boite de courriers
    boite: Boite
    # instancier le boite
    boite = Boite()
    # ajouter les 3 courriers à la boite
    boite.ajouter_courrier(lettre, colis_1, colis_2)
    # ajouter un nouveau courrier
    boite.ajouter_courrier(Lettre(50, "France", "A3"))
    # afficher les caractéristiques des courriers de la boite
    print(boite)
    # afficher le nombre de courriers invalides de la boite
    print(boite.courriers_invalides())
