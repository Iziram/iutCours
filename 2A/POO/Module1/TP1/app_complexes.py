from math import atan2, cos, sin, pi
import copy


class Complexe:
    MODE_REPRESENTATION = "math"

    def __init__(self) -> None:
        self.__reel = None
        self.__img = None

    def set_rectangulaires(self, reel: float, img: float) -> None:
        self.__reel = reel
        self.__img = img

    def set_polaire(self, ro: float, teta: float) -> None:
        self.__reel = ro * cos(teta)
        self.__img = ro * sin(teta)

    def get_reel(self) -> float:
        return self.__reel

    def get_img(self) -> float:
        return self.__img

    def get_ro(self) -> float:
        return (self.__reel**2 + self.__img**2) ** 0.5

    def get_teta(self) -> float:
        return atan2(self.__reel, self.__img)

    def get(self) -> str:
        message: str = ""
        if Complexe.MODE_REPRESENTATION == "math":
            message = f"{self.__reel} + {self.__img} * i"
        elif Complexe.MODE_REPRESENTATION == "elec":
            message = f"[{self.get_ro()};{self.get_teta()}]"
        return message

    @staticmethod
    def change_mode(nouveau_mode: str) -> None:
        if nouveau_mode in ("math", "elec"):
            Complexe.MODE_REPRESENTATION = nouveau_mode


class MaClasseMath:
    """!
    @brief [Description de la classe]


    """

    @staticmethod
    def addition(c_1: Complexe, c_2: Complexe) -> Complexe:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param c_1 : Complexe => [description]
            @param c_2 : Complexe => [description]
        Retour de la fonction :
            @return Complexe => [description]

        """
        calcul: Complexe
        calcul = Complexe()
        calcul.set_rectangulaires(
            c_1.get_reel() + c_2.get_reel(), c_1.get_img() + c_2.get_img()
        )
        return calcul

    @staticmethod
    def soustraire(c_1: Complexe, c_2: Complexe) -> Complexe:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param c_1 : Complexe => [description]
            @param c_2 : Complexe => [description]
        Retour de la fonction :
            @return Complexe => [description]

        """
        calcul: Complexe
        calcul = Complexe()
        calcul.set_rectangulaires(
            c_1.get_reel() - c_2.get_reel(), c_1.get_img() - c_2.get_img()
        )
        return calcul

    @staticmethod
    def multiplier(c_1: Complexe, c_2: Complexe) -> Complexe:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param c1 : Complexe => [description]
            @param c2 : Complexe => [description]
        Retour de la fonction :
            @return Complexe => [description]

        """
        calcul: Complexe = Complexe()

        calcul.set_polaire(c_1.get_ro() * c_2.get_ro(), c_1.get_teta() + c_2.get_teta())

        return calcul

    @staticmethod
    def diviser(c_1: Complexe, c_2: Complexe) -> Complexe:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param c1 : Complexe => [description]
            @param c2 : Complexe => [description]
        Retour de la fonction :
            @return Complexe => [description]

        """
        calcul: Complexe = Complexe()

        calcul.set_polaire(c_1.get_ro() / c_2.get_ro(), c_1.get_teta() - c_2.get_teta())

        return calcul


if __name__ == "__main__":
    # déclarez variables de type Complexe nommés z1, z2, z3, z4 et z5
    z1: Complexe = Complexe()
    z2: Complexe = Complexe()
    z3: Complexe = Complexe()
    z4: Complexe = Complexe()
    z5: Complexe = Complexe()
    # instanciez z1, z2, z3
    # initialisez z1 avec les valeurs [1.0 ; 45.0°]
    z1.set_polaire(1.0, pi / 4)

    # instanciez z2 avec les valeurs Re= 0.7071 Im=-0.7071
    z2.set_rectangulaires(0.7071, -0.7071)
    # afficher les 3 complexes
    print(z1.get())
    print(z2.get())
    print(z3.get())
    print("---------suite------------")
    # Modifier les coordonnées de z3 avec les valeurs : Ro=2.0 Téta=90.0
    z3.set_polaire(2.0, pi / 2)
    # copier z3 dans z4 en utilisant la méthode copy du module copy
    z4 = copy.copy(z3)
    # modification de z4 pour vérification avec les valeurs Re=0.0 et Im=0.0
    z4.set_rectangulaires(0.0, 0.0)
    # afficher z4
    print(z4.get())
    # Multiplier z1 par z2 et mettre le résultat dans z5
    z5 = MaClasseMath.multiplier(z1, z2)
    # Ajouter z1 par z2 et mettre le résultat dans z6
    z6 = MaClasseMath.addition(z1, z2)
    print("---------nouveau mode affichage------------")
    # changer le mode d'affichage et afficher les – complexes
    Complexe.change_mode("elec")
    print(z1.get())
    print(z2.get())
    print(z3.get())
    print(z4.get())
    print(z5.get())
    print(z6.get())
