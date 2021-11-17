#! /bin/bash
path="/home/iziram/Documents/GitHub/iutCours/SAE_15/TP_1/Tmp/"
for i in $(ls $path)
do
    file=$path$i
    if test -f $file;
    then
        depoch=$(date +%s)
        tailleD=$(du $file -k | cut -f 1);
        echo "$i,$tailleD,$depoch"
    fi;
done

exit 0;