from enum import Enum
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, MSG_PEEK


class Flag(Enum):
    pass


class Flag(str, Enum):

    # signing
    REG = "reg"  # Starts the signing exchange
    LOG = "log"  # Sends the username "log <username>"
    PSS = "pss"  # Sends the password "pss <password>"
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

    CAL = "cal"  # Demands to call client "cal <username>"
    SOC = "soc"  # Answers with port to send data "soc 12345"
    POR = "por"  # Client gives his audio socket "por 127.0.0.1 42069"
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

    def encode(self, encoding: str, _: str = None) -> bytes:
        return self.value.encode(encoding)


class Connector:
    """ """

    pass


class Connector:
    def __init__(
        self,
        command_channel: socket = None,
        audio_in_channel: socket = None,
        audio_out_channel: socket = None,
    ) -> None:

        self.__command_channel: socket = (
            command_channel
            if command_channel is not None
            else socket(AF_INET, SOCK_STREAM)
        )
        self.__audio_in_channel: socket = (
            audio_in_channel
            if audio_in_channel is not None
            else socket(AF_INET, SOCK_DGRAM)
        )
        self.__audio_out_channel: socket = (
            audio_out_channel
            if audio_out_channel is not None
            else socket(AF_INET, SOCK_DGRAM)
        )

    def command_send(self, data: bytes):
        if not self.is_command_closed():
            self.__command_channel.sendall(data)

    def command_receive(self) -> bytes:
        if not self.is_command_closed():
            data: bytes = self.__command_channel.recv(255)
            return data

    def command_close(self):
        self.__command_channel.close()

    def command_prepare_listening(self, addr: str, port: int, timeout: int = None):
        self.__command_channel.bind((addr, port))
        self.__command_channel.listen(1)
        if timeout is not None:
            self.__command_channel.settimeout(timeout)

    def command_listen(self) -> tuple[socket, tuple[str, int]]:
        try:
            return self.__command_channel.accept()
        except OSError:
            if not self.is_command_closed:
                self.command_close()

    def command_connect(self, addr: str, port: int):
        self.__command_channel.connect((addr, port))

    def is_command_closed(self) -> bool:
        try:
            # this will try to read bytes without blocking and also without removing them from buffer (peek only)
            self.__command_channel.setblocking(False)
            data = self.__command_channel.recv(16, MSG_PEEK)
            if len(data) == 0:
                return True
        except BlockingIOError:
            return False  # socket is open and reading from it would block
        except ConnectionResetError:
            return True  # socket was closed for some other reason
        except Exception:
            return True
        finally:
            try:
                self.__command_channel.setblocking(True)
            except:
                return True
        return False

    def command_peer(self) -> tuple[str, int]:
        return self.__command_channel.getpeername()

    def audio_in_bind(self, addr: str, port: int):
        print(type(addr), type(port))
        print(addr, port)
        self.__audio_in_channel.bind((addr, port))

    def audio_in_receive(self, buffer: int = 2048) -> tuple[bytes, tuple[str, int]]:
        return self.__audio_in_channel.recvfrom(buffer)

    def audio_out_send(self, data: bytes, addr: str, port: int):
        self.__audio_out_channel.sendto(data, (addr, port))

    def audio_out_bind(self, addr: str, port: int):
        self.__audio_out_channel.bind((addr, port))


class function:
    pass


class CommandInterpreter:
    def __init__(self, *functions: tuple[object, function]) -> None:
        self.__switch: dict[object, function] = {}
        for kwd, func in functions:
            self.__switch[kwd] = func

    def get_switch(self) -> dict[object, function]:
        return self.__switch

    def run_command(self, identifier: object, *data: tuple[object]):
        if identifier in self.__switch:
            self.__switch[identifier](*data)
        else:
            self.__switch["__default__"]()

    def set_default_command(self, function: function):
        self.__switch["__default__"] = function
