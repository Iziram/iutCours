#!/bin/bash
groupadd compta
groupadd client
useradd compta1 -b /home/test/compta -m -s /bin/bash -p `mkpasswd lannion` -g compta
useradd compta2 -b /home/test/compta -m -s /bin/bash -p `mkpasswd lannion` -g compta
useradd client1 -b /home/test/client -m -s /bin/bash -p `mkpasswd lannion` -g client
useradd client2 -b /home/test/client -m -s /bin/bash -p `mkpasswd lannion` -g client