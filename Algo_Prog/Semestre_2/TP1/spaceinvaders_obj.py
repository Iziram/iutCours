from typing import List, Dict, Tuple
from os import system
from time import sleep
from saisiCar import SaisiCar

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
                pos : List[Alien] = [a for a in jeu.aliens if a.position() == (col, ligne)]
                alien : Alien or str = pos[0] if len(pos) > 0 else " " 
                print(alien, end=Plateau.normalC)
                
            print("\n", end="")

class Vaisseau:
    vaisseauC : str = "\033[1;31;40m"
    def __init__(self, x:int = 0):
        self.posX : int = x
        self.tir : bool = False
        self.nivTir : int = 1
    
    def action(self, keyPressed: str):
        if keyPressed == "o":
            self.tir = True
        elif keyPressed == "k":
            if(self.posX > 0):
                self.posX -= 1
        elif keyPressed == "m":
            if(self.posX < Plateau.largeur - 1):
                self.posX += 1
    def __repr__(self):
        return f'Vaisseau : position = {self.posX} tir spécial = {self.nivTir}'
    def __str__(self):
        return f'{self.vaisseauC}#'

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
        self.initialiserAliens(nombreAlien)
    
    def initialiserAliens(self, nbAliens:int, nbLignes:int = 10):
        self.aliens = []
        y = -1 
        for i in range(nbAliens):
            x = i % nbLignes
            if(x == 0) : y += 1
            self.aliens.append(Alien(x+Plateau.largeur//2 - nbLignes//2,y))
    
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
                    self.aliens.remove(aliens.pop())
            return nombre
        return 0
    
    def boucleDeJeu(self, plateau:Plateau):
        action : str = ""
        kb = SaisiCar()
        while self.vie > 0 and action !="q":
            system("cls")
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
                self.initialiserAliens(20 + 10 * self.niveau)
            else:
                self.deplacementAliens()
            sleep(.1)
    
    def finJeu(self, alien: Alien) -> bool:
        if len(self.aliens) < 1 :
            self.niveau += 1
            return True
        elif alien.posY == Plateau.hauteur - 1:
            self.vie -= 1
            return True
        else:
            return False
            

    def affichageModeEmploi(self):
        print(PartieJeu.modeEmploi)

plateau : Plateau = Plateau()
partie : PartieJeu = PartieJeu(Vaisseau(Plateau.largeur // 2))
partie.affichageModeEmploi()
partie.boucleDeJeu(plateau)