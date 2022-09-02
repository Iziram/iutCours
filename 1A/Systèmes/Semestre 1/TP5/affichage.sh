#!/bin/bash
echo "----Fichiers----"
ls -al $1 | grep ^-
echo "----Répertoires----"
ls -al $1 | grep ^d
