<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>WEB2 TD1 EX2 : Formulaires POST</title>
	</head>
	<body>
		<?php 
		
		if(!empty($_POST) 
		&& isset($_POST["mail"]) 
		&& isset($_POST["pass"])
		&& isset($_POST["connect"])
		&& !empty($_POST["mail"]) 
		&& !empty($_POST["connect"]) 
		&& !empty($_POST["pass"])){
			var_dump($_POST);
			echo "<br/>";
			if($_POST["mail"] == "phil@free.fr" && $_POST["pass"] == "phil"){
				echo "Identification OK de l'utilisateur phil@free.fr";
			}else{
				echo "Echec de l'identification de l'utilisateur ".$_POST["mail"];
			}
		}

		?>
	</body>
</html>