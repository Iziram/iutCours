from common import Connector
from threading import Thread
from time import sleep


def tcp_test():
    def worker(connect: Connector):
        print("worker started")
        msg: str = " "
        while msg != "fin":
            msg = connect.command_receive().decode("utf-8")
            print(f"C{connect.command_peer()}", msg)
            connect.command_send(f"s: {msg}".encode("utf-8"))

    server: Connector = Connector()
    server.command_prepare_listening("127.0.0.1", 5000)
    count: int = 0
    while input("finished ? ") != "y":
        print("listening...")
        cserver: Connector = Connector(command_channel=server.command_listen()[0])
        print("found !")
        count += 1
        Thread(target=worker, args=(cserver,), name=f"CServ-{count}").start()


def udp_test(addr: int = "127.0.0.1", port: int = 5001):

    server: Connector = Connector()
    server.audio_in_bind(addr, port)
    server.audio_out_bind(addr, port + 1)

    clients: list[tuple[str, int]] = []

    def receiver(connect: Connector, clients: list[tuple[str, int]]):
        msg: str or bytes = ""
        while msg != "fin":
            msg, client = connect.audio_in_receive()
            print(client, msg)
            msg = msg.decode("utf-8")
            ADDR, port = client
            if (ADDR, port - 1) not in clients:
                clients.append((ADDR, port - 1))

    def sender(connect: Connector, clients: list[tuple[str, int]]):
        for i in range(10):
            for c_a, c_p in clients:
                connect.audio_out_send(f"client-{i}".encode("utf-8"), c_a, c_p)
            sleep(i * 0.1)
        for c_a, c_p in clients:
            connect.audio_out_send(f"fin".encode("utf-8"), c_a, c_p)

    print("audio_in_launched")
    Thread(target=receiver, args=(server, clients), name="audio_in").start()
    sleep(5)
    print("audio_out_launched")
    Thread(target=sender, args=(server, clients), name="audio_out").start()


if __name__ == "__main__":
    tcp_test()
    # udp_test()
