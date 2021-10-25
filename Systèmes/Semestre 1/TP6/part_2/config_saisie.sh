#!/bin/bash
read -p "Veuillez entrer le dernier octet de l'adresse ip : " octet
if [ -n "$octet" ]
then
    sed -i "s/address 10.254.7.*/address 10.254.7.$octet/" /etc/network/interfaces
    #systemctl restart networking.service
else
 echo "Vous devez donner le dernier octet de l'adresse ip."
fi