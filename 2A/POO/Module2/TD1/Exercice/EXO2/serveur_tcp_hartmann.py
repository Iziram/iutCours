from socket import socket, AF_INET, SOCK_STREAM
import sys


class ServiceEcoute:
    def __init__(self, port_serveur: int) -> None:
        # Mise en écoute

        self.__socket_ecoute: socket = socket(
            AF_INET, SOCK_STREAM)
        self.__socket_ecoute.bind(("", port_serveur))

        self.__socket_ecoute.listen(1)

        # Affichage du message
        print(f"Le serveur écoute sur le port {port_serveur}")

    def attente(self) -> socket:
        # Attente de connexion
        connexion, ADDR = self.__socket_ecoute.accept()
        # Affichage des informations
        print(f"Informations du client : {connexion} ip: {ADDR}")
        # Fermeture du socket d'écoute
        self.__socket_ecoute.close()
        # Retourne le socket d'échange
        return connexion


class ServiceEchange:
    def __init__(self, socket_echange: socket) -> None:
        self.__socket_echange: socket = socket_echange

    def envoyer(self, msg: str) -> None:
        tab_bytes: list[bytes] = msg.encode("utf-8")
        self.__socket_echange.send(tab_bytes)

    def recevoir(self) -> str:
        tab_bytes: list[bytes] = self.__socket_echange.recv(255)
        print(tab_bytes)
        msg: str = tab_bytes.decode("utf-8")
        return msg

    def echange(self) -> None:
        # vérif bytes vide
        try:
            while True:
                msg_client: str = self.recevoir()
                print(f"Client:  {msg_client}")
                msg_server: str = f"[{msg_client}]"
                self.envoyer(msg_server)
        except:
            self.arret()

    def arret(self) -> None:
        self.__socket_echange.close()
        print("Le serveur a fermé sa connexion")


if __name__ == "__main__":
    # declaration des variables
    port_ecoute: int = None
    service_ecoute: ServiceEcoute = None
    socket_client: socket = None
    service_echange: ServiceEchange = None
    # lecture des parametres (le numero de port)
    if len(sys.argv) >= 2:
        port_ecoute = int(sys.argv[1])
    else:
        port_ecoute = 5000
    try:
        service_ecoute = ServiceEcoute(port_ecoute)
        socket_client = service_ecoute.attente()
        service_echange = ServiceEchange(socket_client)
        service_echange.echange()
    except Exception as err:
        print("erreur : " + str(err))
