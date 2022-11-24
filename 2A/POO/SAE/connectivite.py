"""
Classe Connecteur afin de permettre des connexions avec socket
Connecteur:
    -> Ouvrir une connexion
    -> Fermer une connexion
        -> Code binaire de FIN
    -> Envoyer une suite d'octet
    -> Recevoir une suite d'octet
    -> Se mettre en écoute V
    -> Gérer UDP ET TCP
"""
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, timeout

from enum import Enum


class Protocols(Enum):
    UDP = SOCK_DGRAM
    TCP = SOCK_STREAM


class TypesConnecteur(Enum):
    ECOUTE = 1
    CONNEXION = 0


class Connecteur:
    pass


class Connecteur:
    def __init__(
        self,
        protocol: Protocols = Protocols.TCP,
        type: TypesConnecteur = TypesConnecteur.CONNEXION,
        socket: socket = None,
    ) -> None:
        self.__socket: socket = socket

        self.__proto: Protocols = protocol
        self.__type: TypesConnecteur = type

    def lier_ip(self, port: int, adresse_ip: str = "", timeout: float = None):
        if self.__socket == None:
            self.__socket = socket(AF_INET, self.__proto)
            if self.__type == TypesConnecteur.ECOUTE:
                self.__socket.bind((adresse_ip, port))
                self.__socket.listen(1)
                self.__socket.settimeout(timeout)

    def attendre_connexion(self, auto_close: bool = True) -> Connecteur or None:
        nouv_connecteur: Connecteur = None
        if self.__type.value:
            connexion, ADDR = self.__socket_ecoute.accept()
            nouv_connecteur = Connecteur(socket=connexion)
            if auto_close:
                self.__socket_ecoute.close()

        return nouv_connecteur
