from common import Connector, CommandInterpreter, Flag
from threading import Thread
import pyaudio as pyaud
from socket import timeout

from time import sleep

from sys import argv
from sys import exit as sysExit


class Client(Connector):
    AUDIO = pyaud.PyAudio()
    FORMAT = pyaud.paInt16
    CHANNELS = 1
    FREQUENCE = 8000
    CHUNKS = 512

    def __init__(
        self,
        username: str,
        password: str,
        addr: str = "127.0.0.2",
        port: int = 5000,
        server_ip: str = "127.0.0.1",
        server_port: int = 5000,
    ) -> None:
        Connector.__init__(self)

        self.__username: str = username
        self.__password: str = password

        self.command_channel_bind(addr, port)

        self.audio_in_bind(addr, port + 1)
        self.audio_out_bind(addr, port + 2)
        self.__connected: bool = False
        self.__initial_connected: bool = False

        self.__audio_connected: bool = False

        self.__command_interpreter: CommandInterpreter = self.get_commands_worker()

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

    def get_commands_worker(self):
        def ent():
            self.disconnect()

        def lsr(*data):
            print(data)

        def default():
            pass

        def ask(callName: str):
            pass

        def sta():

            Thread(target=self.receive_audio, name="audioClientIn").start()

            Thread(target=self.send_audio, name="audioClientOut").start()

        def fin():
            self.__audio_connected = False

        interpreter: CommandInterpreter = CommandInterpreter(
            (Flag.LSR, lsr),
            (Flag.ENT, ent),
            (Flag.ASK, ask),
            (Flag.STA, sta),
            (Flag.FIN, fin),
        )
        interpreter.set_default_command(default)

        return interpreter

    def getInterpreter(self):
        return self.__command_interpreter

    def setAudioConnected(self, b: bool):
        self.__audio_connected = b

    def connect(self, var):
        try:
            if not self.__initial_connected:
                self.command_connect(self.__server_ip, self.__server_port)
                self.__initial_connected = True

            # Phase de connexion

            self.sendFlag(Flag.REG)

            ans, ans_data = self.getFlagData()

            if ans == Flag.VLD:
                self.sendFlag(Flag.LOG, self.__username)
                ans, ans_data = self.getFlagData()
                if ans == Flag.VLD:
                    self.sendFlag(Flag.PSS, self.__password)
                    ans, ans_data = self.getFlagData()
                    if ans == Flag.AUT:
                        self.__connected = True
                        print("connected: ", self.__username)
                        return self.__connected
                    else:
                        var.set(" ".join(ans_data))
                else:
                    var.set(" ".join(ans_data))
            else:
                var.set(" ".join(ans_data))
            self.__connected = False
            return self.__connected
        except Exception as e:
            print(e)
            self.__connected = False
            var.set("Une erreur s'est passée")
            return self.__connected

    def sendData(self):
        while self.__connected:
            flag: Flag = Flag.getFlagFromStr(input("Flag: "))
            data: str = input("Data: ")
            print("BEFORE")
            if self.__connected:
                print("AFTER TRUE")

                self.sendFlag(flag, data)
            print("AFTER FALSE")

    def receiveData(self):
        while self.__connected:
            flag: Flag
            data: list[str]

            flag, data = self.getFlagData()
            print("reçu: ", flag, data)
            self.__command_interpreter.run_command(flag, *data)

    def getFlagData(self) -> tuple[Flag, list[str]]:
        try:
            msg = self.command_receive().decode("utf-8").split(" ")
            print(*msg)
            flag: Flag = Flag.getFlagFromStr(msg[0])
            data: list[str] = msg[1:]
            return (flag, data)
        except:
            self.__connected = False
            return None

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
            self.__audio_connected = False

        except:
            self.__connected = False
        sysExit()

    def save_audio(self) -> bytes:
        return self.__stream_in.read(Client.CHUNKS)

    def listen_audio(self, data: bytes):
        self.__stream_out.write(data)

    def receive_audio(self):
        self.__audio_connected = True
        while self.__audio_connected:
            try:
                data: bytes = self.audio_in_receive(Client.CHUNKS * 2)[0]
                self.listen_audio(data)
            except timeout:
                pass

    def send_audio(self):
        while self.__audio_connected:
            data: bytes = self.save_audio()
            self.audio_out_send(data, self.__server_ip, self.__server_port)

    def setUsername(self, username: str):
        self.__username = username

    def setPassword(self, password: str):
        self.__password = password


if __name__ == "__main__":
    client_name: str = "bob"
    password: str = "1234"
    ip = "2"
    if len(argv) > 1:
        client_name = argv[1]
        password = argv[2]
        if len(argv) >= 4:
            ip = argv[3]

    client: Client = Client(client_name, password, addr=f"127.0.0.{ip}")
    if client.connect():
        th: Thread = Thread(target=client.receiveData, name="clientReceive")
        th.start()
        th: Thread = Thread(target=client.sendData, name="clientSend")
        th.start()
    else:
        print("Connexion refusée")
