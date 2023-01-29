"""! @brief IHM du client
 @file IHM_Telephonie_Client.py
 @section libs Librairies/Modules
  - threading
  - time
  - tkinter
  - tkinter.filedialog
  - client
  - common
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
  - Mis à jour par Matthias HARTMANN le 24/01/2023 .
"""
# pylint: disable=function-redefined,broad-except,too-many-ancestors,too-few-public-methods,too-many-arguments,too-many-instance-attributes,pointless-statement


from threading import Thread
from time import sleep
from tkinter import (
    END,
    INSERT,
    MULTIPLE,
    Button,
    Entry,
    Event,
    Frame,
    Label,
    Listbox,
    Menu,
    StringVar,
    Tk,
    Toplevel,
)
from tkinter.filedialog import askopenfile

from client import Client
from common import CommandInterpreter, Flag


class CoteClient(Tk):
    """!
    @brief Interface principale, option de lancement

    ## Héritage :
        - Implémente Tk

    """

    # Constructeur de la classe
    def __init__(self):
        # Définition des variables
        Tk.__init__(self)

        self.__client: Client
        self.__client_infos: dict[str, object]

        self.__lbl_static: Label
        self.__lbl_error: Label
        self.__lbl_usrnm: Label
        self.__entry_usrnm: Entry
        self.__lbl_pswd: Label
        self.__entry_pswd: Entry
        self.__btn_con: Button
        self.__btn_create: Button
        self.__btn_set: Button
        self.__str_var: StringVar
        self.__usr_pwd_frame: Frame

        # Instanciation des variables

        self.__client = None
        self.__client_infos = {
            "username": None,
            "password": None,
            "ip_serv": None,
            "ip_client": None,
            "port_serv": None,
        }

        self.__usr_pwd_frame = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__str_var = StringVar()
        self.__lbl_static = Label(
            self, text="Vive Mitel !", padx=5, pady=5, anchor="center"
        )
        self.__lbl_error = Label(self, textvariable=self.__str_var, fg="crimson")
        self.__lbl_usrnm = Label(
            self.__usr_pwd_frame, text="Userame : ", padx=3, pady=3
        )
        self.__entry_usrnm = Entry(self.__usr_pwd_frame, width=20)
        self.__lbl_pswd = Label(
            self.__usr_pwd_frame, text="Password : ", padx=3, pady=3
        )
        self.__entry_pswd = Entry(self.__usr_pwd_frame, width=20)
        self.__btn_con = Button(self, text="Connexion", command=self.connexion)
        self.__btn_create = Button(self, text="➕", command=lambda: self.connexion(True))
        self.__btn_set = Button(self, text="⚙️", command=lambda: ClientParam(self))
        self.title("Connexion")

        # Ajout des widget
        self.__lbl_static.grid(row=0, column=0)
        self.__lbl_error.grid(row=1, column=0)
        self.__usr_pwd_frame.grid(row=2, column=0)
        self.__lbl_usrnm.grid(row=0, column=0)
        self.__entry_usrnm.grid(row=0, column=1)
        self.__lbl_pswd.grid(row=1, column=0)
        self.__entry_pswd.grid(row=1, column=1)
        self.__btn_con.grid(row=3, column=0)
        self.__btn_create.grid(row=3, column=1)
        self.__btn_set.grid(row=0, column=1)

    def connexion(self, create: bool = False):
        """!
        @brief Connecte le client au serveur

        Paramètres :
            @param self => le GUI principale du client
            @param create : bool = False => Met le client en mode Création

        """

        username: str = self.__entry_usrnm.get()
        password: str = self.__entry_pswd.get()

        infos: dict[str, object] = self.get_client_infos()

        infos["username"] = username
        infos["password"] = password

        self.set_client_infos(infos)

        if self.__client is None:
            self.__client = Client(
                infos["username"],
                infos["password"],
                infos["ip_client"],
                server_ip=infos["ip_serv"],
                server_port=infos["port_serv"],
            )
        else:
            self.__client.set_password(infos["password"])
            self.__client.set_username(infos["username"])

        self.__client.set_create_client(create)

        if self.__client.connect(self.__str_var):
            thd: Thread = Thread(
                target=self.__client.receive_data, name="clientReceive"
            )
            thd.start()
            ClientConnected(self)

    def get_client(self):
        """!
        @brief Retourne la représentation interne du client

        Paramètres :
            @param self => le GUI principale du client

        """
        return self.__client

    def get_client_infos(self):
        """!
        @brief Retourne les informations de configuration du client
        (
            username,
            password,
            ip_client,
            ip_server,
            port_server
        )

        Paramètres :
            @param self => le GUI principale du client

        """
        return self.__client_infos

    def set_client_infos(self, infos: dict[str, object]):
        """!
        @brief Définit les informations de configuration du client

        Paramètres :
            @param self => le GUI principale du client
            @param infos : dict[str,object] => Un dictionnaire représentant la configuration

        """
        self.__client_infos = infos


