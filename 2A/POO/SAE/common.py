from enum import Enum
from socket import socket, AF_INET, SOCK_STREAM


class Flag(Enum):
    pass


class Flag(str, Enum):

    # signing
    REG = "reg"  # Starts the signing exchange
    LOG = "log"  # Sends the username "log <username>"
    PSS = "pss"  # Sends the password "pss <password: hash?>"
    AUT = "aut"  # Client is authenticated
    # Quality control
    VLD = "vld"  # Valid
    REF = "ref"  # Refused "ref [why]"
    ENT = "ent"  # End TCP connection
    TIM = "tim"  # Maintain channel connection
    NUL = "nul"  # Null flag
    # Commands
    LSD = "lsd"  # Demands clients list
    LSR = "lsr"  # Answers with clients list "lsg <username> <username> ..."

    CAL = "cal"  # Demands to call client "cal <username> <port client>"
    SOC = "soc"  # Answers with port to send data "soc 12345"
    STA = "sta"  # Start the call
    INF = "inf"  # general info of call "info time:1000 rec:username"
    FIN = "fin"  # Close current call

    # JSON
    GAN = "gan"  # Get the phone book "get {[...]}"
    PAN = "pan"  # upload the phone  book "pan {[...]}"

    @staticmethod
    def getFlagFromStr(str_flag: str) -> Flag:
        flag: Flag
        try:
            flag = Flag[str_flag.upper()]
        except:
            flag = Flag.NUL
        return flag

    def encode(self, encoding: str, _: str) -> bytes:
        return self.value.encode(encoding)


class CommandLink:
    def __init__(self) -> None:
        self.__command_channel: socket = socket(AF_INET, SOCK_STREAM)

    def receiveFlag(self) -> tuple[Flag, list[str]]:
        bytes_array: bytes = self.getCommandChannel().recv(255)
        data: str = bytes_array.decode("utf-8").split(" ")

        flag: Flag = Flag.getFlagFromStr(data[0])
        return (flag, data[1:])

    def sendFlag(self, flag: Flag = None, data: str = None):
        bytes_array: bytes
        if data is not None:
            bytes_array = f"{flag} {data}".encode("utf-8")
        else:
            bytes_array = flag.encode("utf-8")
        self.getCommandChannel().send(bytes_array)

    def sendTim(self):
        try:
            self.sendFlag(Flag.TIM)
        except:
            pass

    def closeCommandChannel(self) -> None:
        print("CloseCommandChannel USED")
        try:
            self.getCommandChannel().close()
        except:
            pass

    def getCommandChannel(self) -> socket:
        return self.__command_channel

    def setCommandChannel(self, _socket_: socket):
        self.__command_channel = _socket_
