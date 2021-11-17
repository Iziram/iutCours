"""! @brief [description du fichier]
 @file /home/iziram/Documents/GitHub/iutCours/SAE 15/TD 3/td.py
 @section libs Librairies/Modules
  - [Nom du module] (lien)

 @section authors Author(s)
  - Créé par [Prénom] [Nom] le [Date] .
"""
import numpy as np
import matplotlib.pyplot as plt

def partie1 (data1 : np.ndarray, 
             data2 : np.ndarray) :
    """!
    @brief Cette fonction gère la partie 1 du TD 3

    Paramètre(s) : 
        @param data1 : np.ndarray => Un tableau à 2 dimensions représantant des données
        @param data2 : np.ndarray => Un tableau à 2 dimensions représantant des données

    """
    fig, axs = plt.subplots(2)
    axs[0].scatter(data1[: , 0],data1[: , 1])
    axs[1].scatter(data2[: , 0],data2[: , 1])
    plt.show()

def partie2(data:np.ndarray) :
    """!
    @brief Cette fonction gère la partie 2 du TD 3

    Paramètre(s) : 
        @param data : np.ndarray => Un tableau à 2 dimensions représantant des données

    """
    maxi = data.max(0)
    mini = data.min(0)
    moy = data.mean(0)
    std = data.std(0)
    
    #plt.errorbar([étiquette1, étiquette2...], "point central à placer", ["taille min de l'error bar", "taille max de l'error bar"])
    plt.errorbar(['x','y'], moy, std, fmt='ok', lw=1, capsize=2, elinewidth=2)
    
    plt.errorbar(['x','y'], moy, [moy-mini, maxi-moy], fmt='.k', lw=1, capsize=1, elinewidth=1, ecolor="gray")
    
    
    plt.show()
    


if __name__ == "__main__":
    data1 : np.ndarray = np.genfromtxt("data1.csv", delimiter=",")
    data2 : np.ndarray = np.genfromtxt("data2.csv",delimiter=",")
    # partie1(data1, data2)
    partie2(data1)