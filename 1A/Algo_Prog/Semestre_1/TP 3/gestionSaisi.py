#Module de gestion de la saisie de caractères au clavier
#Utilisation du module termios donc à utiliser depuis un terminal


import termios
import sys, tty

def recupcar() -> str:
    """
    Fonction permettant de récupérer directement (sans
    attendre le caractère entrée) un caractère saisi
    ex : car : str = recupcar()
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == "__main__":
    print("Exemple d'utilisation de la fonction recupcar. Saisissez des caractères, q met fin à la saisie.")
    c : str = ""
    while c != "q":
        c = recupcar()
        print("saisi ", c)
