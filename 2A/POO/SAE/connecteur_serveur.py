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
        Thread.__init__(self)

        # Command Server relationship
        CommandLink.__init__(self)
        self.setCommandChannel(socket)
        self.__username: str = "Unknown"
        self.__status: Status = Status.IDLE
        self.__parent_server: Server = parent

        self.__audio_port: int = None
        self.__audio_ip: str = None

    def setAudioConnectionInfo(self, addr: tuple[str, int]) -> None:
        self.__audio_ip, self.__audio_port = addr

    def getAudioConnectionInfo(self) -> tuple[str, int]:
        return (self.__audio_ip, self.__audio_port)

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
        def callClient(username: str = None):
            if self.__status in [Status.AUTHENTICATED, Status.ONCALL]:
                if self.__status == Status.AUTHENTICATED:
                    client: ClientSRV = self.__parent_server.getClient(username)
                    if client is not None:
                        if client.getStatus == Status.AUTHENTICATED:
                            call: Call = Call(
                                self, client, self.__parent_server.getAudioSocket()
                            )
                            call.start()
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass

        def closeCall():
            if self.__status == Status.ONCALL:
                client_call: Call = self.__parent_server.getClientCall(self)
                if client_call is not None:
                    client_call.closeCall()
                else:
                    self.sendFlag(Flag.REF, "Call not found")
            else:
                self.sendFlag(Flag.REF, "Client not on call")

        def setRegistering():
            if self.__status == Status.IDLE:
                self.__status = Status.REGISTERING
                self.sendFlag(Flag.VLD)
            else:
                self.sendFlag(Flag.REF, "not idling")

        def setUserName(username: str = None):
            if self.__status == Status.REGISTERING:
                if username not in self.__parent_server.getClientsNames():
                    if username is None:
                        self.sendFlag(Flag.REF, "username can't be None")
                    self.__username = username
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

        def listClients():
            client_list_str: str = " ".join(self.__parent_server.getClientsNames())
            self.sendFlag(Flag.LSR, client_list_str)

        def unknownCommand():
            self.sendFlag(Flag.REF, "unknown command")

        def endChannelCommand():
            self.disconnect()

        def tim():
            self.sendTim()

        switch: dict[Flag, function] = {
            Flag.REG: setRegistering,
            Flag.LOG: setUserName,
            Flag.PSS: authenticate,
            Flag.LSD: listClients,
            Flag.TIM: tim,
            Flag.ENT: endChannelCommand,
            Flag.FIN: closeCall,
            Flag.CAL: callClient,
        }

        action: function = switch.get(flag, unknownCommand)
        action(*data)

    def run(self) -> None:
        end: bool = False
        try:
            while not end:
                ready = select([self.getCommandChannel()], [], [], 5)
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
        Thread.__init__(self)
        self.__clientA: ClientSRV = clientA
        self.__clientB: ClientSRV = clientB
        self.__finished: bool = False
        self.__server_audio_socket: socket = server_audio_socket

    def run(self) -> None:
        self.__clientA.sendFlag(Flag.STA)
        self.__clientB.sendFlag(Flag.STA)
        self.audioCall()

    def audioCall(self):
        while not self.__finished:
            data, ADDR = self.__server_audio_socket.recvfrom(1024)
            if ADDR == self.__clientA.getAudioConnectionInfo():
                self.sendData(self.__clientB)
            elif ADDR == self.__clientB.getAudioConnectionInfo():
                self.sendData(self.__clientA)

    def sendData(self, client: ClientSRV, data: bytes) -> None:
        try:
            if not self.__finished:
                self.__server_audio_socket.sendto(data, client.getAudioConnectionInfo())
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

        self.__audio_socket: socket = socket(AF_INET, SOCK_DGRAM)
        self.__audio_socket.bind(("", port + 1))

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
        filtered_calls: list[Call] = [
            call for call in self.__calls if call.hasClient(client.getUserName())
        ]
        if filtered_calls != []:
            call = filtered_calls[0]
        return call

    def getAudioSocket(self) -> socket:
        return self.__audio_socket


if __name__ == "__main__":
    srv = Server(5000)
    while True:
        srv.listen()
