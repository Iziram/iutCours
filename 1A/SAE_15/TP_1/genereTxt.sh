path="/home/iziram/Documents/GitHub/iutCours/SAE_15/TP_1/Tmp/"
for i in $(ls $path)
do
    if test -f $path$i;
    then
        txt=""
        typeset -i nbT=$RANDOM
        typeset -i j=0
        while test $j -lt $nbT;
        do
            txt="${txt}a";
            j=$j+1;
        done
        echo "$txt" >> $path$i
    fi;
done
exit 0;