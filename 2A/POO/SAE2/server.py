"""! @brief Représentation interne du serveur
 @file server.py
 @section libs Librairies/Modules
  - socket
  - sys
  - threading
  - time
  - common
  - database
 @section authors Auteur(s)
  - Créé par Matthias HARTMANN le 06/12/2022 .
"""
# pylint: disable=function-redefined,broad-except,too-many-ancestors
#  pylint: disable=too-few-public-methods,too-many-arguments,too-many-instance-attributes,too-many-statements

from socket import socket, timeout
from sys import exit as sysExit
from threading import Thread
from time import sleep, time

from common import CommandInterpreter, Connector, Flag, Logger, seconds_to_clock
from database import Database


class Server(Connector):
    """!
    @brief Représentation interne du serveur

    ## Héritage :
        - Implémente Connector

    """


class ClientServer(Connector, Thread):
    """!
    @brief Représentation d'un client coté serveur,
    Utilise uniquement le coté TCP

    ## Héritage :
        - Implémente Connector
        - Implémente Thread

    """

    def __init__(
        self, command_channel: socket, connection_infos: tuple[str, int]
    ) -> None:
        Connector.__init__(self, command_channel=command_channel)
        Thread.__init__(self)

        self.__status: str = "UNKNOWN"

        self.__username: str = "UNKNOWN"
        self.__interpreter: CommandInterpreter = self.create_commands_worker()
        self.__active: bool = True
        self.__connection_infos: tuple[str, int] = connection_infos

        self.__asked_call: tuple[int, bool] = (None, False)

    def __str__(self) -> str:
        return f"<{self.__username}:{self.__status}>"

    def get_command_interpreter(self):
        """!
        @brief Retourne l'interpréteur de commande

        Paramètres :
            @param self => la représentation du client coté serveur

        """
        return self.__interpreter

    def get_asked_call(self) -> tuple[int, bool]:
        """!
        @brief Retourne la notification d'appel (n°appel, réponse)

        Paramètres :
            @param self => la représentation du client coté serveur
        Retour de la fonction :
            @return tuple[int, bool] => la notification d'appel (n°appel, réponse)

        """
        return self.__asked_call

    def set_asked_call(self, asked_call: int = None, res: bool = False):
        """!
        @brief Définit la notification d'appel

        Paramètres :
            @param self => la représentation du client coté serveur
            @param asked_call : int = None => le numéro d'appel
            @param res : bool = False => la réponse du client

        """
        self.__asked_call = (asked_call, res)

    def get_status(self) -> str:
        """!
        @brief Retourne le statut du client

        Paramètres :
            @param self => la représentation du client coté serveur
        Retour de la fonction :
            @return str => Le statut du client

        """
        return self.__status

    def set_status(self, status: str):
        """!
        @brief Définit le statut du client

        Paramètres :
            @param self => la représentation du client coté serveur
            @param status : str => Le statut

        """
        self.__status = status

    def get_connection_infos(self) -> tuple[str, int]:
        """!
        @brief Retourne les informations du client distant

        Paramètres :
            @param self => la représentation du client coté serveur
        Retour de la fonction :
            @return tuple[str, int] => les informations du client distant (@ip,port)

        """
        return self.__connection_infos

    def run(self):
        while self.__active:
            try:
                flag, data = self.get_flag_data()
                Server.LOG.add(f"{self} ⬅ {flag} {data}")
                self.__interpreter.run_command(flag, *data)
            except Exception:
                pass

    def close(self):
        """!
        @brief Termine la connexion avec le client

        Paramètres :
            @param self => la représentation du client coté serveur

        """
        self.command_close()
        self.__active = False

    def get_username(self):
        """!
        @brief Retourne le nom d'utilisateur du client

        Paramètres :
            @param self => la représentation du client coté serveur

        """
        return self.__username

    def set_username(self, username):
        """!
        @brief Définit le nom d'utilisateur du client

        Paramètres :
            @param self => la représentation du client coté serveur
            @param username => le login du client

        """
        self.__username = username

    def create_commands_worker(self):
        """!
        @brief Créer un interpréteur de commande

        Paramètres :
            @param self => la représentation du client coté serveur

        """

        def lsd():
            self.send_flag(
                Flag.LSR,
                " ".join([c.get_username() for c in Server.CLIENT_DICT.values()]),
            )

        def reg():
            if self.__status == "UNKNOWN":
                self.send_flag(Flag.VLD)
                self.__status = "REGISTERING"
            else:
                self.send_flag(Flag.REF, "DÉJÀ ENREGISTRÉ")

        def log(username):
            if self.__status == "REGISTERING":
                if username not in [
                    c.get_username() for c in Server.CLIENT_DICT.values()
                ]:
                    self.set_username(username)
                    self.send_flag(Flag.VLD)
                else:
                    self.send_flag(Flag.REF, "LE PSEUDO EST DÉJÀ UTILISÉ")
            else:
                self.send_flag(Flag.REF, "NON ENREGISTRÉ")

        def pss(password):
            if self.__status == "REGISTERING":
                bdd: Database = Database("bdd.sqlite")
                bdd.ouverture_bdd()
                if bdd.is_login_valid(self.__username, password):
                    self.__status = "AUTHENTICATED"
                    self.send_flag(Flag.AUT)
                else:
                    self.send_flag(Flag.REF, "MOT DE PASSE INCORRECT")
                    self.set_status("UNKNOWN")
                    self.set_username("UNKNOWN")
                bdd.fermeture_bdd()
            else:
                self.send_flag(Flag.REF, "NON ENREGISTRÉ")

        def cre(username, password):
            bdd: Database = Database("bdd.sqlite")
            bdd.ouverture_bdd()
            if not bdd.is_username_known(username):
                bdd.create_user(username, password)
                Server.LOG.add(f"🖥 Utilisateur créé : {username} {password}")
                self.send_flag(Flag.VLD)
            else:
                self.send_flag(Flag.REF, "USERNAME NON UNIQUE")

        def ent():
            self.send_flag(Flag.ENT)
            self.command_close()
            self.__active = False

            Server.CLIENT_DICT.pop(self.get_connection_infos()[0])

        def res(resp: str):
            resp: bool = bool(int(resp))
            conf_call: ConfCall = Server.CONFCALL_DICT.get(self.get_asked_call()[0])
            self.set_asked_call(conf_call.get_id(), resp)
            conf_call.prepare_client(self)

        def fin():
            if self.get_status().startswith("CALLING:"):
                call_id: int = int(self.get_status().replace("CALLING:", ""))
                conf_call: ConfCall = Server.CONFCALL_DICT.get(call_id)
                conf_call.remove_active_client(self)
                self.send_flag(Flag.FIN)

        def cal(*names):
            if not self.get_status().startswith("CALLING:"):
                clients: list[ClientServer] = [
                    c
                    for c in list(Server.CLIENT_DICT.values())
                    if c.get_username() in names
                ]
                clients.append(self)
                new_call: ConfCall = ConfCall(*clients)
                Server.CONFCALL_DICT[new_call.get_id()] = new_call

                new_call.prepare_conf()

                def launch():
                    sleep(11)
                    new_call.start_call()

                Thread(target=launch, name="startpoint").start()

        def default():
            Server.LOG.add(f"<{self.__username}> ⬅ Flag Invalide")

        interpreter: CommandInterpreter = CommandInterpreter(
            (Flag.ENT, ent),
            (Flag.PSS, pss),
            (Flag.LOG, log),
            (Flag.REG, reg),
            (Flag.RES, res),
            (Flag.CAL, cal),
            (Flag.FIN, fin),
            (Flag.CRE, cre),
            (Flag.LSD, lsd),
        )
        interpreter.set_default_command(default)

        return interpreter


