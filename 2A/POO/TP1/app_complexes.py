from math import atan2, cos, sin, pi


class Complexe:
    MODE_REPRESENTATION = "math"

    def __init__(self, x: float, y: float) -> None:
        if Complexe.MODE_REPRESENTATION == "math":
            self.set_rectangulaires(x, y)
        elif Complexe.MODE_REPRESENTATION == "elec":
            self.set_polaire(x, y)

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
    @staticmethod
    def multiplier(c1: Complexe, c2: Complexe) -> Complexe:
        calcul: Complexe = None
        temp_mode: str = Complexe.MODE_REPRESENTATION
        Complexe.change_mode("elec")
        calcul = Complexe(
            c1.get_ro() * c2.get_ro(),
            (cos(c1.get_teta() + c2.get_teta()) + sin(c1.get_teta() + c2.get_teta())),
        )
        Complexe.change_mode(temp_mode)
        return calcul


if __name__ == "__main__":
    z1 = Complexe(-0.5, -0.5)
    print(z1.get())
    Complexe.change_mode("elec")
    print(z1.get())
    z2 = Complexe(5, -3 * pi / 2.0)
    Complexe.change_mode("math")
    print(z2.get())

    z3 = MaClasseMath.multiplier(z1, z2)
    print(z3.get())
