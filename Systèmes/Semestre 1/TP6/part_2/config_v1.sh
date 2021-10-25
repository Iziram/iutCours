#!/bin/bash
echo "auto eth0">/etc/network/interfaces
echo "inface eth0 inet static">>/etc/network/interfaces
echo "address 10.254.7.2">>/etc/network/interfaces
echo "network 10.254.0.0">>/etc/network/interfaces
echo "netmask 255.255.0.0">>/etc/network/interfaces
echo "broadcast 10.254.255.255">>/etc/network/interfaces
echo "gateway 10.254.0.254">>/etc/network/interfaces
