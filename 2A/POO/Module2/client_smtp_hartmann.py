from socket import socket, AF_INET, SOCK_STREAM


class SMTPClient:
    # Méthodes
    def __init__(self, server: str, source: str, port: int = 25) -> None:
        self.__server: str = server
        self.__source: str = source
        self.__socket: socket = socket(AF_INET, SOCK_STREAM)
        self.__port: int = port

    def ok_from_server(self, message: str) -> bool:
        return message.startswith("2")

    def send_command(self, command: str) -> None:
        if not command.endswith("\r\n"):
            command += "\r\n"

        tab_bytes: bytes = command.encode("utf-8")
        self.__socket.send(tab_bytes)
        print("Send :", command)

    def receive(self) -> str:
        string: str = "erreur"
        tab_bytes: bytes = self.__socket.recv(4098)
        string = tab_bytes.decode("utf-8")
        print(string)
        return string

    def connect_to(self) -> bool:
        authenticated: bool = False
        server_message: str
        self.__socket.connect((self.__server, self.__port))
        server_message = self.receive()
        domain: str = self.__source[self.__source.index("@") :]
        if self.ok_from_server(server_message):
            self.send_command(f"HELO {domain}")
            server_message = self.receive()
            if self.ok_from_server(server_message):
                authenticated = True

        return authenticated

    

    def send_mail(
        self, destination: str, copy: str, subject: str, message: str
    ) -> None:
        content : list[str] = [
            f"From: {self.__source}",
            f"To: {destination}",
            f"Cc: {copy}",
            f"Subject: {subject}",
            f"{message}",
            "\r\n.\r\n"
        ]

        self.send_command(f"MAIL FROM: {self.__source}")
        self.send_command(f"RCPT TO: {destination}")
        self.send_command("DATA")
        self.receive()
        for msg in content:
            self.send_command(msg)

    def quit(self) -> None:
        self.send_command("QUIT")
        if self.receive().startswith("+OK"):
            self.__socket.close()


if __name__ == "__main__":
    serv_addr: str = "148.60.235.240"
    source: str = "RT-G021-10@mail.gtr"

    copy: str = source
    destination: str = "RT-G020-12@mail.gtr"
    message: str = "Bonjour valentin,\n je teste ce super message\naurevoir"


    smtp_client: SMTPClient = SMTPClient(server=serv_addr, source=source)
    print("Is Connected ? ", smtp_client.connect_to())

    smtp_client.send_mail(destination, copy, "essay", message)

    smtp_client.quit()
