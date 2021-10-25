#!/bin/bash
if [ $# -eq 2 ]
then
    echo "Bonjour, Monsieur $1 $2" 
else
    echo "Erreur : la syntaxe doit être \"$0 votre_prénom votre_nom\""
fi