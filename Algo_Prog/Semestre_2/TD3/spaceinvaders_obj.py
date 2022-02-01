from typing import List
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
    aliens : List[object] = []
    alienC : str = "\033[1;32;47m"
    def __init__(self, x:int, y:int, nivTir : int = None):
        self.posX = x
        self.posY = y
        self.nivTir = nivTir
        Alien.aliens.append(self)
    def __repr__(self):
        return f'Alien : position = ({self.posX}, {self.posY}) tir spécial = {self.nivTir}'
    def __str__(self):
        return f'{self.alienC}@' 
    
    def deplacer(x:int, y:int):
        self.posX = x
        self.posY = y
