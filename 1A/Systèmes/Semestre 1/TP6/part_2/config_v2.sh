#!/bin/bash
if [ $# -eq 1 ]
then
    sed -i "s/address 10.254.7.*/address 10.254.7.$1/" /etc/network/interfaces
    #systemctl restart networking.service
else
 echo "Vous devez donner en paramètre le dernier octet de l'adresse ip."
fi