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
function listeEtudiantParVille($No_ville){
$retour=false;
		$madb = new PDO('sqlite:bdd/IUT.sqlite');
		$No_ville = $madb->quote($No_ville);	
		$requete = "SELECT mail, adresse, commune FROM etudiants e, villes v WHERE v.insee= $No_ville AND e.insee = v.insee" ;//	var_dump($requete); echo "<br/>";  
		$resultat = $madb->query($requete);
		$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);//var_dump($tableau_assoc);echo "<br/>";   
		if (sizeof($tableau_assoc)!=0) $retour = $tableau_assoc;
return $retour;
}


 ?>

