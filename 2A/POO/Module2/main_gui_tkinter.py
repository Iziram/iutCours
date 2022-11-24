from tkinter import *

# déclaration des variables
ihm: Tk
btn: Button
label: Label
entree: Entry
texte: Text
fen_gauche: Frame
fen_droite: Frame
# instanciation
ihm = Tk()
fen_gauche = Frame(ihm, borderwidth=10, relief="groove", padx=10, pady=10)
fen_droite = Frame(ihm, borderwidth=10, relief="groove", padx=10, pady=10)
btn = Button(
    fen_droite, text="voici un bouton", borderwidth=5, relief="raised", padx=5, pady=5
)
label = Label(
    fen_droite, text="voici un label", borderwidth=5, relief="ridge", padx=5, pady=5
)
entree = Entry(fen_droite, width=30)
texte = Text(fen_gauche, width=40, height=10)
# initialisation
ihm.title("Ma première IHM")
texte.insert(0.0, "voici une zone de texte")
# ajout des widget à l'IHM
fen_gauche.pack(side=LEFT)
texte.pack()
fen_droite.pack(side=RIGHT)
label.grid(row=0, column=0)
btn.grid(row=0, column=1)
entree.grid(row=1)
# lancer la boucle d'évènements


def action(nb_repetition: int) -> None:
    chaine: str = entree.get()
    for i in range(nb_repetition):
        texte.insert(INSERT, f"{chaine} \n")  # INSERT pour ajouter du texte
    entree.delete(first=0, last=END)  # pour effecer le contenu de la barre de saisie


btn.configure(command=lambda: action(3))

btn_quitter = Button(fen_gauche, text="quitter", bg="orange", command=ihm.destroy)


ihm.mainloop()
