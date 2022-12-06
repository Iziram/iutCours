from common import Connector, CommandInterpreter, Flag
from threading import Thread
import pyaudio as pyaud


class Client(Connector):
    AUDIO = pyaud.PyAudio()
    FORMAT = pyaud.paInt16
    CHANNELS = 1
    FREQUENCE = 8000
    CHUNKS = 512

    def __init__(
        self,
        username: str,
        command_interpreter: CommandInterpreter,
        addr: str = "127.0.0.2",
        port: int = 5001,
        server_ip: str = "127.0.0.1",
        server_port: int = 5001,
    ) -> None:
        Connector.__init__(self)

        self.__username: str = username

        self.audio_in_bind(addr, port)
        self.audio_in_bind(addr, port + 1)
        self.__connected: bool = False

        self.__audio_connected: bool = False

        self.command_interpreter: CommandInterpreter = command_interpreter

        self.__stream_out = Client.AUDIO.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.FREQUENCE,
            output=True,
        )

        self.__stream_in = Client.AUDIO.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.FREQUENCE,
            input=True,
            frames_per_buffer=Client.CHUNKS,
        )

        self.__server_ip: str = server_ip
        self.__server_port: int = server_port

    def connect(self):
        try:
            self.command_connect()
        except:
            self.__connected = False
        else:
            self.__connected = True

    def disconnect(self):
        try:
            self.command_close()
            self.__stream_in.close()
            self.__stream_out.close()
            self.__audio_in_channel.close()
            self.__audio_out_channel.close()
        except:
            self.__connected = False

    def get_command(self) -> tuple[Flag, list[str]]:
        tab_bytes: bytes = self.command_receive()
        to_str: str = tab_bytes.decode("utf-8")
        flag, data = Flag.getFlagFromStr(to_str)
        return (flag, data)

    def send_command(
        self, flag: Flag = None, data: list[str] = None, flag_str: str = None
    ):
        tab_bytes: bytes = None
        if flag_str is not None:
            tab_bytes = flag_str.encode("utf-8")
        else:
            data_str: str = " ".join(data)
            tab_bytes = f"{flag.value} {data_str}"

        self.command_send(tab_bytes)

    def save_audio(self) -> bytes:
        self.__stream_in.read(Client.CHUNKS)

    def listen_audio(self, data: bytes):
        self.__stream_out.write(data)

    def get_command_worker(self):
        while self.__connected:
            flag, data = self.get_command()
            self.command_interpreter.run_command(flag, data)

    def listen_audio(self):
        while self.__audio_connected:
            data: bytes = self.audio_in_receive(Client.CHUNKS * 2)[0]
            self.listen_audio(data)

    def send_audio(self):
        while self.__audio_connected:
            data: bytes = self.save_audio()
            self.audio_out_send(data, self.__server_ip, self.__server_port)
