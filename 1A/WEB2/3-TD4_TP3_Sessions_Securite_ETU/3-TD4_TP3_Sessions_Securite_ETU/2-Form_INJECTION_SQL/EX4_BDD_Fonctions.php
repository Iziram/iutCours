<?php
	function listeEtudiants(){
		try {
			$retour = array();
			
			$madb = new PDO('sqlite:bdd/IUT.sqlite');	
			// $requete = "SELECT * FROM etudiants";	
			$requete = "SELECT * FROM etudiants e INNER JOIN villes v ON e.insee = v.insee";
			$resultat = $madb->query($requete);
			$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);
			//var_dump($tableau_assoc );	
			if (sizeof($tableau_assoc)!=0) {		
				$retour = $tableau_assoc;
			}// fin if
		}// fin try
		catch (Exception $e) {		
			echo "Erreur BDD" . $e->getMessage();		
		}	// fin catch	
		return $retour;
	}
	
	//****************************************************************************************   
	function utilisateurExiste($login,$pass){ 
		try {
			$retour = false;
			$madb = new PDO('sqlite:bdd/IUT.sqlite');	
			
			$requete = "SELECT * FROM etudiants WHERE mail = ".$madb->quote($login)." AND mdp = ".$madb->quote($pass)."";
			var_dump($requete);
			$resultat = $madb->query($requete);
			$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);
			//var_dump($tableau_assoc );	
			if (sizeof($tableau_assoc)!=0) {	// s'il y a une réponse	=> utilisateur éxiste
				echo "<h3>On affiche les données du compte car il est connecté !!!!!! avec ".$_POST["mail"]." && ".$_POST["pass"]."</h3>";
				foreach ($tableau_assoc as $compte)      { 
					echo '<p>'.$compte["mail"]." | ";
					echo $compte["mdp"]." </p> ";		
				}	
				$retour = true;
			}// fin if
		}// fin try
		catch (Exception $e) {		
			echo "Erreur BDD" . $e->getMessage();		
		}	// fin catch	
		return $retour;
	}		
	
	
	//****************************************************************************************   
	function afficheTableauHTML($tab){   
		echo '<table>';
		// les entetes des colonnes qu'on lit dans le premier tableau par exemple
		echo '<tr>';
		foreach($tab[0] as $cle=>$valeur){
			echo "<th>$cle</th>";
		}
		echo "</tr>\n";
		// le corps de la table
		foreach($tab as $ligne){
			echo '<tr>';
			foreach($ligne as $valeur)      {
				echo "<td>$valeur</td>";
			}
			echo "</tr>\n";
		}
		echo '</table>';
		echo '<hr/>';
	}		
	
?>
