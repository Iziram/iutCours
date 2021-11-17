#! /bin/bash

tailleD=$(du /home/iziram -s | cut -f 1)

depoch=$(date +%s)
echo "$tailleD,$depoch" >> /tmp/resTest
exit 0