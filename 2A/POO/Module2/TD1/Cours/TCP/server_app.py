import socket
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
socket_ecoute.bind(("", port_ecoute))
# mise en ecoute avec le nombre de connexion simultanées possibles
socket_ecoute.listen(1)
print(f"serveur en ecoute sur le port {port_ecoute} ...")
# attente d'une demande de connexion
socket_echange, ADDR = socket_ecoute.accept()  # bloquante
# fermeture de l'ecoute (ici gestion d'un seul client)
socket_ecoute.close()
print("une nouvelle demande de connexion")
# affichage des information de la machine distante
print(f"sochet echange : {socket_echange}")
print(f"adr : {ADDR}")
# attente d'un message du client
print("en attente d'un message ...")
tab_bytes = socket_echange.recv(255)  # 255 octets maxi blooquante
# affichage du résultat brut
print(tab_bytes)
# mise en forme et affichage du message du client
msg_client = tab_bytes.decode("utf-8")
print(f"C => S : {msg_client}")
# preparation de la réponse
msg_serveur = f"[{msg_client}]"
# envoi de la réponse
tab_bytes = msg_serveur.encode("utf-8")
socket_echange.send(tab_bytes)
# attente dernier message du client (lors de la fermeture du client)
socket_echange.recv(255)  # 255 octets maxi bloquante
# fermeture de la socket échange
print(f"Connexion fermée")
socket_echange.close()
