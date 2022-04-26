<!DOCTYPE html>
<html lang="fr" >
	<head>
		<?php  
			include 'EX4_BDD_Fonctions.php';
		?>
		<meta charset="utf-8">
		<title>WEB2 TD12 EX4 : Formulaires & BDD ETUDIANTS</title>
	</head>
	<body>
		<h1>WEB2 TD12 EX4 : Formulaires & BDD ETUDIANTS</h1>   
		
		<?php	
			if (!empty($_POST) && isset($_POST["mail"]) && isset($_POST["pass"]) && $_POST["mail"]!="" && $_POST["pass"]!="")	{
				/********** Nous affichons le contenu de la variable $_POST ***********/	
			?>
			<h2>Voici la liste des paramètres reçus via HTTP par le Formulaire : </h2>
			<?php
				var_dump($_POST);
				
				if ( utilisateurExiste($_POST["mail"],$_POST["pass"]) )				
				echo "<h3>Identification OK de l'utilisateur ".$_POST["mail"]."</h3>";
				else {// sinon on affiche un message d'erreur
					echo "<p>Erreur d'identification de l'utilisateur ".$_POST["mail"]."</p>";
				?>	
				<a href="javascript:history.back()">Retour à la page d'authentification</a>
				<?php
				}	// fin else	
			}
		?>
		
	</body>
</html>