# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:57:41 2021

@author: Philippe
"""

# coding: utf-8

import socket
import sys


hote = 'localhost'
port = 5000


try : 
    #Configuration du socket en serveur
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serveur.bind((hote, port))
    serveur.listen(1)
    
    
    #Attente Connexion
    print(f"Attente Connexion client {hote}:{port}")
    clientSocket, adresse = serveur.accept()
    
    #Reception
    buff :bytes
    buff = clientSocket.recv(100)
    message : str 
    message = buff.decode('utf-8')
    print(f"Reception du message client : {message} Socket du client {adresse}")
    
    #Envoi
    envoi : str = "Message Serveur vers Client\n"
    buff = envoi.encode('utf-8')
    clientSocket.send(envoi.encode('utf-8'))
    print(f"Emission vers le client {envoi}")
    
    #Deconnexion
    print(f"Deconnexion  {hote}:{port}.")
    clientSocket.shutdown(socket.SHUT_RDWR)
    clientSocket.close()
    #serveur.shutdown(socket.SHUT_RDWR)
    serveur.close()
    sys.exit()
    
except Exception as err:
         print(f"voici le message d'erreur {err}")

"""while True:
    try :
        clientsocket, adresse = serveur.accept()
        buff :bytes = clientsocket.recv(100)
        message : str = buff.decode('utf-8')
        print(message, adresse)
        clientsocket.sendall(f"Message du serveur vers le Client {hote}:{port}".encode('utf-8'))
    
    except KeyboardInterrupt:
        print(f"fermeture connection  {hote}:{port}.")
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
        serveur.shutdown(socket.SHUT_RDWR)
        serveur.close()
        sys.exit()
"""    
    
    