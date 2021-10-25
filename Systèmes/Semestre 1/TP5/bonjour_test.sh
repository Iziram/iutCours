#!/bin/bash
if [ $# -eq 2 ]
then
    echo "Bonjour, Monsieur $1 $2" 
else
    echo "Erreur : la syntaxe doit être \"afficher votre_prénom votre_nom\""
fi