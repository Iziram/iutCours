"""
Thread:
    Thread(target, args/kwargs, name)
        target => une fonction qui sera exécuté par le thread
        args => les arguments de la fonction exécutée
        name => le nom du thread (optionnel)

    Thread.run() => Lance la fonction en tenant compte du current thread
        @override -> pour changer ce que doit faire le thread dans une classe enfant
    Thread.start() => Lance le thread de son coté
"""
from threading import Thread
from time import sleep


class Enfant(Thread):
    """
    Exemple de classe
    """

    # On remplace l'init de Thread
    def __init__(self, age) -> None:
        # On utilise l'init de Thread
        Thread.__init__(self)

        # On définit les valeurs de Enfant
        self.age = age

    # On remplace le run de thread par le code qui sera exécuté par le thread parallèle.
    def run(self):
        sleep(1)
        print(self.age)


e = Enfant(21)
e.start()
