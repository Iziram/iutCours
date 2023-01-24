"""! @brief [description du fichier]
 @file IHM_Telephonie_Serveur.py
 @section libs Librairies/Modules
  - tkinter (lien)
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
  - Mis à jour par Matthias HARTMANN le 24/01/2023 .
"""
from tkinter import *
from tkinter.messagebox import *

from server import Server

"""
Début de l'IHM côté serveur
"""


class TextWithVar(Text):
    """A text widget that accepts a 'textvariable' option"""

    def __init__(self, parent, *args, **kwargs):
        try:
            self._textvariable = kwargs.pop("textvariable")
        except KeyError:
            self._textvariable = None

        Text.__init__(self, parent, *args, **kwargs)

        # if the variable has data in it, use it to initialize
        # the widget
        if self._textvariable is not None:
            self.insert("1.0", self._textvariable.get())

        # this defines an internal proxy which generates a
        # virtual event whenever text is inserted or deleted
        self.tk.eval(
            """
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                # return the result from the real widget command
                return $result
            }
            """
        )

        # this replaces the underlying widget with the proxy
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        """.format(
                widget=str(self)
            )
        )

        # set up a binding to update the variable whenever
        # the widget changes
        self.bind("<<Change>>", self._on_widget_change)

        # set up a trace to update the text widget when the
        # variable changes
        if self._textvariable is not None:
            self._textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *args):
        """Change the text widget when the associated textvariable changes"""

        # only change the widget if something actually
        # changed, otherwise we'll get into an endless
        # loop
        text_current = self.get("1.0", "end-1c")
        var_current = self._textvariable.get()
        if text_current != var_current:
            self.delete("1.0", "end")
            self.insert("1.0", var_current)
            self.see(END)

    def _on_widget_change(self, event=None):
        """Change the variable when the widget changes"""
        if self._textvariable is not None:
            self._textvariable.set(self.get("1.0", "end-1c"))
            self.see(END)


class cote_server(Tk, Server):
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
        self.__Frame_top = Frame(master=self, relief=GROOVE)
        self.__Frame_btm = Frame(master=self, relief=GROOVE)

        self.__Frame_top.pack(padx=5, pady=10)
        self.__Frame_btm.pack(padx=5, pady=10)

        self.title("Interface côté serveur")
        self.__lbl_ip_serv = Label(self.__Frame_top, text="ip du serveur : ")
        self.__lbl_port_commande = Label(self.__Frame_top, text="port commande")
        self.__entry_ip_serv = Entry(self.__Frame_top, width=25)
        self.__entry_port_commande = Entry(self.__Frame_top, width=25)
        self.__btn_start = Button(
            self.__Frame_top, text="Démarrer", command=self.demarrer
        )
        self.__btn_csl = Button(
            self.__Frame_top, text="©", command=lambda: console_serv(self)
        )

        self.__var_log = StringVar()

        self.__win_log = TextWithVar(
            self.__Frame_btm,
            width=120,
            height=40,
            textvariable=self.__var_log,
            bg="white",
            relief=GROOVE,
        )
        self.__btn_quit = Button(
            self.__Frame_top, text="Quitter", bg="red", command=self.callback
        )

        # Ajout des widget défini ci-dessuss + Ajout de frame pour superposé les éléments

        self.__lbl_ip_serv.grid(row=0, column=0)
        self.__entry_ip_serv.grid(row=0, column=1)
        self.__lbl_port_commande.grid(row=2, column=0)
        self.__entry_port_commande.grid(row=2, column=1)
        self.__btn_start.grid(row=3, column=1)
        self.__btn_csl.grid(row=3, column=2)
        self.__btn_quit.grid(row=3, column=3)
        self.__win_log.pack()

        self.__win_log.bind("<Key>", lambda e: "break")

        Server.LOG.setEvent(lambda x: self.__var_log.set(x))

        self.__entry_ip_serv.insert(INSERT, "127.0.0.1")
        self.__entry_port_commande.insert(INSERT, "5000")

        self.__btn_csl["state"] = "disable"

    def callback(self):
        msg_box = askquestion("Quitter", "Etes-vous sûr de vouloir quitter ?")
        if msg_box == "yes":
            self.getInterpreter().run_command("quit", *[])
            self.destroy()

    def getVarLog(self):
        return self.__var_log

    def demarrer(self):
        ip: str = self.__entry_ip_serv.get()
        port: int = int(self.__entry_port_commande.get())

        self.setter(ip, port)
        Server.LOG.add("Serveur lancé")

        self.__btn_start["state"] = "disable"
        self.__btn_csl["state"] = "active"


class console_serv(Toplevel):
    def __init__(self, fp: cote_server):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__btn_hlp: Button
        self.__text_log: Text
        self.__entry_input: Entry
        self.__btn_send: Button
        self.__btn_retour: Button
        self.title("console")

        # Instancation des variables
        self.__fp.withdraw()
        self.__btn_hlp = Button(self, text="❓", command=lambda: hlp_srv(self))
        self.__text_log = TextWithVar(
            self,
            textvariable=self.__fp.getVarLog(),
            bg="white",
            relief=GROOVE,
        )
        self.__btn_send = Button(self, text="Envoyer", command=self.action)
        self.__entry_input = Entry(self, width=160)
        self.__btn_retour = Button(self, text="Retour", command=self.configuration)

        # Ajout des widgets
        self.__text_log.grid(row=1, column=0, padx=5, pady=5)

        self.__btn_hlp.grid(row=0, column=1, padx=5, pady=5)
        self.__entry_input.grid(row=2, column=0, padx=5, pady=5)
        self.__btn_send.grid(row=2, column=1, padx=5, pady=5)
        self.__btn_retour.grid(row=0, column=0, padx=5, pady=5)
        self.protocol("WM_DELETE_WINDOW", self.configuration)

        # ajout d'evenements
        self.__entry_input.bind("<Return>", self.action)
        self.__entry_input.bind("<KP_Enter>", self.action)
        self.__text_log.bind("<Key>", lambda e: "break")

    def configuration(self) -> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify()  # afficher la fenetre principale
        self.destroy()  # detruire la fenetre courante

    def action(self, _: Event = None) -> None:
        cmd_line: str = self.__entry_input.get()

        Server.LOG.add(f"COMMAND : {cmd_line}")

        self.__fp.execute(cmd_line)

        self.__entry_input.delete(0, END)


class hlp_srv(Toplevel):
    def __init__(self, fp: console_serv):
        # Déclaration des variablesstar
        Toplevel.__init__(self)
        self.__fp = fp
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


"""
Fin de l'IHM côté serveur.
"""

if __name__ == "__main__":
    server: cote_server = cote_server()
    server.mainloop()