class ConfCall:
    """!
    @brief Représentation interne d'un appel
    """

    NB_CALL = 0
    SERVER: Server = None

    def __init__(self, *clients: ClientServer) -> None:
        self.__clients: tuple[ClientServer] = clients
        self.__active_clients: list[ClientServer] = []
        ConfCall.NB_CALL += 1
        self.__id: int = ConfCall.NB_CALL

        self.__start_time: float = None

    def get_id(self) -> int:
        """!
        @brief Retourne le numéro de l'appel

        Paramètres :
            @param self => la représentation interne d'un appel
        Retour de la fonction :
            @return int => le numéro de l'appel

        """
        return self.__id

    def get_name(self) -> str:
        """!
        @brief Retourne le nom de l'appel

        Paramètres :
            @param self => la représentation interne d'un appel
        Retour de la fonction :
            @return str => Le nom de l'appel

        """
        return ":".join([c.get_username() for c in self.__clients])

    def start_call(self):
        """!
        @brief Lance l'appel

        Paramètres :
            @param self => la représentation interne d'un appel

        """
        if len(self.__active_clients) > 1:
            for cli in self.__active_clients:
                cli.send_flag(Flag.STA)
                cli.set_status(f"CALLING:{self.get_id()}")
            self.__start_time = time()

            Thread(
                target=self.send_period_infos, name=f"periodInfoCall{self.__id}"
            ).start()

    def stop_call(self):
        """!
        @brief Termine l'appel

        Paramètres :
            @param self => la représentation interne d'un appel

        """
        self.__start_time = None
        self.send_all_active_clients(Flag.FIN)
        for cli in self.__active_clients:
            self.remove_active_client(cli)
        Server.CONFCALL_DICT.pop(self.get_id())

    def send_period_infos(self):
        """!
        @brief Envoi périodiquement les informations de l'appel

        Paramètres :
            @param self => la représentation interne d'un appel

        """
        while len(self.__active_clients) > 1:
            try:
                sleep(1)
                elapsed_time: float = time() - self.__start_time
                clients: str = self.get_name().replace(":", ",")
                infos: str = f"time:{seconds_to_clock(elapsed_time)} act:{clients}"
                self.send_all_active_clients(Flag.INF, infos)
            except Exception:
                pass

    def send_all_active_clients(self, flag: Flag, data: str = ""):
        """!
        @brief Envoi un flag à tous les clients connectés à l'appel

        Paramètres :
            @param self => la représentation interne d'un appel
            @param flag : Flag => Le Flag
            @param data : str = "" => Les données du flag

        """
        for cli in self.__active_clients:
            cli.send_flag(flag, data)

    def remove_active_client(self, client: ClientServer):
        """!
        @brief Retire un client actif de l'appel

        Paramètres :
            @param self => la représentation interne d'un appel
            @param client : ClientServer => La représentation du client actif

        """
        if client in self.__active_clients:
            self.__active_clients.remove(client)
            client.set_status("AUTHENTICATED")
            if len(self.__active_clients) < 2 and self.__start_time is not None:
                self.stop_call()

    def prepare_conf(self):
        """!
        @brief Envoie une notification d'appel à tous les clients de l'appel

        Paramètres :
            @param self => la représentation interne d'un appel

        """
        for cli in self.__clients:
            cli.send_flag(Flag.ASK, self.get_name())
            cli.set_asked_call(self.get_id(), Flag.NUL)

    def prepare_client(self, client: ClientServer):
        """!
        @brief Met à jour la liste des clients actifs en fonction de la réponse du client

        Paramètres :
            @param self => la représentation interne d'un appel
            @param client : ClientServer => La représentation du client

        """
        if client in self.__clients:
            if client.get_asked_call()[1]:
                self.__active_clients.append(client)
            client.set_asked_call()

    def redirect_audio_data(self, audio_data: bytes, client_from: ClientServer):
        """!
        @brief Redirige le flux audio en fonction du client source

        Paramètres :
            @param self => la représentation interne d'un appel
            @param audio_data : bytes => flux audio
            @param client_from : ClientServer => client source

        """
        redirected_clients: list[ClientServer] = [
            cli for cli in self.__active_clients if cli != client_from
        ]

        for cli in redirected_clients:
            ConfCall.SERVER.audio_out_send(
                audio_data, cli.get_connection_infos()[0], 5001
            )


