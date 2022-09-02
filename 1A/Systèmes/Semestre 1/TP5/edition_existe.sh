#!/bin/bash
if [ -f "$1" ]
then
    gedit "$1"&
else
    echo "Erreur: le fichier $1 n'existe pas"
fi
