from typing import List, Dict, Tuple
from os import system, name
from time import sleep
from saisiCar import SaisiCar
from random import sample, randint
from json import load, dump

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

class Plateau:
    largeur: int = 30
    hauteur: int = 20
    normalC : str = "\033[0;37;40m"

    typeTirs : List[str] = [":","+","|"]
    def afficherLigne():
        print("-"*Plateau.largeur)
        
    def afficherBandeau(self,jeu):
        Plateau.afficherLigne()
        print(" " * 2 + "SCORE" + " " * 4 + "VIE" + " " * 4 + "NIVEAU")
        print(
        f'  {jeu.score:5}  {jeu.vie : 5}     {jeu.niveau : 5}')
        Plateau.afficherLigne()
        
    def afficherPlateau(self,jeu, posTir:Tuple[int,int] = None):
        for ligne in range(Plateau.hauteur):
            for col in range(Plateau.largeur):
                if posTir != None and col == posTir[0] and ligne < Plateau.hauteur -1 and ligne > posTir[1]:
                    print(Plateau.typeTirs[jeu.vaisseau.nivTir -1], end=Plateau.normalC)
                    continue
                if(ligne == Plateau.hauteur - 1 and jeu.vaisseau.posX == col):
                    print(jeu.vaisseau, end=Plateau.normalC)
                    continue
                char : str = " "
                posA : List[Alien] = [a for a in jeu.aliens if a.position() == (col, ligne)]
                posP : List[any] = [a for a in jeu.PowersUp if a.position() == (col, ligne)]
                
                if len(posP) > 0 :
                    char = posP[0]
                
                if len(posA) > 0 :
                    char = posA[0]
                
                print(char, end=Plateau.normalC)
                
            print("\n", end="")



class Vaisseau:
    vaisseauC : str = "\033[1;31;40m"
    def __init__(self, x:int = 0):
        self.posX : int = x
        self.tir : bool = False
        self.nivTir : int = 1
        self.cooldown : int = 0
    
    def action(self, keyPressed: str):
        if keyPressed == "o" and self.cooldown == 0:
            self.tir = True
            self.cooldown = 2
        elif keyPressed == "k":
            if(self.posX > 0):
                self.posX -= 1
        elif keyPressed == "m":
            if(self.posX < Plateau.largeur - 1):
                self.posX += 1
    
    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
    def __repr__(self):
        return f'Vaisseau : position = {self.posX} tir spécial = {self.nivTir}'
    def __str__(self):
        return f'{self.vaisseauC}#'

class PowerUp:
    def __init__(self, posX: int, posY: int, niveau: int = 2, type_: str = "powerup"):
        self.posX = posX
        self.posY = posY
        self.niveau = niveau
        self.type = type_
    def update(self, partie: any):
        if (self.posY < Plateau.hauteur):
            if(self.posX == partie.vaisseau.posX and self.posY == Plateau.hauteur - 1):
                if(self.type == "powerup"):
                    partie.vaisseau.nivTir = max(partie.vaisseau.nivTir, self.niveau)
                elif self.type == "bombe":
                    if(partie.vaisseau.nivTir > 1):
                        partie.vaisseau.nivTir -= 1
                    else:
                        partie.vie -= 1
                PartieJeu.PowersUp.remove(self)
            else:
                self.posY += 1
        else:
            PartieJeu.PowersUp.remove(self)
    def position(self):
        return (self.posX, self.posY)
    def __str__(self):
        return "\033[1;34;40m" + f"{self.niveau}" if self.type == "powerup" else "\033[1;31;40m" + "¤"

class Alien:
    alienC : str = "\033[1;32;40m"
    def __init__(self, x:int, y:int, nivTir : int = 0):
        self.posX = x
        self.posY = y
        self.sens = True
        self.nivTir = nivTir
    def __repr__(self):
        return f'en position ({self.posX}, {self.posY}) - tir {self.nivTir}'
    def __str__(self):
        return f'{self.alienC}@'
    
    def mort(self):
        return True if self.nivTir > 0 else False
    
    def larguerBombe(self):
        rdm : int = randint(1,200)
        if rdm == 1:
            return True
        return False

    def position(self) -> Tuple[int, int]:
        return (self.posX, self.posY)

