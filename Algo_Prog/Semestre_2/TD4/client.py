# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:59:24 2021

@author: Philippe
"""

# coding: utf-8

import socket


hote = "localhost"
portServeur = 5000

"""
#hote = "iut-lannion.univ-rennes1.fr"
hote = "fakestoreapi.com"
port = 80
"""
#print(dir(socket))
try :
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((hote, portServeur))
    #clientSocket.sendall("GET /index.html HTTP/1.1 \n".encode('utf-8'))
    
    
    
    print(f"Connexion sur serveur {hote}:{portServeur}")
    print(f"Socket du client : {clientSocket.getsockname()}")
    
    envoi : str = "Message Client vers Serveur\n"
    clientSocket.send(envoi.encode('utf-8'))
    print(f"Emission vers le serveur : {envoi}")
    
    
    reception : bytes = clientSocket.recv(500)
    print(f"Reception du message client : {reception.decode('utf-8')}")
    
    
    # clientSocket.close()
    print(f"Deconnexion  {hote}:{portServeur}.")

except Exception as err :
    print(f"voici le message d'erreur {err}")

    
