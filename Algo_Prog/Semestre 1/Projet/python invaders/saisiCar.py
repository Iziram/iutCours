#!/usr/bin/env python
"""! @brief Classe pour simplifier la gestion des saisies caractère par caractère
en mode non bloquant (sans attendre une saisie)
et en mode canonique (sans presser entrée et sans remplir le buffer)
 @file saisiCar.py
 @section saisiCar Libraries/Modules
  - termios standard library (https://docs.python.org/fr/3/library/termios.html)
  - atexit standard library (https://docs.python.org/fr/3/library/atexit.html)
  - sys standard library (https://docs.python.org/fr/3/library/sys.html)
  - select standard library (https://docs.python.org/fr/3/library/select.html)

 @section author_libraries_saisiCar Author(s)
 - Crée par Grégory Smits le 25/08/2021.

 Copyright (c) 2021 IUT de Lannion.  All rights reserved.

"""

import os
from typing import List

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select


class SaisiCar:

    def __init__(self):
        '''
        Constructeur de la classe SaisiCar.
        Détecte l'OS et initialise le terminal
        '''

        if os.name == 'nt':
            pass

        else:

            # Récupération du profil actuel du terminal
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # Pas de bufferisation
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Réinitialisation en fin de session
            atexit.register(self.reinitialise)


    def reinitialise(self):
        ''' 
            Réinitialise les paramètres initiaux du terminal
        '''
        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def recupCar(self, l : List[str]= None) -> str:
        ''' Retourne le caractère saisi (sauf flêches)
            @param l : List[str]= None filtre des caractères captés, si défini et touche en dehors de l'ensemble retourne None
            @return str une chaîne de longueur 1
        '''
        s : str = None
        ret : str = None
        if self.carDispo():
            if os.name == 'nt':
                s= msvcrt.getch().decode('utf-8')
            else:
                s= sys.stdin.read(1)
            
            if filter is not None and s in l:
                ret = s
        return ret
   


    def carDispo(self):
        '''
            Test si un caractère est disponible pour la lecture non bloquante.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []


# Test    
if __name__ == "__main__":

    kb = SaisiCar()

    print("Capture les touches 'k' 'm' 'o' et 'q' pour quitter")
    i = 0
    while True:
        if i == 0:
            print("WAIT ...")
            i = 1

        c = kb.recupCar(['k','m','o','q'])
        if c is not None:
            if c == 'q':
                break
            print("Saisi",c)
            i = 0

    kb.reinitialise()