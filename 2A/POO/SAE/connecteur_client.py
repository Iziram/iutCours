from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from sys import argv
from time import sleep
from common import Flag, CommandLink


class Client(CommandLink):
    def __init__(self, server_ip: str, port: int, username: str, password: str) -> None:
        CommandLink.__init__(self)
        self.__server_ip: str = server_ip
        self.__server_port: int = port

        self.__username: str = username
        self.__password: str = password
        self.__alive: bool = True

        # Call relationship
        self.__audio_port: int = None
        self.__audio_channel: socket = socket(AF_INET, SOCK_DGRAM)

    def get_audio_port(self) -> int:
        return self.__audio_port

    def set_audio_port(self, port: int) -> None:
        self.__audio_port = port

    def set_audio_channel(self, address: str = "127.0.0.1") -> None:
        self.__audio_channel.bind((address, self.__audio_port))

    def close_audio_channel(self) -> None:
        try:
            self.__audio_channel.close()
        except Exception:
            pass
        self.__audio_port = None

    def maintain_command_channel(self, timeout: float = 4.8):
        while self.__alive:
            sleep(timeout)
            if self.__alive:
                self.sendTim()

    def connect_to_command_server(self) -> bool:
        connected: bool = False
        self.getCommandChannel().connect((self.__server_ip, self.__server_port))

        actions: list[str or Flag] = [
            Flag.REG.value,
            Flag.LOG.value + f" {self.__username}",
            Flag.PSS.value + f" {self.__password}",
        ]

        iterator: object = iter(actions)
        nxt: str = next(iterator, False)
        ans: Flag = Flag.VLD
        while nxt and ans == Flag.VLD:
            self.sendFlag(nxt)
            ans, _ = self.receiveFlag()
            print("flag_cli", ans, _)
            nxt = next(iterator, False)

        if ans == Flag.AUT:
            connected = True
        print("connected", connected)
        return connected

    def command_sender(self):
        while self.__alive:
            inp: str = input("f: ")
            if inp != "":
                flag: Flag = Flag.getFlagFromStr(inp)
                if self.__alive:
                    self.sendFlag(flag)

    def command_receiver(self):
        try:
            while self.__alive:
                flag_r, data = self.receiveFlag()
                if flag_r is not None:
                    print(flag_r, data)
                if flag_r == Flag.ENT:
                    self.__alive = False
        except Exception:
            pass
        self.closeCommandChannel()

    def closeCommandChannel(self) -> None:
        CommandLink.closeCommandChannel(self)
        self.__alive = False


if __name__ == "__main__":
    clt = Client("127.0.0.1", 5000, argv[1], "mdp")
    if clt.connect_to_command_server():
        rec = Thread(target=clt.command_receiver)
        sen = Thread(target=clt.command_sender)
        tims = Thread(target=clt.maintain_command_channel)
        sen.start()
        rec.start()
        tims.start()
