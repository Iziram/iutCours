"""! @brief [description du fichier]
 @file app_baignoire.py
 @section libs Librairies/Modules
 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 21/09/2022 .
"""
from time import sleep
import threading


class Baignoire:
    def __init__(
        self, vol_max: int, vol_init: int, tempo_remplissage: float, tempo_fuite: float
    ) -> None:
        self.__volume_maxi: int = vol_max
        self.__volume: int = vol_init
        self.__tempo_remplissage: float = tempo_remplissage
        self.__tempo_fuite: float = tempo_fuite
        self.__fin: bool = None

    def remplir(self, qantite: int) -> None:
        self.__fin = False
        while not self.__fin and self.__volume + qantite < self.__volume_maxi:
            self.__volume += qantite
            sleep(self.__tempo_remplissage)
            print(f" remplissage : volume de la baigoire : {self.__volume:.2f}")
        self.__volume = self.__volume_maxi
        self.__fin = True

    def fuite(self, qantite: int) -> None:
        self.__fin = False
        while not self.__fin and self.__volume - qantite > 0:
            self.__volume -= qantite
            sleep(self.__tempo_fuite)
            print(f" fuite : volume de la baigoire : {self.__volume:.2f}")
        self.__volume = 0
        self.__fin = True


def pgrm_simple(vmax, vinit, tmp_remp, tmp_f):
    baignoire = Baignoire(vmax, vinit, tmp_remp, tmp_f)

    print("Remplissage")
    baignoire.remplir(5.5)
    print("Fuite")
    baignoire.fuite(4.5)


def pgrm_thread(vmax, vinit, tmp_remp, tmp_f, nb_r, nb_f):
    baignoire = Baignoire(vmax, vinit, tmp_remp, tmp_f)

    th1 = threading.Thread(target=baignoire.remplir, name="remplir", args=(nb_r,))
    th2 = threading.Thread(target=baignoire.fuite, name="fuire", args=(nb_f,))

    th1.start()
    th2.start()


if __name__ == "__main__":
    print("Simple")
    # pgrm_simple(60, 0, 0.5, 0.5)
    print("Thread")
    pgrm_thread(100, 50, 0.5, 0.3, 10, 8)
    print("Thread2")
    # pgrm_thread(100, 50, 0.5, 0.3, 10, 5)
