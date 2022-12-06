from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from threading import Thread
from enum import Enum, auto
from select import select
from common import Flag, CommandLink


class Server:
    pass


class Status(str, Enum):
    IDLE = "IDLE"
    REGISTERING = "REGISTERING"
    AUTHENTICATED = "AUTHENTICATED"
    TIMEDOUT = "TIMEDOUT"
    ONCALL = "ONCALL"


class ClientSRV(Thread, CommandLink):
    def __init__(self, socket: socket, parent: Server) -> None:

        # Command Server relationship
        CommandLink.__init__(self)
        self.setCommandChannel(socket)
        self.__username: str = "Unknown"
        self.__status: Status = Status.IDLE
        self.__parent_server: Server = parent

        self.__audio_port_in: int = None
        self.__audio_port_out: int = None
        self.__audio_ip: str = None

        Thread.__init__(self, name=repr(self))

    def get_audio_in(self):
        return (self.__audio_ip, self.__audio_port_in)

    def get_audio_out(self):
        return (self.__audio_ip, self.__audio_port_out)

    def __repr__(self) -> str:
        return f"<Client:{self.__username}|{self.__status.value}>"

    def __str__(self) -> str:
        return f"{self.__username}"

    def getUserName(self) -> str:
        return self.__username

    def setStatus(self, status: Status) -> None:
        self.__status = status

    def getStatus(self) -> Status:
        return self.__status

    def timedout(self) -> None:
        self.disconnect()
        self.closeCommandChannel()
        print("TimedOut", repr(self))

    def disconnect(self):
        self.sendFlag(Flag.ENT)
        self.__parent_server.getClients().remove(self)

    def reactToFlag(self, flag: Flag, data: list[str] = None):
        def call_client(username: str = None):
            if self.__status in [Status.AUTHENTICATED, Status.ONCALL]:
                if self.__status == Status.AUTHENTICATED:
                    client: ClientSRV = self.__parent_server.getClient(username)
                    if client is not None:
                        if client.getStatus() == Status.AUTHENTICATED:
                            call: Call = Call(
                                self, client, self.__parent_server.getAudioSocket()
                            )
                            self.sendFlag(
                                Flag.SOC, self.__parent_server.get_audio_port()
                            )
                            client.sendFlag(
                                Flag.SOC, self.__parent_server.get_audio_port()
                            )

                            self.__parent_server.getCalls().append(call)

                        else:
                            self.sendFlag(Flag.REF, "Client is already on call")
                    else:
                        self.sendFlag(Flag.REF, "Client does not exist")
                else:
                    self.sendFlag(Flag.REF, "Already on call")
            else:
                self.sendFlag(Flag.REF, "Action not permitted")

        def set_client_audio_socket(addr: str, port_in: str, port_out):
            self.__audio_port_in = int(port_in)
            self.__audio_port_out = int(port_out)
            call: Call = self.__parent_server.getClientCall(self)
            if call is not None and call.is_ready():
                call.start()

        def close_call():
            if self.__status == Status.ONCALL:
                client_call: Call = self.__parent_server.getClientCall(self)
                if client_call is not None:
                    client_call.closeCall()
                else:
                    self.sendFlag(Flag.REF, "Call not found")
            else:
                self.sendFlag(Flag.REF, "Client not on call")

        def set_registering():
            print("REG Used")
            if self.__status == Status.IDLE:
                self.__status = Status.REGISTERING
                print("Registering")
                self.sendFlag(flag=Flag.VLD)
            else:
                self.sendFlag(Flag.REF, "not idling")

        def set_user_name(username: str = None):
            if self.__status == Status.REGISTERING:
                if username not in self.__parent_server.getClientsNames():
                    if username is None:
                        self.sendFlag(Flag.REF, "username can't be None")
                    self.__username = username
                    self.setName(repr(self))
                    self.sendFlag(Flag.VLD)

                else:
                    self.sendFlag(Flag.REF, "username already taken")
                    self.disconnect()
            else:
                self.sendFlag(Flag.REF, "outside registration")

        def authenticate(password: str = None):
            if self.__status == Status.REGISTERING:
                if password is None:
                    self.sendFlag(Flag.REF, "password can't be None")
                    # self.disconnect()
                    return
                # check login / password
                self.__status = Status.AUTHENTICATED
                self.sendFlag(Flag.AUT)
                return

            self.sendFlag(Flag.REF, "Authentification failed")

        def list_clients():
            client_list_str: str = " ".join(self.__parent_server.getClientsNames())
            self.sendFlag(flag=Flag.LSR, data=client_list_str)

        def unknown_command():
            self.sendFlag(Flag.REF, "unknown command")

        def end_channel_command():
            self.disconnect()

        def tim():
            self.sendTim()

        switch: dict[Flag, function] = {
            Flag.REG: set_registering,
            Flag.LOG: set_user_name,
            Flag.PSS: authenticate,
            Flag.LSD: list_clients,
            Flag.TIM: tim,
            Flag.ENT: end_channel_command,
            Flag.FIN: close_call,
            Flag.CAL: call_client,
            Flag.POR: set_client_audio_socket,
        }

        action: function = switch.get(flag, unknown_command)
        action(*data)

    def run(self) -> None:
        end: bool = False
        try:
            while not end:
                ready = select([self.getCommandChannel()], [], [], 25.5)
                if ready[0]:
                    flag, data = self.receiveFlag()
                    if flag == Flag.ENT:
                        end = True
                    print("flag_srv: ", flag, data)
                    self.reactToFlag(flag, data)
                    print(repr(self))
                else:
                    end = True
                    self.__status = Status.TIMEDOUT
                    self.timedout()
        except:
            pass

        self.closeCommandChannel()


