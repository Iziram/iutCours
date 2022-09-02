#!/bin/bash

if [ $# -eq 3 ]
then
    useradd $1 -b /home/test/$3 -m -s /bin/bash -p `mkpasswd $2` -g "$3"
else
    echo "Erreur: la syntaxe doit être $0 nom_utilisateur mot_de_passe nom_du_groupe"
fi