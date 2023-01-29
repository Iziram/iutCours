"""! @brief Elements communs au serveur et au client
 @file common.py
 @section libs Librairies/Modules
  - enum
  - socket
  - tkinter
 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 04/12/2022 .
"""
from enum import Enum
from socket import AF_INET, MSG_PEEK, SOCK_DGRAM, SOCK_STREAM, socket
from tkinter import END, Text

# pylint: disable=function-redefined,broad-except,too-many-ancestors,too-few-public-methods


class Flag(str, Enum):
    """!
    @brief Enum des Flags attribué au protocol client/server
    ## Héritage :
        - Implémente Enum
        - Implémente str
    """


class Flag(str, Enum):
    """!
    @brief Enum des Flags attribué au protocol client/server
    ## Héritage :
        - Implémente Enum
        - Implémente str
    """

    # signing
    REG = "reg"  # Starts the signing exchange
    LOG = "log"  # Sends the username "log <username>"
    PSS = "pss"  # Sends the password "pss <password>"
    AUT = "aut"  # Client is authenticated
    CRE = "cre"  # Create a user with "cre <username> <password>"
    # Quality control
    VLD = "vld"  # Valid
    REF = "ref"  # Refused "ref [why]"
    ENT = "ent"  # End TCP connection
    NUL = "nul"  # Null flag
    # Commands
    LSR = "lsr"  # Answers with clients list "lsr <username> <username> ..."
    LSD = "lsd"  # Demands clients list "lsd <username> <username> ..."

    CAL = "cal"  # Demands to call client "cal <username> [usernames...]"
    ASK = "ask"  # ask a client if he wants to answer the call "ask <callName>"
    RES = "res"  # response to ASK flag "res <bool:1|0>"
    STA = "sta"  # Start the call
    INF = "inf"  # general info of call "info time:00h00m00s act:usr1,usr2,usr3,..."
    FIN = "fin"  # Close current call

    @staticmethod
    def get_flag_from_str(str_flag: str) -> Flag:
        """!
        @brief récupère un Flag à partir d'un string

        Paramètres :
            @param str_flag : str => un string contenant ou non un Flag
        Retour de la fonction :
            @return Flag => le Flag contenu ou Flag.NUL

        """
        flag: Flag
        try:
            flag = Flag[str_flag.upper()]
        except KeyError:
            flag = Flag.NUL
        return flag


class Connector:
    """!
    @brief Connecteur gérant les sockets (tcp/udp)
    """


