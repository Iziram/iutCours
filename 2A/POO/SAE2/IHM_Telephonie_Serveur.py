"""! @brief [description du fichier]
 @file IHM_Telephonie_Serveur.py
 @section libs Librairies/Modules
  - tkinter (lien)
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
"""
from tkinter import *
from tkinter.messagebox import *

"""
Début de l'IHM côté serveur
"""
class cote_server(Tk):
    def __init__(self):
        # déclaration des variables
        Tk.__init__(self)
        self.__lbl_ip_serv : Label
        self.__entry_ip_serv : Entry
        self.__lbl_port_audio: Label
        self.__entry_port_audio : Entry
        self.__lbl_port_commande: Label
        self.__entry_port_commande: Entry
        self.__btn_start: Button
        self.__btn_csl: Button
        self.__win_log: Text
        self.__btn_quit: Button

        # Initialisation des variables
        self.__Frame_top = Frame(master=self, relief=GROOVE)
        self.__Frame_btm = Frame(master=self, relief=GROOVE)

        self.__Frame_top.pack(padx=5,pady=10)
        self.__Frame_btm.pack(padx=5,pady=10)

        self.title("Interface côté serveur")
        self.__lbl_ip_serv = Label(self.__Frame_top, text="ip du serveur : ")
        self.__lbl_port_commande = Label(self.__Frame_top, text="port commande")
        self.__entry_ip_serv = Entry(self.__Frame_top, width=25)
        self.__entry_port_audio = Entry(self.__Frame_top, width=25)
        self.__entry_port_commande = Entry(self.__Frame_top, width=25)
        self.__btn_start = Button(self.__Frame_top, text="Démarrer")
        self.__btn_csl = Button(self.__Frame_top, text="©", command= lambda: console_serv(self))
        self.__win_log = Text(self.__Frame_btm, width=120, height=40)
        self.__btn_quit = Button(self.__Frame_top, text="Quitter", bg="red", command=self.callback)

        # Ajout des widget défini ci-dessuss + Ajout de frame pour superposé les éléments

        self.__lbl_ip_serv.grid(row=0, column=0)
        self.__entry_ip_serv.grid(row=0, column=1)
        self.__lbl_port_commande.grid(row=2, column=0)
        self.__entry_port_commande.grid(row=2, column=1)
        self.__btn_start.grid(row=3, column=1)
        self.__btn_csl.grid(row=3, column=2)
        self.__btn_quit.grid(row=3, column=3)
        self.__win_log.pack()

    def callback(self):
        msg_box = askquestion('Quitter','Etes-vous sûr de vouloir quitter ?')
        if msg_box == 'yes':
            self.destroy()

class console_serv(Toplevel):
    def __init__(self, fp : cote_server):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__btn_hlp : Button
        self.__text_log: Text
        self.__entry_input: Entry
        self.__btn_send: Button
        self.__btn_retour: Button
        self.title("console")

        # Instancation des variables
        self.__fp.withdraw()
        self.__btn_hlp = Button(self, text="❓",command=lambda: hlp_srv(self))
        self.__text_log = Text(self, width=120, height=40)
        self.__btn_send = Button(self, text="Envoyer", command=self.action)
        self.__entry_input = Entry(self, width=160)
        self.__btn_retour = Button(self, text="Retour", command=self.configuration)

        # Ajout des widgets
        self.__text_log.grid(row=1, column=0,padx=5,pady=5)
        self.__btn_hlp.grid(row=0, column=1,padx=5,pady=5)
        self.__entry_input.grid(row=2, column=0,padx=5,pady=5)
        self.__btn_send.grid(row=2, column=1,padx=5,pady=5)
        self.__btn_retour.grid(row=0, column=0,padx=5,pady=5)
        self.protocol("WM_DELETE_WINDOW", self.configuration)

        # ajout d'evenements
        self.__entry_input.bind("<Return>", self.action)
        self.__entry_input.bind("<KP_Enter>", self.action)

    def configuration(self)-> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify() # afficher la fenetre principale
        self.destroy() # detruire la fenetre courante

    def action(self, evt:Event = None)-> None:
        if evt is not None:
            print(evt)
        chaine: str = self.__entry_input.get() # lecture de la chaine du widget entree
        self.__text_log.insert(INSERT, f"{chaine} \n") # INSERT pour ajouter du texte au widget texte
        self.__entry_input.delete(first=0, last= END) # pour effacer le contenu de la barre de saisie
        
class hlp_srv(Toplevel):
    def __init__(self, fp : console_serv):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_list : Label
        self.__txt_command : Text        

        # Instanciation des variables
        self.title("help commandes")
        self.__lbl_list = Label(self,text="Liste des commandes",borderwidth=5,relief="ridge")
        self.__txt_command = Text(self,width=40,height=30)

        # Ajout des widgets
        self.__lbl_list.pack(padx=10,pady=10)
        self.__txt_command.pack(padx=10,pady=10)

"""
Fin de l'IHM côté serveur.
"""

if __name__=="__main__":
    server: cote_server = cote_server()
    server.mainloop()