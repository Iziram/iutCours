from common import Connector, CommandInterpreter, Flag
from threading import Thread
from socket import socket, timeout


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

    # Put the command worker


class Server(Connector, Thread):
    def __init__(self, addr: str = "127.0.0.1", port: int = 5000) -> None:
        self.__clients_list: list[ClientServer] = []
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
                self.__clients_list.append(client_server)

                client_server.start()
            except timeout:
                pass
            except TypeError:
                pass

    def stop_self(self):
        self.__active = False
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
            peers: list[str] = [f"{c.command_peer()}" for c in self.__clients_list]
            print(peers)

        def quit():
            pass

        def disconnect(peer: str):
            if peer == "all":
                for c in self.__clients_list:
                    c.command_close()
                self.__clients_list.clear()
            else:
                client: ClientServer = [
                    c for c in self.__clients_list if c.command_peer()[1] == int(peer)
                ]
                client.command_close()
                self.__clients_list.remove(client)

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
