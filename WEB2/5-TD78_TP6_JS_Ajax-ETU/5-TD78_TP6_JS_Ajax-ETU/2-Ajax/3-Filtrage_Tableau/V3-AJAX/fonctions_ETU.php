<?php
//*******************************************************************************************
function afficheTableau($tab){
	echo '<table>';	
	echo '<tr>';// les entetes des colonnes qu'on lit dans le premier tableau par exemple
	foreach($tab[0] as $colonne=>$valeur){		echo "<th>$colonne</th>";		}
	echo "</tr>\n";
	// le corps de la table
	foreach($tab as $ligne){
		echo '<tr>';
		foreach($ligne as $cellule)		{		echo "<td>$cellule</td>";		}
		echo "</tr>\n";
		}
	echo '</table>';
}





//*********************************************************************************************
function listeEtudiantParVille($insee){
$retour=false;




return $retour;
}


 ?>

