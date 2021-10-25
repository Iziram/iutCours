#!/bin/bash
useradd $1 -b /home/test -m -s /bin/bash -p `mkpasswd $2`