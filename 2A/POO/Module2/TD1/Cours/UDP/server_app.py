import socket
if __name__ == "__main__":
    # declaration des variables
    socket_ecoute_echange: socket = None
    port: int = None
    msg_client: str = None
    msg_serveur: str = None
    tab_bytes: bytes
    # initialisation
    port = 5000
    # créer le socket_echange UDP/IP
    socket_ecoute_echange = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # lier le socket au port d'écoute
    socket_ecoute_echange.bind(("", port))
    print(f"information socket locale : {socket_ecoute_echange}")
    print(f"serveur en ecoute sur le port {port}")
    # attente du message du client
    tab_bytes, ADDR = socket_ecoute_echange.recvfrom(255)
    print(f"adresse machine distante : {ADDR}")
    # affichage des information reçues:
    print(f"données brutes : {tab_bytes}")
    msg_client = tab_bytes.decode("utf-8")
    print(f"C=>S : {msg_client}")
    # préparation du message à envoyer
    msg_serveur = f"[{msg_client}]"
    tab_bytes = msg_serveur.encode("utf-8")
    # envoi du message :
    socket_ecoute_echange.sendto(tab_bytes, ADDR)
    # fermeture application
    socket_ecoute_echange.close()
