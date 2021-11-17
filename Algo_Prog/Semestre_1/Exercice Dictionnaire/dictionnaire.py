"""
@name: dictionnaire.py
@date: 29/10/2021
@author: Iziram
"""
#Importation des modules
from typing import Dict
from csv import reader

#Définitions des Fonctions
def getUsersDictionnary(file: str) -> Dict[str,int]:
    """
    Cette fonction prend en paramètre le nom d'un fichier. Le contenu de ce fichier
    doit être dans le format du fichier /etc/passwd (7 champs séparés par un `:`)
    Cette fonction renverra un dictionnaire qui aura comme clé le nom de l'utilisateur
    et comme valeur son identifiant.

    Args:
        file (str): le nom du fichier

    Returns:
        Dict[str,int]: le dictionnaire => [nom_utilisateur: identifiant]
    """
    with open(file) as csv_file:
        data : Dict[str,int] = {}
        csv = reader(csv_file, delimiter=':')
        for row in csv:
            assert len(row) == 7 , 'Chaque ligne du fichier doit avoir 7 champs séparés par un `:`'
            data[row[0]] = int(row[2])
    return data

def getUserIndentifier(username:str, users:Dict[str,int]) -> int | None:
    """
    Cette fonction renvoit un identifiant en fonction du nom d'utilisateur passé en entrée.

    Args:
        username (str): le nom de l'utilisateur
        users (Dict[str,int]): le dictionnaire contenant les nom d'utilisateurs et leurs identifiants

    Returns:
        [int]: L'identifiant si l'utilisateur existe
        [None]: None si l'utilisateur n'existe pas.
    """
    res = None
    if username in users:
        res = users[username]
    return res
    # return users.get(username, None)

#Tests de fonctionnement
test : Dict[str, int] = {'root':0, 'bin':1, 'toto':3}
assert getUserIndentifier('root', test) == 0
assert getUserIndentifier('bin', test) == 1
assert getUserIndentifier('', test) == None
assert getUserIndentifier(1, test) == None
del(test)

#Programme Principal
if __name__ == "__main__":
    users : Dict[str,int] = getUsersDictionnary('/etc/passwd')
    print(getUserIndentifier('iziram', users))