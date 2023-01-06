from tkinter import *

from gene_mdp_etu import generateur_mdp


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
        self.__lbl_nb_car: Label = Label(self.__fen_configuration, text="nb caracteres")
        self.__entree_nb_car: Entry = Entry(self.__fen_configuration, width=5)
        self.__entree_nb_car.insert(INSERT, "12")
        self.__var_chiffre: BooleanVar = BooleanVar(self.__fen_configuration)
        self.__check_chiffres: Checkbutton = Checkbutton(
            self.__fen_configuration,
            variable=self.__var_chiffre,
            text="chiffres",
        )
        self.__var_majuscules: BooleanVar = BooleanVar(self.__fen_configuration)
        self.__check_majuscules: Checkbutton = Checkbutton(
            self.__fen_configuration,
            variable=self.__var_majuscules,
            text="majuscules",
        )
        self.__var_special: BooleanVar = BooleanVar(self.__fen_configuration)
        self.__check_car_special: Checkbutton = Checkbutton(
            self.__fen_configuration,
            variable=self.__var_special,
            text="caractères spéciaux",
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
        self.__entree_nb_car.grid(column=1, row=0)
        self.__check_chiffres.grid(column=0, row=1)
        self.__check_majuscules.grid(column=0, row=2)
        self.__check_car_special.grid(column=0, row=3)

        self.__entree_mdp.pack(fill="y")
        self.__btn_gen.pack(side="left", padx=5)
        self.__btn_quitter.pack(side="right", padx=5)

        self.__entree_nb_car.bind("<KeyRelease>", self.generer_mdp)
        self.__check_car_special.bind("<ButtonRelease-1>", self.generer_mdp)
        self.__check_chiffres.bind("<ButtonRelease-1>", self.generer_mdp)
        self.__check_majuscules.bind("<ButtonRelease-1>", self.generer_mdp)

    def generer_mdp(self, _: Event = None):

        nb_char: int = int(self.__entree_nb_car.get())
        has_chiffre: bool = self.__var_chiffre.get()
        has_maj: bool = self.__var_majuscules.get()
        has_special: bool = self.__var_special.get()

        mdp = generateur_mdp(nb_char, has_chiffre, has_maj, has_special)

        self.__entree_mdp.delete(0, END)
        self.__entree_mdp.insert(0, mdp)


if __name__ == "__main__":
    ihm: Ihm_Mdp = Ihm_Mdp()

    ihm.mainloop()