class ClientParam(Toplevel):
    """!
    @brief GUI de la configuration réseau

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, fp: CoteClient):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_static: Label
        self.__lbl_ip_srv: Label
        self.__lbl_ip_client: Label
        self.__entry_ip_srv: Entry
        self.__lbl_port_srv: Label
        self.__entry_port_srv: Entry
        self.__btn_valid: Button
        self.__frame_center: Frame
        self.title("Paramètres")

        # Instanciation dse variables
        self.__fp.withdraw()
        self.__frame_center = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__lbl_static = Label(
            self,
            text="Paramètre",
            anchor="center",
            padx=5,
            pady=5,
            borderwidth=5,
            relief="ridge",
        )
        self.__lbl_ip_srv = Label(
            self.__frame_center, text="ip serveur", padx=3, pady=3
        )
        self.__lbl_ip_client = Label(
            self.__frame_center, text="ip client", padx=3, pady=3
        )
        self.__entry_ip_srv = Entry(self.__frame_center, width=15)
        self.__entry_ip_client = Entry(self.__frame_center, width=15)
        self.__lbl_port_srv = Label(
            self.__frame_center, text="port serveur", padx=3, pady=3
        )
        self.__entry_port_srv = Entry(self.__frame_center, width=10)
        self.__btn_valid = Button(self, text="Valider", command=self.valider_param)

        # Ajout des widget
        self.__lbl_static.pack()
        self.__frame_center.pack()
        self.__lbl_ip_client.grid(row=0, column=0)
        self.__lbl_ip_srv.grid(row=1, column=0)
        self.__entry_ip_srv.grid(row=1, column=1)
        self.__entry_ip_client.grid(row=0, column=1)
        self.__lbl_port_srv.grid(row=2, column=0)
        self.__entry_port_srv.grid(row=2, column=1)
        self.__btn_valid.pack()
        self.protocol("WM_DELETE_WINDOW", self.valider_param)

        self.__entry_ip_client.insert(INSERT, "127.0.0.2")
        self.__entry_ip_srv.insert(INSERT, "127.0.0.1")
        self.__entry_port_srv.insert(INSERT, "5000")

    def valider_param(self):
        """!
        @brief Valide la configuration réseau

        Paramètres :
            @param self => le GUI de la configuration réseau

        """
        ip_server: str = self.__entry_ip_srv.get()
        ip_client: str = self.__entry_ip_client.get()
        port_server: int = int(self.__entry_port_srv.get())

        infos: dict[str, object] = self.__fp.get_client_infos()

        infos["ip_client"] = ip_client
        infos["ip_serv"] = ip_server
        infos["port_serv"] = port_server

        self.__fp.set_client_infos(infos)

        self.__fp.deiconify()  # afficher la fenêtre principale
        self.destroy()  # détruire la fenêtre courante


class ClientConnected(Toplevel):
    """!
    @brief GUI Client après connexion

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, fp: CoteClient):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__middle_frame: Frame
        self.__right_frame: Frame
        self.__btn_annuaire: Button
        self.__middle_list: Listbox
        self.__middle_btn_call: Button
        self.__right_pp: Label
        self.__right_lbl_usr: Label
        self.__right_btn_disc: Button
        self.__call: ClientCall

        # Instanciation des variables
        self.__fp.withdraw()
        self.__middle_frame = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__right_frame = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__btn_annuaire = Button(
            self.__middle_frame,
            text="Annuaire",
            borderwidth=3,
            relief="ridge",
            command=lambda: Annuaire(self.__fp),
        )
        self.__middle_list = Listbox(self.__middle_frame, width=17, height=10)
        self.__middle_btn_call = Button(
            self.__middle_frame,
            text="Appeler",
            relief="ridge",
            padx=2,
            pady=2,
            command=self.call,
        )
        self.__right_pp = Label(
            self.__right_frame,
            text="Connected",
            padx=2,
            pady=2,
            borderwidth=3,
            relief="ridge",
            bg="MediumSpringGreen",
        )
        self.__right_lbl_usr = Label(
            self.__right_frame,
            text=f"{self.__fp.get_client_infos()['username']}",
            padx=2,
            pady=2,
            borderwidth=3,
            relief="ridge",
        )
        self.__right_btn_disc = Button(
            self.__right_frame,
            text="Déconnecter",
            fg="crimson",
            command=self.disconnect_from_serv,
        )

        self.__call = None

        # Ajout des widget
        self.__middle_frame.grid(row=0, column=0)
        self.__right_frame.grid(row=0, column=1)
        self.__btn_annuaire.grid(row=0, column=0)
        self.__middle_list.grid(row=1, column=0)
        self.__middle_btn_call.grid(row=1, column=1)
        self.__right_pp.pack()
        self.__right_lbl_usr.pack()
        self.__right_btn_disc.pack()
        self.protocol("WM_DELETE_WINDOW", self.disconnect_from_serv)

        self.__middle_list.config(selectmode=MULTIPLE)

        cmd_i: CommandInterpreter = self.__fp.get_client().get_interpreter()
        cmd_i.set_command(Flag.LSR, self.set_client_list)
        cmd_i.set_command(Flag.ASK, self.get_asked_call)
        cmd_i.set_command(Flag.STA, self.start_call)
        cmd_i.set_command(Flag.FIN, self.close_call)
        cmd_i.set_command(Flag.INF, self.show_call_infos)

    def close_call(self):
        """!
        @brief Ferme l'appel courant

        Paramètres :
            @param self => le GUI client après connexion

        """
        self.__fp.get_client().set_audio_connected(False)
        self.__call.destroy()

    def show_call_infos(self, time: int, user: str):
        """!
        @brief Affiche les informations de l'appel courant

        Paramètres :
            @param self => le GUI client après connexion
            @param time : int => la durée de l'appel en secondes
            @param user : str => les clients participant à l'appel

        """
        self.__call.actualize(time.replace("time:", ""), user.replace("act:", ""))

    def get_asked_call(self, name: str):
        """!
        @brief Affiche la notification d'appel

        Paramètres :
            @param self => le GUI client après connexion
            @param name : str => Nom de l'appel

        """
        ClientReceive(self.__fp, name)

    def start_call(self):
        """!
        @brief Lance un appel

        Paramètres :
            @param self => le GUI client après connexion

        """
        cli = self.__fp.get_client()
        Thread(target=cli.receive_audio, name="audioClientIn").start()
        Thread(target=cli.send_audio, name="audioClientOut").start()
        self.__call: ClientCall = ClientCall(self.__fp)

    def set_client_list(self, *names):
        """!
        @brief Met à jour la liste des clients connectés

        Paramètres :
            @param self => le GUI client après connexion
            @param *names => Liste des clients connectés

        """
        try:
            current_names: list[str] = list(self.__middle_list.get(0, END))
            current_names.append(self.__fp.get_client_infos()["username"])
            if set(current_names) != set(names):
                self.__middle_list.delete(0, END)
                for i, val in enumerate(names):
                    if val != self.__fp.get_client_infos()["username"]:
                        self.__middle_list.insert(i, val)
        except Exception:
            pass

    def call(self):
        """!
        @brief Appel les clients sélectionnés

        Paramètres :
            @param self => le GUI client après connexion

        """
        selected: tuple[int] = self.__middle_list.curselection()
        names: list[str] = [self.__middle_list.get(i) for i in selected]

        if len(names) > 0:
            self.__fp.get_client().send_flag(Flag.CAL, " ".join(names))

    def disconnect_from_serv(self):
        """!
        @brief Déconnecte le client

        Paramètres :
            @param self => le GUI client après connection

        """

        self.__fp.get_client().send_flag(Flag.ENT)

        self.__fp.deiconify()  # afficher la fenêtre principale
        self.destroy()  # detruire la fenêtre courante


