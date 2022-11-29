from tkinter import *


class MonIHM(Tk):
    def __init__(self) -> None:
        # déclaration des variabes
        self.texte: Text
        self.btn_quitter: Button
        self.entree: Entry
        self.btn_valide: Button
        # instanciation
        Tk.__init__(self)
        self.texte = Text(self, width=40, height=10)
        self.btn_quitter = Button(self, text="quitter", bg="red", command=self.destroy)
        self.entree = Entry(self, width=30)
        self.btn_valide = Button(
            self,
            text="validez votre saisie",
            borderwidth=3,
            relief=RAISED,
            command=self.action,
        )
        # initialisation
        self.title("Ma première IHM")
        # ajout des widgets à l'IHM
        self.texte.grid(row=0, column=0)
        self.btn_quitter.grid(row=1, column=0)
        self.entree.grid(row=0, column=1)
        self.btn_valide.grid(row=1, column=1)

    def action(self):
        chaine: str = self.entree.get()  # lecture de la chaine du widget entree
        self.texte.insert(
            INSERT, f"{chaine} \n"
        )  # INSERT pour ajouter du texte au widget texte
        self.entree.delete(
            first=0, last=END
        )  # pour effacer le contenu de la barre de saisie


if __name__ == "__main__":
    test = MonIHM()
    test.mainloop()
