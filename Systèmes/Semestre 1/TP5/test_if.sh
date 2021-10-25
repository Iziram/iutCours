#!/bin/bash
if [ -w "$1" ]
then
    gedit "$1"&
else
    echo "Erreur: Vous ne disposez pas des droits d'écriture de ce fichier."
fi
