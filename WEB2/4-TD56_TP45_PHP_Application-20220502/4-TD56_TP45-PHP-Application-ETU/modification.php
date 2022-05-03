<?php session_start();?>
<?php 
	include 'fonctions.php';
	include 'formulaires.php';
?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<link href="style.css" rel="stylesheet" type="text/css" />
		<title>WEB2 TD56 TP45 PHP Une Application BDD HARTMANN_ETU 2021-2022 : Modification</title>
	</head>
	<body>
		<header>
			<h1>WEB2 TD56 TP45 PHP Une Application BDD BDD HARTMANN_ETU 2021-2022 : Modification</h1>
		</header>
		<nav>
			<?php
				if(empty($_SESSION) || !isset($_SESSION["statut"]) || $_SESSION["statut"] != "Prof"){
					echo "<p>Vous n'êtes pas autorisé sur cette page.</p>";
					echo '<script> setTimeout(function() {window.location.href="index.php"},2000);</script>';
				}else{
					afficheMenu($_SESSION["login"], $_SESSION["statut"]);
				}
			?>
		</nav>
		<article>
			<?php
				
				if(!empty($_GET) && isset($_GET["action"])){
					switch($_GET["action"]){
						case "supprimer_utilisateur":
							afficheFormulaireChoixUtilisateur("Supprimer");
							break;
						case "modifier_utilisateur":
							afficheFormulaireChoixUtilisateur("Modifier");
							break;
						default:
							echo "<h2>Cette page n'est pas reconnue</h2>";
					}
				}

				if(!empty($_POST) 
					&& isset($_POST["mail"])
					&& isset($_POST["valider"])
				){
					switch($_POST["valider"]){
						case "Supprimer":
							if(supprimerUtilisateur($_POST["mail"])){
								echo "<h2>L'utilisateur a bien été supprimé</h2>";
							}else{
								echo "<h2>L'utilisateur n'a pas pu être supprimé</h2>";
							}
							afficheTableau(listeCompte());
							break;
						case "Modifier":
							break;
					}
				}

				
				
			?>	
		</article>
		<footer>
			<p>Pied de la page <?php echo $_SERVER['PHP_SELF']; ?> </p>
			<a href="javascript:history.back()">Retour à la page précédente</a>
		</footer>
	</body>
</html>	

