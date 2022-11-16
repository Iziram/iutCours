from random import randint


class Devine(Exception):
    NB_TENTATIVES = -1
    NB_MAGIQUE = None

    def __init__(self, proposition, *args: object) -> None:
        super().__init__(*args)
        self.__proposition = proposition
        self.__fin = False
        Devine.NB_TENTATIVES += 1

    def get_fin(self) -> bool:
        return self.__fin

    def __str__(self) -> str:
        if Devine.NB_TENTATIVES >= 10:
            self.__fin = True
            return "Trop tard"
        if self.__proposition > Devine.NB_MAGIQUE:
            return "Trop Grand"
        if self.__proposition < Devine.NB_MAGIQUE:
            return "Trop petit"

        self.__fin = True

        return f"Bravo vous avez trouvé en {Devine.NB_TENTATIVES}"

    @staticmethod
    def set_nb_magique():
        Devine.NB_MAGIQUE = randint(0, 100)


if __name__ == "__main__":
    Devine.set_nb_magique()
    devine: Devine = Devine("-1")
    while not devine.get_fin():
        try:
            devine = Devine(int(input("nb: ")))
            raise devine
        except Devine as e:
            print(e)
