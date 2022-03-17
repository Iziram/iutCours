import numpy as np
from typing import List, Tuple
print("-- Partie 1 --")
M = np.array([[2,3,1],[0,1,5],[0,0,2]])
print(np.linalg.inv(M))
print("-- Partie 2 --")
def is_symetrique(M: np.ndarray) -> bool:
    if M.shape[0] == M.shape[1]:
        tM = np.transpose(M)
        sym = True 
        col = 0
        line = 0
        while sym == True and line < M.shape[0]:
            while sym == True and col < M.shape[0]:
                sym = M[line,col] == tM[line,col]
                col += 1
            line += 1
        return sym        
    else:
        return False  
    
def is_positive(M:np.ndarray) -> bool or List[Tuple[float,float]]:
    cases = []
    ttLine, ttCol = M.shape
    for line in range(ttLine):
        for col in range(ttCol):
            if M[line,col] < 0:
                cases.append((line,col))
    return cases if len(cases) > 0 else True

print(is_symetrique(np.zeros((3,3))))
print(is_positive(np.zeros((3,3)) * -1))

print("-- Partie 3 --")


A = np.array([[4,2],[2,10]])

T = np.array([[2,1],[0,3]])

print(A)
print(np.dot(np.transpose(T), T))
print("-- Partie 3.8 --")
def factorisation_cholesky(M: np.ndarray) -> np.ndarray:
    if M.shape == (2,2):
        [[w,x],[y,z]] = M
        a = w**0.5
        b = x/a
        c = (z - b**2)**0.5
        return np.array([[a,b],[0, c]])
    else:
        return False

print("Cholesky: \n",factorisation_cholesky(A))
Test = factorisation_cholesky(A)
print("A:\n",A)
print("A (Cholesky): \n",np.dot(np.transpose(T), T))