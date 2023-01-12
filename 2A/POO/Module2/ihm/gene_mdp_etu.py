#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import string, random, os
from typing import List

def generateur_mdp(taille: int= 12, chiffres: bool= True, majuscules: bool= True, ponctuations: bool = True)-> str:
   """retourne un mot de passe
   Args:
       taille (int): nombre de cractères du mot de passe
       chiffes (bool, optional): avec ou sans chiffres
       majuscules (bool, optional): navec ou sans majuscules
       ponctuations (bool, optional): avec ou sans caractères spéciaux

   Returns:
       str: le mot de pass sous la forme d'une chaine de carateres
   """
   mdp: str
   mdp = ""
   liste_carateres_possibles: List[str] = []
   liste_mdp: List[str] = []

   liste_carateres_possibles = list(string.ascii_lowercase)
   if chiffres:
      liste_carateres_possibles += string.digits
   if majuscules:
      liste_carateres_possibles += string.ascii_uppercase
   if ponctuations:
      liste_carateres_possibles += string.punctuation
   for i in range(taille):
      liste_mdp.append(random.choice(liste_carateres_possibles))
   #print(liste_mdp)
   mdp = "".join(liste_mdp)
   return mdp