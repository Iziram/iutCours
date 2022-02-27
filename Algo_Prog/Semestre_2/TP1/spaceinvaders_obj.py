from typing import List, Dict, Tuple
from os import system
from time import sleep
from saisiCar import SaisiCar
from random import sample, randint
from json import load, dump
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
                del(self)
            else:
                self.posY += 1
        else:
            del(self)
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
    def __init__(self, vaisseau: Vaisseau, nombreAlien : int = 30,
                vie : int = 3, score : int = 0, niveau : int = 1):
        self.vie : int = vie
        self.score : int = score
        self.niveau : int = niveau
        self.vaisseau : Vaisseau = vaisseau
        self.aliens : List[Alien] = []
        self.PowersUp : List[PowerUp] = []
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
                        self.PowersUp.append(PowerUp(mort.posX, mort.posY, mort.nivTir))
                    self.aliens.remove(mort)
            return nombre
        return 0
    
    def boucleDeJeu(self, plateau:Plateau):
        action : str = ""
        kb = SaisiCar()
        while self.vie > 0 and action !="q":
            system("clear")
            #system("cls") #Windows
            action = kb.recupCar(["m", "k", "o", "q"])
            if(action != None and action != ""):
                self.vaisseau.action(action)
            
            plateau.afficherBandeau(partie)
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
                self.PowersUp = []
                self.initialiserAliens(20 + 10 * self.niveau)

            else:
                self.deplacementAliens()
                for a in self.aliens :
                    if(a.larguerBombe()):
                        self.PowersUp.append(PowerUp(a.posX, a.posY, type_="bombe"))
                for p in self.PowersUp : p.update(self)
                
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
    def affichageFinDuJeu(self):
        infos : str = ""

    def affichageModeEmploi(self):
        print(PartieJeu.modeEmploi)


class Sauvegarde:
    def __init__(self, partie: PartieJeu = None):
        self.sauvegarde : Dict[any] = {}
    
    def chargerPartie(self, chemin : str = "./partie.space"):
        try:
            self.sauvegarde = load(chemin)
        except Exception:
            print("Le jeu n'a pas pu charger la sauvegarde")
    
    def sauvegarderPartie(self, chemin : str = "./partie.space"):
        with open(chemin, 'w') as fichier:
            fichier.write(dump(self.sauvegarde))
    
    def ajouterScore(self, pseudo:str, score: int):
        self.sauvegarde["scores"][pseudo] = score
        
    def recupererScore(self, pseudo:str) -> int:
        return self.sauvegarde["score"].get(pseudo, 0)
    

class Menu:
    def __init__(self):
        self.selection = 0
        self.selections = []
        self.menu = "Titre"
        self.click = False
        self.stop = False
    
    def affichage(self):
        if self.menu == "Titre":
            titre : str = "PYTHON INVADERS"
            self.selections : List[str] = ["Jouer", "Classement","Credit","Quitter"]
            print("*"*Plateau.largeur)
            print(" "*(Plateau.largeur//2 - len(titre)//2) + titre + " "*(Plateau.largeur//2 - len(titre)//2 - 1))
            print("\n")
            for i in range(len(self.selections)):
                pointeur : str = "-"
                if self.selection == i :
                    pointeur = ">"
                print(f" {pointeur} {self.selections[i]}")
            print("\n")
            print("*"*Plateau.largeur)
        if self.menu == "Quitter":
            self.stop = True
        
        
    def selectionner(self, action:str):
        if self.menu == "Titre":
            if action == "o":
                if self.selection > 0 : self.selection -= 1
                else : self.selection = 3
            elif action == "l":
                if self.selection < 3 : self.selection += 1
                else : self.selection = 0
            elif action == "k":
                self.click = True
    def boucle(self):
        kb = SaisiCar()
        action : str = ""
        while not self.stop:
            system("clear")
            #system("cls") #Windows
            self.affichage()
            action = kb.recupCar(["k","o","l"])
            self.selectionner(action)
            self.selectionClick()
            sleep(.05)
    
    def selectionClick(self):
        if self.click == True:
            self.menu = self.selections[self.selection]
            
menu = Menu()
plateau : Plateau = Plateau()
partie : PartieJeu = PartieJeu(Vaisseau(Plateau.largeur // 2))

menu.boucle()
