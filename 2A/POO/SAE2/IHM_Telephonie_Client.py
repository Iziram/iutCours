"""! @brief [description du fichier]
 @file IHM_Telephonie_Client.py
 @section libs Librairies/Modules
  - tkinter (lien)
 @section authors Auteur(s)
  - Créé par Sandra Valentin le 06/01/2023 .
"""
from tkinter import *

class cote_client(Tk):
    # Constructeur de la classe
    def __init__(self):
        # Définition des variables
        Tk.__init__(self)
        self.__lbl_static : Label
        self.__lbl_error : Label
        self.__lbl_usrnm : Label
        self.__entry_usrnm : Entry
        self.__lbl_pswd : Label
        self.__entry_pswd : Entry
        self.__btn_con : Button
        self.__btn_create : Button
        self.__btn_set : Button
        self.__str_var : StringVar
        self.__usr_pwd_frame : Frame

        # Instanciation des variables
        self.__usr_pwd_frame = Frame(master=self,relief='ridge',padx=5,pady=5,borderwidth=3)
        self.__str_var = StringVar()
        self.__lbl_static = Label(self,text="Vive Mitel !",padx=5,pady=5,anchor='center')
        self.__lbl_error = Label(self,textvariable=self.__str_var,fg='crimson')
        self.__lbl_usrnm = Label(self.__usr_pwd_frame,text='Userame : ',padx=3,pady=3)
        self.__entry_usrnm = Entry(self.__usr_pwd_frame,width=20)
        self.__lbl_pswd = Label(self.__usr_pwd_frame,text='Password : ',padx=3,pady=3)
        self.__entry_pswd = Entry(self.__usr_pwd_frame,width=20)
        self.__btn_con = Button(self,text='Connexion',command=lambda: client_connected(self))
        self.__btn_create = Button(self,text='➕',command=lambda: create_client(self))
        self.__btn_set = Button(self,text='⚙️',command=lambda: client_param(self))
        self.title('Connexion')

        # Ajout des widget
        self.__lbl_static.grid(row=0,column=0)
        self.__lbl_error.grid(row=1,column=0)
        self.__usr_pwd_frame.grid(row=2,column=0)
        self.__lbl_usrnm.grid(row=0,column=0)
        self.__entry_usrnm.grid(row=0,column=1)
        self.__lbl_pswd.grid(row=1,column=0)
        self.__entry_pswd.grid(row=1,column=1)
        self.__btn_con.grid(row=3,column=0)
        self.__btn_create.grid(row=3,column=1)
        self.__btn_set.grid(row=0,column=1)