class Call(Thread):
    def __init__(
        self, clientA: ClientSRV, clientB: ClientSRV, server_audio_socket: socket
    ) -> None:
        self.__clientA: ClientSRV = clientA
        self.__clientB: ClientSRV = clientB
        self.__finished: bool = True
        self.__server_audio_socket: socket = server_audio_socket
        Thread.__init__(self, name=repr(self))

    def __repr__(self) -> str:
        return (
            f"<CALL: {self.__clientA.getUserName()}<-->{self.__clientB.getUserName()} >"
        )

    def is_ready(self):
        ready: bool = (
            self.__clientA.getAudioConnectionInfo()[1] != None
            and self.__clientB.getAudioConnectionInfo()[1] != None
        )
        return ready

    def run(self) -> None:
        if self.__finished:
            self.__finished = False
            self.__clientA.sendFlag(Flag.STA)
            self.__clientB.sendFlag(Flag.STA)
            self.__clientA.sendFlag(Flag.INF, "call started")
            self.__clientB.sendFlag(Flag.INF, "call started")
            self.__clientA.setStatus(Status.ONCALL)
            self.__clientB.setStatus(Status.ONCALL)
            self.audioCall()

    def audioCall(self):
        while not self.__finished:
            data, ADDR = self.__server_audio_socket.recvfrom(2048)
            if ADDR == self.__clientA.get_audio_in():
                self.sendData(self.__clientB, data)
            elif ADDR == self.__clientB.get_audio_in():
                self.sendData(self.__clientA, data)

    def sendData(self, client: ClientSRV, data: bytes) -> None:
        try:
            if not self.__finished:
                self.__server_audio_socket.sendto(data, client.get_audio_out())
        except:
            pass

    def closeCall(self):
        self.__finished = True

        self.__clientA.sendFlag(Flag.FIN)
        self.__clientA.setStatus(Status.AUTHENTICATED)

        self.__clientB.sendFlag(Flag.FIN)
        self.__clientB.setStatus(Status.AUTHENTICATED)

    def hasClient(self, username: str):
        return username in [self.__clientA.getUserName(), self.__clientB.getUserName()]


class Server:
    def __init__(self, port: int) -> None:
        self.__listener: socket = socket(AF_INET, SOCK_STREAM)
        self.__listener.bind(("", port))
        self.__listener.listen(1)
        self.__clients: list[ClientSRV] = []
        self.__calls: list[Call] = []
        self.__audio_port: int = port + 1

        self.__audio_socket: socket = socket(AF_INET, SOCK_DGRAM)
        self.__audio_socket.bind(("", self.__audio_port))

    def getCalls(self) -> list[Call]:
        return self.__calls

    def get_audio_port(self):
        return self.__audio_port

    def listen(self) -> None:
        connection, _ = self.__listener.accept()

        client: ClientSRV = ClientSRV(connection, self)
        client.start()
        self.__clients.append(client)

    def getClient(self, username: str) -> ClientSRV or None:
        clients: list[ClientSRV] = [
            cli for cli in self.__clients if cli.getUserName() == username
        ]
        client: ClientSRV
        if clients != []:
            client = clients[0]
        else:
            client = None

        return client

    def getClientsNames(self) -> list[str]:
        return [cli.getUserName() for cli in self.__clients]

    def getClients(self) -> list[ClientSRV]:
        return self.__clients

    def getClientCall(self, client: ClientSRV) -> Call:
        call: Call = None
        filtered_calls = []
        for call in self.__calls:
            if call.hasClient(client.getUserName()):
                filtered_calls.append(call)
        if filtered_calls != []:
            call = filtered_calls[0]
        return call

    def getAudioSocket(self) -> socket:
        return self.__audio_socket


if __name__ == "__main__":
    srv = Server(5000)
    while True:
        srv.listen()
