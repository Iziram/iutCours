import numpy as np
def partie1():
    #1
    v1 : np.ndarray = np.array([6.5, 7.5, 8.75, 7.1])
    m1 : np.ndarray = np.array(([1,2,3],[11,12,13]))
    m2 : np.ndarray = np.ones((3,7))
    m3 : np.ndarray = np.arange(0,1.25,.25)
    
    print(v1)
    print(m1)
    print(m2)
    print(m3)
    
    #1.2
    vecteur : np.ndarray = vec
    print(vecteur)
    print(vecteur.size)
    print(vecteur.shape)
    print(vecteur[3])
    print(vecteur[:10])

def valeur_min(vecteur : np.ndarray) -> float:
    mini : float = vecteur[0]
    for i in range(1, vecteur.size):
         if vecteur[i] < mini :
             mini = vecteur[i]
    return mini

def valeur_max(vecteur : np.ndarray) -> float:
    maxi : float = vecteur[0]
    for i in range(1, vecteur.size):
         if vecteur[i] > maxi :
             maxi = vecteur[i]
    return maxi

def moyenne_arithmétique(vecteur : np.ndarray) -> float:
    add : float = 0
    for i in vecteur:
        add += i
    return add / vecteur.size

def mediane(vecteur : np.ndarray) -> float:
    vecteur = np.sort(vecteur, 0)
    res : float = 0
    indice : int = vecteur.size // 2
    res = vecteur[indice]
    if vecteur.size % 2 == 0 :
        res = (vecteur[indice] + vecteur[indice - 1]) / 2
    return res

def variance(vecteur : np.ndarray) -> float:
    m = moyenne_arithmétique(vecteur)
    # calculate variance using a list comprehension
    var_res = sum((item - m) ** 2 for item in vecteur) / len(vecteur)
    return var_res

def ecartType(vecteur : np.ndarray) -> float:
    return variance(vecteur) ** .5

def quartiles(vecteur : np.ndarray, q : int)-> float:
    vecteur  = np.sort(vecteur, 0)
    sq : float = .25 * q
    indice = round(vecteur.size * sq)
    return vecteur[indice]

vec = np.arange(3,37,.5)
assert valeur_max(vec) == max(vec)
assert valeur_min(vec) == min(vec)
assert variance(vec) == np.var(vec)
assert ecartType(vec) == np.var(vec) ** .5
assert moyenne_arithmétique(vec) == sum(vec) / vec.size
assert quartiles(vec, 2) == np.quantile(vec, .5, interpolation = "higher")
assert mediane(vec) == np.median(vec)

def affichage(vecteur):
    print(valeur_max(vecteur))
    print(valeur_min(vecteur))
    print(moyenne_arithmétique(vecteur))
    print(variance(vecteur))
    print(mediane(vecteur))
    print(ecartType(vecteur))
    print(quartiles(vecteur, 1))
    print(quartiles(vecteur, 3))
    print("="*40)

def partie2():
    v1 = np.arange(3,37,.5)
    v2 = np.array([3,497,400,443])
    
    for vecteur in [v1,v2]:
        affichage(vecteur)
        
def partie2bis():
    tabData : np.ndarray = np.genfromtxt("../data1.csv", delimiter=",")
    print(tabData.size, tabData.shape, tabData.dtype)
    print("="*40)
    axis_x = np.array([x[0] for x in tabData])
    axis_y = np.array([x[1] for x in tabData])
    affichage(axis_x)
    affichage(axis_y)
    
if __name__ == "__main__":
    # partie1()
    # partie2()
    partie2bis()
    pass