from typing import Dict, Tuple, List


class Article:
    def __init__(self, nom: str, quantite: int, prix: float):
        self.set(nom, quantite, prix)

    def set(self, nom: str, quantite: int, prix: float) -> None:
        self.__nom: str = nom
        self.__quantite: int = quantite
        self.__prix: float = prix

    def acheter(self, quantite: int) -> float:
        total: float = None
        if quantite <= self.__quantite:
            total = quantite * self.__prix
            self.__quantite -= quantite
        else:
            total = None
        return total

    def get(self) -> str:
        return f"Nom : {self.__nom} | Quantité : {self.__quantite} | Prix Unitaire : {self.__prix}€"

    def get_nom(self) -> str:
        return self.__nom

    def get_quantite(self) -> int:
        return self.__quantite

    def get_prix(self) -> float:
        return self.__prix

    def get_dict(self) -> Dict[str, str or int or float]:
        return self.__dict__

    def get_attributs(self) -> Tuple[str, int, float]:
        return (self.__nom, self.__quantite, self.__prix)


class Magasin:
    def __init__(self) -> None:
        self.__liste_articles: List[Article] = []
        self.__chiffre_affaire: float = 0.0

    def ajouter(self, nom: str, quantite: int, prix: float) -> None:
        self.__liste_articles.append(Article(nom, quantite, prix))

    def acheter(self, indice: int, quantite: int) -> float:
        total: float = 0.0
        if indice < len(self.__liste_articles):
            total = self.__liste_articles[indice].acheter(quantite)
            if total:
                self.__chiffre_affaire += total
        return total

    def get(self) -> str:
        return str([a.get_attributs() for a in self.__liste_articles])

    def get_indice(self, nom: str) -> int:
        iterator: int = 0
        indice: int = -1
        while iterator < len(self.__liste_articles):
            if self.__liste_articles[iterator].get_nom() == nom:
                indice = iterator
                iterator = len(self.__liste_articles)
            iterator += 1
        return indice

    def get_chiffre_affaire(self) -> float:
        return self.__chiffre_affaire


if __name__ == "__main__":
    print("---- Première partie : Objets simples ----")
    a1: Article
    a2: Article
    a3: Article

    a1 = Article("Bols", 100, 10.23)
    a2 = Article("Chemises", 50, 45.32)
    a3 = Article("Guitares", 35, 150.0)

    print("- Get")
    print(a1.get())
    print(a2.get())
    print(a3.get())
    print("- Acheter")
    print(a1.acheter(5))
    print(a2.acheter(3))
    print("- Attributs")
    print(a1.get_attributs())
    print(a2.get_attributs())
    print(a3.get_attributs())

    print("-------- un magasin, une liste d'articles ----------------")
    # déclare une variable de Type Magasin appeler magasin
    magasin: Magasin
    # instancier l'objet magasin
    magasin = Magasin()
    # ajouter 3 articles au magasin
    magasin.ajouter("bols", 100, 10.23)
    magasin.ajouter("chemises", 50, 45.32)
    magasin.ajouter("guitares", 35, 150.0)
    # afficher tous les attributs des articles du magasin
    print(magasin.get())
    # acheter 5 éléments au 1er article et afficher de cout correspondant
    print(magasin.acheter(0, 5))
    # acheter 3 éléments de 2eme article et afficher de cout correspondant
    print(magasin.acheter(1, 3))
    # afficher de chiffre d'affaires global (tous les articles)
    print(magasin.get_chiffre_affaire())
    print("---------- acheter a partir du nom -----------")
    # acheter 2 guitares et afficher le cout
    print(magasin.acheter(magasin.get_indice("guitares"), 2))
    # afficher à nouveau tous les attributs des articles du magasin
    print(magasin.get())
