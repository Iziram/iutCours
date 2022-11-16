import socket
if __name__ == "__main__":

    # Process d'écoute
    # declaration des variables
    port_ecoute: int = None
    socket_ecoute: socket = None
    socket_echange: socket = None
    msg_client: str = None
    msg_serveur: str = None
    tab_bytes: bytes = None
    # initialisation
    port_ecoute = 5000
    # instanciation d'un socket d'écoute (AF_INET pour IPV4, SOCK_STREAM pour TCP)
    socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # liaison du socket avec le couple @IP/port "" : toutes les @IP de la machine.
    socket_ecoute.bind(("localhost", port_ecoute))
    # mise en ecoute avec le nombre de connexion simultanées possibles
    socket_ecoute.listen(1)
    print(f"serveur en ecoute sur le port {port_ecoute} ...")
    # attente d'une demande de connexion
    socket_echange, ADDR = socket_ecoute.accept()  # bloquante
    # fermeture de l'ecoute (ici gestion d'un seul client)
    socket_ecoute.close()

    while msg_client != "fin":
        tab_bytes = socket_echange.recv(255)
        msg_client = tab_bytes.decode("utf-8")

        msg_serveur = f"Reply: |{msg_client}|"
        tab_bytes = msg_serveur.encode("utf-8")
        socket_echange.send(tab_bytes)

    msg_serveur = "kill"
    tab_bytes = msg_serveur.encode("utf-8")
    socket_echange.send(tab_bytes)

    socket_echange.close()