class Connector:
    """!
    @brief Connecteur gérant les sockets (tcp/udp)
    """

    def __init__(
        self,
        command_channel: socket = None,
        audio_in_channel: socket = None,
        audio_out_channel: socket = None,
    ) -> None:

        self.__command_channel: socket = (
            command_channel
            if command_channel is not None
            else socket(AF_INET, SOCK_STREAM)
        )
        self.__audio_in_channel: socket = (
            audio_in_channel
            if audio_in_channel is not None
            else socket(AF_INET, SOCK_DGRAM)
        )
        self.__audio_out_channel: socket = (
            audio_out_channel
            if audio_out_channel is not None
            else socket(AF_INET, SOCK_DGRAM)
        )

        self.__audio_in_channel.settimeout(4.0)

    def command_channel_bind(self, addr: str, port: int):
        """!
        @brief Permet de fixer une adresse ip et un port au channel de commande (tcp)

        Paramètres :
            @param self => Le connecteur
            @param addr : str => une adresse ip
            @param port : int => un port

        """
        self.__command_channel.bind((addr, port))

    def command_send(self, data: bytes):
        """!
        @brief Permet d'envoyer des octets sur le channel de commandes (tcp)

        Paramètres :
            @param self => Le connecteur
            @param data : bytes => les octets à envoyer

        """
        if not self.is_command_closed():
            self.__command_channel.sendall(data)

    def command_receive(self) -> bytes:
        """!
        @brief Permet de recevoir des octets sur le channel de commandes

        Paramètres :
            @param self => Le connecteur
        Retour de la fonction :
            @return bytes => les octets reçus

        """
        data: bytes = None
        if not self.is_command_closed():
            data = self.__command_channel.recv(255)
        return data

    def command_close(self):
        """!
        @brief Permet de fermer le channel de commandes

        Paramètres :
            @param self => Le connecteur

        """
        self.__command_channel.close()

    def command_prepare_listening(self, addr: str, port: int, timeout: int = None):
        """!
        @brief Permet de mettre en mode écoute un channel tcp (commandes)

        Paramètres :
            @param self => Le connecteur
            @param addr : str => l'adresse qui sera utilisée
            @param port : int => le port d'écoute
            @param timeout : int = None => Un délai d'expiration si donné

        """
        self.__command_channel.bind((addr, port))
        self.__command_channel.listen(1)
        if timeout is not None:
            self.__command_channel.settimeout(timeout)

    def command_listen(self) -> tuple[socket, tuple[str, int]]:
        """!
        @brief Permet d'attendre une connection sur le channel qui écoute (tcp)

        Paramètres :
            @param self => Le connecteur
        Retour de la fonction :
            @return tuple[socket, tuple[str, int]] => socket serveur + addr client

        """
        connection: tuple[socket, tuple[str, int]] = None
        try:
            connection = self.__command_channel.accept()
        except OSError:
            if not self.is_command_closed:
                self.command_close()
        return connection

    def command_connect(self, addr: str, port: int):
        """!
        @brief Permet de connecter le channel de commandes à une adresse distante

        Paramètres :
            @param self => Le connecteur
            @param addr : str => l'adresse ip distante
            @param port : int => le port distant

        """
        self.__command_channel.connect((addr, port))

    def is_command_closed(self) -> bool:
        """!
        @brief Vérifie si le channel de commandes est fermé ou non

        Paramètres :
            @param self => Le connecteur
        Retour de la fonction :
            @return bool => Vrai si le channel est fermé, faux sinon

        """
        is_closed: bool = False
        try:
            # On essaye de lire les octets sans bloquer le channel
            # et sans retirer les octets du buffer
            self.__command_channel.setblocking(False)
            data = self.__command_channel.recv(16, MSG_PEEK)
            if len(data) == 0:
                is_closed = True
        except BlockingIOError:
            # Le channel est ouvert et lire le bloquerai
            is_closed = False
        except ConnectionResetError:
            # Le channel est fermée pour une autre raison
            is_closed = True
        except Exception:
            # Le channel est fermée pour une autre raison
            is_closed = True
        finally:
            try:
                self.__command_channel.setblocking(True)
            except Exception:
                # Le channel est fermée pour une autre raison
                is_closed = True
        return is_closed

    def command_peer(self) -> tuple[str, int]:
        """!
        @brief Permet d'obtenir les informations du client distant

        Paramètres :
            @param self => Le connecteur
        Retour de la fonction :
            @return tuple[str, int] => @ip + port client distant

        """
        return self.__command_channel.getpeername()

    def send_flag(self, flag: Flag = None, data: str = "", flag_str: str = None):
        """!
        @brief Envoi un flag et ses données sur le channel de commande

        Paramètres :
            @param self => le client
            @param flag : Flag = None => Un Flag
            @param data : str = "" => les données du flag
            @param flag_str : str = None => la représentation string du flag + data

        """
        if flag_str is not None:
            self.command_send(flag_str.encode("utf-8"))
        else:
            msg: str = flag.value
            if data != "":
                msg += " " + data
            self.command_send(msg.encode("utf-8"))

    def get_flag_data(self) -> tuple[Flag, list[str]]:
        """!
        @brief Réception et conversion d'un msg (octets) en un Flag + Data

        Paramètres :
            @param self => le client
        Retour de la fonction :
            @return tuple[Flag, list[str]] => (Flag, data)

        """
        try:
            msg = self.command_receive().decode("utf-8").split(" ")
            flag: Flag = Flag.get_flag_from_str(msg[0])
            data: list[str] = msg[1:]
            return (flag, data)
        except Exception:
            return None

    def audio_in_bind(self, addr: str, port: int):
        """!
        @brief Permet de fixer une adresse ip et un port sur le channel d'écoute audio (udp)

        Paramètres :
            @param self => Le connecteur
            @param addr : str => une adresse ip
            @param port : int => un port

        """
        self.__audio_in_channel.bind((addr, port))

    def audio_in_receive(self, buffer: int = 2048) -> tuple[bytes, tuple[str, int]]:
        """!
        @brief Permet de recevoir des octets sur le channel d'écoute audio (udp)

        Paramètres :
            @param self => Le connecteur
            @param buffer : int = 2048 => le tampon mémoire nécessaire à l'écoute
        Retour de la fonction :
            @return tuple[bytes, tuple[str, int]] => les octets + (@ip, port) source

        """
        return self.__audio_in_channel.recvfrom(buffer)

    def audio_out_bind(self, addr: str, port: int):
        """!
        @brief Permet de fixer une adresse ip et un port au channel d'envoi audio

        Paramètres :
            @param self => Le connecteur
            @param addr : str => une adresse ip
            @param port : int => un port

        """
        self.__audio_out_channel.bind((addr, port))

    def audio_out_send(self, data: bytes, addr: str, port: int):
        """!
        @brief Permet d'envoyer des octets sur le channel d'envoi audio

        Paramètres :
            @param self => Le connecteur
            @param data : bytes => les octets à envoyer
            @param addr : str => une adresse ip
            @param port : int => un port

        """
        self.__audio_out_channel.sendto(data, (addr, port))


class Function:
    """!
    @brief Décrit une fonction [Uniquement pour le typage]
    """


