class SaisieError(Exception):
    NOMBRE_EXCEPT = 0

    def __init__(self, message, *args: object) -> None:
        super().__init__(*args)
        self.__message: str = message
        SaisieError.NOMBRE_EXCEPT += 1

    def get_message(self) -> str:
        return self.__message


if __name__ == "__main__":
    VALEURS: range = range(0, 21)
    nombre: int = -1
    while nombre not in VALEURS:
        try:
            nombre = input("Veuillez entrer un nombre: ")
            nombre = int(nombre)
            if nombre not in VALEURS:
                raise SaisieError("La valeur n'est pas comprise entre 0 et 20")
        except SaisieError as e:
            print(e.get_message())
        except ValueError as e:
            print("Vous devez entrer un nombre")
            SaisieError.NOMBRE_EXCEPT += 1
    print(
        f"Votre nombre est {nombre} vous avez reussit en {SaisieError.NOMBRE_EXCEPT} tentatives"
    )
