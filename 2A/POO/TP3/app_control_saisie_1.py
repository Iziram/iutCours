if __name__ == "__main__":
    nombre: int = -1
    tentative: int = 0
    while nombre < 0 or nombre > 20:
        try:
            tentative += 1
            nombre = input("Veuillez entrer un nombre: ")
            nombre = int(nombre)
            while nombre < 0 or nombre > 20:
                raise IndexError("La valeur n'est pas comprise entre 0 et 20")
        except ValueError as e:
            print("Vous devez entrer un nombre")
            nombre = -1
        except IndexError as e:
            print(e)
    print(f"Votre nombre est {nombre} vous avez reussit en {tentative} tentatives")
