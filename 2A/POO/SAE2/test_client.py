from common import Connector
from threading import Thread
from time import sleep
from sys import argv


def tcp_test():
    client: Connector = Connector()
    client.command_connect("127.0.0.1", 5000)
    msg: str = " "

    while msg != "fin":
        msg = input("msg: ")
        client.command_send(msg.encode("utf-8"))
        print(client.command_receive().decode("utf-8"))


def udp_test(addr: int = "127.0.0.2", port: int = 5001):

    client: Connector = Connector()
    client.audio_in_bind(addr, port)
    client.audio_out_bind(addr, port + 1)

    def receiver(connect: Connector):
        msg: str or bytes = ""
        while msg != "fin":
            msg, server = connect.audio_in_receive()
            print(server, msg)
            msg = msg.decode("utf-8")

    def sender(connect: Connector):
        for i in range(10):
            connect.audio_out_send(f"client-{i}".encode("utf-8"), "127.0.0.1", 5001)
            sleep(i * 0.1)
        connect.audio_out_send(f"fin".encode("utf-8"), "127.0.0.1", 5001)

    Thread(target=receiver, args=(client,), name="audio_in").start()
    Thread(target=sender, args=(client,), name="audio_out").start()


if __name__ == "__main__":
    # tcp_test()
    if len(argv) > 1:
        udp_test(f"127.0.0.{argv[1]}")
    else:
        udp_test()
