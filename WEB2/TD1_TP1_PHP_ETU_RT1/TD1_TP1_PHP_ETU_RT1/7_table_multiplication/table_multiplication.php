<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<title>EXO Tables Multiplication</title>
</head>
<body>

<?php
		  
    function table($val){
        //On créé un tableau html sans entête
        echo '<table><tbody>';
        //On fait une boucle for pour parcourir les chiffres de 1 à 10
        for ($i = 1; $i<=10; $i++){
            //Pour chaque chiffre on créé une ligne puis on donne les valeurs
            echo "<tr>";
            //Le chiffre de la table
            echo "<td>$val</td>";
            //Le symbole multiplier
            echo "<td>*</td>";
            //le chiffre à multiplier
            echo "<td>$i</td>";
            //le symbole égal
            echo "<td>=</td>";
            $eval = $i * $val;
            //le résultat de $i fois $val
            echo "<td>$eval</td>";
            echo "</tr>";
        }
        //On ferme le tableau
        echo '</tbody></table>';
    }
    //On utilise la fonction table pour chaque chiffre de 1 à 9
    for ($i = 1; $i < 10; $i++){
        table($i);
        echo "<br/>";
    }
 ?>
</body></html>