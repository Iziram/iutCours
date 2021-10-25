#!/bin/bash
if [ $# -eq 1 ]
then
    addr=$(cat /etc/network/interfaces | grep -e "address \K([0-9]{1,3}\.){3}" -oP)
    sed -i "s/address $addr*/address $addr$1/" /etc/network/interfaces
    #systemctl restart networking.service
else
 echo "Vous devez donner en paramètre le dernier octet de l'adresse ip."
fi
