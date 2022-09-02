#!/bin/bash
read -p "Veuillez saisir le nom d'utilisateur : " utilisateur
read -p "Veuillez saisir le mot de passe : " mot_de_passe
read -p "Veuillez saisir le nom du groupe : " groupe
useradd $utilisateur -b /home/test/$groupe -m -s /bin/bash -p `mkpasswd "$mdp"` -g $groupe