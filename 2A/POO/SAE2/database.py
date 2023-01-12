import sqlite3


class RequeteBDD:
    def __init__(self, nom_bdd: str) -> None:

        self.__nom_bdd = nom_bdd

        self.__connexion = None

        self.__cursor = None

        self.ouverture_BDD()

    def ouverture_BDD(self) -> None:

        self.__connexion = sqlite3.connect(self.__nom_bdd)

        self.__cursor = self.__connexion.cursor()

    def reponse_unique(self, requete, *args) -> tuple:

        try:

            return self.__cursor.execute(requete, args).fetchone()

        except Exception as e:
            print(e)

    def reponse_multiple(self, requete, *args) -> list[tuple]:

        try:

            return self.__cursor.execute(requete, args).fetchall()

        except Exception as e:
            print(e)

    def execute(self, requete: str, *args) -> None:

        try:

            self.__cursor.execute(requete, args)

            self.sauvegarde_BDD()

        except Exception as e:
            print(e)

    def sauvegarde_BDD(self) -> None:

        self.__connexion.commit()

    def fermeture_BDD(self) -> None:

        self.__connexion.close()


class Database(RequeteBDD):
    def __init__(self, nom_bdd: str) -> None:
        RequeteBDD.__init__(self, nom_bdd)

    def isLoginValid(self, username: str, password: str):

        requete: str = f"select * from identifiants where username=? and password=?"

        reponse = self.reponse_unique(requete, username, password)

        if reponse is None:
            return False
        else:
            return True


if __name__ == "__main__":

    db = Database("bdd.sqlite")
    db.ouverture_BDD()

    print(db.isLoginValid("bob", "1234"), db.isLoginValid("b", "mdp"))
