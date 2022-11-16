"""! @brief [description du fichier]
 @file app_personne.py
 @section libs Librairies/Modules
 @section authors Auteur(s)
  - Créé par Hartmann Matthias le 07/09/2022 .
"""


class Personne2:
    """!
    @brief [Description de la classe]


    """

    def __init__(self, dictionnaire: dict) -> None:
        for key in dictionnaire:
            setattr(self, key, dictionnaire[key])

    def get_nom(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return str => [description]

        """
        return getattr(self, "_Personne2__nom")

    def get_pays(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return str => [description]

        """
        return getattr(self, "_Personne2__pays")

    def get_anniversaire(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return str => [description]

        """
        return getattr(self, "_Personne2__anniversaire")

    def get_age(self) -> int:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return int => [description]

        """
        return getattr(self, "_Personne2__age")

    def get_id(self) -> int:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return int => [description]

        """
        return getattr(self, "_Personne2__id")

    def get_internet(self) -> bool:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return bool => [description]

        """
        return getattr(self, "_Personne2__internet")

    def get_langue(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return str => [description]

        """
        return getattr(self, "_Personne2__langue")

    def get_genre(self) -> str:
        """!
        @brief [Description de la fonction]

        Paramètres :
            @param self => variable représentant l'instance de l'objet Personne2
        Retour de la fonction :
            @return str => [description]

        """
        return getattr(self, "_Personne2__genre")

    def get_dict(self) -> dict:
        return self.__dict__


if __name__ == "__main__":
    dict_p = {
        "_Personne2__nom": "etienne",
        "_Personne2__age": 34,
        "_Personne2__pays": "france",
        "_Personne2__anniversaire": "1988-12-27",
        "_Personne2__id": 227417393,
        "_Personne2__internet": False,
        "_Personne2__langue": "francais",
        "_Personne2__genre": "homme",
    }
    # déclarez une variable de type Personne2
    variable: Personne2
    # instanciez la variable en utilisant de dictionnaire ci dessus
    variable = Personne2(dict_p)
    # affichez les attributs en utilisant les observateurs
    print(variable.get_age())
    print(variable.get_anniversaire())
    print(variable.get_nom())
    print(variable.get_pays())
    print(variable.get_id())
    print(variable.get_genre())
    print(variable.get_internet())
    print(variable.get_langue())
