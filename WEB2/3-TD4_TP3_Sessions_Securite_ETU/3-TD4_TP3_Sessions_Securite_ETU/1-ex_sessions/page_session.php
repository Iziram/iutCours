<?php session_start();?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>TD3 Sessions</title>
	</head>
	<body>

		<?php
		
		if(empty($_SESSION)){
			?>
			<p><a href="frm_cnx_sessions.php">Vous êtes déconnecté, cliquer pour retourner à la page accueil</a></p>
			<?php
		}else{		
		echo " Bonjour ".$_SESSION["login"]." Vous êtes ".$_SESSION["statut"];
			?>
			<p><a href="frm_cnx_sessions.php?action=logout">Se déconnecter et retourner à la page accueil</a></p>
			<?php
		}

		?>
		
		
		
		<body>
		</html>		