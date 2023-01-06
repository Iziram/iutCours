from tkinter import *

from gene_mdp_etu import generateur_mdp


class Ihm_Mdp(Tk):
    pass


class Ihm_Config(Toplevel):
    def __init__(self, master: Ihm_Mdp) -> None:
        self.__ihm_mdp: Ihm_Mdp = master
        Toplevel.__init__(self, master)

        self.title("configuration")

        self.__lbl_nb_car: Label = Label(self, text="nb caracteres")
        self.__entree_nb_car: Entry = Entry(self, width=5)
        self.__entree_nb_car.insert(INSERT, "12")
        self.__var_chiffre: BooleanVar = BooleanVar(self)
        self.__check_chiffres: Checkbutton = Checkbutton(
            self,
            variable=self.__var_chiffre,
            text="chiffres",
        )
        self.__var_majuscules: BooleanVar = BooleanVar(self)
        self.__check_majuscules: Checkbutton = Checkbutton(
            self,
            variable=self.__var_majuscules,
            text="majuscules",
        )
        self.__var_special: BooleanVar = BooleanVar(self)
        self.__check_car_special: Checkbutton = Checkbutton(
            self,
            variable=self.__var_special,
            text="caractères spéciaux",
        )

        self.__validation_btn: Button = Button(
            self, text="Validation", command=self.validation
        )

        self.__lbl_nb_car.grid(column=0, row=0)
        self.__entree_nb_car.grid(column=1, row=0)
        self.__check_chiffres.grid(column=0, row=1)
        self.__check_majuscules.grid(column=0, row=2)
        self.__check_car_special.grid(column=0, row=3)
        self.__validation_btn.grid(column=0, row=4)

    def validation(self):
        nb_char: int = int(self.__entree_nb_car.get())
        has_chiffre: bool = self.__var_chiffre.get()
        has_maj: bool = self.__var_majuscules.get()
        has_special: bool = self.__var_special.get()

        self.__ihm_mdp.set_var(
            nb=nb_char, chiffres=has_chiffre, maj=has_maj, special=has_special
        )

        self.deiconify()
        self.destroy()


class Ihm_Mdp(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)

        self.title("Générateur de mot de passe")

        self.__fen_configuration: Frame = Frame(
            self, borderwidth=10, relief="groove", padx=10, pady=10
        )
        self.__fen_generation: Frame = Frame(
            self, borderwidth=10, relief="groove", padx=10, pady=10
        )
        self.__lbl_nb_car: Label = Label(
            self.__fen_configuration, text="nb caracteres: 12"
        )
        self.__lbl_chiffres: Label = Label(
            self.__fen_configuration, text="sans chiffres"
        )
        self.__lbl_majs: Label = Label(self.__fen_configuration, text="sans majuscules")
        self.__lbl_spec: Label = Label(
            self.__fen_configuration, text="sans caractères spéciaux"
        )

        self.__btn_configuration: Button = Button(
            self.__fen_configuration,
            command=lambda: Ihm_Config(self),
            text="Configurer",
        )

        self.__entree_mdp: Entry = Entry(self.__fen_generation)
        self.__btn_gen: Button = Button(
            self.__fen_generation, text="nouveau mdp", command=self.generer_mdp
        )

        self.__btn_quitter: Button = Button(
            self.__fen_generation, command=self.destroy, text="Quitter", bg="red"
        )

        self.__fen_configuration.grid(column=0, row=0)
        self.__fen_generation.grid(column=0, row=1)

        self.__lbl_nb_car.grid(column=0, row=0)
        self.__lbl_chiffres.grid(column=0, row=1)
        self.__lbl_majs.grid(column=0, row=2)
        self.__lbl_spec.grid(column=0, row=3)
        self.__btn_configuration.grid(column=0, row=4)

        self.__entree_mdp.pack(fill="y")
        self.__btn_gen.pack(side="left", padx=5)
        self.__btn_quitter.pack(side="right", padx=5)

        self.__val_chiffres: bool = False
        self.__val_majs: bool = False
        self.__val_spec: bool = False
        self.__val_nb_char: int = 12

    def set_var(self, **kwargs: dict[str, object]):
        for k in kwargs:
            if k == "chiffres":
                check: str = "avec" if kwargs[k] else "sans"
                self.__lbl_chiffres["text"] = check + " chiffres"
                self.__val_chiffres = kwargs[k]
            elif k == "maj":
                check: str = "avec" if kwargs[k] else "sans"
                self.__lbl_majs["text"] = check + " majuscules"
                self.__val_majs = kwargs[k]

            elif k == "special":
                check: str = "avec" if kwargs[k] else "sans"
                self.__lbl_spec["text"] = check + " caractères spéciaux"
                self.__val_spec = kwargs[k]

            elif k == "nb":
                self.__lbl_nb_car["text"] = f"nb caracteres: {kwargs[k]}"
                self.__val_nb_char = kwargs[k]

    def generer_mdp(self, _: Event = None):

        mdp = generateur_mdp(
            self.__val_nb_char, self.__val_chiffres, self.__val_majs, self.__val_spec
        )

        self.__entree_mdp.delete(0, END)
        self.__entree_mdp.insert(0, mdp)


if __name__ == "__main__":
    ihm: Ihm_Mdp = Ihm_Mdp()

    ihm.mainloop()
