<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<title>EXO Tables Multiplication</title>
</head>
<body>

<?php
		  
    function table($val){
        echo '<table><tbody>';
        for ($i = 1; $i<=10; $i++){
            echo "<tr>";
            echo "<td>$val</td>";
            echo "<td>*</td>";
            echo "<td>$i</td>";
            echo "<td>=</td>";
            $eval = $i * $val;
            echo "<td>$eval</td>";
            echo "</tr>";
        }
        echo '</tbody></table>';
    }

    for ($i = 1; $i < 10; $i++){
        table($i);
        echo "<br/>";
    }
 ?>
</body></html>