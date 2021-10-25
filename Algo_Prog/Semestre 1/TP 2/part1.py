"""
Script Python (TP 2)
Découverte de la structuration d'un script python
"""

#Utilisation de la biliothèque datetime
from datetime import datetime

#Mes fonctions
def quelHeure():
    """
    Procédure effectuant l'affichagede l'heure actuelle au format :
    Il est actuellement 20h23
    """
    #récupère l'heure actuelle
    d : datetime = datetime.now()
    h : int = d.hour
    m : int  = d.minute
    print(f"Il est actuellement {h}h{m}")

def quiSuisJe():
    nom : str = input("Votre nom: ")
    prenom : str = input("Votre prénom: ")

    print(f"Bonjour {nom} {prenom}")

if __name__ == "__main__":
    """
    Point d'entrée
    """
    print("Début du programme")
    quiSuisJe()
    quelHeure()
    print("Fin du programme")
