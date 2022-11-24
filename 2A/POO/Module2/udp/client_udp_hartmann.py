from socket import socket, AF_INET, SOCK_DGRAM


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
    client_udp.echange()
    client_udp.close()
