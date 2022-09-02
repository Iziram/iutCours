#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:12:37 2022

@author: phdurand
"""
from typing import Dict


class Etudiant:
    
    # propriétés de classe
    nbEtu : int = 0 # permet de compter le nombre d'étudiants crées
    
    # Constructeur
    
    def __init__(self, nom_ : str, mail_ :str, diplome_ :str  ) :
        if '@' not in mail_:
            raise Exception("Mail erroné")
        self.mail=mail_
        self.nom=nom_
        self.diplome=diplome_
        self.notes : Dict[str, float]={}
        Etudiant.nbEtu=Etudiant.nbEtu+1
        self.identifiant = 1000 + Etudiant.nbEtu # le premier id sera 1001 puis 1002 ...
        
        
        
    
    # Méthodes d'objets
    
    def afficherEtudiant(self):
        print(self.nom,end=' ')
        print(self.mail,end=' ')
        print(self.diplome,end=' ')
        print(self.identifiant,end=' ')
        print(self.notes,end=' ')
        print()
    
    def modifierEtudiant(self,nom_ : str="", mail_ :str="", diplome_ :str=""  ) :
        if nom_=="" :
            nom_ : str = input("saisir le nom")
        if mail_=="" :
            mail_ :str = input("saisir le mail")
        if '@' not in mail_:
            raise Exception("Mail erroné")
        if diplome_=="" :
            diplome_ : str = input("saisir le diplome")
        
        self.nom = nom_
        self.mail= mail_
        self.diplome=diplome_
     
    def ajouterNote(self,exam_:str,note_:float) :        
        if  exam_ in self.notes.keys()   :
            raise Exception("Examen déjà renseigné")        
        self.notes[exam_] = note_
    

    def modifierNote(self,exam_:str,note_:float) :        
        if  exam_ not in self.notes.keys()   :
            raise Exception("Examen inexistant")        
        self.notes[exam_] = note_
    
        
    # Méthodes de classe
     
    
if __name__ == "__main__":
    print(Etudiant.nbEtu)
    try :
        etu1 : Etudiant = Etudiant("toto","toto@etu.fr","BUT R&T")
        etu2 : Etudiant = Etudiant("titi","titi@etu.fr","BUT MP")
    except Exception as e :
        print(e)
    print(Etudiant.nbEtu)   
    etu1.afficherEtudiant()
    etu2.afficherEtudiant()
    #print(etu1)
    
    #etu1.modifierEtudiant()
    #etu1.afficherEtudiant()
    etu1.modifierEtudiant("toto","toto123333@etu.fr","BUT R&T")
    etu1.afficherEtudiant()
    
    etu1.ajouterNote("Prog",15.0)
    etu1.afficherEtudiant()
    try :
        etu1.ajouterNote("Prog",10.0)        
    except Exception as e :
        print(e)
        etu1.modifierNote("Prog",10.0)
    etu1.afficherEtudiant()