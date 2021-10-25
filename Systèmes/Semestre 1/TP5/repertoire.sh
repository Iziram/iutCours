#!/bin/bash
if [ -f "$1" ]
then
    echo "Erreur: il existe déjà un fichier comportant le même nom."
else
    if [ -d "$1" -o $# -ne 1 ]
    then
        echo "Erreur: il existe déjà un dossier comportant le même nom."
    else
        mkdir "$1"
    fi
fi