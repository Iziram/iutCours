from socket import socket, AF_INET, SOCK_STREAM


class POPClient:
    # Méthodes
    def __init__(self, server: str, user: str, mdp: str, port: int = 110) -> None:
        self.__server: str = server
        self.__user: str = user
        self.__pass: str = mdp
        self.__socket: socket = socket(AF_INET, SOCK_STREAM)
        self.__port: int = port

    def send_command(self, command: str) -> None:
        if not command.endswith("\n"):
            command += "\n"

        tab_bytes: bytes = command.encode("utf-8")
        self.__socket.send(tab_bytes)
        print("Send :", command)

    def receive(self) -> str:
        string: str = "error"
        tab_bytes: bytes = self.__socket.recv(4098)
        string = tab_bytes.decode("utf-8")
        print(string)
        return string

    def authentification(self) -> bool:
        authenticated: bool = False
        server_message: str
        self.__socket.connect((self.__server, self.__port))
        server_message = self.receive()
        if server_message.startswith("+OK"):
            self.send_command(f"USER {self.__user}")
            server_message = self.receive()
            self.send_command(f"PASS {self.__pass}")
            server_message = self.receive()
            if server_message.startswith("+OK"):
                authenticated = True

        return authenticated

    def get_statistics(self) -> str:
        self.send_command("STAT")
        return self.receive()

    def get_statistic(self, mail_number: int) -> str:
        self.send_command(f"LIST {mail_number}")
        print(self.receive())

    def get_mail(self, num_message: int) -> str:
        self.send_command(f"RETR {num_message}")
        return self.receive()

    def quit(self) -> None:
        self.send_command("QUIT")
        if self.receive().startswith("+OK"):
            self.__socket.close()


if __name__ == "__main__":
    # initialisation
    serv_addr: str = "148.60.235.240"
    user: str = "RT-G021-10@mail.gtr"
    mdp: str = "RT-G021-10"
    # instanciation
    pop_client: POPClient = POPClient(server=serv_addr, user=user, mdp=mdp)
    print("Is Connected ? ", pop_client.authentification())
    print("statistics: ", pop_client.get_statistics())
    mail_number: int = int(input(" Mail's number : "))
    print(f"statistic({mail_number})", pop_client.get_statistic(mail_number))
    print(f"mail({mail_number}): ", pop_client.get_mail(mail_number))
    pop_client.quit()
