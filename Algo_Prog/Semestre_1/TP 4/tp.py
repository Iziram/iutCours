#Partie 1
"""
chaine : str
chaine = input()
print(type(chaine))
print(len(chaine))
print(chaine[0])
print(chaine[-1])
"""

# Partie 2

import string

def verifMDP(chaine: str) -> bool:
    """
    Fonction permettant de vérifier la validité d'un mot de passe. Retourne vrai si le mot de passe donné est valide.
    Args:
        chaine (str): le mot de passe à tester.

    Returns:
        bool: un booléen symbolisant la validité du mot de passe. True si valide, False sinon.
    """
    res : bool = False
    if len(chaine) >= 8:
        i : int = 0
        punc : bool = False
        chiffre : bool = False
        space : bool = True
        while i < len(chaine) and space :
            if not punc : punc = chaine[i] in string.punctuation
            if not chiffre : chiffre = chaine[i] in string.digits
            if space : space = chaine[i] != " "
            i +=1 
        print(chaine+"|", i,space, punc, chiffre)
        res = space and punc and chiffre
    return res

assert verifMDP("") == False 
assert verifMDP("Matthias") == False 
assert verifMDP("Matthias1") == False
assert verifMDP("Matthias1.") == True
assert verifMDP(" M1atthias.") == False



def nombreMaj(chaine:str) -> int :

    count : int = 0
    for i in range(len(chaine)):
        if chaine[i] in string.ascii_uppercase :
            count +=1
    return count

assert nombreMaj("Matthias") == 1
assert nombreMaj("matthias") == 0
assert nombreMaj("MAtthIAS") == 5



def majuscule(s:str) -> str:
    """
    Fonction prenant en paramètre une chaine et la retournant en majuscule.
    Paramètre : s -> str la chaîne à mettre en majuscule
    Retour : str la chaîne en majuscule.
    """
    return s.upper()
assert majuscule("Bonjour") == "BONJOUR"
assert majuscule("B") == "B"
assert majuscule("") == ""

def minuscule(s : str) -> str:
    """
    Fonction prenant en paramètre une chaîne et la retournant en minuscule
    Param`etre : s -> str la chaîne à mettre en minuscule
    Retour : str la chaîne en minuscule
    """
    return s.lower()

assert minuscule("Bonjour") == "bonjour"
assert minuscule("b") == "b"
assert minuscule("") == ""

def inverseCase(chaine : str) -> str:
    """
    Fonction inversant la case d'une chaine de caractère
    Args:
        chaine (str): la chaine de caractère à modifier

    Returns:
        str: la chaine de caractère modifiée.
    """
    inverse : str = ""
    for s in chaine:
        if s in string.ascii_uppercase:
            inverse += minuscule(s)
        elif s in string.ascii_lowercase:
            inverse += majuscule(s)
        else:
            inverse += s
    return inverse

assert inverseCase("Matthias") == "mATTHIAS"
assert inverseCase("") == ""
assert inverseCase("mATTHIAS1") == "Matthias1"


def posCar(s: str, c:str) -> int:
    """
    Fonction renvoyant la position d'un caractère c dans une chaîne s
    Renvoie -1 si c n'est pas un caractère ou bien que c n'est pas dans s
    Args:
        s (str): Chaine de caractère à parcourir
        c (str): Caractère à tester.
    Returns:
        int: l'indice de c dans s sinon -1 
    """
    if c == None or len(c) > 1 or len(c) == 0 :
        return -1
    else :
        i : int = 0
        pos : int = -1
        while i<len(s) and pos == -1:
            if s[i] == c :
                pos = i
            i += 1
        return pos 

assert posCar("Matthias", "") == -1
assert posCar("Matthias", "bl") == -1
assert posCar("Matthias", "z") == -1
assert posCar("Matthias", "M") == 0
assert posCar("Matthias", "t") == 2


def palindrome(s: str) -> bool:
    """
    Fonction prenant en paramètre une chaîne et retourne Vrai si la chaine est
    un palindrome sinon faux

    Args:
        s (str): La chaine de caractère à tester 

    Returns:
        bool: un booléen. Vrai si la chaîne s est un palindrome.
    """
    i : int = 0
    while i < len(s) // 2 and s[i] == s[len(s)-1-i]:
        i += 1
    return i == len(s)//2

assert palindrome(" ") == True
assert palindrome("") == True
assert palindrome("anna") == True
assert palindrome("anne") == False
assert palindrome("Kayak") == False



if __name__ == "__main__":
    # print(string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation)
    # print(verifMDP(input("votre mdp: ")))
    # print(palindrome(input("mot: ")))
    pass