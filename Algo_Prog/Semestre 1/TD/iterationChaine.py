def getOccurence(c:str, chaine:str) -> int:
    count : int = 0
    for i in chaine:
        if c == i : count += 1
    return count

assert getOccurence('t',"Matthias") == 2
assert getOccurence('z',"Matthias") == 0


def getFirstOccurence(c:str, s:str) -> int:
    pos : int = -1
    i : int = 0
    while pos == -1 and i <len(s):
        if c == s[i] : pos = i
        else : i += 1 
    return pos

assert getFirstOccurence('t',"Matthias") == 2
assert getFirstOccurence('z', "Matthias") == -1

def getLastOccurence(c:str, s:str) -> int:
    pos : int = -1
    i : int = len(s)-1
    while i > 0 and pos == -1:
        if c == s[i] : pos = i
        else : i -= 1 
    return pos 

assert getLastOccurence('t',"Matthias") == 3
assert getLastOccurence('z', "Matthias") == -1

def getVowels(s:str) -> int:
    count : int = 0
    for i in s:
        if i in "aeiouy": count += 1
    return count

assert getVowels("Matthias") == 0
assert getVowels("Bljzgd") == 0

        