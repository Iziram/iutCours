"""! @brief [description du fichier]
 @file tp.py
 @section libs Librairies/Modules
  - [Nom du module] (lien)

 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 20/05/2022 .
"""
from typing import Tuple, List 
from math import log
def racines(a : float, b : float, c : float) -> Tuple[float]:
    """!
    @brief [Description de la fonction]

    Paramètres : 
        @param a : float => a de "ax² + bx + c"
        @param b : float => b de "ax² + bx + c"
        @param c : float => c de "ax² + bx + c"
    Retour de la fonction : 
        @return Tuple[float] => Les racines 

    """
    delta : float = b**2 - 4*a*c
    if delta < 0 : return None
    elif delta >0 : return (
        (-1*b + delta**0.5)/(2*a),
        (-1*b - delta**0.5)/(2*a)
    )
    else : return (-1*b)/(2*a)

def integrale_cas1(a,b,c,A,b1,b2):
    inte = lambda x: A*(-1/(a *(x-racines(a, b, c))))
    haut,bas = inte(b2), inte(b1)
    return haut - bas

def calcul_constante(a,A,B,x1,x2):
    calc = lambda y,z : ( (y*A) + B ) /( a * (y - z) )
    C1 = calc(x1,x2)
    C2 = calc(x2,x1)
    return (C1,C2)

def integrale_cas2(a,b,c,A,B,b1,b2):
    r = racines(a,b,c)
    const = calcul_constante(a, A, B, r[0], r[1])
    inte = lambda x : const[0] * log(abs(x - r[0])) + const[1] * log(abs(x - r[1]))
    _a = inte(b2)
    _b = inte(b1)
    return  _a - _b

if __name__ == "__main__":
    print(racines(1,-4, -12))
    print(racines(4,4, 1))
    print(racines(4,4, 10))

    print(integrale_cas1(4, 4, 1, 2, 0, 1))
    print(calcul_constante(1,6,-4,-2,6))

    print(integrale_cas2(1, -4, -12, 6, -4, 0, 1))
    print(integrale_cas2(2,3,1,0,6,0,1))