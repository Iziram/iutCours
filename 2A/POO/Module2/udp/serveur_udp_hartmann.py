from socket import socket, AF_INET, SOCK_DGRAM


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


if __name__ == "__main__":
    # declaration des variables
    port_ecoute_echange: int = None
    serveur_udp: Serveur_UDP
    # initialisation
    port_ecoute_echange = 5000
    # instanciation
    serveur_udp = Serveur_UDP(port_ecoute_echange=port_ecoute_echange)
    # traitement
    serveur_udp.echange()
    serveur_udp.close()
