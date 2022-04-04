<!DOCTYPE html>
<html lang="fr" >
	<head>
		
		<meta charset="utf-8">
		<title>WEB2 TD12 EX4 : Formulaires & BDD ETUDIANTS</title>
	</head>
	<body>
		<h1>WEB2 TD12 EX4 : Formulaires & BDD ETUDIANTS</h1>   
		
		<?php	
			
			include("fonctions.php");
			$erreur = "Erreur Identification";
			if(!empty($_POST) 
			&& isset($_POST["mail"])
			&& isset($_POST["pass"])
			&& !empty($_POST["mail"])
			&& !empty($_POST["pass"])){

				if(utilisateurExiste($_POST["mail"], $_POST["pass"])){
					echo "Identification OK";
				}else{
					echo $erreur;
				}

			}else{
				echo $erreur;
			}
			
			
			
		?>
		
	</body>
</html>