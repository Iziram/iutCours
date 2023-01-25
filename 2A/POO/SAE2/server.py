from common import Connector, CommandInterpreter, Flag, secondsToClock, Logger
from threading import Thread
from socket import socket, timeout
from database import Database
from time import time, sleep
from sys import exit as sysExit


class Server(Connector):
    pass


class ClientServer(Connector, Thread):
    """
    Représentation d'un client coté serveur,
    Utilise uniquement le coté TCP
    """

    def __init__(
        self, command_channel: socket, connection_infos: tuple[str, int]
    ) -> None:
        Connector.__init__(self, command_channel=command_channel)
        Thread.__init__(self)

        self.__status: str = "UNKNOWN"

        self.__username: str = "UNKNOWN"
        self.__interpreter: CommandInterpreter = self.get_commands_worker()
        self.__active: bool = True
        self.__connection_infos: tuple[str, int] = connection_infos

        self.__asked_call: tuple[int, bool] = (None, False)

    def __str__(self) -> str:
        return f"<{self.__username}:{self.__status}>"

    def getInterpreter(self):
        return self.__interpreter

    def getAskedCall(self) -> tuple[int, bool]:
        return self.__asked_call

    def setAskedCall(self, asked_call: int = None, res: bool = False):
        self.__asked_call = (asked_call, res)

    def getStatus(self) -> str:
        return self.__status

    def setStatus(self, status: str):
        self.__status = status

    def getConnectionInfos(self) -> tuple[str, int]:
        return self.__connection_infos

    def run(self):
        while self.__active:
            try:
                flag, data = self.getFlagData()
                Server.LOG.add(f"{self} ⬅ {flag} {data}")
                self.__interpreter.run_command(flag, *data)
            except:
                pass

    def close(self):
        self.command_close()
        self.__active = False

    def getUserName(self):
        return self.__username

    def setUserName(self, username):
        self.__username = username

    def getFlagData(self) -> tuple[Flag, list[str]]:
        msg = self.command_receive().decode("utf-8").split(" ")
        flag: Flag = Flag.getFlagFromStr(msg[0])
        data: list[str] = msg[1:]
        return (flag, data)

    def sendFlag(self, flag: Flag = None, data: str = "", flag_str: str = None):
        if flag_str is not None:
            self.command_send(flag_str.encode("utf-8"))
        else:

            if flag not in (Flag.LSR, Flag.INF):
                Server.LOG.add(f"{self.__username} ➡ {flag} {data}")

            msg: str = flag.value
            if data != "":
                msg += " " + data
            self.command_send(msg.encode("utf-8"))

    def get_commands_worker(self):
        def reg():
            if self.__status == "UNKNOWN":
                self.sendFlag(Flag.VLD)
                self.__status = "REGISTERING"
            else:
                self.sendFlag(Flag.REF, "DÉJA ENREGISTRÉ")

        def log(username):
            if self.__status == "REGISTERING":
                if username not in [
                    c.getUserName() for c in Server.CLIENT_DICT.values()
                ]:
                    self.setUserName(username)
                    self.sendFlag(Flag.VLD)
                else:
                    self.sendFlag(Flag.REF, "LE PSEUDO EST DÉJÀ UTILISÉ")
            else:
                self.sendFlag(Flag.REF, "NON ENREGISTRÉ")

        def pss(password):
            if self.__status == "REGISTERING":
                db: Database = Database("bdd.sqlite")
                db.ouverture_BDD()
                if db.isLoginValid(self.__username, password):
                    self.__status = "AUTHENTICATED"
                    self.sendFlag(Flag.AUT)
                else:
                    self.sendFlag(Flag.REF, "MOT DE PASSE INCORRECT")
                    self.setStatus("UNKNOWN")
                    self.setUserName("UNKNOWN")
                db.fermeture_BDD()
            else:
                self.sendFlag(Flag.REF, "NON ENREGISTRÉ")

        def cre(username, password):
            db: Database = Database("bdd.sqlite")
            db.ouverture_BDD()
            if not db.isUsernameKnown(username):
                db.createUser(username, password)
                Server.LOG.add(f"🖥 Utilisateur créé : {username} {password}")
                self.sendFlag(Flag.VLD)
            else:
                self.sendFlag(Flag.REF, "USERNAME NON UNIQUE")

        def ent():
            self.sendFlag(Flag.ENT)
            self.command_close()
            self.__active = False

            Server.CLIENT_DICT.pop(self.getConnectionInfos()[0])

        def res(b: str):
            b: bool = bool(int(b))
            conf_call: ConfCall = Server.CONFCALL_DICT.get(self.getAskedCall()[0])
            self.setAskedCall(conf_call.getId(), b)
            conf_call.prepareClient(self)

        def fin():
            if self.getStatus().startswith("CALLING:"):
                call_id: int = int(self.getStatus().replace("CALLING:", ""))
                conf_call: ConfCall = Server.CONFCALL_DICT.get(call_id)
                conf_call.removeActiveClient(self)
                self.sendFlag(Flag.FIN)

        def cal(*names):
            if not self.getStatus().startswith("CALLING:"):
                clients: list[ClientServer] = [
                    c
                    for c in list(Server.CLIENT_DICT.values())
                    if c.getUserName() in names
                ]
                clients.append(self)
                new_call: ConfCall = ConfCall(*clients)
                Server.CONFCALL_DICT[new_call.getId()] = new_call

                # self.setAskedCall(new_call.getId(), True)
                # new_call.prepareClient(self)

                new_call.prepareConf()

                def launch():
                    sleep(11)
                    new_call.startCall()

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
        )
        interpreter.set_default_command(default)

        return interpreter


