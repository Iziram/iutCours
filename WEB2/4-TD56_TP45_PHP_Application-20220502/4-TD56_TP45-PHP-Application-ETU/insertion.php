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
		<title>WEB2 TD56 TP45 PHP Une Application BDD NOM_ETU 2021-2022 : Insertion</title>
	</head>
	<body>
		<header>
			<h1>WEB2 TD56 TP45 PHP Une Application BDD BDD NOM_ETU 2021-2022 : Insertion</h1>
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
				
				if(empty($_SESSION) || !isset($_SESSION["statut"]) || $_SESSION["statut"] != "Prof"){
					echo "<p>Vous n'êtes pas autorisé sur cette page.</p>";
				}else{
					echo "<h1>Bienvenue".$_SESSION["login"]." sur la page d'Insertion</h1>";
					afficheFormulaireAjoutUtilisateur();
				}

				if(!empty($_POST) 
		&& isset($_POST["mail"])
		&& isset($_POST["pass"])
		&& isset($_POST["status"])
		&& isset($_POST["rue"])
		&& isset($_POST["ville_etu"])
		){

			if(ajoutUtilisateur(
				$_POST["mail"],
				$_POST["pass"],
				$_POST["rue"],
				$_POST["ville_etu"],
				$_POST["status"]
			)){
				afficheTableau(listeCompte());
			}else{
				echo "<h2>L'utilisateur n'a pas été ajouté</h2>";
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

