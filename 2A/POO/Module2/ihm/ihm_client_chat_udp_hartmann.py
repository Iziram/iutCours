from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from tkinter import *
import os
from random import randint


class Client_UDP:
    def __init__(self, ip_serveur: str, port_serveur: int, msg_serv: Text) -> None:
        self.__ip_serveur: str = ip_serveur
        self.__port_serveur = port_serveur
        self.__socket_echange: socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket_echange.bind((ip_serveur, randint(25000, 65000)))

        self.__text_msg_server: Text = msg_serv

        self.__fin: bool = False
        self.__thread_recevoir: Thread = Thread(target=self.recevoir)
        self.__thread_recevoir.start()

    def recevoir(self) -> str:
        try:

            while not self.__fin:
                tab_bytes, _ = self.__socket_echange.recvfrom(1024)
                msg: str = tab_bytes.decode("utf-8")
                self.__text_msg_server.insert(INSERT, msg + "\n")

                if msg == "[fin]":
                    self.__fin = True
        except:
            pass

    def envoyer(self) -> None:
        while not self.__fin:
            msg: str = input("")
            if not self.__fin:
                self.__socket_echange.sendto(
                    msg.encode("utf-8"), (self.__ip_serveur, self.__port_serveur)
                )

    def envoyer_simple(self, msg):
        if not self.__fin:
            self.__socket_echange.sendto(
                msg.encode("utf-8"), (self.__ip_serveur, self.__port_serveur)
            )

    def close(self) -> None:
        self.__socket_echange.close()

    def fin(self):
        self.__fin = not self.__fin


client_chat_udp: Client_UDP = None


def instanciation_client_udp() -> None:
    global client_chat_udp
    try:
        print("connexion")
        ip_serveur = entree_ip_serveur.get()
        port_serveur = int(entree_port_serveur.get())
        # instanciation du client UDP
        client_chat_udp = Client_UDP(ip_serveur, port_serveur, text_msg_serveur)
    except Exception as ex:
        print("erreur de connexion : ", ex)
    else:
        btn_validation["state"] = DISABLED
        btn_envoyer["state"] = NORMAL
        btn_quitter["state"] = NORMAL
        entree_msg_client["state"] = NORMAL


def envoyer() -> None:
    msg = entree_msg_client.get()
    if msg != "":
        entree_msg_client.delete(0, END)
        client_chat_udp.envoyer_simple(msg=msg)


def quitter() -> None:
    client_chat_udp.envoyer_simple("fin")
    client_chat_udp.fin()
    client_chat_udp.close()
    ihm.destroy()


if __name__ == "__main__":
    ihm: Tk
    fen_connexion: Frame
    label_ip: Label
    entree_ip_serveur: Entry
    label_port: Label
    entree_port_serveur: Entry
    btn_validation: Button
    fen_echange: Frame
    entree_msg_client: Entry
    btn_envoyer: Button
    text_msg_serveur: Text
    btn_quitter: Button

    ihm = Tk()
    ihm.geometry = "1200x720"
    ihm.title("client udp chat")

    # Connexion
    fen_connexion = Frame(ihm, borderwidth=10, relief="groove", padx=10, pady=10)
    label_ip = Label(fen_connexion, text="ip server")
    entree_ip_serveur = Entry(fen_connexion, width=30)
    label_port = Label(fen_connexion, text="port server")
    entree_port_serveur = Entry(fen_connexion, width=30)
    btn_validation = Button(
        fen_connexion, text="Validation", command=instanciation_client_udp
    )

    fen_connexion.grid(column=0, row=0)
    label_ip.grid(column=0, row=0)
    entree_ip_serveur.grid(column=1, row=0)
    label_port.grid(column=0, row=1)
    entree_port_serveur.grid(column=1, row=1)
    btn_validation.grid(column=2, row=0)

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
