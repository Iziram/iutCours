"""! @brief Gestionnaire de base de données
 @file database.py
 @section libs Librairies/Modules
  - sqlite3
 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 09/01/2023 .
"""
import sqlite3

# pylint: disable=function-redefined,broad-except,too-many-ancestors,too-few-public-methods


class RequeteBDD:
    """!
    @brief Classe facilitant les échanges avec la BDD


    """

    def __init__(self, nom_bdd: str):

        self.__nom_bdd = nom_bdd

        self.__connexion = None

        self.__cursor = None

        self.ouverture_bdd()

    def ouverture_bdd(self):
        """!
        @brief Permet de se connecter à une base de donnée

        Paramètres :
            @param self => Le connecteur BDD
        """

        self.__connexion = sqlite3.connect(self.__nom_bdd)

        self.__cursor = self.__connexion.cursor()

    def reponse_unique(self, requete, *args) -> tuple:
        """!
        @brief Permet d'envoyer une requête qui n'attend qu'un seul résultat

        Paramètres :
            @param self => Le connecteur BDD
            @param requete => la requête à exécuter
            @param *args => les données à compléter dans la requête
        Retour de la fonction :
            @return tuple => le résultat de la requête

        """
        res: tuple = None
        try:
            res = self.__cursor.execute(requete, args).fetchone()
        except Exception as err:
            print(err)

        return res

    def reponse_multiple(self, requete, *args) -> list[tuple]:
        """!
        @brief Permet d'envoyer une requête qui attend de multiples résultats

        Paramètres :
            @param self => Le connecteur BDD
            @param requete => la requête à exécuter
            @param *args => les données à compléter dans la requête
        Retour de la fonction :
            @return list[tuple] => la liste des résultats de la requête

        """
        res: list[tuple] = None
        try:
            res = self.__cursor.execute(requete, args).fetchall()

        except Exception as err:
            print(err)

        return res

    def execute(self, requete: str, *args):
        """!
        @brief Permet d'envoyer une requête qui n'attend pas de résultat

        Paramètres :
            @param self => Le connecteur BDD
            @param requete : str => la requête à exécuter
            @param *args => les données à compléter dans la requête

        """
        try:
            self.__cursor.execute(requete, args)
            self.sauvegarde_bdd()
        except Exception as err:
            print(err)

    def sauvegarde_bdd(self):
        """!
        @brief Permet de sauvegarder les modifications de la bdd

        Paramètres :
            @param self => Le connecteur BDD

        """

        self.__connexion.commit()

    def fermeture_bdd(self):
        """!
        @brief Ferme la connexion à la bdd

        Paramètres :
            @param self => Le connecteur BDD

        """
        self.__connexion.close()


class Database(RequeteBDD):
    """!
    @brief Implémentation de la classe RequeteBDD
      dans le cadre de la SAE3.02

    ## Héritage :
        - Implémente RequeteBDD

    """

    def __init__(self, nom_bdd: str):
        RequeteBDD.__init__(self, nom_bdd)

    def is_login_valid(self, username: str, password: str):
        """!
        @brief Vérifie si le couple (username,password) existe dans la bdd

        Paramètres :
            @param self => Le connecteur BDD
            @param username : str => le login du client
            @param password : str => le mot de passe du client

        """

        requete: str = "select * from identifiants where username=? and password=?"

        reponse = self.reponse_unique(requete, username, password)

        return reponse is not None

    def is_username_known(self, username: str):
        """!
        @brief Vérifie si un username est présent dans la bdd

        Paramètres :
            @param self => Le connecteur BDD
            @param username : str => le login du client

        """
        requete: str = "select * from identifiants where username=?"

        reponse = self.reponse_unique(requete, username)

        return reponse is not None

    def create_user(self, username, password):
        """!
        @brief Créer un nouveau couple (login,mdp) dans la bdd

        Paramètres :
            @param self => Le connecteur BDD
            @param username => le login du client
            @param password => le mot de passe du client

        """
        requete: str = "insert into identifiants (username,password) values (?,?)"
        self.execute(requete, username, password)
        self.sauvegarde_bdd()


if __name__ == "__main__":

    db = Database("bdd.sqlite")
    db.ouverture_bdd()

    print(db.is_login_valid("bob", "1234"), db.is_login_valid("b", "mdp"))
