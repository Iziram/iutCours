"""! @brief IHM du Serveur
 @file ihm_server.py
 @section libs Librairies/Modules
  - tkinter
  - tkinter.messagebox
  - common
  - server
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
  - Mis à jour par Matthias HARTMANN le 24/01/2023 .
"""
# pylint: disable=function-redefined,broad-except,too-many-ancestors,too-few-public-methods,too-many-arguments,too-many-instance-attributes

from tkinter import (
    END,
    GROOVE,
    INSERT,
    Button,
    Entry,
    Event,
    Frame,
    Label,
    StringVar,
    Text,
    Tk,
    Toplevel,
)
from tkinter.messagebox import askquestion

from common import TextWithVar
from server import Server


class CoteServer(Tk, Server):
    """!
    @brief GUI Représentant le serveur (Interface d'entrée)

    ## Héritage :
        - Implémente Tk
        - Implémente Server

    """

    def __init__(self):
        # déclaration des variables
        Tk.__init__(self)
        Server.__init__(self)

        self.__lbl_ip_serv: Label
        self.__entry_ip_serv: Entry
        self.__lbl_port_commande: Label
        self.__entry_port_commande: Entry
        self.__btn_start: Button
        self.__btn_csl: Button
        self.__win_log: Label
        self.__btn_quit: Button
        self.__var_log: StringVar

        # Initialisation des variables
        self.__frame_top = Frame(master=self, relief=GROOVE)
        self.__frame_btm = Frame(master=self, relief=GROOVE)

        self.__frame_top.pack(padx=5, pady=10)
        self.__frame_btm.pack(padx=5, pady=10)

        self.title("Interface côté serveur")

        self.__lbl_ip_serv = Label(self.__frame_top, text="ip du serveur : ")
        self.__lbl_port_commande = Label(self.__frame_top, text="port commande")
        self.__entry_ip_serv = Entry(self.__frame_top, width=25)
        self.__entry_port_commande = Entry(self.__frame_top, width=25)
        self.__btn_start = Button(
            self.__frame_top, text="Démarrer", command=self.demarrer
        )
        self.__btn_csl = Button(
            self.__frame_top, text="©", command=lambda: ConsoleServ(self)
        )

        self.__var_log = StringVar()

        self.__win_log = TextWithVar(
            self.__frame_btm,
            width=120,
            height=40,
            textvariable=self.__var_log,
            bg="white",
            relief=GROOVE,
        )
        self.__btn_quit = Button(
            self.__frame_top, text="Quitter", bg="red", command=self.quitter
        )

        # Ajout des widget défini ci-dessus + Ajout de frame pour superposé les éléments

        self.__lbl_ip_serv.grid(row=0, column=0)
        self.__entry_ip_serv.grid(row=0, column=1)
        self.__lbl_port_commande.grid(row=2, column=0)
        self.__entry_port_commande.grid(row=2, column=1)
        self.__btn_start.grid(row=3, column=1)
        self.__btn_csl.grid(row=3, column=2)
        self.__btn_quit.grid(row=3, column=3)
        self.__win_log.pack()

        self.__win_log.bind("<Key>", lambda e: "break")

        Server.LOG.set_event(self.__var_log.set)

        self.__entry_ip_serv.insert(INSERT, "127.0.0.1")
        self.__entry_port_commande.insert(INSERT, "5000")

        self.__btn_csl["state"] = "disable"

    def quitter(self):
        """!
        @brief Quitte l'interface

        Paramètres :
            @param self => le GUI du serveur

        """
        msg_box = askquestion("Quitter", "Êtes-vous sûr de vouloir quitter ?")
        if msg_box == "yes":
            self.get_interpreter().run_command("quit", *[])
            self.destroy()

    def get_var_log(self):
        """!
        @brief Retourne la variable de logging de l'interface

        Paramètres :
            @param self => le GUI du serveur

        """
        return self.__var_log

    def demarrer(self):
        """!
        @brief Démarre l'instance du serveur

        Paramètres :
            @param self => le GUI du serveur

        """
        addr: str = self.__entry_ip_serv.get()
        port: int = int(self.__entry_port_commande.get())

        self.set_connection_infos(addr, port)
        Server.LOG.add("Serveur démarré")

        self.__btn_start["state"] = "disable"
        self.__btn_csl["state"] = "active"


class ConsoleServ(Toplevel):
    """!
    @brief GUI de la console du serveur

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, fp: CoteServer):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__btn_hlp: Button
        self.__text_log: Text
        self.__entry_input: Entry
        self.__btn_send: Button
        self.__btn_retour: Button
        self.title("console")

        # Instanciation des variables
        self.__fp.withdraw()
        self.__btn_hlp = Button(self, text="❓", command=lambda: HelpServ(self))
        self.__text_log = TextWithVar(
            self,
            textvariable=self.__fp.get_var_log(),
            bg="white",
            relief=GROOVE,
        )
        self.__btn_send = Button(self, text="Envoyer", command=self.send_command)
        self.__entry_input = Entry(self, width=160)
        self.__btn_retour = Button(self, text="Retour", command=self.back)

        # Ajout des widgets
        self.__text_log.grid(row=1, column=0, padx=5, pady=5)

        self.__btn_hlp.grid(row=0, column=1, padx=5, pady=5)
        self.__entry_input.grid(row=2, column=0, padx=5, pady=5)
        self.__btn_send.grid(row=2, column=1, padx=5, pady=5)
        self.__btn_retour.grid(row=0, column=0, padx=5, pady=5)
        self.protocol("WM_DELETE_WINDOW", self.back)

        # ajout d’événements
        self.__entry_input.bind("<Return>", self.send_command)
        self.__entry_input.bind("<KP_Enter>", self.send_command)
        self.__text_log.bind("<Key>", lambda e: "break")

    def back(self):
        """!
        @brief Retourne sur le GUI principal

        Paramètres :
            @param self => le GUI de la console du serveur
        """
        # appel du modificateur de la classe mere
        self.__fp.deiconify()  # afficher la fenêtre principale
        self.destroy()  # détruire la fenêtre courante

    def send_command(self, _: Event = None):
        """!
        @brief Envoie une commande

        Paramètres :
            @param self => le GUI de la console du serveur
            @param _ : Event = None => Event Tkinter inutile ici

        """
        cmd_line: str = self.__entry_input.get()

        Server.LOG.add(f"COMMAND : {cmd_line}")

        self.__fp.execute(cmd_line)

        self.__entry_input.delete(0, END)


class HelpServ(Toplevel):
    """!
    @brief GUI d'affichage des commandes

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, _: ConsoleServ):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__lbl_list: Label
        self.__txt_command: Text

        # Instanciation des variables
        self.title("help commandes")
        self.__lbl_list = Label(
            self, text="Liste des commandes", borderwidth=5, relief="ridge"
        )
        self.__txt_command = Text(self, width=40, height=30)

        # Ajout des widgets
        self.__lbl_list.pack(padx=10, pady=10)
        self.__txt_command.pack(padx=10, pady=10)

        self.__txt_command.bind("<Key>", "break")

        commands: list[str] = [
            "start ➡ Ouvre le serveur en mode écoute",
            "stop ➡ Ferme toutes les connexions du serveur mais laisse l'instance ouverte",
            "quit ➡ Ferme toutes les connexions du serveur et coupe l'instance",
            "list ➡ Renvoie la liste des clients",
            "calls ➡ Renvoie la liste des ConfCalls",
        ]
        self.__txt_command.insert(INSERT, "\n".join(commands))


if __name__ == "__main__":
    server: CoteServer = CoteServer()
    server.mainloop()
