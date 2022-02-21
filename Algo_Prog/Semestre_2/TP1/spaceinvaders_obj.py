from typing import List, Dict, Tuple
class Plateau:
    largeur: int = 30
    hauteur: int = 20
    normalC : str = "\033[0;37;40m"
    def afficherLigne():
        print("-"*Plateau.largeur)
        
    def afficherBandeau(self,jeu):
        Plateau.afficherLigne()
        print(" " * 2 + "SCORE" + " " * 4 + "VIE" + " " * 4 + "NIVEAU")
        print(
        f'  {jeu.score:5}  {jeu.vie : 5}     {jeu.niveau : 5}')
        Plateau.afficherLigne()
        
    def afficherPlateau(self,jeu):
        for ligne in range(Plateau.hauteur):
            for col in range(Plateau.largeur):
                alien : Alien = jeu.aliens.get((col, ligne), " ")
                print(alien, end=Plateau.normalC)
                if(ligne == Plateau.hauteur - 1 and jeu.vaisseau.posX == col):
                    print(jeu.vaisseau, end=Plateau.normalC)
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

class PartieJeu:
    modeEmploi : str = """Bienvenue Dans SpaceInvaders:
        Utilisez els touches o,k,m pour tirer, se déplacer à gauche ou à droite"""
    def __init__(self, vaisseau: Vaisseau, nombreAlien : int = 30,
                vie : int = 3, score : int = 0, niveau : int = 1):
        self.vie : int = vie
        self.score : int = score
        self.niveau : int = niveau
        self.vaisseau : Vaisseau = vaisseau
        self.aliens : Dict[Tuple[int, int], Alien] = {}
        self.initialiserAliens(nombreAlien)
    
    def initialiserAliens(self, nbAliens:int, nbLignes:int = 10):
        y = -1 
        for i in range(nbAliens):
            x = i % nbLignes
            if(x == 0) : y += 1
            self.aliens[(x+Plateau.largeur//2 - nbLignes//2,y)] = Alien(x+Plateau.largeur//2 - nbLignes//2,y)
    
    def afficherAliens(self):
        print("Les aliens: ")
        for a in self.aliens.values():
            print(f'\t {repr(a)}')

    def affichageModeEmploi(self):
        print(PartieJeu.modeEmploi)
class Alien:
    alienC : str = "\033[1;32;47m"
    def __init__(self, x:int, y:int, nivTir : int = 0):
        self.posX = x
        self.posY = y
        self.nivTir = nivTir
    def __repr__(self):
        return f'en position ({self.posX}, {self.posY}) - tir {self.nivTir}'
    def __str__(self):
        return f'{self.alienC}@' 
    
    def deplacer(x:int, y:int):
        self.posX = x
        self.posY = y

    def position(self) -> Tuple[int, int]:
        return (self.posX, self.posY)

plateau : Plateau = Plateau()
partie : PartieJeu = PartieJeu(Vaisseau(Plateau.largeur // 2))
partie.afficherAliens()
partie.affichageModeEmploi()
plateau.afficherBandeau(partie)
plateau.afficherPlateau(partie)