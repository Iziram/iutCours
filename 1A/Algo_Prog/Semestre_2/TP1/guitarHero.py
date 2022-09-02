from random import randint
from time import sleep
from os import system
from saisiCar import SaisiCar
class Note:
    couleurs  = ["\033[1;31;40m", "\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;47m"]
    lettres = ["a","b","c","d"]
    
    def __init__(self, posX: int, posY:int = 0):
        self.posX = posX
        self.posY = posY
        self.couleur= posX
        
    def update(self):
        if self.posY < Jeu.hauteur:
            self.posY += 1
        else:
            Jeu.notes.remove(self)
            Jeu.vie -= 1
            
    def __str__(self):
        return Note.couleurs[self.couleur] + Note.lettres[self.posX] + "\033[0;37;40m"
    

class Jeu:
    hauteur : int = 30
    frames : float = 0.1
    notes = []
    vie = 5
    def __init__(self):
        self.vitesse : float = 1.0
        self.noteCoolDown : float = 0
        Jeu.notes = []
        self.score = 0
        Jeu.vie = 3
        self.elapsed = 0
    
    def genererNote(self):
        if self.noteCoolDown < 0:
            Jeu.notes.append(Note(randint(0,3)))
            self.noteCoolDown = self.vitesse
        else:
            self.noteCoolDown -= Jeu.frames
    
    def bandeau(self):
        print("----")
        print(f"Score : {self.score} Vie : {self.vie}")
        txt : str = ""
        for i in range(len(Note.lettres)):
            txt += f"{Note.couleurs[i]}{Note.lettres[i]}"
        print(txt, end="\033[0;37;40m\n")
        print("----")
    
    def affichage(self):
        self.bandeau()
        for ligne in range(Jeu.hauteur):
            for col in range(4):
                char : str = " " if ligne != Jeu.hauteur - 1 else "-" 
                for n in Jeu.notes:
                    if n.posX == col and n.posY == ligne:
                        char = n
                print(char, end="")
            print("\n", end="")
        lettres = ["j","k","l","m"]
        txt = ""
        for i in range(len(lettres)):
            txt += f"{Note.couleurs[i]}{lettres[i]}"
        print(txt, end="\033[0;37;40m\n")
    
    def acceleration(self, acc:float = 0.01):
        if self.elapsed > 2:
            self.vitesse -= acc
            self.elapsed = 0
    
    def notesBasses(self):
        notes = []
        for n in Jeu.notes :
            if n.posY >= Jeu.hauteur-3:
                n.couleur = 4
                
                notes.append(n)
        return notes
    
    def verification(self, col:int, notes):
        for n in reversed(notes):
                if n.posX == col:
                    self.score += 1
                    Jeu.notes.remove(n)
                    break
    def actionUtilisateur(self, action: str, notes):
        if action == "j":
            self.verification(0,notes)
        elif action == "k":
            self.verification(1,notes)
        elif action == "l":
            self.verification(2,notes)
        elif action == "m":
            self.verification(3,notes)
    
    def boucle(self):
        kb = SaisiCar()
        action = ""
        while Jeu.vie > 0 and action != "q":
            system("clear")
            action = kb.recupCar(["j","k","l","m","q"])
            self.genererNote()
            self.affichage()
            for n in Jeu.notes: n.update()
            notes = self.notesBasses()
            self.actionUtilisateur(action, notes)
            
            self.acceleration()
            sleep(Jeu.frames)
            self.elapsed += Jeu.frames
            

game = Jeu()
game.boucle()