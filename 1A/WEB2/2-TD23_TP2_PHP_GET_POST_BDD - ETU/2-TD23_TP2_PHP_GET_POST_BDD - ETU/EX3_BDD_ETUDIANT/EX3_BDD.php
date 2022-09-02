<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>WEB2 TD12 EX3 : Liste BDD ETUDIANTS</title>
	</head>
	<body>
		<h1>WEB2 TD12 EX3 : Liste BDD ETUDIANTS</h1>   
		<h2>Liste tous les étudiants</h2>  
		<?php  
			
			function listeEtudiants(){
				try{
					$bdd = new PDO("sqlite:bdd/IUT.sqlite");
					//$res = $bdd->query("select * from etudiants");
					$res = $bdd->query("select * from etudiants INNER JOIN villes on etudiants.insee = villes.insee");
					if($res){
						return $res->fetchAll(PDO::FETCH_ASSOC);
					}
				}catch(Exception $e){
					echo "Erreur : ".$e->getMessage();
				}
				return False;
			}
			$liste = listeEtudiants();
			if($liste){
				afficheTableauHTML($liste);
			}
			
		?>
		<h2>Teste les étudiants</h2>  
		<?php
			// test fonction utilisateurExiste
				$nom = "etu@etu.fr";
				$pass = "etu";
				$test = utilisateurExiste($nom,$pass);
				if ($test) echo '<p>'.$nom." : ".$pass.' existe</p>';
				else echo '<p>'.$nom." : ".$pass.' n\'existe pas</p>';
				
				$nom = "titi@etu.fr";
				$pass = "etu";
				$test = utilisateurExiste($nom,$pass);
				if ($test) echo '<p>'.$nom." : ".$pass.' existe</p>';
				else echo '<p>'.$nom." : ".$pass.' n\'existe pas</p>';
				
		?>
		<h2>Insère un étudiant</h2>  
		<?php	
				$nom = "titi@etu.fr";
				$pass = "etu";
				$test = insereUtilisateur($nom,$pass,"Rue de Perros Guirec","22300","Lannion");
				if ($test) echo '<p>Insertion réussie de '.$nom." : ".$pass.'</p>';	
				else echo '<p>ERREUR Insertion '.$nom." : ".$pass.' soit la ville n\'existe pas soit l\'utilisateur existe déjà</p>';	
				
			
			
			
			
			
			//****************************************************************************************   
			function utilisateurExiste($login,$pass){ 
				$bdd = new PDO("sqlite:bdd/IUT.sqlite");
				$res = $bdd->query("select * from etudiants where mail='$login' and mdp='$pass'");
				if($res){
					$tab = $res->fetch(PDO::FETCH_ASSOC);
					if(!$tab){
						return False;
					}else{
						return True;
					}
				}
			}		
			
			//****************************************************************************************   
			function insereUtilisateur($login,$pass,$rue,$codepostal,$ville){ 
				$bdd = new PDO("sqlite:bdd/IUT.sqlite");
				$ville = strtoupper($ville);
				$res = $bdd->query("select insee from villes where commune='$ville' and cp='$codepostal'");
				if($res){
					$tab = $res->fetch(PDO::FETCH_ASSOC);
					if($tab){
						try{
							$sql = "insert into etudiants (mail,mdp,adresse) values (".$bdd->quote($login).",".$bdd->quote($pass).",".$bdd->quote($rue).",".$tab["insee"].")";
							$res = $bdd->exec($sql);
							if($res){
								return True;
							}
						}catch(Exception){
							return False;
						}
					}
				}
				return False;
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
	</body>
</html>