class PartieJeu:
    modeEmploi : str = """Bienvenue Dans SpaceInvaders:
        Utilisez els touches o,k,m pour tirer, se déplacer à gauche ou à droite"""
    PowersUp : List[PowerUp] = []
    def __init__(self, vaisseau: Vaisseau, nombreAlien : int = 30,
                vie : int = 3, score : int = 0, niveau : int = 1):
        self.vie : int = vie
        self.score : int = score
        self.niveau : int = niveau
        self.vaisseau : Vaisseau = vaisseau
        self.aliens : List[Alien] = []
        self.nombreAlien = nombreAlien
        self.initialiserAliens(nombreAlien)
    
    def initialiserAliens(self, nbAliens:int, nbLignes:int = 10, powerUp : int = 5):
        self.aliens = []
        y = -1 
        for i in range(nbAliens):
            x = i % nbLignes
            if(x == 0) : y += 1
            self.aliens.append(Alien(x+Plateau.largeur//2 - nbLignes//2,y))
            
        aliensPower : List[Alien] = sample(self.aliens, powerUp)
        for a in aliensPower:
            a.nivTir = randint(2,3)
    
    def afficherAliens(self):
        print("Les aliens: ")
        for a in self.aliens:
            print(f'\t {repr(a)}')
    
    def deplacementAliens(self):
        sens = self.aliens[0].sens
        bord : bool = False
        if not sens:
            for a in self.aliens:
                if a.posX <= 0:
                    bord = True
        else:
            for a in self.aliens:
                if a.posX >= Plateau.largeur - 1:
                    bord = True

        for a in self.aliens:
            if bord:
                a.posY += 1
                a.sens = not(a.sens)
            else:
                if sens:
                    a.posX += 1
                else:
                    a.posX -= 1
    
    def alienPlusBas(self) -> Alien:
        if(len(self.aliens) > 0 ):
            return max(self.aliens, key = lambda alien:alien.posY)
        return None
    def aliensSurColonne(self, colonne:int) -> List[Alien]:
        aliens = [a for a in self.aliens if a.posX == colonne]
        
        return aliens
    def tuerAliens(self, aliens:List[Alien], nombre:int) -> int:
        if(aliens != None or len(aliens) > 0):
            for i in range(nombre):
                if len(aliens) > 0:
                    mort : Alien = aliens.pop()
                    if mort.mort():
                        PartieJeu.PowersUp.append(PowerUp(mort.posX, mort.posY, mort.nivTir))
                    self.aliens.remove(mort)
            return nombre
        return 0
    
    def boucleDeJeu(self, plateau:Plateau):
        action : str = ""
        kb = SaisiCar()
        while self.vie > 0 and action !="q":
            clear()
            action = kb.recupCar(["m", "k", "o", "q"])
            if(action != None and action != ""):
                self.vaisseau.action(action)
            
            plateau.afficherBandeau(self)
            if (self.vaisseau.tir == True):
                aliens : List[Alien] = self.aliensSurColonne(self.vaisseau.posX)
                self.score += 5 * self.tuerAliens(aliens, self.vaisseau.nivTir)  
                self.vaisseau.tir = False
                if len(aliens) > 0:
                    plateau.afficherPlateau(self, aliens[-1].position())
                else:
                    plateau.afficherPlateau(self, (self.vaisseau.posX, -1))
            else:
                plateau.afficherPlateau(self)
            if(self.finJeu(self.alienPlusBas())):
                PartieJeu.PowersUp = []
                self.initialiserAliens(20 + 10 * self.niveau)

            else:
                self.deplacementAliens()
                for a in self.aliens :
                    if(a.larguerBombe()):
                        PartieJeu.PowersUp.append(PowerUp(a.posX, a.posY, type_="bombe"))
                for p in PartieJeu.PowersUp : p.update(self)
                
            self.vaisseau.update()
            sleep(.1)
    
    def finJeu(self, alien: Alien) -> bool:
        if len(self.aliens) < 1 :
            self.niveau += 1
            return True
        elif alien.posY == Plateau.hauteur - 1:
            self.vie -= 1
            self.vaisseau.nivTir = 1
            self.vaisseau.cooldown = 0
            return True
        else:
            return False

    def affichageModeEmploi(self):
        print(PartieJeu.modeEmploi)

    def copy(self):
        return PartieJeu(Vaisseau(Plateau.largeur//2), self.nombreAlien, self.vie, self.score, self.niveau)


class Sauvegarde:
    def __init__(self):
        self.sauvegarde : Dict[any] = {"scores":{}}
    
    def chargerPartie(self, chemin : str = "./partie.space"):
        try:
            with open(chemin, "r") as fichier:
                self.sauvegarde = load(fichier)
        except Exception:
            print("Le jeu n'a pas pu charger la sauvegarde")
    
    def sauvegarderPartie(self, chemin : str = "./partie.space"):
        with open(chemin, 'w') as fichier:
            dump(self.sauvegarde, fichier)
    
    def ajouterScore(self, pseudo:str, score: int):
        self.sauvegarde["scores"][pseudo] = score
        
    def recupererScore(self, pseudo:str) -> int:
        return self.sauvegarde["scores"].get(pseudo, 0)
    

class Menu:
    def __init__(self, partie: PartieJeu, sauvegarde : Sauvegarde):
        self.selection = 0
        self.selections = []
        self.menu = "Titre"
        self.click = False
        self.stop = False
        self.partie = partie.copy()
        self.partieOri = partie
        self.sauvegarde = sauvegarde
        self.sauvegarde.chargerPartie()
    
    def affichage(self):
        if self.menu == "Titre":
            titre : str = "PYTHON INVADERS"
            self.selections : List[str] = ["Jouer", "Classement","Credit","Quitter"]
            print("*"*Plateau.largeur)
            Menu.affichageCentre(titre)
            print("\n")
            for i in range(len(self.selections)):
                pointeur : str = "-"
                if self.selection == i :
                    pointeur = ">"
                print(f" {pointeur} {self.selections[i]}")
            print("\n")
            print("*"*Plateau.largeur)
        elif self.menu == "GameOver":
            titre : str = "GAME OVER"
            self.selections : List[str] = ["Rejouer", "Sauvegarder Le Score","Quitter"]
            
            print("*"*Plateau.largeur)
            Menu.affichageCentre(titre)
            texte : str = f"Score : {self.partie.score}"
            print("\n")
            Menu.affichageCentre(texte)
            print("\n")
            for i in range(len(self.selections)):
                pointeur : str = "-"
                if self.selection == i :
                    pointeur = ">"
                print(f" {pointeur} {self.selections[i]}")
            print("\n")
            print("*"*Plateau.largeur)
        
        elif self.menu == "Sauvegarder Le Score":
            titre : str = "Sauvegarder Le Score"
            self.selections : List[str] = ["Sauver","Titre"]
            
            print("*"*Plateau.largeur)
            Menu.affichageCentre(titre)
            texte : str = f"Score : {self.partie.score}"
            print("\n")
            Menu.affichageCentre(texte)
            print("\n")
            for i in range(len(self.selections)):
                pointeur : str = "-"
                if self.selection == i :
                    pointeur = ">"
                print(f" {pointeur} {self.selections[i]}")
            print("\n")
            print("*"*Plateau.largeur)
        
        elif self.menu == "Sauver":
            titre : str = "Entrez votre pseudo"
            self.selections : List[str] = []
            print("*"*Plateau.largeur)
            Menu.affichageCentre(titre)
            texte : str = f"Score : {self.partie.score}"
            print("\n")
            Menu.affichageCentre(texte)
            print("\n")
            pseudo : str = input("Pseudo: ")
            Menu.affichageCentre(pseudo)
            print("\n")
            print("*"*Plateau.largeur)
            sleep(.5)
            self.sauvegarde.ajouterScore(pseudo, self.partie.score)
            self.menu = "Titre"

        elif self.menu == "Quitter":
            self.stop = True
        
        elif self.menu == "Jouer" or self.menu == "Rejouer":
            PartieJeu.PowersUp = []
            self.partie = self.partieOri.copy()
            self.partie.boucleDeJeu(Plateau())
            self.menu = "GameOver"
        
        elif self.menu == "Classement":
            self.selection = 0
            titre : str = "Classement"
            self.selections : List[str] = ["Titre"]
            print("*"*Plateau.largeur)
            Menu.affichageCentre(titre)
            print("\n")
            classement = self.sauvegarde.sauvegarde["scores"]
            classement = list(classement.items())
            classement.sort(key= lambda x: x[1], reverse=True)
            for i in range(10):
                if i < len(classement):
                    print(f" - {classement[i][0]} : {classement[i][1]}")
            print("\n")
            for i in range(len(self.selections)):
                pointeur : str = "-"
                if self.selection == i :
                    pointeur = ">"
                print(f" {pointeur} {self.selections[i]}")
            print("\n")
            print("*"*Plateau.largeur)



    @staticmethod
    def affichageCentre(texte:str) :
        print(" "*(Plateau.largeur//2 - len(texte)//2) + texte + " "*(Plateau.largeur//2 - len(texte)//2 - 1))

        
    def selectionner(self, action:str):
        if action == "o":
            if self.menu == "Titre":
                if self.selection > 0 : self.selection -= 1
                else : self.selection = 3
            elif self.menu == "GameOver":
                if self.selection > 0 : self.selection -= 1
                else : self.selection = 2
            elif self.menu == "Sauvegarder Le Score":
                if self.selection > 0 : self.selection += 1
                else : self.selection = 1
        elif action == "l":
            if self.menu == "Titre":
                if self.selection < 3 : self.selection += 1
                else : self.selection = 0
            elif self.menu == "GameOver":
                if self.selection < 2 : self.selection += 1
                else : self.selection = 0
            elif self.menu == "Sauvegarder Le Score":
                if self.selection < 1 : self.selection += 1
                else : self.selection = 0
        
        elif action == "k":
            self.click = True
        
    def boucle(self):
        kb = SaisiCar()
        action : str = ""
        while not self.stop:
            clear()
            self.affichage()
            action = kb.recupCar(["k","o","l"])
            if action != None:
                self.selectionner(action)
                self.selectionClick()
            sleep(.05)
    
    def selectionClick(self):
        if self.click == True:
            self.menu = self.selections[self.selection]
            self.selection = 0
            self.click = False
            

partie : PartieJeu = PartieJeu(Vaisseau(Plateau.largeur // 2), vie=1)
sauvegarde : Sauvegarde = Sauvegarde()
menu = Menu(partie, sauvegarde)
menu.menu = "Titre"

menu.boucle()
menu.sauvegarde.sauvegarderPartie()