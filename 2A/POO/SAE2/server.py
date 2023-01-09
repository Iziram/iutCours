from common import Connector, CommandInterpreter, Flag
from threading import Thread
from socket import socket, timeout
from database import Database


class ClientServer(Connector, Thread):
    """
    Représentation d'un client coté serveur,
    Utilise uniquement le coté TCP
    """

    def __init__(
        self,
        command_channel: socket,
    ) -> None:
        Connector.__init__(self, command_channel=command_channel)
        Thread.__init__(self)

        self.__status: str = "UNKNOWN"

        self.__username: str = "UNKNOWN"
        self.__interpreter: CommandInterpreter = self.get_commands_worker()
        self.__active: bool = True

    def __str__(self) -> str:
        return f"<{self.__username}:{self.__status}>"

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


class Server(Connector, Thread):
    CLIENT_LIST: list[ClientServer] = []

    def __init__(self, addr: str = "127.0.0.1", port: int = 5000) -> None:
        self.__addr = addr
        self.__port = port
        self.__active: bool = True

        Connector.__init__(self)
        Thread.__init__(self, name="ThreadPrincipServer")

        self.__command_interpreter: CommandInterpreter = self.get_commands_worker()

    def start_self(self):
        self.command_prepare_listening(self.__addr, self.__port, timeout=10)
        while self.__active:
            try:
                client_server: ClientServer = ClientServer(self.command_listen()[0])
                Server.CLIENT_LIST.append(client_server)

                client_server.start()
            except timeout:
                pass
            except TypeError:
                pass

    def stop_self(self):
        self.__active = False
        for c in Server.CLIENT_LIST:
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
            peers: list[str] = [f"{c.command_peer()}" for c in Server.CLIENT_LIST]
            print(peers)

        def quit():
            stop()

        def disconnect(peer: str):
            if peer == "all":
                for c in Server.CLIENT_LIST:
                    c.command_close()
                Server.CLIENT_LIST.clear()
            else:
                client: ClientServer = [
                    c for c in Server.CLIENT_LIST if c.command_peer()[1] == int(peer)
                ]
                client.command_close()
                Server.CLIENT_LIST.remove(client)

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


if __name__ == "__main__":
    server: Server = Server()

    server.start()
