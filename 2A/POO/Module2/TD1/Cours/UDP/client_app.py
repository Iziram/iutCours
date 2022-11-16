import socket
if __name__ == "__main__":
    # declaration des variables
    ip_serveur: str = None
    port: int = None
    socket_echange: socket = None
    msg_client: str = None
    msg_serveur: str = None
    tab_bytes: bytes = None
    # initialisation
    ip_serveur = "127.0.0.1"
    port = 5000
    # Création d'un socket UDP
    socket_echange = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Saisie du message à envoyer
    msg_client = input("votre message : ")
    # envoi du message
    tab_bytes = msg_client.encode("utf-8")
    socket_ecoute.sendto(tab_bytes, (ip_serveur, port))
    # attente de la réponse du serveur
    tab_bytes, ADDR = socket_echange.recvfrom(255)
    # affichage de la réponse
    msg_serveur = tab_bytes.decode("utf-8")
    print(f"données brutes : {tab_bytes}")
    print(f"S=>C : {msg_serveur}")
    # fermeture de l'application
    socket_echange.close()
