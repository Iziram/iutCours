#!/bin/bash

if [ $# -eq 2 ]
then
    useradd $1 -b /home/test -m -s /bin/bash -p `mkpasswd $2`
else
    echo "Erreur: la syntaxe doit être creation_verif nom_utilisateur mot_de_passe"
fi