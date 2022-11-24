from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import os


class Serveur_UDP:
    def __init__(self, port_ecoute_echange: int) -> None:
        self.__socket_ecoute_echange = socket(AF_INET, SOCK_DGRAM)
        self.__socket_ecoute_echange.bind(("", port_ecoute_echange))
        self.__liste_addr_clients: list[tuple] = []

    def recevoir(self) -> str:
        try:
            tab_bytes, ADDR = self.__socket_ecoute_echange.recvfrom(255)
            if ADDR not in self.__liste_addr_clients:
                self.__liste_addr_clients.append(ADDR)
                print(f"Nouveau client : {ADDR}")
            msg: str = tab_bytes.decode("utf-8")
            if msg == "fin":
                self.__liste_addr_clients.remove(ADDR)
                self.envoyer("fin", ADDR)
                msg = None
            return msg
        except:
            pass

    def envoyer(self, msg: str, addr_client) -> None:
        tab_bytes: bytes = f"[{msg}]".encode("utf-8")
        self.__socket_ecoute_echange.sendto(tab_bytes, addr_client)

    def envoyer_a_tous(self, msg: str):
        tab_bytes: bytes = f"[{msg}]".encode("utf-8")
        for addr in self.__liste_addr_clients:
            try:
                self.envoyer(msg, addr)
            except:
                self.__liste_addr_clients.remove(addr)

    def echange(self) -> None:
        while True:
            msg = self.recevoir()
            if msg is not None:
                print(f"Client: {msg}")
                self.envoyer_a_tous(msg)

    def close(self) -> None:
        self.__socket_ecoute_echange.close()
        self.__liste_addr_clients.clear()
        print(f"Le serveur à fini son écoute")

    def commande(self):
        def envoie(*args):
            self.envoyer_a_tous(" ".join(args))

        def nb():
            print(f"Il y a {len(self.__liste_addr_clients)} clients en ligne")

        def delete(adresse_ip: str, port: str):
            client = (adresse_ip, int(port))
            try:
                self.__liste_addr_clients.remove(client)
                self.envoyer("fin", client)
            except:
                print("£: Le client n'existe pas")

        def quit():
            self.envoyer_a_tous("fin")
            self.close()
            print("Fin de l'application")
            os._exit(0)

        def liste():
            print(self.__liste_addr_clients)

        cmd: str = "X"
        cmdline: list[str] = []

        switch: dict = {
            "envoi": envoie,
            "nb": nb,
            "delete": delete,
            "quit": quit,
            "liste": liste,
        }

        while cmd != "quit":
            cmdline = input("£: ").split(" ")
            cmd = cmdline[0]

            commande: function = switch.get(cmd)
            if commande is not None:
                commande(*cmdline[1:])
            else:
                print("£: Commande invalide")


if __name__ == "__main__":
    # declaration des variables
    port_ecoute_echange: int = None
    serveur_udp: Serveur_UDP
    # initialisation
    port_ecoute_echange = 5000
    # instanciation
    serveur_udp = Serveur_UDP(port_ecoute_echange=port_ecoute_echange)
    # traitement
    commande_thread: Thread = Thread(target=serveur_udp.commande)
    commande_thread.start()
    serveur_udp.echange()
