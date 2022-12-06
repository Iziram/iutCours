from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from sys import argv
from time import sleep
import pyaudio
from random import randint
from select import select
from common import Flag, CommandLink


class Client(CommandLink):
    # Audio consts
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 0.2

    def __init__(
        self,
        server_ip: str,
        port: int,
        username: str,
        password: str,
        client_ip: str = "127.0.0.1",
    ) -> None:
        CommandLink.__init__(self)
        self.__server_ip: str = server_ip
        self.__server_port: int = port
        self.__client_ip: str = client_ip

        self.__username: str = username
        self.__password: str = password
        self.__alive: bool = True

        # Call relationship
        self.__audio_port: int = None
        self.__server_audio_port: int = None
        self.__audio_channel_out: socket = socket(AF_INET, SOCK_DGRAM)
        self.__audio_channel_in: socket = socket(AF_INET, SOCK_DGRAM)
        self.__audio_alive: bool = True
        self.__audio = pyaudio.PyAudio()

        self.__mic = self.__audio.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.RATE,
            input=True,
            frames_per_buffer=Client.CHUNK,
        )

        self.__speaker = self.__audio.open(
            format=Client.FORMAT,
            channels=Client.CHANNELS,
            rate=Client.RATE,
            output=True,
        )

    def get_audio_port(self) -> int:
        return self.__audio_port

    def set_audio_port(self, port: int) -> None:
        self.__audio_port = port

    def set_server_audio_port(self, port: int) -> None:
        self.__server_audio_port = port

    def set_audio_channel_in(self, port: int, address: str = "127.0.0.1") -> None:
        self.__audio_channel_in.bind((address, port))

    def set_audio_channel_out(self, port: int, address: str = "127.0.0.1") -> None:
        self.__audio_channel_out.bind((address, port))

    def close_audio_channel(self) -> None:
        try:
            self.__audio_channel_in.close()
            self.__audio_channel_out.close()
            self.__speaker.close()
            self.__mic.close()
            self.__audio.terminate()
        except Exception:
            pass
        self.__audio_port = None
        self.__server_audio_port = None

    def send_audio_to_server(self):
        try:
            while self.__audio_alive:
                # Record voice data
                data: bytes = self.__mic.read(Client.CHUNK)
                # Send with UDP to Server
                if self.__audio_alive:
                    self.__audio_channel_out.sendto(
                        data, (self.__server_ip, self.__server_audio_port)
                    )
        except Exception:
            self.close_audio_channel()

    def receive_audio_from_server(self):
        try:
            while self.__audio_alive:
                data, _ = self.__audio_channel_in.recvfrom(2048)
                self.__speaker.write(data)
        except Exception:
            self.close_audio_channel()

    def maintain_command_channel(self, timeout: float = 25.0):
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
                if self.__alive:
                    self.sendFlag(flag_str=inp)

    def command_receiver(self):
        try:
            while self.__alive:
                flag_r, data = self.receiveFlag()
                self.command_runner(flag_r, data)
        except Exception as e:
            print("except: ", e)
            pass
        # self.closeCommandChannel()

    def command_runner(self, flag: Flag = Flag.NUL, data: list[str] = []):
        def end_connection():
            self.sendFlag(Flag.FIN)
            self.closeCommandChannel()
            self.__alive = False

        def set_audio_channel_options(server_port: int):
            self.__server_audio_port = int(server_port)
            self.__audio_port = randint(20_000, 64_000)
            self.sendFlag(
                Flag.POR,
                f"{self.__client_ip} {self.__audio_port} {self.__audio_port + 1}",
            )
            self.set_audio_channel_in(self.__audio_port + 1, self.__client_ip)
            self.set_audio_channel_out(self.__audio_port, self.__client_ip)

        def start_audio_channel():
            mic_thread: Thread = Thread(target=self.send_audio_to_server)
            speaker_thread: Thread = Thread(target=self.receive_audio_from_server)
            mic_thread.start()
            speaker_thread.start()

        def nothing(*_):
            pass

        def show(*param):
            print(" ".join(param))

        def close_audio():
            self.close_audio_channel()
            print("Call Ended")

        switch: dict[Flag, function] = {
            Flag.ENT: end_connection,
            Flag.SOC: set_audio_channel_options,
            Flag.STA: start_audio_channel,
            Flag.TIM: nothing,
            Flag.INF: show,
            Flag.FIN: close_audio,
            Flag.VLD: nothing,
        }

        action: function = switch.get(flag, show)
        action(*data)

    def closeCommandChannel(self) -> None:
        CommandLink.closeCommandChannel(self)
        self.__alive = False


if __name__ == "__main__":
    name = argv[1] if len(argv) > 1 else "bob"
    clt = Client("127.0.0.1", 5000, name, "mdp")
    if clt.connect_to_command_server():
        rec = Thread(target=clt.command_receiver, name="client_receiver")
        sen = Thread(target=clt.command_sender, name="client_sender")
        tims = Thread(target=clt.maintain_command_channel, name="client_tim")
        sen.start()
        rec.start()
        tims.start()
