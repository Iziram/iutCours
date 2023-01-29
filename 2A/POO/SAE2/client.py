"""! @brief Fonctionnement interne du client
 @file client.py
 @section libs Librairies/Modules
  - json
  - socket
  - sys
  - threading
  - pyaudio
  - common
 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 06/12/2022 .
"""
# pylint: disable=function-redefined,broad-except,too-many-ancestors,too-few-public-methods,too-many-arguments,too-many-instance-attributes
from json import dump, load
from socket import timeout
from sys import exit as sysExit
from threading import Thread

import pyaudio as pyaud

from common import CommandInterpreter, Connector, Flag, Function


class Book:
    """!
    @brief Représente un Annuaire
    """

    def __init__(self) -> None:
        self.__names: list[str] = []
        self.__event = None

    def add_name(self, name: str):
        """!
        @brief Permet d'ajouter un nom dans l'annuaire

        Paramètres :
            @param self => l'annuaire
            @param name : str => un nom

        """
        if name not in self.__names:
            self.__names.append(name)
            self.__event(self.__names)

    def get_names(self):
        """!
        @brief Permet d'obtenir la liste des noms

        Paramètres :
            @param self => l'annuaire

        """
        return self.__names

    def remove_name(self, name: str):
        """!
        @brief Permet de retirer un nom de l'annuaire

        Paramètres :
            @param self => l'annuaire
            @param name : str => le nom à retirer

        """
        if name in self.__names:
            self.__names.remove(name)
            self.__event(self.__names)

    def export_file(self, filename):
        """!
        @brief Permet d'exporter l'annuaire dans un fichier python

        Paramètres :
            @param self => l'annuaire
            @param filename => le nom du fichier exporté

        """
        with open(filename, "w", encoding="utf-8") as file:
            dump({"names": self.__names}, file)

    def import_file(self, file):
        """!
        @brief Permet d'importer un annuaire depuis un fichier json

        Paramètres :
            @param self => l'annuaire
            @param file => un fichier json

        """
        json: dict[str, list[str]] = load(file)
        names: list[str] = json.get("names")

        self.__names = names
        self.__event(self.__names)

    def set_event(self, evn: Function):
        """!
        @brief Définit la fonction qui sera exécutée à chaque actualisation

        Paramètres :
            @param self => l'annuaire
            @param evn : Function => la fonction exécutée
        """
        self.__event = evn


