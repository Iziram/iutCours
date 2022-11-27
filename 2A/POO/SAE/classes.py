from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM


class Client_UDP:
    def __init__(self, ip_serveur: str, port_serveur: int) -> None:
        self.__ip_serveur: str = ip_serveur
        self.__port_serveur = port_serveur
        self.__socket_echange: socket = socket(AF_INET, SOCK_DGRAM)

    def recevoir(self) -> str:
        try:
            tab_bytes, ADDR = self.__socket_echange.recvfrom(255)
            return tab_bytes.decode("utf-8")
        except:
            return "[fin]"

    def envoyer(self, msg: str) -> None:
        self.__socket_echange.sendto(
            msg.encode("utf-8"), (self.__ip_serveur, self.__port_serveur)
        )

    def echange(self) -> None:
        fin: bool = False

        while not fin:

            msg: str = input("Message à transmettre: ")

            self.envoyer(msg)

            msg_server: str = self.recevoir()
            print(f"Server:  {msg_server}")
            fin = msg_server == "[fin]"

    def close(self) -> None:
        self.__socket_echange.close()


class Serveur_UDP:
    def __init__(self, port_ecoute_echange: int) -> None:
        self.__socket_ecoute_echange = socket(AF_INET, SOCK_DGRAM)
        self.__socket_ecoute_echange.bind(("", port_ecoute_echange))
        self.__addr_client: set = set()

    def recevoir(self) -> str:
        tab_bytes, ADDR = self.__socket_ecoute_echange.recvfrom(255)
        self.__addr_client = ADDR
        return tab_bytes.decode("utf-8")

    def envoyer(self, msg: str) -> None:
        tab_bytes: bytes = f"[{msg}]".encode("utf-8")
        self.__socket_ecoute_echange.sendto(tab_bytes, self.__addr_client)

    def echange(self) -> None:
        msg: str = "X"
        while msg != "fin":
            msg = self.recevoir()
            print(f"Client: {msg}")
            self.envoyer(msg)

    def close(self) -> None:
        self.__socket_ecoute_echange.close()
        print(f"Le serveur à fini son écoute")
