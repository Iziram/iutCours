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
        command_interpreter: CommandInterpreter = None,
        addr: str = "127.0.0.2",
        port: int = 5001,
        server_ip: str = "127.0.0.1",
        server_port: int = 5000,
    ) -> None:
        Connector.__init__(self)

        self.__username: str = username

        self.audio_in_bind(addr, port)
        self.audio_out_bind(addr, port + 1)
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
            self.command_connect(self.__server_ip, self.__server_port)

            # Phase de connexion

            self.sendFlag(Flag.REG)

            ans, ans_data = self.getFlagData()

            if ans == Flag.VLD:
                self.sendFlag(Flag.LOG, self.__username)
                ans, ans_data = self.getFlagData()
                if ans == Flag.VLD:
                    self.sendFlag(Flag.PSS, "1234")
                    ans, ans_data = self.getFlagData()
                    if ans == Flag.AUT:
                        print("YAY")
                        self.__connected = True
                        return self.__connected
                    else:
                        print(ans, ans_data)
                else:
                    print(ans, ans_data)
            else:
                print(ans, ans_data)
            self.__connected = False
            return self.__connected
        except:
            self.__connected = False
            return self.__connected

    def getFlagData(self) -> tuple[Flag, list[str]]:
        msg = self.command_receive().decode("utf-8").split(" ")
        flag: Flag = Flag.getFlagFromStr(msg[0])
        data: list[str] = msg[1:]
        return (flag, data)

    def sendFlag(self, flag: Flag = None, data: str = "", flag_str: str = None):
        if flag_str is not None:
            self.command_send(flag_str.encode("utf-8"))
        else:
            msg: str = flag.value
            if data != "":
                msg += " " + data
            self.command_send(msg.encode("utf-8"))

    def disconnect(self):
        try:
            self.command_close()
            self.__stream_in.close()
            self.__stream_out.close()
            self.__audio_in_channel.close()
            self.__audio_out_channel.close()
            self.__connected = False

        except:
            self.__connected = False

    def save_audio(self) -> bytes:
        self.__stream_in.read(Client.CHUNKS)

    def listen_audio(self, data: bytes):
        self.__stream_out.write(data)

    def listen_audio(self):
        while self.__audio_connected:
            data: bytes = self.audio_in_receive(Client.CHUNKS * 2)[0]
            self.listen_audio(data)

    def send_audio(self):
        while self.__audio_connected:
            data: bytes = self.save_audio()
            self.audio_out_send(data, self.__server_ip, self.__server_port)


if __name__ == "__main__":
    client: Client = Client("bob")
    print(client.connect())
