from typing import List, Tuple,Set

def sommeListe(liste : List[float] = []) -> float :
    """
    Cette fonction renvoie la somme de tous les réels contenus dans la liste `liste`

    Args:
        liste (List[float], optional): La liste de réels. par défaut la liste est vide et la fonction renvoie 0.0

    Returns:
        float: La somme des réels de la liste
    """
    compteur : float = 0.0
    for i in liste:
        compteur += i
    return compteur

assert sommeListe([]) == 0
assert sommeListe() == 0
assert sommeListe([0.0]) == 0
assert sommeListe([0.0, 1.3]) == 1.3
assert sommeListe([0.6, 1.3, 4.0]) == 5.9

def moyenneBornee(liste : List[float], deb : int, fin: int) -> float :
    """
    Cette fonction renvoie la moyenne bornée de la liste `liste` à partir des deux bornes
    deb, le début, fin, la fin.

    Args:
        liste (List[float]): Une liste de réels
        deb (int): l'indice de la borne de début
        fin (int): l'indice de la borne de fin

    Returns:
        float: La moyenne bornée de la liste en fonction de deb et fin.
    """

    if deb < 0 : deb = 0
    if fin >= len(liste) : fin = len(liste) - 1

    listeBornee : List[float] = liste[deb:fin+1]
    
    return sommeListe(listeBornee) / len(listeBornee)

assert moyenneBornee([0, 2, -5, 1, 1, 3, 10], 2, 4) == -1
assert moyenneBornee([0, 2, -5, 1, 1, 3, 10], 2, 10) == 2
assert moyenneBornee([0, 2, -5, 1, 1, 3, 10], -3, 2) == -1

#-------------------------------------------------------------------------------

def union(ensembleA : Set[float], ensembleB : Set[float]) -> Set[float] :
    return ensembleA | ensembleB

assert union({1,4,3,5}, {4,2,1,9}) == set({4,2,1,9}).union({1,4,3,5})

def intersection(ensembleA : Set[float], ensembleB : Set[float]) -> Set[float] :
    return ensembleA & ensembleB

assert intersection({1,4,3,5}, {4,2,1,9}) == set({4,2,1,9}).intersection({1,4,3,5})

def difference(ensembleA : Set[float], ensembleB : Set[float]) -> Set[float] :
    return ensembleA - ensembleB

assert difference({4,2,1,9}, {1,4,3,5}) == set({4,2,1,9}).difference({1,4,3,5})

def sousEnsemble(ensembleA : Set[float], ensembleB : Set[float]) -> Set[float] :
    return ensembleB > ensembleA

assert sousEnsemble({4,2,1,9}, {1,4,3,5}) == set({4,2,1,9}).issubset({1,4,3,5})
assert sousEnsemble({1}, {1,4,3,5}) == set({1}).issubset({1,4,3,5})

#-------------------------------------------------------------------------------

def affichageJoueur(joueur: Tuple[int, str, int, List[str]]) -> None:
    """
    Cette fonction affiche les informations relative au joueur donnée
    Args:
        joueur (Tuple[int, str, int, List[str]]): Tuple représentant le joueur
    """
    print(f'{joueur[1]}[{joueur[0]}] : Score : {joueur[2]}')
    print(f'Liste des niveaux terminés par le joueur')
    for i in joueur[3]:
        print(f'- {i}')
def affichageJoueur(joueur: Tuple[int, str, int, List[str]]) -> None:
    """
    Cette fonction affiche les informations relative au joueur donnée
    Args:
        joueur (Tuple[int, str, int, List[str]]): Tuple représentant le joueur
    """
    print(f'{joueur[1]}[{joueur[0]}] : Score : {joueur[2]}')
    print(f'Liste des niveaux terminés par le joueur')
    for i in joueur[3]:
        print(f'- {i}')


if __name__ == "__main__":
    # --- Les Listes ---
    # jours : List[str] = ["lundi","mardi","mercredi","jeudi","vendredi","samedi"]
    # print(len(jours))
    # jours.append("dimanche")
    # print(len(jours))
    # nouveau : List[str] = jours[:5]
    # weekend : List[str] = jours[-2:]
    # ouverture : List[str] = jours[:6]
    # mitemps : List[str] = jours[0::2]
    # print(nouveau, weekend, ouverture, mitemps)

    # # --- Ensemble --- 
    # couleurs : Set[str] = {'rouge','jaune','vert'}
    # print(couleurs)
    # couleurs.add('bleu')
    # couleurs.add('bleu')
    # print(len(couleurs))
    # #pas de troisième élément dans un set car le set n'est pas ordonné
    # couleurs.remove('rouge')
    # print('bleu' in couleurs)
    # print('marron' in couleurs)
    valeurs : Set[float] = set([0, 2, -5, 1, 1, 3, 10])
    
    # --- Tuple ---
    # joueur : Tuple[int, str, int, List[str]] = (7, 'John Doe', 42, ["Temple","Cave","Manoir"])
    # affichageJoueur(joueur)
    pass
