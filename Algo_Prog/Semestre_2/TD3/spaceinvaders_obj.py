from typing import List, Dict, Tuple
class Plateau:
    largeur: int = 30
    hauteur: int = 20
    
class Vaisseau:
    vaisseauC : str = "\033[1;31;40m"
    
    def __init__(self, x:int = 0):
        self.posX = x
        self.tir = False
        self.nivTir = 1
    
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
    aliens : Dict[Tuple[int,int], object] = {}
    alienC : str = "\033[1;32;47m"
    def __init__(self, x:int, y:int, nivTir : int = None):
        self.posX = x
        self.posY = y
        self.nivTir = nivTir
        Alien.aliens[(x,y)] = self
    def __repr__(self):
        return f'Alien : position = ({self.posX}, {self.posY}) tir spécial = {self.nivTir}'
    def __str__(self):
        return f'{self.alienC}@' 
    
    def deplacer(x:int, y:int):
        self.posX = x
        self.posY = y

    @staticmethod
    def genererAliens(nbAliens:int, nbLignes:int = 10):
        y = -1 
        for i in range(nbAliens):
            x = i % nbLignes
            if(x == 0) : y += 1
            Alien(x,y)
    
    @staticmethod
    def alienEnPos(x,y):
        return Alien.aliens.get((x,y), " ")


v = Vaisseau()
Alien.genererAliens(10)
for ligne in range(Plateau.hauteur):
    for col in range(Plateau.largeur):
        print(Alien.alienEnPos(col, ligne),end=f"\033[0;37;40m")
        if(ligne == Plateau.hauteur - 1 and v.posX == col):
            print(v, end=f"\033[0;37;40m")
    print("\n")