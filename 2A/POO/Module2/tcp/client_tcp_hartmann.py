from socket import socket, AF_INET, SOCK_STREAM

import sys


class Client:
    def __init__(self, ip_server: str, port_server: int) -> None:
        self.__ip_serv: str = ip_server
        self.__port_serv: int = port_server

        self.__socket_echange: socket = socket(AF_INET, SOCK_STREAM)
        self.__fin: bool = False

    def connexion(self) -> bool:

        try:
            self.__socket_echange.connect((self.__ip_serv, self.__port_serv))
            return True

        except:
            print("La connexion n'a pas pu se faire")
            return False

    def envoyer(self, msg: str) -> None:
        if msg == "":
            msg = " "
        tab_bytes: list[bytes] = msg.encode("utf-8")

        self.__socket_echange.send(tab_bytes)

    def recevoir(self) -> str:

        tab_bytes: list[bytes] = self.__socket_echange.recv(255)

        msg: str = tab_bytes.decode("utf-8")

        return msg

    def echange(self) -> None:

        while not self.__fin:

            msg: str = input("Message à transmettre: ")

            self.envoyer(msg)

            msg_server: str = self.recevoir()
            print(f"Server:  {msg_server}")
            self.__fin = msg_server == "[fin]"

    def arret(self) -> None:
        self.__fin = True
        self.__socket_echange.close()


if __name__ == "__main__":

    # declaration des variables

    ip_serveur: str = None

    port_serveur: int = None

    client: Client = None

    # lecture des paramètres

    if len(sys.argv) == 3:

        ip_serveur = sys.argv[1]

        port_serveur = int(sys.argv[2])
    else:

        ip_serveur = "127.0.0.1"

        port_serveur = 5000

    client = Client(ip_serveur, port_serveur)

    if client.connexion():
        client.echange()
        client.arret()
