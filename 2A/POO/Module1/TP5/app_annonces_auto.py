from typing import List, Dict, Tuple

import sqlite3
import json

import csv


class RequeteBDD:
    def __init__(self, nom_bdd: str) -> None:

        self.__nom_bdd = nom_bdd

        self.__connexion = None

        self.__cursor = None

        self.ouverture_BDD()

    def ouverture_BDD(self) -> None:

        self.__connexion = sqlite3.connect(nom_bdd)

        self.__cursor = self.__connexion.cursor()

    def reponse_unique(self, requete, *args) -> Tuple:

        try:

            return self.__cursor.execute(requete, args).fetchone()

        except Exception as e:
            print(e)

    def reponse_multiple(self, requete, *args) -> List[Tuple]:

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


def init(nom_bdd, *requete):

    bdd = RequeteBDD(nom_bdd)

    bdd.ouverture_BDD()

    for req in requete:

        bdd.execute(req)

    return bdd


def importer_csv(nom_csv: str, BDD: RequeteBDD, requete: str) -> None:

    with open(nom_csv, "tr", encoding="utf-8") as file:

        file.readline()
        for line in file:

            params: List[str] = line.split(",")

            params[-1] = params[-1].replace("\n", "")

            BDD.execute(requete, *params)


def sauvegarder_csv(nom_csv, *args):
    with open(nom_csv, "w", encoding="utf-8") as file:
        for ite in args:
            line = ""
            for param in ite:
                line += str(param) + ","
            line = line[:-1] + "\n"
            file.write(line)


def sauvegarder_json(nom_json, args):
    with open(nom_json, "w", encoding="utf-8") as file:
        json.dump(args, file)


