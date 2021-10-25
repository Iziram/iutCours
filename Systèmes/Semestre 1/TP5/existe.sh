#!/bin/bash
if [ $# -eq 1 ]
then 
    cat /etc/passwd | grep -q "$1" &&  echo "Cet utilisateur existe." || echo "Cet utilisateur n'existe pas."
else
    echo "Veuillez donner en paramètre un nom d'utilisateur."
fi