class Server(Connector):
    """!
    @brief Représentation interne du serveur

    ## Héritage :
        - Implémente Connector

    """

    CLIENT_DICT: dict[str, ClientServer] = {}
    CONFCALL_DICT: dict[int, ConfCall] = {}

    LOG: Logger = Logger()

    def __init__(self, addr: str = "127.0.0.1", port: int = 5000) -> None:
        self.__addr = addr
        self.__port = port
        self.__active: bool = True

        Connector.__init__(self)

        ConfCall.SERVER = self

        self.__command_interpreter: CommandInterpreter = self.set_command_worker()

    def set_connection_infos(self, addr: str, port: int):
        """!
        @brief Définit l'adresse ip et le port du serveur

        Paramètres :
            @param self => la représentation interne du serveur
            @param addr : str => une adresse ip
            @param port : int => un port

        """
        self.__addr = addr
        self.__port = port

    def start_server(self):
        """!
        @brief Lance le serveur en mode écoute

        Paramètres :
            @param self => la représentation interne du serveur

        """
        self.command_prepare_listening(self.__addr, self.__port, timeout=10)
        self.audio_in_bind(self.__addr, self.__port + 1)
        self.audio_out_bind(self.__addr, self.__port + 2)
        Thread(target=self.redirect_audio, name="audioRedirect").start()

        def start_thread():
            while self.__active:
                try:
                    command_channel, addr = self.command_listen()
                    Server.LOG.add("🖥" + f"Un nouveau client s'est connecté: {addr}")

                    client_server: ClientServer = ClientServer(command_channel, addr)
                    Server.CLIENT_DICT[addr[0]] = client_server
                    client_server.start()
                except timeout:
                    pass
                except TypeError:
                    pass

        Thread(target=start_thread, name="ThreadPrincipal").start()

    def stop_self(self):
        """!
        @brief Stop toutes les connexions clients et ferme l'écoute

        Paramètres :
            @param self => la représentation interne du serveur

        """
        self.__active = False
        for cli in Server.CLIENT_DICT.values():
            cli.close()
        self.command_close()

    def set_command_worker(self):
        """!
        @brief définit l'interpréteur de commande

        Paramètres :
            @param self => la représentation interne du serveur

        """

        def start():
            Server.LOG.add("🖥 Le serveur est en écoute")
            thd: Thread = Thread(name="ServerListen", target=self.start_server)
            thd.start()

            thd2: Thread = Thread(name="ServerList", target=self.send_clients_list)
            thd2.start()

        def stop():
            print("Server stopped listening")
            self.stop_self()

        def lists():
            peers: list[str] = [
                f"{cli.command_peer()[0]}/{cli.get_username()}"
                for cli in Server.CLIENT_DICT.values()
            ]
            if len(peers) > 0:
                Server.LOG.add("🖥 " + " | ".join(peers))
            else:
                Server.LOG.add("🖥 Aucun client connecté")

        def calls():
            confcalls: list[str] = [
                f"{cli.get_name()}[{cli.get_id()}]"
                for cli in Server.CONFCALL_DICT.values()
            ]
            if len(confcalls) > 0:
                Server.LOG.add("🖥 " + " | ".join(confcalls))
            else:
                Server.LOG.add("🖥 Aucun ConfCall en cours")

        def quitting():
            stop()
            sysExit()

        def default():
            Server.LOG.add("🖥 Commande Inconnue")

        interpreter: CommandInterpreter = CommandInterpreter(
            ("start", start),
            ("stop", stop),
            ("list", lists),
            ("quit", quitting),
            ("calls", calls),
        )
        interpreter.set_default_command(default)

        return interpreter

    def get_interpreter(self):
        """!
        @brief Retourne l'interpréteur de commande

        Paramètres :
            @param self => la représentation interne du serveur

        """
        return self.__command_interpreter

    def execute(self, cmd_line):
        """!
        @brief Exécute une ligne de commande (cmd + [...args])

        Paramètres :
            @param self => la représentation interne du serveur
            @param cmd_line => la ligne de commande

        """
        cmds = cmd_line.split(" ")
        self.__command_interpreter.run_command(cmds[0], *cmds[1:])

    def redirect_audio(self):
        """!
        @brief Redirige l'audio envoyé par les clients dans les bons calls

        Paramètres :
            @param self => la représentation interne du serveur

        """
        while self.__active:
            try:
                audio_data_in: bytes
                addr: tuple[str, int]
                audio_data_in, addr = self.audio_in_receive()
                client: ClientServer = Server.CLIENT_DICT.get(addr[0])
                if client is not None:
                    status: str = client.get_status()
                    if status.startswith("CALLING:"):
                        call_id: int = int(status.removeprefix("CALLING:"))
                        call: ConfCall = Server.CONFCALL_DICT[call_id]
                        call.redirect_audio_data(audio_data_in, client)
            except timeout:
                pass

    def send_clients_list(self):
        """!
        @brief Envoie périodiquement la liste des clients aux différents clients

        Paramètres :
            @param self => la représentation interne du serveur

        """
        while self.__active:
            sleep(1)
            try:
                for client in Server.CLIENT_DICT.values():
                    if client.get_status() not in ("UNKNOWN", "REGISTERING"):
                        client.get_command_interpreter().run_command(Flag.LSD)
            except Exception:
                pass
