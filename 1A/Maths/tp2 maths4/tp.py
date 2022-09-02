"""! @brief [description du fichier]
 @file tp.py
 @section libs Librairies/Modules
  - [Nom du module] (lien)

 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 20/05/2022 .
"""
from typing import Tuple, List 
from math import log, atan
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

def integrale_cas1(a,b,c,A,b1 = None, b2 = None, x = None):
    inte = lambda x: A*(-1/(a *(x-racines(a, b, c))))
    if(x == None):
        haut,bas = inte(b2), inte(b1)
        retour = haut - bas
    else:
        retour = inte(x)
    
    return retour

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


"""
ax² + bx + c avec delta < 0
forme canonique : 
a(x+p)²+q
soit 

avec p = -b/2a et q = -(b²-4ac)/4a²

4(x² + 2x + 3)
4( ( x + 1 )² + 2 )
donc p = 1 et q = 2

"""

def canonique(a,b,c):
    p = b/(2*a)
    q = c / a - p**2
    return (p,q)

def integrale_cas3(a,b,c,A,b1 = None,b2 = None, x=None):
    p,q = canonique(a, b, c)
    out = A / a / q
    inte = lambda x : out * atan( (x+p) / (q**0.5) ) * q**0.5
    if x == None:
        retour =  inte(b2) - inte(b1)
    else :
        retour = inte(x)
    return retour

def constante_cas4(a,b,c,A,B):
    k = A / (2*a)
    d = -( k*b - B)
    return (k,d)

def integrale_cas4(a,b,c,A,B,b1,b2):
    k,d = constante_cas4(a, b, c, A, B)
    p,q = canonique(a, b, c)
    out = d / a / q

    inte = lambda x : k * log(abs(a*x**2 + b*x + c)) + integrale_cas3(a, b, c, d, x=x)

    return inte(b2) - inte(b1)

def integrale(a,b,c,A,B,b1,b2):
    delta = b**2 - 4*a*c
    retour : float = None
    if delta >= 1:
        retour = integrale_cas2(a, b, c, A, B, b1, b2)
    elif delta == 0:
        k,d = constante_cas4(a, b, c, A, B)
        inte = lambda x : k * log(abs(a*x**2 + b*x + c)) + integrale_cas1(a, b, c, d, x=x)
        retour = inte(b2) - inte(b1)
    else :
        retour = integrale_cas4(a, b, c, A, B, b1, b2)

    return retour

if __name__ == "__main__":
    # print(racines(1,-4, -12))
    # print(racines(4,4, 1))
    # print(racines(4,4, 10))

    # print(integrale_cas1(4, 4, 1, 2, 0, 1))
    # print(calcul_constante(1,6,-4,-2,6))

    # print(integrale_cas2(1, -4, -12, 6, -4, 0, 1))
    # print(integrale_cas2(2,3,1,0,6,0,1))

    # print(integrale_cas3(4, 8, 12,3,0,1))
    # print(constante_cas4(4, 8, 12, 16, 2))
    # print(integrale_cas4(4, 8, 12, 16, 2, 0,1))

    print(integrale(1, 4, 4, 2, 1, 0, 1))
    print(integrale(2, 5, 10, 5, 1, 0, 1))
    print(integrale(4, -1, -5, 2, 5, 0, 1))

