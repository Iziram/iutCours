from common import Connector, CommandInterpreter, Flag, secondsToClock
from threading import Thread
from socket import socket, timeout
from database import Database
from time import time, sleep


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
            flag, data = self.getFlagData()
            print(f"{self}", flag, data)
            self.__interpreter.run_command(flag, *data)

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
        print("envoi flag:", flag, data)
        if flag_str is not None:
            self.command_send(flag_str.encode("utf-8"))
        else:
            msg: str = flag.value
            if data != "":
                msg += " " + data
            self.command_send(msg.encode("utf-8"))

    def get_commands_worker(self):
        def tim():
            self.sendFlag(Flag.TIM)

        def reg():
            if self.__status == "UNKNOWN":
                self.sendFlag(Flag.VLD)
                self.__status = "REGISTERING"
            else:
                self.sendFlag(Flag.REF, "ALREADY REGISTERED")

        def log(username):
            if self.__status == "REGISTERING":
                if username not in [
                    c.getUserName() for c in Server.CLIENT_DICT.values()
                ]:
                    self.setUserName(username)
                    self.sendFlag(Flag.VLD)
                else:
                    self.sendFlag(Flag.REF, "username already taken")
            else:
                self.sendFlag(Flag.REF, "NOT REGISTERING")

        def pss(password):
            if self.__status == "REGISTERING":
                db: Database = Database("bdd.sqlite")
                db.ouverture_BDD()
                if db.isLoginValid(self.__username, password):
                    self.__status = "AUTHENTICATED"
                    self.sendFlag(Flag.AUT)
                else:
                    self.sendFlag(Flag.REF, "password invalid")
                db.fermeture_BDD()
            else:
                self.sendFlag(Flag.REF, "NOT REGISTERING")

        def ent():
            self.sendFlag(Flag.ENT)
            self.command_close()
            self.__active = False

            Server.CLIENT_DICT.pop(self.getConnectionInfos())

        def res(b: str):
            b: bool = bool(int(b))
            conf_call: ConfCall = Server.CONFCALL_DICT.get(self.getAskedCall()[0])
            self.setAskedCall(conf_call.getId(), b)
            conf_call.prepareClient(self)

        def fin():
            call_id: int = int(self.getStatus().replace("CALLING:", ""))
            conf_call: ConfCall = Server.CONFCALL_DICT.get(call_id)
            conf_call.removeActiveClient(self)

        def lsd():
            self.sendFlag(
                Flag.LSR,
                " ".join([c.getUserName() for c in Server.CLIENT_DICT.values()]),
            )

        def cal(*names):
            if not self.getStatus().startswith("CALL"):
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
                    sleep(15)
                    new_call.startCall()

                Thread(target=launch, name="startpoint").start()

        def default():
            print(f"<{self.__username}> Invalid Command")

        interpreter: CommandInterpreter = CommandInterpreter(
            (Flag.TIM, tim),
            (Flag.LSD, lsd),
            (Flag.ENT, ent),
            (Flag.PSS, pss),
            (Flag.LOG, log),
            (Flag.REG, reg),
            (Flag.RES, res),
            (Flag.CAL, cal),
            (Flag.FIN, fin),
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
        print("debug: ", "starting call", len(self.__active_clients))
        if len(self.__active_clients) > 1:
            for cli in self.__active_clients:
                cli.sendFlag(Flag.STA)
                cli.setStatus(f"CALLING:{self.getId()}")
            self.__start_time = time()

            # Thread(
            #     target=self.sendPeriodInfos, name=f"periodInfoCall{self.__id}"
            # ).start()

    def joinCall(self, client: ClientServer):
        if client in self.__clients:
            client.sendFlag(Flag.STA)
            client.setStatus(f"CALLING:{self.getId()}")

    def sendPeriodInfos(self):
        while len(self.__active_clients) > 1:
            sleep(1)
            elapsed_time: float = time() - self.__start_time
            clients: str = self.getName().replace(":", ",")
            infos: str = f"time:{secondsToClock(elapsed_time)} act:{clients}"
            self.sendAllActiveClients(Flag.INF, infos)

    def sendAllActiveClients(self, flag: Flag, data: str = ""):
        for cli in self.__active_clients:
            cli.sendFlag(flag, data)

    def removeActiveClient(self, client: ClientServer):
        if client in self.__active_clients:
            self.__active_clients.remove(client)

    def prepareConf(self):
        for c in self.__clients:
            c.sendFlag(Flag.ASK, self.getName())
            c.setAskedCall(self.getId(), Flag.NUL)

    def prepareClient(self, client: ClientServer):
        print("debug: prepareclient: ", client.getUserName())
        if client in self.__clients:
            if client.getAskedCall()[1]:
                self.__active_clients.append(client)
            client.setAskedCall()

    def redirectAudioData(self, audioData: bytes, clientfrom: ClientServer):

        redirected_clients: list[ClientServer] = [
            c for c in self.__active_clients if c != clientfrom
        ]

        for c in redirected_clients:
            ConfCall.SERVER.audio_out_send(audioData, *c.getConnectionInfos())


class Server(Connector, Thread):
    CLIENT_DICT: dict[tuple[str, int], ClientServer] = {}
    CONFCALL_DICT: dict[int, ConfCall] = {}

    def __init__(self, addr: str = "127.0.0.1", port: int = 5000) -> None:
        self.__addr = addr
        self.__port = port
        self.__active: bool = True

        Connector.__init__(self)
        Thread.__init__(self, name="ThreadPrincipServer")

        self.audio_in_bind(self.__addr, self.__port + 1)
        self.audio_out_bind(self.__addr, self.__port + 2)

        ConfCall.SERVER = self

        self.__command_interpreter: CommandInterpreter = self.get_commands_worker()

    def start_self(self):
        self.command_prepare_listening(self.__addr, self.__port, timeout=10)
        while self.__active:
            try:
                command_channel, addr = self.command_listen()
                client_server: ClientServer = ClientServer(command_channel, addr)
                Server.CLIENT_DICT[addr] = client_server

                client_server.start()
            except timeout:
                pass
            except TypeError:
                pass

    def stop_self(self):
        self.__active = False
        for c in Server.CLIENT_DICT.values():
            c.close()
        self.command_close()

    def get_commands_worker(self):
        def start():
            print("Server started listening")
            th: Thread = Thread(name="ServerListen", target=self.start_self)
            th.start()

        def stop():
            print("Server stopped listening")
            self.stop_self()

        def list():
            peers: list[str] = [
                f"{c.command_peer()}" for c in Server.CLIENT_DICT.values()
            ]
            print(peers)

        def quit():
            stop()

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
            print("Invalid Command")

        interpreter: CommandInterpreter = CommandInterpreter(
            ("start", start),
            ("stop", stop),
            ("list", list),
            ("quit", quit),
            ("disconnect", disconnect),
        )
        interpreter.set_default_command(default)

        return interpreter

    def run(self):
        cmd: str = " "
        while cmd != "quit":
            cmds = input("£ ").split(" ")
            cmd = cmds[0]
            self.__command_interpreter.run_command(cmd, *cmds[1:])

    def getAudioRedirect(self):
        while self.__active:
            audioDataIn: bytes
            addr: tuple[str, int]
            audioDataIn, addr = self.audio_in_receive()
            client: ClientServer = Server.CLIENT_DICT.get(addr, None)
            print("debug datain audio:", audioDataIn)
            if client is not None:
                status: str = client.getStatus()
                if status.startswith("CALL:"):
                    call_id: int = int(status.removeprefix("CALL:"))
                    call: ConfCall = Server.CONFCALL_DICT[call_id]
                    call.redirectAudioData(audioDataIn, client)


if __name__ == "__main__":
    server: Server = Server()

    server.start()
