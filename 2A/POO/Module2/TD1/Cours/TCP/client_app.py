import socket
# declaration des variables
ip_serveur: str = None
port_serveur: int = None
socket_echange: socket = None
msg_client: str = None
msg_serveur: str = None
tab_bytes: bytes
# initialisation
ip_serveur = "127.0.0.1"
port_serveur = 5000
# instanciation d'un socket d'échange (AF_INET pour IPV4, SOCK_STREAM pour TCP)
socket_echange = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tentative de connexion au serveur
socket_echange.connect((ip_serveur, port_serveur))
print("Connecté au serveur")
# saisie du message
msg_client = input("votre message : ")
# envoi du message
tab_bytes = msg_client.encode("utf-8")
socket_echange.send(tab_bytes)
# attente de la réponse du serveur
tab_bytes = socket_echange.recv(255)
msg_serveur = tab_bytes.decode("utf-8")
# affichage de la réponse
print(tab_bytes)
print(f"S=>C : {msg_serveur}")
# fermeture de la connexion
print("Connexion fermée")
socket_echange.close()
