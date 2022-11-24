from socket import socket, AF_INET, SOCK_DGRAM
import os
from threading import Thread
from random import randint


class Client_UDP:
    def __init__(self, ip_serveur: str, port_serveur: int) -> None:
        self.__ip_serveur: str = ip_serveur
        self.__port_serveur = port_serveur
        self.__socket_echange: socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket_echange.bind((ip_serveur, randint(25000, 65000)))

        self.__fin: bool = False
        self.__thread_recevoir: Thread = Thread(target=self.recevoir)
        self.__thread_recevoir.start()

    def recevoir(self) -> str:
        try:

            while not self.__fin:
                tab_bytes, ADDR = self.__socket_echange.recvfrom(1024)
                msg: str = tab_bytes.decode("utf-8")
                print(f"{msg}")

                if msg == "[fin]":
                    self.__fin = True
        except:
            client_udp.arret_brutal()

    def envoyer(self) -> None:
        while not self.__fin:
            msg: str = input("")
            if not self.__fin:
                self.__socket_echange.sendto(
                    msg.encode("utf-8"), (self.__ip_serveur, self.__port_serveur)
                )

    def close(self) -> None:
        self.__socket_echange.close()

    def arret_brutal(self) -> None:
        self.__socket_echange.close()
        print("fermeture brutale de l'apprication par le serveur")
        os._exit(0)


if __name__ == "__main__":
    # declaration des variables
    ip_serveur: str = None
    port_serveur: int = None
    client_udp: Client_UDP
    # initialisation
    ip_serveur = "127.0.0.1"
    port_serveur = 5000
    # instanciation:
    client_udp = Client_UDP(ip_serveur=ip_serveur, port_serveur=port_serveur)
    client_udp.envoyer()
    client_udp.close()
