def ChaineToList(s:str) -> list:
    return list(s)

def getStatistics(liste: list) -> tuple:
    maxi : int = max(liste)
    mini : int = min(liste)
    moy : int = sum(liste)/len(liste)
    return (maxi, mini, moy) 

def union(l1:list, l2:list) -> list:
    return l1 + l2

def difference(l1:list, l2:list) -> list:
    return [i for i in l1 if i not in l2] + [i for i in l2 if i not in l1]

def intersection(l1:list, l2:list) -> list:
    return [i for i in l1 if i in l2]

if __name__ == "__main__":
    liste : list = [i for i in range(100)]
    # print(liste[4])

    # print(liste[0:5])

    # print(liste[0:6])
    # print([i for i in range(len(liste)) if i < 6 ])

    # print(liste[6:len(liste)])
    # print([i for i in range(len(liste)) if i >= 6 ])
    
    # print(liste[0], liste[-1])

    # print(getStatistics(liste))

    print(union([12,55,32],[14,25,32]))
    print(difference([12,55,32],[14,25,32]))
    print(intersection([12,55,32],[14,25,32]))
    