class Client(Connector):
    """!
    @brief Représentation interne du client

    ## Héritage :
        - Implémente Connector

    """

    AUDIO = pyaud.PyAudio()
    FORMAT = pyaud.paInt16
    CHANNELS = 1
    FREQUENCE = 8000
    CHUNKS = 512

    def __init__(
        self,
        username: str,
        password: str,
        addr: str = "127.0.0.2",
        port: int = 5000,
        server_ip: str = "127.0.0.1",
        server_port: int = 5000,
    ) -> None:
        Connector.__init__(self)

        self.__username: str = username
        self.__password: str = password

        self.command_channel_bind(addr, port)

        self.audio_in_bind(addr, port + 1)
        self.audio_out_bind(addr, port + 2)
        self.__connected: bool = False
        self.__initial_connected: bool = False

        self.__audio_connected: bool = False

        self.__command_interpreter: CommandInterpreter = self.create_commands_worker()

        self.__stream_out = Client.AUDIO.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.FREQUENCE,
            output=True,
        )

        self.__stream_in = Client.AUDIO.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.FREQUENCE,
            input=True,
            frames_per_buffer=Client.CHUNKS,
        )

        self.__server_ip: str = server_ip
        self.__server_port: int = server_port
        self.__book: Book = Book()

        self.__create: bool = False

    def set_create_client(self, is_creating: bool = False):
        """!
        @brief Définit l'état du client en mode Création (ou non)

        Paramètres :
            @param self => le client
            @param is_creating : bool = False => En mode création (par défaut : non)

        """
        self.__create = is_creating

    def get_book(self):
        """!
        @brief Récupère l'annuaire du client

        Paramètres :
            @param self => le client

        """
        return self.__book

    def create_commands_worker(self):
        """!
        @brief Créer un interpréteur de commande pour le client

        Paramètres :
            @param self => le client

        """

        def ent():
            self.disconnect()

        def lsr(*data):
            print(data)

        def default():
            pass

        def ask(_: str):
            pass

        def sta():

            Thread(target=self.receive_audio, name="audioClientIn").start()

            Thread(target=self.send_audio, name="audioClientOut").start()

        def fin():
            self.__audio_connected = False

        interpreter: CommandInterpreter = CommandInterpreter(
            (Flag.LSR, lsr),
            (Flag.ENT, ent),
            (Flag.ASK, ask),
            (Flag.STA, sta),
            (Flag.FIN, fin),
        )
        interpreter.set_default_command(default)

        return interpreter

    def get_interpreter(self) -> CommandInterpreter:
        """!
        @brief Récupère l'interpréteur de commande du client

        Paramètres :
            @param self => le client
        Retour de la fonction :
            @return CommandInterpreter => l'interpréteur de commande

        """
        return self.__command_interpreter

    def set_audio_connected(self, is_audio_connected: bool):
        """!
        @brief Définit si les canaux audio sont utilisable ou non

        Paramètres :
            @param self => le client
            @param is_audio_connected : bool => Un booléen Vrai si utilisable

        """
        self.__audio_connected = is_audio_connected

    def connect(self, var):
        """!
        @brief Établie la connexion au serveur (et la création du client si Mode création actif)

        Paramètres :
            @param self => le client
            @param var => Variable d'affichage sur l'IHM Client

        """
        try:
            if not self.__initial_connected:
                self.command_connect(self.__server_ip, self.__server_port)
                self.__initial_connected = True

            # Phase de Création

            if self.__create:
                self.send_flag(Flag.CRE, f"{self.__username} {self.__password}")
                ans, ans_data = self.get_flag_data()
                if ans == Flag.REF:
                    var.set(" ".join(ans_data))
                    self.__connected = False
                    self.__create = False
                    return self.__connected

                self.__create = False

            # Phase de connexion

            self.send_flag(Flag.REG)

            ans, ans_data = self.get_flag_data()

            if ans == Flag.VLD:
                self.send_flag(Flag.LOG, self.__username)
                ans, ans_data = self.get_flag_data()
                if ans == Flag.VLD:
                    self.send_flag(Flag.PSS, self.__password)
                    ans, ans_data = self.get_flag_data()
                    if ans == Flag.AUT:
                        self.__connected = True
                        print("connected: ", self.__username)
                        return self.__connected
                    var.set(" ".join(ans_data))
                else:
                    var.set(" ".join(ans_data))
            else:
                var.set(" ".join(ans_data))
            self.__connected = False
            return self.__connected

        except Exception as err:
            print(err)
            self.__connected = False
            var.set("Une erreur s'est passée")
            return self.__connected

    def receive_data(self):
        """!
        @brief Boucle de réception des commandes / exécutions des commandes

        Paramètres :
            @param self => le client

        """
        while self.__connected:
            flag: Flag
            data: list[str]

            flag, data = self.get_flag_data()
            self.__command_interpreter.run_command(flag, *data)

    def disconnect(self):
        """!
        @brief Ferme tous les canaux du client et quitte le programme

        Paramètres :
            @param self => le client

        """
        try:
            self.command_close()
            self.__stream_in.close()
            self.__stream_out.close()
            self.__audio_in_channel.close()
            self.__audio_out_channel.close()
            self.__connected = False
            self.__audio_connected = False

        except Exception:
            self.__connected = False
        sysExit()

    def save_audio(self) -> bytes:
        """!
        @brief Enregistre la voix du client

        Paramètres :
            @param self => le client
        Retour de la fonction :
            @return bytes => les octets de voix

        """
        return self.__stream_in.read(Client.CHUNKS)

    def listen_audio(self, data: bytes):
        """!
        @brief Écoute des octets audio

        Paramètres :
            @param self => le client
            @param data : bytes => des octets audio

        """
        self.__stream_out.write(data)

    def receive_audio(self):
        """!
        @brief Boucle de réception et d'écoute des octets audio

        Paramètres :
            @param self => le client

        """
        self.__audio_connected = True
        while self.__audio_connected:
            try:
                data: bytes = self.audio_in_receive(Client.CHUNKS * 2)[0]
                self.listen_audio(data)
            except timeout:
                pass

    def send_audio(self):
        """!
        @brief Boucle d'enregistrement et d'envoi de la voix cliente

        Paramètres :
            @param self => le client

        """
        while self.__audio_connected:
            data: bytes = self.save_audio()
            self.audio_out_send(data, self.__server_ip, self.__server_port + 1)

    def set_username(self, username: str):
        """!
        @brief Définit le nom d'utilisateur

        Paramètres :
            @param self => le client
            @param username : str => le login du client

        """
        self.__username = username

    def set_password(self, password: str):
        """!
        @brief Définit le mot de passe du client

        Paramètres :
            @param self => le client
            @param password : str => le mot de passe du client

        """
        self.__password = password
