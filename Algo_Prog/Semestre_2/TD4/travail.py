import socket

class Client :
    # def __init__(self):
    #     self.clientSocket : None

    def connect(self, hote: str, portServeur:int):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((hote, portServeur))
        except Exception:
            print(f"Le client n'a pas pu se connecter au serveur demandé.")

    def sendMessage(self, message:str):
        try:
            self.clientSocket.send(message.encode('utf-8'))
        except Exception:
            print(f"Le message n'a pas pu être envoyé.")

    def receiveMessage(self) -> str:
        try:
            print('a')
            self.clientSocket.settimeout(60)
            reception : bytes = self.clientSocket.recv(500)
            print('b')
            message = reception.decode('utf-8')
            print('c')

            return message
        except Exception:
            print(f"Aucun message n'a pu être récuppéré.")


    def close(self):
        try:
            self.clientSocket.close()
        except Exception :
            print(f"La connection n'a pas pu être fermée ou bien elle l'était déjà.")

if __name__ == "__main__":
    message = input("Votre message: ")
    bob = Client()
    bob.connect("localhost", 5000)
    bob.sendMessage(message)
    print("debug")
    print(bob.receiveMessage())
    bob.close()