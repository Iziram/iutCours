from socket import socket, AF_INET, SOCK_STREAM, timeout
import sys
from threading import Thread


class ServiceEchange:
    pass


class Manager:
    CLIENTS: dict[socket, str] = {}

    @classmethod
    def nouveau_client(cls, client: ServiceEchange) -> None:
        cls.CLIENTS[client] = f"Client {len(cls.CLIENTS) + 1}"

    @classmethod
    def retirer_client(cls, client: ServiceEchange):
        cls.CLIENTS.pop(client)

    @classmethod
    def afficher(cls):
        return cls.CLIENTS.__str__


class ServiceEchange(Thread):
    def __init__(self, socket_echange: socket) -> None:
        Thread.__init__(self)
        self.__socket_echange: socket = socket_echange

    def envoyer(self, msg: str) -> None:
        tab_bytes: list[bytes] = msg.encode("utf-8")
        self.__socket_echange.send(tab_bytes)

    def recevoir(self) -> str:
        tab_bytes: list[bytes] = self.__socket_echange.recv(255)
        msg: str = tab_bytes.decode("utf-8")
        return msg

    def run(self):
        self.echange()

    def echange(self) -> None:
        fin: bool = False
        # vérif bytes vide
        try:
            while not fin:
                msg_client: str = self.recevoir()
                print(f"{Manager.CLIENTS[self]}:  {msg_client}")
                if msg_client == "fin":
                    fin = True
                msg_server: str = f"[{msg_client}]"
                self.envoyer(msg_server)
            self.recevoir()
        except:
            print(f"Le serveur a fermé sa connexion avec {Manager.CLIENTS[self]}")
            self.arret()

    def arret(self) -> None:
        self.__socket_echange.close()
        Manager.retirer_client(self)


class ServiceEcoute:
    def __init__(self, port_serveur: int) -> None:
        # Mise en écoute
        self.__port_serveur: int = port_serveur
        self.__socket_ecoute: socket = None
        self.__socket_ecoute: socket = socket(AF_INET, SOCK_STREAM)
        self.__socket_ecoute.bind(("", port_serveur))
        self.__socket_ecoute.listen(1)
        self.__socket_ecoute.settimeout(20)
        # Affichage du message
        print(f"Le serveur écoute sur le port {port_serveur}")

    def attente(self) -> socket:
        timedOut: bool = False
        while not timedOut:
            try:
                # Attente de connexion
                connexion, ADDR = self.__socket_ecoute.accept()
                # Affichage des informations
                print(f"Informations du client : {connexion} ip: {ADDR}")
                # Créer un nouveau thread service echange
                service: ServiceEchange = ServiceEchange(connexion)
                Manager.nouveau_client(service)
                service.start()
            except timeout:
                timedOut = True
                self.__socket_ecoute.close()
                print("Le server n'écoute plus car le délai d'attente est dépassé")


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
        # service_echange(socket_client)
    except Exception as err:
        print("erreur : " + str(err))
