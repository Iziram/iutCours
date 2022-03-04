import numpy as np 


#Partie 1
print("---Partie 1.1---")

#1
MATRICE = np.array([[8,3],[5,2]])
print(np.dot(MATRICE, np.linalg.inv(MATRICE)))
#2
MATRICE = np.array([[2,3,4],[1,2,1],[-1,-1,2]])
INV_MATRICE = np.linalg.inv(MATRICE)
print("---Partie 1.2---")
print(np.dot(MATRICE, INV_MATRICE))

print(np.dot(INV_MATRICE, np.array([[0],[3],[-7]])))

#Partie 2
print("---Partie 2.6---")
def inverseMatrice2(A) -> np.ndarray:
    det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
    if det != 0:
        return det * np.array([[A[1,1], -A[0,1]],[-A[1,0],A[0,0]]])
    raise ValueError("La matrice n'est pas inversible.")

print(inverseMatrice2(np.array([[8,3],[5,2]])))
#Partie 3

def mineur(M, i, j) -> np.ndarray:
    MINEUR = np.copy(M)
    MINEUR = np.delete(MINEUR, i-1, axis=0)
    MINEUR = np.delete(MINEUR, j-1, axis=1)
    det = MINEUR[0,0]*MINEUR[1,1] - MINEUR[0,1]*MINEUR[1,0]
    return det

print("---Partie 3.7---")
M = np.array([[1,2,-1],[3,1,3],[-2,0,1]])
print(mineur(M, 1, 2))

print("---Partie 3.8---")

def cofacteur(M, i,j) -> np.ndarray:
    val = M[i-1,j-1]
    return (-1)**(i+j) * mineur(M, i,j)

print(cofacteur(M, 1, 2))

print("---Partie 3.10---")

def comatrice(A) -> np.ndarray:
    l = A.shape[0]
    C =  np.zeros((l,l))
    for i in range(l):
        for j in range(l):
            C[i,j] = cofacteur(A, i+1, j+1)
    return C
    
print(comatrice(M))

print("---Partie 3.11---")

def inverse(M):
    det = np.linalg.det(M)
    if det != 0:
        return (1/det) * np.transpose(comatrice(M)) 
    
    raise ValueError("La matrice M n'est pas inversible")

print(inverse(M))
print("\n")
print(np.linalg.inv(M))