class CommandInterpreter:
    """!
    @brief Classe mettant en place un switch
      pour executer des fonctions à partir d'un
      identifier


    """

    def __init__(self, *functions: tuple[object, Function]) -> None:
        self.__switch: dict[object, Function] = {}
        for kwd, func in functions:
            self.__switch[kwd] = func

    def get_switch(self) -> dict[object, Function]:
        """!
        @brief Retourne le switch (un dictionnaire python)
          utilisé par l'interpréteur

        Paramètres :
            @param self => l'interpréteur
        Retour de la fonction :
            @return dict[object, Function] => le Switch (dictionnaire python)

        """
        return self.__switch

    def run_command(self, identifier: object, *data: tuple[object]):
        """!
        @brief Execute une commande en fonction de l'identifier et des données

        Paramètres :
            @param self => l'interpréteur
            @param identifier : object => l'identifiant dans le switch
            @param *data : tuple[object] => les données utiles à la fonction

        """
        if identifier in self.__switch:
            self.__switch[identifier](*data)
        else:
            self.__switch["__default__"]()

    def set_default_command(self, func: Function):
        """!
        @brief Définit la fonction exécuté quand l'identifier n'est pas connu

        Paramètres :
            @param self => l'interpréteur
            @param func : Function => la fonction par défaut

        """
        self.__switch["__default__"] = func

    def set_command(self, identifier: object, func: Function):
        """!
        @brief Définit une commande à partir d'un identifier et d'une fonction

        Paramètres :
            @param self => l'interpréteur
            @param identifier : object => l'identifier à utiliser
            @param func : Function => la fonction qui sera appliquée

        """
        self.__switch[identifier] = func


class TextWithVar(Text):
    """A text widget that accepts a 'textvariable' option"""

    def __init__(self, parent, *args, **kwargs):
        try:
            self.__textvariable = kwargs.pop("textvariable")
        except KeyError:
            self.__textvariable = None

        Text.__init__(self, parent, *args, **kwargs)

        # if the variable has data in it, use it to initialize
        # the widget
        if self.__textvariable is not None:
            self.insert("1.0", self.__textvariable.get())

        # this defines an internal proxy which generates a
        # virtual event whenever text is inserted or deleted
        self.tk.eval(
            """
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                # return the result from the real widget command
                return $result
            }
            """
        )

        # this replaces the underlying widget with the proxy
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        """.format(
                widget=str(self)
            )
        )

        # set up a binding to update the variable whenever
        # the widget changes
        self.bind("<<Change>>", self._on_widget_change)

        # set up a trace to update the text widget when the
        # variable changes
        if self.__textvariable is not None:
            self.__textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *_):
        """Change the text widget when the associated textvariable changes"""

        # only change the widget if something actually
        # changed, otherwise we'll get into an endless
        # loop
        try:
            text_current = self.get("1.0", "end-1c")
            var_current = self.__textvariable.get()
            if text_current != var_current:
                self.delete("1.0", "end")
                self.insert("1.0", var_current)
                self.see(END)
        except Exception:
            pass

    def _on_widget_change(self, _=None):
        """Change the variable when the widget changes"""
        try:
            if self.__textvariable is not None:
                self.__textvariable.set(self.get("1.0", "end-1c"))
                self.see(END)
        except Exception:
            pass


class Logger:
    """!
    @brief Classe définissant un outil de logging
    """

    def __init__(self) -> None:
        self.__logs: list[str] = []
        self.__event: Function = None

    def add(self, msg: str):
        """!
        @brief Permet d'ajouter une ligne au logger

        Paramètres :
            @param self => le logger
            @param msg : str => la ligne à ajouter

        """
        self.__logs.append(msg)
        self.__event("\n".join(self.__logs))

    def remove(self, msg: str):
        """!
        @brief Permet de retirer une ligne du logger

        Paramètres :
            @param self => le logger
            @param msg : str => la ligne à retirer

        """
        if msg in self.__logs:
            self.__logs.remove(msg)
            self.__event(self.__logs)

    def set_event(self, func: Function):
        """!
        @brief Définit une fonction qui sera exécuté à chaque actualisation
          du logger

        Paramètres :
            @param self => le logger
            @param func : Function => La fonction à executer

        """
        self.__event = func


def seconds_to_clock(secs) -> str:
    """!
    @brief Transforme un temps en secondes
      En un temps `HH:MM:SS`

    Paramètres :
        @param secs => le temps en secondes

    Retour de la fonction :
        @return str => la représentation du temps

    """

    secs: int = int(secs)
    hours: int = secs // 3600
    secs %= 3600
    minutes: int = secs // 60
    secs %= 60

    if hours < 10:
        hours: str = f"0{hours}"
    if minutes < 10:
        minutes: str = f"0{minutes}"
    if secs < 10:
        secs: str = f"0{secs}"

    return f"{hours}h{minutes}m{secs}s"