class ConfCall:
    NB_CALL = 0
    SERVER: Server = None

    def __init__(self, *clients: ClientServer) -> None:
        self.__clients: tuple[ClientServer] = clients
        self.__active_clients: list[ClientServer] = []
        ConfCall.NB_CALL += 1
        self.__id: int = ConfCall.NB_CALL

        self.__start_time: float = None

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return ":".join([c.getUserName() for c in self.__clients])

    def startCall(self):
        if len(self.__active_clients) > 1:
            for cli in self.__active_clients:
                cli.sendFlag(Flag.STA)
                cli.setStatus(f"CALLING:{self.getId()}")
            self.__start_time = time()

            Thread(
                target=self.sendPeriodInfos, name=f"periodInfoCall{self.__id}"
            ).start()

    def stopCall(self):
        self.__start_time = None
        self.sendAllActiveClients(Flag.FIN)
        for c in self.__active_clients:
            self.removeActiveClient(c)
        Server.CONFCALL_DICT.pop(self.getId())

    def joinCall(self, client: ClientServer):
        if client in self.__clients:
            client.sendFlag(Flag.STA)
            client.setStatus(f"CALLING:{self.getId()}")

    def sendPeriodInfos(self):
        while len(self.__active_clients) > 1:
            try:
                sleep(1)
                elapsed_time: float = time() - self.__start_time
                clients: str = self.getName().replace(":", ",")
                infos: str = f"time:{secondsToClock(elapsed_time)} act:{clients}"
                self.sendAllActiveClients(Flag.INF, infos)
            except:
                pass

    def sendAllActiveClients(self, flag: Flag, data: str = ""):
        for cli in self.__active_clients:
            cli.sendFlag(flag, data)

    def removeActiveClient(self, client: ClientServer):
        if client in self.__active_clients:
            self.__active_clients.remove(client)
            client.setStatus("AUTHENTICATED")
            if len(self.__active_clients) < 2 and self.__start_time is not None:
                self.stopCall()

    def prepareConf(self):
        for c in self.__clients:
            c.sendFlag(Flag.ASK, self.getName())
            c.setAskedCall(self.getId(), Flag.NUL)

    def prepareClient(self, client: ClientServer):
        if client in self.__clients:
            if client.getAskedCall()[1]:
                self.__active_clients.append(client)
            client.setAskedCall()

    def redirectAudioData(self, audioData: bytes, clientfrom: ClientServer):
        redirected_clients: list[ClientServer] = [
            c for c in self.__active_clients if c != clientfrom
        ]

        for c in redirected_clients:
            ConfCall.SERVER.audio_out_send(audioData, c.getConnectionInfos()[0], 5001)


