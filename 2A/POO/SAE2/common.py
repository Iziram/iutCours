from enum import Enum
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, MSG_PEEK
from tkinter import Text, END


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

    CAL = "cal"  # Demands to call client "cal <username> [usernames...]"
    ASK = "ask"  # ask a client if he wants to answer the call "ask <callName>"
    RES = "res"  # response to ASK flag "res <bool:1|0>"
    STA = "sta"  # Start the call
    JON = "jon"  # Join a call (if call not ended) "jon <confName>"
    INF = "inf"  # general info of call "info time:00h00m00s act:usr1,usr2,usr3,..."
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

        self.__audio_in_channel.settimeout(4.0)

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
        self.__audio_in_channel.bind((addr, port))

    def audio_in_receive(self, buffer: int = 2048) -> tuple[bytes, tuple[str, int]]:
        return self.__audio_in_channel.recvfrom(buffer)

    def audio_out_send(self, data: bytes, addr: str, port: int):
        self.__audio_out_channel.sendto(data, (addr, port))

    def audio_out_bind(self, addr: str, port: int):
        self.__audio_out_channel.bind((addr, port))

    def command_channel_bind(self, addr: str, port: int):
        self.__command_channel.bind((addr, port))


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

    def set_command(self, identifier: object, function: function):
        self.__switch[identifier] = function


class TextWithVar(Text):
    """A text widget that accepts a 'textvariable' option"""

    def __init__(self, parent, *args, **kwargs):
        try:
            self._textvariable = kwargs.pop("textvariable")
        except KeyError:
            self._textvariable = None

        Text.__init__(self, parent, *args, **kwargs)

        # if the variable has data in it, use it to initialize
        # the widget
        if self._textvariable is not None:
            self.insert("1.0", self._textvariable.get())

        # this defines an internal proxy which generates a
        # virtual event whenever text is inserted or deleted
        self.tk.eval(
            """
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                # return the result from the real widget command
                return $result
            }
            """
        )

        # this replaces the underlying widget with the proxy
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        """.format(
                widget=str(self)
            )
        )

        # set up a binding to update the variable whenever
        # the widget changes
        self.bind("<<Change>>", self._on_widget_change)

        # set up a trace to update the text widget when the
        # variable changes
        if self._textvariable is not None:
            self._textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *args):
        """Change the text widget when the associated textvariable changes"""

        # only change the widget if something actually
        # changed, otherwise we'll get into an endless
        # loop
        text_current = self.get("1.0", "end-1c")
        var_current = self._textvariable.get()
        if text_current != var_current:
            self.delete("1.0", "end")
            self.insert("1.0", var_current)
            self.see(END)

    def _on_widget_change(self, event=None):
        """Change the variable when the widget changes"""
        if self._textvariable is not None:
            self._textvariable.set(self.get("1.0", "end-1c"))
            self.see(END)


class Logger:
    def __init__(self) -> None:
        self.__logs: list[str] = []
        self.__event: function = None

    def add(self, msg: str):
        self.__logs.append(msg)
        self.__event("\n".join(self.__logs))

    def remove(self, msg: str):
        if msg in self.__logs:
            self.__logs.remove(msg)
            self.__event(self.__logs)

    def setEvent(self, func: function):
        self.__event = func


def secondsToClock(secs):
    secs: int = int(secs)
    hours: int = secs // 3600
    secs %= 3600
    minutes: int = secs // 60
    secs %= 60

    if hours < 10:
        hours: str = f"0{hours}"
    if minutes < 10:
        minutes: str = f"0{minutes}"
    if secs < 10:
        secs: str = f"0{secs}"

    return f"{hours}h{minutes}m{secs}s"