if __name__ == "__main__":

    nom_bdd: str = "annonces.sqlite3"

    choix: int = -1

    BDD: RequeteBDD = None

    while choix != 0:

        # menu

        print(" 0 : pour sortir")

        print(" 1 : creer la base de donnees")

        print(" 2 : importer les donnees a partir des fichiers csv")

        print(" 3 : ouvrir la base de données")

        print(" 4 : afficher le nombre d'annonces disponibles")

        print(" 5 : afficher toutes les annonces")

        print(" 6 : afficher le nombre d'annonces par marque")

        print(" 7 : afficher les annonces par marque")

        print(" 8 : afficher les annonces par si km inferieur à ...")

        print(" 9 : afficher les annonces par marque avec km inferieur à ...")

        print("10 : affiche annonce si prix inferieur à ...")

        print("11 : ajouter un véhicule dans le stock")

        print("12 : sauvegarder les donnees aux format csv")

        print("13 : sauvegarder les donnees au format json")

        print("14 : fermer la base de données")

        choix = int(input("votre choix : "))

        if choix == 1:  # creer la BDD

            create_table: List[str] = [
                """CREATE TABLE t_marques (




                id INTEGER PRIMARY KEY AUTOINCREMENT,




                manque TEXT




                );""",
                """




                CREATE TABLE t_modeles (




                id INTEGER PRIMARY KEY AUTOINCREMENT,




                id_marque INTEGER,




                modele TEXT,




                cylindree REAL,




                puissance INTEGER,




                consommation REAL




                );""",
                """




                CREATE TABLE t_annonces (




                id INTEGER PRIMARY KEY AUTOINCREMENT,




                id_marque INTEGER,




                id_modele INTEGER,




                designation TEXT,




                annee INTEGER,




                kilometrage INTEGER,




                prix INTEGER




                );""",
            ]

            BDD = init(nom_bdd, *create_table)

        elif choix == 2:  # importer les donnees a partir des fichiers csv

            importer_csv("t_marques.csv", BDD, "insert into t_marques VALUES(?,?)")

            importer_csv(
                "t_annonces.csv", BDD, "insert into t_annonces VALUES(?,?,?,?,?,?,?)"
            )

            importer_csv(
                "t_modeles.csv", BDD, "insert into t_modeles VALUES(?,?,?,?,?,?)"
            )

        elif choix == 3:  # ouverture de la bdd

            BDD = RequeteBDD(nom_bdd)

        elif choix == 4:  # nombre d'annoces

            nombre_annonces = BDD.reponse_unique("select count(*) from t_annonces")

            print(f"Nombre d'annonces : {nombre_annonces[0]}")

        elif choix == 5:  # afficher toutes les annonces

            annonces = BDD.reponse_multiple("select * from t_annonces")
            for anno in annonces:
                print(anno)

        elif choix == 6:  # nombres d'annonces par marque

            req: str = "select manque,count(*) from t_annonces inner join t_marques on t_marques.id = t_annonces.id_marque group by id_marque"

            nb_annonces_par_marque = BDD.reponse_multiple(req)

            for anno in nb_annonces_par_marque:
                print(anno)

        elif choix == 7:  # afficher les annonces par marque

            req: str = "select manque,* from t_annonces inner join t_marques on t_marques.id = t_annonces.id_marque order by manque"

            nb_annonces_par_marque = BDD.reponse_multiple(req)

            for anno in nb_annonces_par_marque:
                print(anno)

        elif choix == 8:  # afficher les annonces si km inferieur à ...

            req: str = "select * from t_annonces where kilometrage < ?"

            nb_annonces_par_marque = BDD.reponse_multiple(
                req, int(input("Kilometrage: "))
            )
            for anno in annonces:
                print(anno)

        elif choix == 9:  # afficher les annonces par marque avec km inferieur à ...

            req: str = "select manque,* from t_annonces inner join t_marques on t_marques.id = t_annonces.id_marque group by id_marque having kilometrage < ?"

            nb_annonces_par_marque = BDD.reponse_multiple(
                req, int(input("Kilometrage: "))
            )

            for anno in nb_annonces_par_marque:
                print(anno)

        elif choix == 10:  # affiche annonce si prix inferieur à ...

            req: str = "select * from t_annonces where prix < ?"

            annonces = BDD.reponse_multiple(req, int(input("Prix: ")))
            for anno in annonces:
                print(anno)

        elif choix == 11:  # ajouter un véhicule dans le stock
            marque: str = input("Nom de la marque: ")

            # Vérification de l'existance de la marque
            mrq_req = BDD.reponse_unique(
                "select id from t_marques where manque = ?", marque
            )
            if mrq_req != None:
                modele: str = input("Nom modele: ")
                mdl_req = BDD.reponse_unique(
                    "select id from t_modeles where id_marque = ? and modele = ?",
                    mrq_req[0],
                    modele,
                )

                # Vérification de l'existance du modele chez la marque
                if mdl_req != None:
                    designation: str = input("Designation: ")
                    annee: int = int(input("Année: "))
                    kilometrage: int = int(input("Kilometrage: "))
                    prix: int = int(input("Prix: "))
                    req = "insert into t_annonces (id_marque,id_modele,designation,annee,kilometrage,prix) values (?,?,?,?,?,?)"
                    BDD.execute(
                        req,
                        mrq_req[0],
                        mdl_req[0],
                        designation,
                        annee,
                        kilometrage,
                        prix,
                    )
                else:
                    print("Le modele n'existe pas")
            else:
                print(f"La marque {marque} n'existe pas")

        elif choix == 12:  # sauvegarder les donnees aux format csv
            sauvegarder_csv(
                "sauvegarde_csv_t_annonces.csv",
                *BDD.reponse_multiple("select * from t_annonces"),
            )
            sauvegarder_csv(
                "sauvegarde_csv_t_modeles.csv",
                *BDD.reponse_multiple("select * from t_modeles"),
            )
            sauvegarder_csv(
                "sauvegarde_csv_t_marques.csv",
                *BDD.reponse_multiple("select * from t_marques"),
            )

        elif choix == 13:  # sauvegarder les donnees aux format json"
            sauvegarder_json(
                "sauvegarde_json_t_annonces.json",
                BDD.reponse_multiple("select * from t_annonces"),
            )
            sauvegarder_json(
                "sauvegarde_json_t_modeles.json",
                BDD.reponse_multiple("select * from t_modeles"),
            )
            sauvegarder_json(
                "sauvegarde_json_t_marques.json",
                BDD.reponse_multiple("select * from t_marques"),
            )
        elif choix == 14:  # fermer la base de données
            BDD = BDD.fermeture_BDD()
