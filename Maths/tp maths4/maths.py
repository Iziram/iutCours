"""! @brief TP de math4
 @file maths.py
 @section libs Librairies/Modules
  - maths

 @section authors Auteur(s)
  - Cocréé par Hartmann Matthias le 09/05/2022 .
  - Cocréé par Bienvenue Victor le 09/05/2022 .
"""

from numpy import arctan, cos

def f_1(x : float)-> float:
    """!
    @brief Formule de la fonction 1

    Paramètres : 
        @param x : float => la variable x
    Retour de la fonction : 
        @return float => l'image de x par la fonction 1

    """
    return x**2 + 1

def f_2(x : float) -> float :
    """!
    @brief Formule de la fonction 2

    Paramètres : 
        @param x : float => la variable x
    Retour de la fonction : 
        @return float => l'image de x par la fonction 2
    """
    return 2 / ( x**2 + 3)

def f_3(x : float) -> float:
    """!
    @brief Formule de la Fonction 3

    Paramètres : 
        @param x : float => la variable x
    Retour de la fonction : 
        @return float => l'image de x par la fonction 3

    """
    return 5 / ((x + 2) **2 )


def j_3(x : float) -> float:
    """!
    @brief Formule de la fonction pour l'intégrale J3

    Paramètres : 
        @param x : float => la variable x
    Retour de la fonction : 
        @return float => l'image de x par la fonction

    """
    return arctan(cos(x))

def somme_rectangle(f, n : int) -> float:
    """!
    @brief Première approximation de l'air sous la courbe d'une fonction

    Paramètres : 
        @param f => Une fonction f
        @param n : int => le nombre de rectangles
    Retour de la fonction : 
        @return float => l'approximation de l'air sous la courbe d'une fonction

    """
    return sum([f(i) * 1 for i in range(n)])

def methode_rectangle(f,b,n) -> float:
    """!
    @brief Deuxième approximation de l'air sous la courbe d'une fonction

    Paramètres : 
        @param f => Une fonction f
        @param b => La borne haute de l'intégrale
        @param n => Le nombre de rectangles
    Retour de la fonction : 
        @return float => l'approximation de l'air sous la courbe d'une fonction

    """
    
    largeur : float = b/n
    somme : float = 0
    iterator : float = 0
    for i in range(n):
        somme += f(iterator)*largeur
        iterator += largeur
    return somme

def methode_rectangle_v2(f,a,b,n) -> float:
    """!
    @brief Généralisation de l'approximation de l'air sous la courbe d'une fonction

    Paramètres : 
        @param f => Une fonction f
        @param a => la borne basse de l'intégrale
        @param b => La borne haute de l'intégrale
        @param n => Le nombre de rectangles
    Retour de la fonction : 
        @return float => l'approximation de l'air sous la courbe d'une fonction

    """
    
    largeur : float = (b-a)/n
    somme : float = 0
    iterator : float = 0
    while iterator < b:
        somme += f(iterator)*largeur
        iterator += largeur
    return somme

if __name__ == "__main__":
    #Partie 1 : 1
    print(somme_rectangle(f_1, 4))
    print(somme_rectangle(f_2, 4))
    """
    1)Le résulat semble cohérent avec la théorie. 18 est la valeur qui devrait être trouvée.
    2)La marge d'erreur est bien plus grande avec les fonctions décroissantes
    """
    #Partie 1 : 2
    """
    a)
    Valeur en defaut : 22.24
    Valeur en excès : 28.24
    b) largeur rectangle = b / n
    e) 
    """
    print("fonction 1")
    for i in [4, 10, 100,1000]:
        print(methode_rectangle(f_1, 4, i))
    print("fonction 2")
    for i in [4, 10, 100,1000]:
        print(methode_rectangle(f_2, 5, i))
    print("fonction 3")
    for i in [4, 10, 100,1000]:
        print(methode_rectangle(f_3, 20, i))
    
    #Partie 1 : 3
    print("integrale 3")
    for i in [4, 10, 100,1000]:
        print(methode_rectangle_v2(j_3, 1, 10, i))