class ClientCall(Toplevel):
    """!
    @brief GUI de l'appel courant

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, fp: CoteClient):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_usr: Label
        self.__lbl_time: Label
        self.__strvar_time: StringVar
        self.__lbl_time_var: Label
        self.__btn_end: Button

        # Instanciation des variables
        self.__lbl_usr = Label(
            self, text="USER", padx=2, pady=2, borderwidth=3, relief="ridge"
        )
        self.__lbl_time = Label(self, text="Temps Appel :", padx=2, pady=2)
        self.__strvar_time = StringVar(value="HH:MM:SS")
        self.__lbl_time_var = Label(
            self,
            textvariable=self.__strvar_time,
            padx=2,
            pady=2,
            borderwidth=3,
            relief="ridge",
        )
        self.__btn_end = Button(
            self, text="Raccrocher", bg="crimson", command=self.end_call
        )

        # Ajout des widget
        self.__lbl_usr.pack()
        self.__lbl_time.pack()
        self.__lbl_time_var.pack()
        self.__btn_end.pack()

    def end_call(self):
        """!
        @brief Termine l'appel courant

        Paramètres :
            @param self => le GUI de l'appel courant

        """
        self.__fp.get_client().send_flag(Flag.FIN)
        self.destroy()  # détruire la fenêtre courante

    def actualize(self, time: str, user: str):
        """!
        @brief Actualise l'affichage du temps d'appel et des clients connectés

        Paramètres :
            @param self => le GUI de l'appel courant
            @param time : str => Temps de l'appel
            @param user : str => Clients connectés à l'appel

        """
        self.__lbl_usr["text"] = user
        self.__strvar_time.set(time)


class ClientReceive(Toplevel):
    """!
    @brief GUI de la notification d'appel

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, master, name: str):
        # Déclaration des variables
        self.__master: CoteClient = master
        Toplevel.__init__(self, self.__master)
        self.__lbl_call: Label
        self.__btn_ok: Button
        self.__btn_nok: Button

        # Instanciation des variables
        self.__lbl_call = Label(
            self, text=f"{name}", padx=2, pady=2, borderwidth=3, relief="ridge"
        )
        self.__btn_ok = Button(self, text="Accepter", command=self.ok_call)
        self.__btn_nok = Button(self, text="Rejeter", command=self.not_ok_call)

        # Ajout des widget
        self.__lbl_call.grid(row=0, column=1)
        self.__btn_ok.grid(row=1, column=0)
        self.__btn_nok.grid(row=1, column=2)

        self.__is_asking = True

        def answer_time_out():
            time: int = 0
            while self.__is_asking and time < 10:
                sleep(1)
            if self.__is_asking:
                self.not_ok_call

        thd: Thread = Thread(target=answer_time_out, name="answerTimeOUT")
        thd.start()

    def ok_call(self):
        """!
        @brief Accepte l'appel

        Paramètres :
            @param self => GUI de la notification d'appel

        """
        self.__master.get_client().send_flag(Flag.RES, "1")
        self.__is_asking = False
        self.destroy()

    def not_ok_call(self):
        """!
        @brief Refuse l'appel

        Paramètres :
            @param self => GUI de la notification d'appel

        """
        self.__master.get_client().send_flag(Flag.RES, "0")
        self.__is_asking = False
        self.destroy()


