"""! @brief [description du fichier]
 @file IHM_Telephonie_Client.py
 @section libs Librairies/Modules
  - tkinter (lien)
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
"""
from tkinter import *
from common import CommandInterpreter, Flag, TextWithVar
from client import Client
from threading import Thread
from time import sleep


class cote_client(Tk):
    # Constructeur de la classe
    def __init__(self):
        # Définition des variables
        Tk.__init__(self)

        self.__client: Client
        self.__clientInfos: dict[str, object]

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
        self.__clientInfos = {
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
        self.__btn_create = Button(self, text="➕", command=lambda: create_client(self))
        self.__btn_set = Button(self, text="⚙️", command=lambda: client_param(self))
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

    def connexion(self):

        username: str = self.__entry_usrnm.get()
        password: str = self.__entry_pswd.get()

        infos: dict[str, object] = self.getClientInfos()

        infos["username"] = username
        infos["password"] = password

        self.setClientInfos(infos)

        if self.__client is None:
            self.__client = Client(
                infos["username"],
                infos["password"],
                infos["ip_client"],
                server_ip=infos["ip_serv"],
                server_port=infos["port_serv"],
            )
        else:
            self.__client.setPassword(infos["password"])
            self.__client.setUsername(infos["username"])

        if self.__client.connect(self.__str_var):
            th: Thread = Thread(target=self.__client.receiveData, name="clientReceive")
            th.start()
            client_connected(self)

    def getClient(self):
        return self.__client

    def getClientInfos(self):
        return self.__clientInfos

    def setClientInfos(self, infos: dict[str, object]):
        self.__clientInfos = infos


class client_param(Toplevel):
    def __init__(self, fp: cote_client):
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
        self.__entry_ip_srv = Entry(self.__frame_center, width=10)
        self.__entry_ip_client = Entry(self.__frame_center, width=10)
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

    def valider_param(self) -> None:
        ip_server: str = self.__entry_ip_srv.get()
        ip_client: str = self.__entry_ip_client.get()
        port_server: int = int(self.__entry_port_srv.get())

        infos: dict[str, object] = self.__fp.getClientInfos()

        infos["ip_client"] = ip_client
        infos["ip_serv"] = ip_server
        infos["port_serv"] = port_server

        self.__fp.setClientInfos(infos)

        self.__fp.deiconify()  # afficher la fenetre principale
        self.destroy()  # detruire la fenetre courante


class create_client(Toplevel):
    def __init__(self, fp: cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_static: Label
        self.__lbl_nm_usr: Label
        self.__entry_nm_usr: Entry
        self.__lbl_mdp_usr: Label
        self.__entry_mdp_usr: Entry
        self.__btn_valid: Button
        self.__frame_center: Frame
        self.title("Nouvel utilisateur")

        # Instanciation des variables
        self.__fp.withdraw()
        self.__frame_center = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__lbl_static = Label(
            self,
            text="Création nouveau compte",
            anchor="center",
            padx=5,
            pady=5,
            borderwidth=5,
            relief="ridge",
        )
        self.__lbl_nm_usr = Label(
            self.__frame_center, text="Nom utilisateur : ", padx=3, pady=3
        )
        self.__entry_nm_usr = Entry(self.__frame_center, width=20)
        self.__lbl_mdp_usr = Label(
            self.__frame_center, text="mot de passe : ", padx=3, pady=3
        )
        self.__entry_mdp_usr = Entry(self.__frame_center, width=20)
        self.__btn_valid = Button(self, text="Valider", command=self.valider_create)

        # Ajout des widget
        self.__lbl_static.pack()
        self.__frame_center.pack()
        self.__lbl_nm_usr.grid(row=0, column=0)
        self.__entry_nm_usr.grid(row=0, column=1)
        self.__lbl_mdp_usr.grid(row=1, column=0)
        self.__entry_mdp_usr.grid(row=1, column=1)
        self.__btn_valid.pack()
        self.protocol("WM_DELETE_WINDOW", self.valider_create)

    def valider_create(self) -> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify()  # afficher la fenetre principale
        self.destroy()  # detruire la fenetre courante


class client_connected(Toplevel):
    def __init__(self, fp: cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__middle_frame: Frame
        self.__right_frame: Frame
        self.__middle_search: Entry
        self.__middle_btn_search: Button
        self.__middle_list: Listbox
        self.__middle_btn_call: Button
        self.__right_pp: Label
        self.__right_lbl_usr: Label
        self.__right_btn_disc: Button
        self.__call: client_call

        # Instanciatin des variables
        self.__fp.withdraw()
        self.__middle_frame = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__right_frame = Frame(
            master=self, relief="ridge", padx=5, pady=5, borderwidth=3
        )
        self.__middle_search = Entry(self.__middle_frame, width=15)
        self.__middle_btn_search = Button(self.__middle_frame, text="🔍")
        self.__middle_list = Listbox(self.__middle_frame, width=17, height=10)
        self.__middle_btn_call = Button(
            self.__middle_frame,
            text="Appeler",
            relief="ridge",
            padx=2,
            pady=2,
            command=self.setCall,
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
            text=f"{self.__fp.getClientInfos()['username']}",
            padx=2,
            pady=2,
            borderwidth=3,
            relief="ridge",
        )
        self.__right_btn_disc = Button(
            self.__right_frame,
            text="Déconnecter",
            fg="crimson",
            command=self.disconnected,
        )

        self.__call = None

        # Ajout des widget
        self.__middle_frame.grid(row=0, column=0)
        self.__right_frame.grid(row=0, column=1)
        self.__middle_search.grid(row=0, column=0)
        self.__middle_btn_search.grid(row=0, column=1)
        self.__middle_list.grid(row=1, column=0)
        self.__middle_btn_call.grid(row=1, column=1)
        self.__right_pp.pack()
        self.__right_lbl_usr.pack()
        self.__right_btn_disc.pack()
        self.protocol("WM_DELETE_WINDOW", self.disconnected)

        cmd_i: CommandInterpreter = self.__fp.getClient().getInterpreter()
        cmd_i.set_command(Flag.LSR, self.setClientList)
        cmd_i.set_command(Flag.ASK, self.getAskedCall)
        cmd_i.set_command(Flag.STA, self.startCall)
        cmd_i.set_command(Flag.FIN, self.closeCall)

    def closeCall(self):
        self.__fp.getClient().setAudioConnected(False)
        self.__call.destroy()

    def getAskedCall(self, name: str):
        client_receive(self.__fp, name)

    def startCall(self):
        client = self.__fp.getClient()
        Thread(target=client.receive_audio, name="audioClientIn").start()
        Thread(target=client.send_audio, name="audioClientOut").start()
        self.__call: client_call = client_call(self.__fp)

    def setClientList(self, *names):
        try:
            current_names: list[str] = list(self.__middle_list.get(0, END))
            current_names.append(self.__fp.getClientInfos()["username"])
            if set(current_names) != set(names):
                self.__middle_list.delete(0, END)
                for i, v in enumerate(names):
                    if v != self.__fp.getClientInfos()["username"]:
                        self.__middle_list.insert(i, v)
        except:
            pass

    def setCall(self):
        selected: tuple[int] = self.__middle_list.curselection()
        names: list[str] = [self.__middle_list.get(i) for i in selected]

        if len(names) > 0:
            self.__fp.getClient().sendFlag(Flag.CAL, " ".join(names))

    def disconnected(self) -> None:

        self.__fp.getClient().sendFlag(Flag.ENT)

        self.__fp.deiconify()  # afficher la fenetre principale
        self.destroy()  # detruire la fenetre courante


class client_call(Toplevel):
    def __init__(self, fp: cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_usr: Label
        self.__lbl_time: Label
        self.__stgvar_time: StringVar
        self.__lbl_time_var: Label
        self.__btn_end: Button

        # Instanciatin des variables
        self.__lbl_usr = Label(
            self, text="USER", padx=2, pady=2, borderwidth=3, relief="ridge"
        )
        self.__lbl_time = Label(self, text="Temps Appel :", padx=2, pady=2)
        self.__stgvar_time = StringVar(value="HH:MM:SS")
        self.__lbl_time_var = Label(
            self,
            textvariable=self.__stgvar_time,
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

    def end_call(self) -> None:
        self.__fp.getClient().sendFlag(Flag.FIN)
        self.destroy()  # detruire la fenetre courante


class client_receive(Toplevel):
    def __init__(self, master, name: str):
        # Déclaration des variables
        self.__master: cote_client = master
        Toplevel.__init__(self, self.__master)
        self.__lbl_call: Label
        self.__btn_ok: Button
        self.__btn_nok: Button

        # Instanciatin des variables
        self.__lbl_call = Label(
            self, text=f"{name}", padx=2, pady=2, borderwidth=3, relief="ridge"
        )
        self.__btn_ok = Button(self, text="Accepter", command=self.ok)
        self.__btn_nok = Button(self, text="Rejeter", command=self.nok)

        # Ajout des widget
        self.__lbl_call.grid(row=0, column=1)
        self.__btn_ok.grid(row=1, column=0)
        self.__btn_nok.grid(row=1, column=2)

        self.__is_asking = True

        def answerTimeOut():
            time: int = 0
            while self.__is_asking and time < 10:
                sleep(1)
            if self.__is_asking:
                self.nok

        th: Thread = Thread(target=answerTimeOut, name="answerTimeOUT")
        th.start()

    def ok(self):
        self.__master.getClient().sendFlag(Flag.RES, "1")
        self.__is_asking = False
        self.destroy()

    def nok(self) -> None:
        self.__master.getClient().sendFlag(Flag.RES, "0")
        self.__is_asking = False
        self.destroy()  # detruire la fenetre courante


if __name__ == "__main__":
    client: cote_client = cote_client()
    client.mainloop()