class client_param(Toplevel):
    def __init__(self, fp : cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_static : Label
        self.__lbl_ip_srv : Label
        self.__entry_ip_srv : Entry
        self.__lbl_port_srv : Label
        self.__entry_port_srv : Entry
        self.__btn_valid : Button
        self.__frame_center : Frame
        self.title("Paramètres")

        # Instanciation dse variables
        self.__fp.withdraw()
        self.__frame_center = Frame(master=self,relief='ridge',padx=5,pady=5,borderwidth=3)
        self.__lbl_static = Label(self,text='Paramètre', anchor='center',padx=5,pady=5,borderwidth=5,relief='ridge')
        self.__lbl_ip_srv = Label(self.__frame_center,text='ip serveur',padx=3,pady=3)
        self.__entry_ip_srv = Entry(self.__frame_center,width=10)
        self.__lbl_port_srv = Label(self.__frame_center,text='port serveur', padx=3,pady=3)
        self.__entry_port_srv = Entry(self.__frame_center,width=10)
        self.__btn_valid = Button(self,text='Valider',command=self.valider_param)

        #Ajout des widget
        self.__lbl_static.pack()
        self.__frame_center.pack()
        self.__lbl_ip_srv.grid(row=0,column=0)
        self.__entry_ip_srv.grid(row=0,column=1)
        self.__lbl_port_srv.grid(row=1,column=0)
        self.__entry_port_srv.grid(row=1,column=1)
        self.__btn_valid.pack()
        self.protocol("WM_DELETE_WINDOW", self.valider_param)


    def valider_param(self)-> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify() # afficher la fenetre principale
        self.destroy() # detruire la fenetre courante

class create_client(Toplevel):
    def __init__(self, fp : cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_static : Label
        self.__lbl_nm_usr : Label
        self.__entry_nm_usr : Entry
        self.__lbl_mdp_usr : Label
        self.__entry_mdp_usr : Entry
        self.__btn_valid : Button
        self.__frame_center : Frame
        self.title("Nouvel utilisateur")

        # Instanciation des variables
        self.__fp.withdraw()
        self.__frame_center = Frame(master=self,relief='ridge',padx=5,pady=5,borderwidth=3)
        self.__lbl_static = Label(self,text='Création nouveau compte', anchor='center',padx=5,pady=5,borderwidth=5,relief='ridge')
        self.__lbl_nm_usr = Label(self.__frame_center,text='Nom utilisateur : ',padx=3,pady=3)
        self.__entry_nm_usr = Entry(self.__frame_center,width=20)
        self.__lbl_mdp_usr = Label(self.__frame_center,text='mot de passe : ', padx=3,pady=3)
        self.__entry_mdp_usr = Entry(self.__frame_center,width=20)
        self.__btn_valid = Button(self,text='Valider',command=self.valider_create)

        #Ajout des widget
        self.__lbl_static.pack()
        self.__frame_center.pack()
        self.__lbl_nm_usr.grid(row=0,column=0)
        self.__entry_nm_usr.grid(row=0,column=1)
        self.__lbl_mdp_usr.grid(row=1,column=0)
        self.__entry_mdp_usr.grid(row=1,column=1)
        self.__btn_valid.pack()
        self.protocol("WM_DELETE_WINDOW", self.valider_create)


    def valider_create(self)-> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify() # afficher la fenetre principale
        self.destroy() # detruire la fenetre courante


class client_connected(Toplevel):
    def __init__(self, fp : cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__middle_frame : Frame
        self.__right_frame : Frame
        self.__middle_search : Entry
        self.__middle_btn_search : Button
        self.__middle_list : Text
        self.__middle_btn_call : Button
        self.__right_pp : Label
        self.__right_lbl_usr : Label
        self.__right_btn_disc : Button

        # Instanciatin des variables
        self.__fp.withdraw()
        self.__middle_frame = Frame(master=self,relief='ridge',padx=5,pady=5,borderwidth=3)
        self.__right_frame = Frame(master=self,relief='ridge',padx=5,pady=5,borderwidth=3)
        self.__middle_search = Entry(self.__middle_frame,width=15)
        self.__middle_btn_search = Button(self.__middle_frame,text="🔍")
        self.__middle_list = Text(self.__middle_frame,width=17,height=10)
        self.__middle_btn_call = Button(self.__middle_frame,text='Appeler',relief='ridge',padx=2,pady=2,command=lambda: client_call(self))
        self.__right_pp = Label(self.__right_frame,text='Connected',padx=2,pady=2,borderwidth=3,relief='ridge',bg='MediumSpringGreen')
        self.__right_lbl_usr = Label(self.__right_frame,text='USER',padx=2,pady=2,borderwidth=3,relief='ridge')
        self.__right_btn_disc = Button(self.__right_frame,text='Déconnecter',fg='crimson',command=self.disconnected)

        # Ajout des widget
        self.__middle_frame.grid(row=0,column=0)
        self.__right_frame.grid(row=0,column=1)
        self.__middle_search.grid(row=0,column=0)
        self.__middle_btn_search.grid(row=0,column=1)
        self.__middle_list.grid(row=1,column=0)
        self.__middle_btn_call.grid(row=1,column=1)
        self.__right_pp.pack()
        self.__right_lbl_usr.pack()
        self.__right_btn_disc.pack()
        self.protocol("WM_DELETE_WINDOW", self.disconnected)

    def disconnected(self)-> None:
        # applel du modificateur de la classe mêre
        self.__fp.deiconify() # afficher la fenetre principale
        self.destroy() # detruire la fenetre courante


class client_call(Toplevel):
    def __init__(self, fp : cote_client):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__fp = fp
        self.__lbl_usr : Label
        self.__lbl_time : Label
        self.__stgvar_time : StringVar
        self.__lbl_time_var: Label
        self.__btn_end : Button

        # Instanciatin des variables
        self.__lbl_usr = Label(self,text='USER',padx=2,pady=2,borderwidth=3,relief='ridge')
        self.__lbl_time = Label(self,text='Temps Appel :',padx=2,pady=2)
        self.__stgvar_time = StringVar(value='HH:MM:SS')
        self.__lbl_time_var = Label(self,textvariable=self.__stgvar_time,padx=2,pady=2,borderwidth=3,relief='ridge')
        self.__btn_end = Button(self,text='Raccrocher',bg='crimson',command=self.end_call)

        # Ajout des widget
        self.__lbl_usr.pack()
        self.__lbl_time.pack()
        self.__lbl_time_var.pack()
        self.__btn_end.pack()

    def end_call(self)-> None:
        # applel du modificateur de la classe mêre
        self.destroy() # detruire la fenetre courante

class client_receive(Toplevel):
    def __init__(self):
        # Déclaration des variables
        Toplevel.__init__(self)
        self.__lbl_call : Label
        self.__btn_ok : Button
        self.__btn_nok : Button

        # Instanciatin des variables
        self.__lbl_call = Label(self,text='USER',padx=2,pady=2,borderwidth=3,relief='ridge')
        self.__btn_ok = Button(self,text='Accepter',command=lambda: client_call(self))
        self.__btn_nok = Button(self,text='Rejeter',command=self.nok)

        # Ajout des widget
        self.__lbl_call.grid(row=0,column=1)
        self.__btn_ok.grid(row=1,column=0)
        self.__btn_nok.grid(row=1,column=2)
    
    def nok(self)-> None:
        # applel du modificateur de la classe mêre
        self.destroy() # detruire la fenetre courante

if __name__=="__main__":
    client: cote_client = cote_client()
    client.mainloop()
