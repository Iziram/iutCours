"""! @brief TP 3 SAE 15
 @file tp3.py
 @section libs Librairies/Modules
  - typing
  - numpy
  - csv
  - random
  - matplotlib

 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 17/12/2021 .
"""
from typing import Dict, List
import numpy as np 
import csv
from random import sample
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


def csvToDict(f : str) -> Dict[str,np.ndarray]:
    """Fonction chargeant les données stockées dans le fichier f et retournant un dictionnaire où les clés sont les différents noms de fichiers décrits et les valeurs (taille en ko, timestamp) sont stockées dans un ndarray

    Args:
        f (str): Le nom du fichier à charger

    Returns:
        Dict[str,np.ndarray]: les clés sont les noms des fichiers observés et les valeurs un ndarray de dimension 2 [taille,timestamp]
    """
    ret : Dict[str, np.ndarray] = dict()
    c : str = ""
    with open(f, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in datareader:
            c = row[0]
            if c not in ret.keys():
                ret[c] = np.array([[int(row[1]), int(row[2])]])
            else:
                ret[c] = np.append(ret[c], [[int(row[1]), int(row[2])]],axis=0)
    return ret


def augmentationMoyenne(tab : np.ndarray) -> float:
    """[summary]

    Args:
        tab (np.ndarray): [description]

    Returns:
        float: [description]
    """
    #dernière taille observée - première / nombre d'observations
    augMoy : float = (tab[len(tab)-1][0] - tab[0][0]) / len(tab)
    return augMoy
    aug : float = 0
    lastS : float or None = None
    for i in tab:
        if lastS is None:
            lastS = i[0]
        else:
            aug = aug + (i[0] - lastS)
            lastS = i[0]
    return aug / (len(tab) - 1)


def plusGrandeAugmentation(tab : np.ndarray) -> (float,int):
    """[summary]

    Args:
        tab (np.ndarray): [description]

    Returns:
        float: [description]
    """
    maxaug : float = 0
    taug : int or None = None
    lastS : float or None = None
    for i in tab:
        if lastS is None:
            lastS = i[0]
        else:
            aug = (i[0] - lastS)
            if aug > maxaug:
                maxaug, taug =  aug, i[1]
            lastS = i[0]
    return (maxaug,taug)

def limiteAtteinte(tab : np.ndarray, limite : int) -> int or None:
    """[summary]

    Args:
        tab (np.ndarray): [description]

    Returns:
        int or None: [description]
    """
    res : int = None
    i : int = 0
    while i < len(tab) and tab[i][0] < limite:
        i = i + 1
    if i < len(tab):
        res = tab[i][1]
    return res

def repartition(d: Dict[str, np.ndarray], nb: int) -> Dict[str, float]:
    """!
    @brief Calcule la répartition de la taille des fichiers à l'observation nb

    Paramètres : 
        @param d : Dict[str,np.ndarray] => les clés sont les noms de fichiers, les valeurs un ndarray de dimension 2
        @param nb : int => le timestamp
    Retour de la fonction : 
        @return Dict[str, float] => Les clés sont les noms des fichiers observés et la valeur un réel représentant en relatif la place prise par le fichier dans le répertoire

    """
    
    dico : Dict[str, np.ndarray] = {}
    l : List[int] = []
    for clef in d :
        i = 0
        while i < len(d[clef][1]):
            if d[clef][i,1] == nb :
                l.append(d[clef][0][i])
                i = len(d[clef][1])
            i += 1
    
    for i in range(len(l)):
        proportion : float = l[i] / sum(l)
        dico[list(d.keys())[i]] = proportion
    
    return dico

def affichageCamembert(d : Dict[str, np.ndarray]) :
    """!
    @brief Affiche 2 camemberts représentant la proportion des fichiers à la première observation et à la dernière

    Paramètres : 
        @param d : Dict[str,np.ndarray] => les clés sont les noms de fichiers, les valeurs un ndarray de dimension 2
    """
    
    #Premier camembert
    labels : List[str] = list(d.keys())
    sizes : List[float] = repartition(d, d[labels[0]][0,1]).values()
    colors : List[str] = sample(mcolors.CSS4_COLORS.keys(), len(sizes))
    plt.subplot(1,2,1)
    plt.pie(sizes, labels=labels, colors=colors)
    
    #Second camembert
    labels : List[str] = list(d.keys())
    sizes : List[float] = repartition(d, d[labels[0]][d[labels[0]].shape[1]-1,1]).values()
    colors : List[str] = sample(mcolors.CSS4_COLORS.keys(), len(sizes))
    plt.subplot(1,2,2)
    plt.pie(sizes, labels=labels, colors=colors)
    
    plt.show()
    

if __name__ == "__main__":
    f = "donneesTP2_SAE15.csv"
    res = csvToDict(f)
    # for fs in res:
    #     print(f"Fichier {fs} :")
    #     print(f"\t-Augmentation moyenne : {augmentationMoyenne(res[fs])}")
    #     print(f"\t-Augmentation maximale : {plusGrandeAugmentation(res[fs])}")
    #     print(f"\t-Limite atteinte 2000 : {limiteAtteinte(res[fs], 2000)}")
    
    # print(repartition(res, 1636974960))
    affichageCamembert(res)
    