class Annuaire(Toplevel):
    """!
    @brief GUI de l'annuaire

    ## Héritage :
        - Implémente Toplevel

    """

    def __init__(self, master):
        # Déclaration des variables
        self.__master: CoteClient = master
        Toplevel.__init__(self, self.__master)
        self.__entry_add: Entry
        self.__btn_add: Button
        self.__list_annuaire: Listbox
        self.__btn_call: Button
        self.__menubar: Menu
        self.__menu_json: Menu

        # Instanciation dse variables
        self.__entry_add = Entry(self, width=15)
        self.__btn_add = Button(
            self, text="Ajouter", borderwidth=3, relief="ridge", command=self.add_name
        )
        self.__btn_call = Button(
            self, text="Appeler", borderwidth=3, relief="ridge", command=self.call_names
        )
        self.__menubar = Menu(self)
        self.__menu_json = Menu(self.__menubar, tearoff=0)
        self.__menu_json.add_command(label="Importer", command=self.import_file)
        self.__menu_json.add_separator()
        self.__menu_json.add_command(label="Exporter", command=self.export_file)
        self.__menubar.add_cascade(label="JSON", menu=self.__menu_json)
        self.__list_annuaire = Listbox(self, width=20, height=15)

        # Ajout des widgets
        self.title("Annuaire")
        self.config(menu=self.__menubar)
        self.__entry_add.grid(row=0, column=0)
        self.__btn_add.grid(row=0, column=1)
        self.__btn_call.grid(row=1, column=1)
        self.__list_annuaire.grid(row=1, column=0)

        self.__list_annuaire.config(selectmode=MULTIPLE)

        self.__master.get_client().get_book().set_event(self.actualize_book)

        self.__list_annuaire.bind("<BackSpace>", self.remove_names)

    def remove_names(self, _: Event):
        """!
        @brief Retire les noms sélectionnés de l'annuaire

        Paramètres :
            @param self => GUI de l'annuaire
            @param _ : Event => Event Tkinter inutile ici

        """
        selection: tuple[int] = self.__list_annuaire.curselection()
        names: list[str] = [self.__list_annuaire.get(i) for i in selection]
        for name in names:
            self.__master.get_client().get_book().remove_name(name)

    def add_name(self):
        """!
        @brief Ajoute un nom dans l'annuaire

        Paramètres :
            @param self => GUI de l'annuaire

        """
        name: str = self.__entry_add.get()
        self.__master.get_client().get_book().add_name(name)

    def call_names(self):
        """!
        @brief Appelle les noms sélectionnés dans l'annuaire

        Paramètres :
            @param self => GUI de l'annuaire

        """
        selection: tuple[int] = self.__list_annuaire.curselection()
        names: list[str] = [self.__list_annuaire.get(i) for i in selection]
        if len(names) > 0:
            self.__master.get_client().send_flag(Flag.CAL, " ".join(names))

    def import_file(self):
        """!
        @brief Importe un annuaire depuis un fichier json

        Paramètres :
            @param self => GUI de l'annuaire

        """

        file_import = askopenfile(
            title="Fichier json", filetypes=[("json files", ".json")]
        )
        self.__master.get_client().get_book().import_file(file_import)

    def export_file(self):
        """!
        @brief Exporte l'annuaire dans un fichier "annuaire.json"

        Paramètres :
            @param self => GUI de l'annuaire

        """
        self.__master.get_client().get_book().export_file("annuaire.json")

    def actualize_book(self, names: list[str]):
        """!
        @brief Met à jour l'affichage de l'annuaire

        Paramètres :
            @param self => GUI de l'annuaire
            @param names : list[str] => Les noms présents dans l'annuaire

        """
        try:
            current_names: list[str] = list(self.__list_annuaire.get(0, END))
            if set(current_names) != set(names):
                self.__list_annuaire.delete(0, END)
                for i, val in enumerate(names):
                    self.__list_annuaire.insert(i, val)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    client: CoteClient = CoteClient()
    client.mainloop()
