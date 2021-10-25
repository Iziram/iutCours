#!/bin/bash
read -p "Veuillez saisir le nom d'utilisateur : " utilisateur
read -p "Veuillez saisir le mot de passe : " mot_de_passe
useradd $utilisateur -b /home/test -m -s /bin/bash -p `mkpasswd "$mdp"`