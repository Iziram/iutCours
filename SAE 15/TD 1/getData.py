"""
@name: getData.py
@date: 29/10/2012
@author: Iziram
"""
from csv import reader
from typing import List, Tuple
from datetime import datetime

def getDataFromFile(file: str) -> List[Tuple[int, int]]:
    """
    Cette fonction récupère les données du fichier csv passé en entrée et retourne une liste de tuple corspondant à chaque ligne. 
    Args:
        file (str): Fichier csv ayant les données systèmes récupérées par le script "td1.sh" 

    Returns:
        List[Tuple[str, int]]: Liste de tuple correspondant aux lignes du fichier csv.
    """


    with open(file) as csv_file:
        data : List[Tuple[str, int]] = []
        csv = reader(csv_file, delimiter=',')
        row : List[str]
        data = [(int(row[0]),int(row[1])) for row in csv]
    return data


def getSampledData(data: List[Tuple[int,int]], time:int) -> List[Tuple[int, List[Tuple[int,int]]]]:
    """
    Cette fonction permet de générer un échantillonnage des données en fonction d'une période et d'une liste de données.
    Args:
        data (List[Tuple[int,int]]): Liste de Tuple représentant les données
        time (int): entier représentant la période.

    Returns:
        List[Tuple[int, List[Tuple[int,int]]]]: Une liste de tuple de la forme : [ (timestamp du premier échantillon, [ (donnee, timestamp) . . . ]) ]
    """

    sampledData : List[List[Tuple[int,int]]] = []
    tmpList : List[Tuple[int,int]] = [data[0]]
    sumDiff = 0
    count = 0
    for i in range(1, len(data)) :
        d = datetime.fromtimestamp(data[i-1][1])
        d2 = datetime.fromtimestamp(data[i][1])
        diff = (d2 - d).total_seconds() / 60
        sumDiff += diff
        if sumDiff >= time :
            sampledData.append((tmpList[0][1], [i for i in tmpList]))
            tmpList.clear()
            sumDiff = 0
        
        tmpList.append(data[i])
    sampledData.append((tmpList[0][1], tmpList))
    return sampledData

def getSampleStatistic(sampledData: Tuple[int, List[Tuple[int, int]]]) -> Tuple[int, Tuple[int, int, float]]:
    """
    Cette fonction permet de générer des statistiques en fonction d'un échantillons de données.
    Les statistiques :
        - Valeur minimale des données
        - Valeur maximal des données
        - Moyenne des données
    Args:
        sampledData (Tuple[int, List[Tuple[int, int]]]): [description]

    Returns:
        Tuple[int, Tuple[int, int, float]]: Un tuple du format : 
    """
    sample : List[Tuple[int,int]]= sampledData[1]
    maxi : int = max(sample, key= lambda item:item[0])[0]
    mini : int = min(sample, key= lambda item:item[0])[0]
    moy : float = [sum(x) for x in zip(*sample)][0] / len(sample)

    return (sampledData[0], (mini,maxi, moy))

def printSamplesAndStatistics(sampledData: List[Tuple[int, List[Tuple[int,int]]]]):
    """
    Cette fonction permet d'afficher les données échantillonnées ainsi que leurs statistiques.
    Args:
        sampledData (List[Tuple[int, List[Tuple[int,int]]]]): La liste contenant les données échantillonnées.
    """
    for i in sampledData:
        print("Date of the first item of the Sample :",datetime.fromtimestamp(i[0]))
        for j in i[1]:
            print("\t",j)
        mini,maxi,moy = getSampleStatistic(i)[1]
        print("\t---Statistics---")
        print(f'\t- min: {mini} \n\t- max: {maxi} \n\t- moyenne: {moy}')
        print("\t----------------")

if __name__ == "__main__":

    data = getDataFromFile('/tmp/resTest')
    sampledData = getSampledData(data, 5)
    printSamplesAndStatistics(sampledData)