from typing import Dict, List
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
    
    def __str__(self):
        return f'{self.nom} {self.mail} {self.diplome} {self.id} {self.bulletin}'

# if __name__ == "__main__":
#     bob = etudiant("bob", "bob@etu.fr", "BUT R&T")
#     bob.modifierEtudiant()
#     bob.ajouterNote("Res", 12.4)
#     bob.ajouterNote("Maths", 15.7)
#     print(bob.calculerMoyenne())
#     bob.afficherEtudiant()

class GroupeDeTP:
    def __init__(self, nom : str):
        self.nom : str = nom
        self.liste : List[etudiant]= []
    
    def ajouterEtudiant(self, etudiant : etudiant):
        if etudiant in self.liste:
            raise Exception("L'étudiant se trouve déjà dans le groupe.")
        else:
            self.liste.append(etudiant)
    
    def etudiantPresent(self, nom: str) -> bool:
        estLa : bool = False
        i : int = 0
        while i < len(self.liste) and not estLa:
            etu : etudiant = self.liste[i]
            estLa = etu.nom == nom
            i += 1
        return estLa
    
    def moyenneGroupe(self) -> float:  
        moyennes : List[float] = [e.calculerMoyenne() for e in self.liste]
        return sum(moyennes) / len(moyennes)
    
    def __str__(self):
        representation : str = "-- Groupe A --\n"
        for e in self.liste:
            representation += f'{e}\n'
        return representation + "-- Groupe A --"

if __name__ == "__main__":
    # Création des étudiants et du groupe
    toto : etudiant = etudiant("toto", "toto@etu", "r&t")
    tata : etudiant = etudiant("tata", "tata@etu", "r&t")
    tutu : etudiant = etudiant("tutu", "tutu@etu", "r&t")
    groupeA : GroupeDeTP = GroupeDeTP("A")
    
    #Ajout des étudiants dans le groupe
    groupeA.ajouterEtudiant(toto)
    groupeA.ajouterEtudiant(tata)
    groupeA.ajouterEtudiant(tutu)
    
    #Ajout de notes aléatoires
    from random import randint
    matiere : List[str] = ["Maths","Résaux","Prog"]
    for e in groupeA.liste:
        for m in matiere:
            e.ajouterNote(m, float(randint(0, 20)))
    
    
    print(groupeA)
    print(groupeA.moyenneGroupe())
    print(groupeA.etudiantPresent("toto"))
    print(groupeA.etudiantPresent("tati"))
    try:
        groupeA.ajouterEtudiant(toto)
    except Exception as e:
        print(e)