#Modules
from random import randint
from os import system
#Fonctions

def bienvenue() -> str :
    """
    Fontion qui affiche les règles et demande à l'utilisateur son nom
    Si l'utilisateur ne saisit rien la fonction retourne le nom "humain"
    @return str le nom de l'utilisateur ou "humain"
    """ 
    print("Bienvenue au jeu du shi fu mi !")
    nom : str = input("Nom: ")
    if nom == "" : 
        nom = "humain"
    
    return nom


def choixUtilisateur() -> str :
    """
    Fonction qui permet à l’utilisateur de saisir une action P C ou F
    @return str le caractère P ou C ou F 
    """
    res : str = input("Veuillez choisir entre P ou C ou F : ")
    while res != "P" and  res != "C" and res != "F" :
        res = input("Erreur action P ou C ou F ! ")
    return res  
    
# assert choixUtilisateur() in  ["P", "C", "F"] 



def choixOrdi() -> str :
    """
    Fonction qui génère une action aléatoire pour l’ordinateur
    @return str un caratère aléatoire entre P ou C ou F
    """
    a : int = randint(0 , 3)
    res : str 
    if a == 0 : 
        res = "P"
    else :
        if a == 1 :
            res = "F" 
        else :
            res = "C"
    return res 

# assert choixOrdi() in  ["P", "C", "F"] 

def quiGagne(aJ : str, aO : str) -> int : 
    """
    Fonction qui à partir de deux actions celle du joueur en paramètre 1 et celle de l’ordinateur paramètre 2 
    Indique qui gagne (retourne 1 si c’est le joueur -1 si c’est l’ordinateur 0 si match null
    @return int un entier 1 ou 0 ou -1 designant le résultat de combat
    """
    res : int 
    if aJ == aO :
        res = 0 
    else :
        if (aJ ==  "P" and aO == "C") or (aJ ==  "F" and aO == "P") or (aJ ==  "C" and aO == "F") : 
            res = 1 
        else :
            res = -1
            
    return res

# assert quiGagne("P","P") == 0
# assert quiGagne("P","C") == 1
# assert quiGagne("P", "F") == -1


def resultat(res:int, j:str):
    """
    Affiche le résultat du combat entre le joueur et l'ordinateur.
    """
    if res == 0:
        print("Match nul")
    elif res == 1 :
        print(f"{j} a gagné le combat")
    else:
        print(f"{j} a perdu le combat")



#Algorithme pricipal
if __name__ == "__main__":
    """
    Initialisation des variables :
    """
    actionJoueur : str
    actionOrdinateur : str
    joueur : str
    gagnant : int

    pointJ : int = 0
    pointO : int = 0


    """
    Fonctions
    """
    joueur = bienvenue()

    while pointJ < 3 and pointO < 3 :
        actionJoueur = choixUtilisateur()
        actionOrdinateur = choixOrdi() 
        gagnant = quiGagne(actionJoueur, actionOrdinateur)
        system("clear")
        resultat(gagnant, joueur)
        if gagnant == 1 : pointJ +=1
        elif gagnant == -1 : pointO +=1
        print(f'{joueur} : {pointJ} | Ordinateur : {pointO}')
    if pointJ == 3 :
        print(f'{joueur} a gagné la partie')
    else :
        print(f'{joueur} a perdu la partie')