class Server(Connector):
    CLIENT_DICT: dict[str, ClientServer] = {}
    CONFCALL_DICT: dict[int, ConfCall] = {}

    LOG: Logger = Logger()

    def __init__(self, addr: str = "127.0.0.1", port: int = 5000) -> None:
        self.__addr = addr
        self.__port = port
        self.__active: bool = True

        Connector.__init__(self)

        ConfCall.SERVER = self

        self.__command_interpreter: CommandInterpreter = self.get_commands_worker()

    def setter(self, addr: str, port: int):
        self.__addr = addr
        self.__port = port

    def start_self(self):
        self.command_prepare_listening(self.__addr, self.__port, timeout=10)
        self.audio_in_bind(self.__addr, self.__port + 1)
        self.audio_out_bind(self.__addr, self.__port + 2)
        Thread(target=self.getAudioRedirect, name="audioRedirect").start()

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
        self.__active = False
        for c in Server.CLIENT_DICT.values():
            c.close()
        self.command_close()

    def get_commands_worker(self):
        def start():
            Server.LOG.add("🖥 Le serveur est en écoute")
            th: Thread = Thread(name="ServerListen", target=self.start_self)
            th.start()

            th2: Thread = Thread(name="ServerList", target=self.sendClientsList)
            th2.start()

        def stop():
            print("Server stopped listening")
            self.stop_self()

        def list():
            peers: list[str] = [
                f"{c.command_peer()[0]}/{c.getUserName()}"
                for c in Server.CLIENT_DICT.values()
            ]
            if len(peers) > 0:
                Server.LOG.add("🖥 " + " | ".join(peers))
            else:
                Server.LOG.add("🖥 Aucun client connecté")

        def quit():
            stop()
            sysExit()

        def disconnect(peer: str):
            if peer == "all":
                for c in Server.CLIENT_DICT.values():
                    c.command_close()
                Server.CLIENT_DICT.clear()
            else:
                client: ClientServer = [
                    c
                    for c in Server.CLIENT_DICT.values()
                    if c.command_peer()[1] == int(peer)
                ]
                client.command_close()
                Server.CLIENT_DICT.pop(client.getConnectionInfos())

        def default():
            Server.LOG.add("🖥 Commande Inconnue")

        interpreter: CommandInterpreter = CommandInterpreter(
            ("start", start),
            ("stop", stop),
            ("list", list),
            ("quit", quit),
            ("disconnect", disconnect),
        )
        interpreter.set_default_command(default)

        return interpreter

    def getInterpreter(self):
        return self.__command_interpreter

    def execute(self, cmd_line):
        cmds = cmd_line.split(" ")
        self.__command_interpreter.run_command(cmds[0], *cmds[1:])

    def getAudioRedirect(self):
        while self.__active:
            try:
                audioDataIn: bytes
                addr: tuple[str, int]
                audioDataIn, addr = self.audio_in_receive()
                client: ClientServer = Server.CLIENT_DICT.get(addr[0])
                if client is not None:
                    status: str = client.getStatus()
                    if status.startswith("CALLING:"):
                        call_id: int = int(status.removeprefix("CALLING:"))
                        call: ConfCall = Server.CONFCALL_DICT[call_id]
                        call.redirectAudioData(audioDataIn, client)
            except timeout:
                pass

    def sendClientsList(self):
        while self.__active:
            sleep(1)
            try:
                for client in Server.CLIENT_DICT.values():
                    if client.getStatus() not in ("UNKNOWN", "REGISTERING"):
                        client.getInterpreter().run_command(Flag.LSD)
            except:
                pass
