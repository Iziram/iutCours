from typing import Dict
class etudiant:
    nbEtudiant : int = 1001
    
    def __init__(self, nom:str, mail: str, diplome : str):
        if('@' not in mail): raise Exception("email erroné")
        self.id = etudiant.nbEtudiant
        etudiant.nbEtudiant += 1
        
        self.nom = nom
        self.mail = mail
        self.diplome = diplome
        self.bulletin = {}

    def modifierEtudiant(self, nom: str = None, mail : str = None, diplome: str = None):
        if(nom == None and mail == None and diplome == None):
            self.nom = input("Indiquez le nom de l'étudiant: ")
            self.mail = input("Indiquez le mail de l'étudiant: ")
            self.diplome = input("Indiquez le diplome de l'étudiant: ")
        else:
            if nom != None:
                self.nom = nom
            if mail != None:
                self.mail = mail
            if diplome != None:
                self.diplome = diplome
                
        if('@' not in self.mail): raise Exception("email erroné")
        
    def afficherEtudiant(self):
        print(f'{self.nom} {self.mail} {self.diplome} {self.id} {self.bulletin}')
    
    def ajouterNote(self, matiere: str, note:float):
        if(matiere not in self.bulletin):
            self.bulletin[matiere] = note
        else:
            raise Exception("Examen déjà renseigné")
    
    def modifierNote(self, matiere: str, note:float):
        if(matiere in self.bulletin):
            self.bulletin[matiere] = note
        else:
            raise Exception("L'examen n'existe pas")
        
    def calculerMoyenne(self) -> float:
        return sum(self.bulletin.values()) / len(self.bulletin)
    
    
if __name__ == "__main__":
    bob = etudiant("bob", "bob@etu.fr", "BUT R&T")
    bob.modifierEtudiant()
    bob.ajouterNote("Res", 12.4)
    bob.ajouterNote("Maths", 15.7)
    print(bob.calculerMoyenne())
    bob.afficherEtudiant()