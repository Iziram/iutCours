from typing import Dict, List, Tuple
from datetime import datetime
import numpy as np
import csv



def csvToDict(path : str) -> Dict[str, np.ndarray]:
    """!
    @brief Cette fonction génère un dictionnaire qui contient les données d'évolutions des fichiers.

    Paramètre(s) : 
        @param path : str => le chemin (absolu ou relatif) du fichier qui sera utilisé pour obtenir les données
    Retour de la fonction : 
        @return Dict[str, np.ndarray] Un dictionnaire ayant pour clé le nom de chaque fichier et pour valeur les données d'évolution

    """
    data : Dict[str, np.ndarray] = {}
    with open(path) as file: 
        reader = csv.reader(file)
        for row in reader:
            name : str = row[0]
            taille : int = int(row[1])
            temps : int = int(row[2])
            if name in data.keys():
                data[name] = np.append(data[name], [[taille, temps]], axis=0)
            else :
                data[name] = np.array([[taille, temps]])
    return data

def augmentationMoyenne(data : np.ndarray) -> int:
    """!
    @brief Cette fonction retourne l'augmentation moyenne de la taille du fichier entre deux captations

    Paramètre(s) : 
        @param data : np.ndarray => tableau contenant les données d'évolutions (taille et temps)
    Retour de la fonction : 
        @return int la moyenne
    """
    augment = data[-1,0] - data[0,0]
    return augment / data.shape[0]

def plusGrandeAugmentation(data : np.ndarray) -> Tuple[int, int]:
    """!
    @brief Cette fonction retourne la plus grande augmentation de la taille du fichier lors de la période d'évaluation

    Paramètre(s) : 
        @param data : np.ndarray => tableau contenant les données d'évolutions (taille et temps)
    Retour de la fonction : 
        @return Tuple[int, int] Le couple désignant la plus grande augmentation et le timestamp

    """
    augmentation : int = 0
    resultat : Tuple[int,int] = None
    for i in range(1, data.shape[0]):
        augment = data[i,0] - data[i-1,0]
        time : int = data[i, 1]
        if augment > augmentation :
            augmentation = augment
            resultat = (augmentation, time)
    return resultat

def tailleLimite(data : Dict[str, np.ndarray], limite: int) -> int:
    """!
    @brief Cette fonction retourne le timestamp auquel le fichier à dépasser la taille limite passée en paramètre

    Paramètre(s) : 
        @param data : Dict[str, np.ndarray] => tableau contenant les données d'évolutions (taille et temps)
        @param limite : int => La taille limite en Kilo Octet
    Retour de la fonction : 
        @return int le timestamp ou None si la limite n'a pas été dépassée

    """
    time : int = 0
    i : int = 0
    while i < data.shape[0] and data[i, 0] < limite:
        time = data[i,1]
        i += 1
    return None if data.shape[0] == i and data[i-1, 0] < limite else time

def formatTime(t:int) -> str:
    """!
    @brief Cette fonction renvoie une date EPOCH formatée

    Paramètre(s) : 
        @param t : int => le timestamp 
    Retour de la fonction : 
        @return str la date formatée

    """
    return datetime.utcfromtimestamp(t).strftime('%d-%m-%Y %H:%M:%S')

if __name__ == "__main__":
    donnes : Dict[str, np.ndarray] = csvToDict("TP_2/donneesTP2_SAE15.csv")
    for i in donnes:
        print(f'Le fichier {i} a : \n\t- pour valeur d\'augmentation moyenne : {augmentationMoyenne(donnes[i])}', end=" ")
        grande : Tuple[int, int] = plusGrandeAugmentation(donnes[i])
        print(f'\n\t- la plus grande augmentation s\'est passée le {formatTime(grande[1])} ({grande[0]}Ko)', end=" ")
        limite : int or None = tailleLimite(donnes[i], 2000)
        if limite == None :
            print('Le fichier n\'a jamais dépassé les 2Mo')
        else :
            print(f'le fichier a dépassé les 2Mo le : {formatTime(limite)}')