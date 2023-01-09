from common import Connector, CommandInterpreter, Flag
from threading import Thread
from socket import socket, timeout
from database import Database


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

    def __str__(self) -> str:
        return f"<{self.__username}:{self.__status}>"

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
                if username not in [c.getUserName() for c in Server.CLIENT_LIST]:
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

            Server.CLIENT_LIST.remove(self)

        def lsd():
            self.sendFlag(
                Flag.LSR, " ".join([c.getUserName() for c in Server.CLIENT_LIST])
            )

        def default():
            print(f"<{self.__username}> Invalid Command")

        interpreter: CommandInterpreter = CommandInterpreter(
            (Flag.TIM, tim),
            (Flag.LSD, lsd),
            (Flag.ENT, ent),
            (Flag.PSS, pss),
            (Flag.LOG, log),
            (Flag.REG, reg),
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

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return ":".join([c.getUserName() for c in self.__clients])

    def prepareConf(self):
        for c in self.__clients:
            if c.getStatus() == "AUTHENTICATED":
                self.__active_clients.append(c)
                c.setStatus(f"CALL:{self.__id}")
            else:
                c.sendFlag(Flag.ASK, self.getName())

    def redirectAudioData(self, audioData: bytes, clientfrom: ClientServer):

        redirected_clients: list[ClientServer] = [
            c for c in self.__active_clients if c != clientfrom
        ]

        for c in redirected_clients:
            ConfCall.SERVER.audio_out_send(audioData, *c.getConnectionInfos())


class Server(Connector, Thread):
    CLIENT_LIST: dict[tuple[str, int], ClientServer] = {}
    CONFCALL_LIST: dict[int, ConfCall] = {}

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
                Server.CLIENT_LIST[addr](client_server)

                client_server.start()
            except timeout:
                pass
            except TypeError:
                pass

    def stop_self(self):
        self.__active = False
        for c in Server.CLIENT_LIST.values():
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
                f"{c.command_peer()}" for c in Server.CLIENT_LIST.values()
            ]
            print(peers)

        def quit():
            stop()

        def disconnect(peer: str):
            if peer == "all":
                for c in Server.CLIENT_LIST.values():
                    c.command_close()
                Server.CLIENT_LIST.clear()
            else:
                client: ClientServer = [
                    c
                    for c in Server.CLIENT_LIST.values()
                    if c.command_peer()[1] == int(peer)
                ]
                client.command_close()
                Server.CLIENT_LIST.pop(client.getConnectionInfos())

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
            client: ClientServer = Server.CLIENT_LIST.get(addr, None)
            if client is not None:
                status: str = client.getStatus()
                if status.startswith("CALL:"):
                    call_id: int = int(status.removeprefix("CALL:"))
                    call: ConfCall = Server.CONFCALL_LIST[call_id]
                    call.redirectAudioData(audioDataIn, client)


if __name__ == "__main__":
    server: Server = Server()

    server.start()
