#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:20:37 2022

@author: phdurand
"""


class Vaisseau:
    
    # propriétés de classe
    vaisseauC : str = "\033[1;31;40m"
    
    # Constructeur
    
    def __init__(self,posX_:int=0):
        self.posX=posX_
        self.tir : bool = False
        self.typeTir : int= 1
    
    # Méthodes d'objets
    
    def actionnerVaisseau(self,action : str) :
        if action=='o' : 
            self.tir=True
        elif action=='k' and self.posX > 0:
            self.posX = self.posX-1
        elif action=='m' and self.posX < 30-1 : # A MODIFIER plus tard avec Plateau.largeur
            self.posX = self.posX+1
    
    def __str__(self) -> str:
        """
        Retourne la représentation textuelle d'un vaisseau
        Return :
            str une chaîne de caractères
        """
        return f"Vaisseau : position = {self.posX} tir = {self.tir} tir spécial ={self.typeTir}"
    
    
    # Méthodes de classe


class Alien:
    
    # propriétés de classe

    
    # Constructeur
    
    def __init__(self,posX_:int, posY_:int, tir_ : int=None):
        self.posX=posX_
        self.posY=posY_
        self.tir : int = tir_
    
    # Méthodes d'objets
    def deplacerAlien(self,posX_:int, posY_:int):
        self.posX=posX_
        self.posY=posY_
    
    
    def __str__(self) -> str:
       return f"Alien : position = ({self.posX},{self.posY}) tir = {self.tir} "
    
    
    # Méthodes de classe




    

if __name__ == "__main__" :
    
    ##L : int la largeur du plateau de jeu
    L : int = 30
    ##H : int la hauteur du plateau de jeu
    H : int = 10
    ##score : int le score actuel du joueur (initialisé à 0)
    SCORE : int = 0
    ##vie : int le nombre de vies restantes (initialisé à 3)
    VIE : int = 3
    ##niveau : int le niveau du jeu qui conditionne la vitesse de déplacement des aliens (initialisé à 1)
    NIVEAU : int = 1    
    
    
    # tests simples
    if True :
        vaisseau : Vaisseau = Vaisseau(L/2)
        print(vaisseau)
        vaisseau.actionnerVaisseau('o')
        print(vaisseau)
        vaisseau.actionnerVaisseau('m')
        print(vaisseau)
        vaisseau.actionnerVaisseau('k')
        print(vaisseau)
        