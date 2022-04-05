<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>WEB2 TD12 EX5 : Formulaire dynamique & BDD ETUDIANTS</title>
	</head>
	<body>
		<h1>WEB2 TD12 EX5 : Formulaire dynamique & BDD ETUDIANTS</h1>   
		
		<?php	
			afficheFormulaireEtudiantParVille();
		?>
		
		<?php
			/* Définition des fonctions */ 
			function afficheFormulaireEtudiantParVille(){
				$bdd = new PDO("sqlite:bdd/IUT.sqlite");
				$res = $bdd->query("SELECT DISTINCT (e.insee), commune, cp FROM etudiants e INNER JOIN villes v
				ON e.insee=v.insee");
				if($res){
					$tab = $res->fetchAll(PDO::FETCH_ASSOC);
					if($tab){
					}
		?>
			<form action="" method="post">
				<label for="id_ville">Ville :</label> 
				<select id="id_ville" name="ville" size="1">
					<option value="0">Choisir une ville</option>
					<?php
						foreach($tab as $value){
							echo '<option value="'.$value["insee"].'">'.$value["cp"]." ".$value["commune"].'</option>';
						}
					?>
				</select>
				<input type="submit" value="Rechercher Etudiant par Ville"/>
			</form>
			<?php
				}
			}
				
		?>
		
		
		
		
		
		
		
	</body>
</html>