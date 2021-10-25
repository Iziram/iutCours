#Modules
from random import randint

#Fonctions

def nombre()-> int:
    return randint(0,101)
    

def getUserInput() -> int :
    res : int = int(input("Choisir un nombre entre 0 et 100 : "))
    return res

def checkUserInput(Input: int, number : int) -> int :
    res : int 
    if Input == number :
        res = 0
    elif Input > number :
        res = 1
    else:
        res = -1

if __name__ == "__main__" :

    nombre : int = nombre()
    vie : int = 9
    gagnant : bool = False

    guess : int
    while not gagnant and vie > 0 :
        
        guess = checkUserInput(getUserInput(), nombre)
        if guess == 0 : gagnant = True
        else:
            if guess == 1:
                print("Le nombre que vous avez choisi est supérieur au nombre réel")
            else :
                print("Le nombre que vous avez choisi est inférieur au nombre réel")
        
        vie -= 1
    
    if vie > 0 : print("Vous avez trouvé le nombre mystère")
    else : print(f'Vous n\'avez pas trouvé le nombre mystère. C\'était {nombre}')
