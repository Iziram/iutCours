from socket import socket, AF_INET, SOCK_STREAM
from tkinter import *


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


client_tcp: Client = None


def connexion() -> None:
    global client_tcp  # variable globale
    try:
        print("connexion en cours")
        ip_serveur = entree_ip_serveur.get()
        port_serveur = int(entree_port_serveur.get())
        # instanciation du client TCP
        client_tcp = Client(ip_serveur, port_serveur)

        # connexion au serveur
        if not client_tcp.connexion():
            raise Exception("La connexion a été bloquée")

    except Exception as ex:
        print("erreur de connexion : ", ex)
    else:
        # désactiver le bouton de connexion
        # activer les boutons pour envoyer un message et pour quitter
        btn_connexion.config(state="disabled")
        btn_envoyer.config(state="active")
        btn_quitter.config(state="active")


def envoyer() -> None:
    msg = entree_msg_client.get()
    if msg != "":
        entree_msg_client.delete(0, END)
        client_tcp.envoyer(msg=msg)
        chaine = client_tcp.recevoir()
        text_msg_serveur.insert(INSERT, chaine + "\n")


def quitter() -> None:
    client_tcp.envoyer(msg="fin")
    client_tcp.recevoir()
    client_tcp.arret()
    ihm.destroy()


if __name__ == "__main__":
    ihm: Tk
    fen_connexion: Frame
    label_ip: Label
    entree_ip_serveur: Entry
    label_port: Label
    entree_port_serveur: Entry
    btn_connexion: Button
    fen_echange: Frame
    entree_msg_client: Entry
    btn_envoyer: Button
    text_msg_serveur: Text
    btn_quitter: Button

    ihm = Tk()
    ihm.geometry = "1200x720"
    ihm.title("client tcp echo")

    # Connexion
    fen_connexion = Frame(ihm, borderwidth=10, relief="groove", padx=10, pady=10)
    label_ip = Label(fen_connexion, text="ip server")
    entree_ip_serveur = Entry(fen_connexion, width=30)
    label_port = Label(fen_connexion, text="port server")
    entree_port_serveur = Entry(fen_connexion, width=30)
    btn_connexion = Button(fen_connexion, text="Connexion", command=connexion)

    fen_connexion.grid(column=0, row=0)
    label_ip.grid(column=0, row=0)
    entree_ip_serveur.grid(column=1, row=0)
    label_port.grid(column=0, row=1)
    entree_port_serveur.grid(column=1, row=1)
    btn_connexion.grid(column=2, row=0)

    # Echange

    fen_echange = Frame(ihm, borderwidth=10, relief="groove", padx=10, pady=10)
    entree_msg_client = Entry(fen_echange, width=100)
    btn_envoyer = Button(fen_echange, text="Envoyer", command=envoyer)
    text_msg_serveur = Text(fen_echange)
    btn_quitter = Button(fen_echange, text="Quitter", command=quitter)

    btn_quitter.configure(bg="red", state="disabled")
    btn_envoyer.configure(state="disabled")

    fen_echange.grid(column=0, row=1)
    entree_msg_client.grid(column=0, row=0)
    btn_envoyer.grid(column=1, row=0)
    text_msg_serveur.grid(column=0, row=1)
    btn_quitter.grid(column=1, row=1)

    ihm.mainloop()
