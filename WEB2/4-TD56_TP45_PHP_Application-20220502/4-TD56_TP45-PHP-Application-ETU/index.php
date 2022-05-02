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
		<title>WEB2 TD56 TP45 PHP Une Application BDD BDD HARTMANN_ETU 2021-2022</title>
	</head>
	<body>
		<header>
			<h1>WEB2 TD56 TP45 PHP Une Application BDD HARTMANN_ETU 2021-2022</h1>
		</header>
		<nav>
			<?php
				
				
				// affichage du formulaire de connexion ou le menu avec le nom de la personne
				
				if(!empty($_SESSION) && isset($_SESSION["login"]) && isset($_SESSION["statut"])){
					afficheMenu($_SESSION["login"], $_SESSION["statut"]);
				}else{
					afficheFormulaireConnexion();
				}
				
				
				// test de la connexion
				
				if(!empty($_POST) && isset($_POST["login"]) && !empty($_POST["login"])
				&& isset($_POST["pass"]) && !empty($_POST["pass"])
				){
					$login = formater_saisie($_POST["login"]);
					$pass = formater_saisie($_POST["pass"]);
					if(compteExiste($login, $pass)){
						$_SESSION["login"] = $login;
						$_SESSION["statut"] = isAdmin($login) ? "Prof" : "Etudiant";

						echo "<script>window.location.href =\"index.php\"</script>";
					}else{
						echo "<p>Utilisateur introuvable  ou mot de passe incorrect</p>";
					}
				}

				// Destruction de la session 
				
				if(!empty($_GET) && isset($_GET["action"]) && $_GET["action"] == "logout"){
					$_SESSION = array();
					session_destroy();
					echo "<script>window.location.href =\"index.php\"</script>";
				}
				
				
			?>
		</nav>
		<article>
			
			<?php
				// Affichage du message accueil en fonction de la connexion
				if(!empty($_SESSION) && isset($_SESSION["login"])){
					echo "<h1>Vous êtes connecté comme ".$_SESSION["login"]."</h1>";
				}else{
					echo '<h1>Vous êtes déconnectés</h1>';
				}
				
				
				// traitement de la zone centrale de la page en fonction des liens GET du menu s'il y a une session
				if (!empty($_SESSION) && !empty($_GET) && isset($_GET["action"]) ){
					switch($_GET["action"])
					{
						case "liste_utilisateur":	
							echo '<h1>Liste des utilisateurs</h1>';
							afficheTableau(listeCompte());
							break;
						case "liste_utilisateur_ville":	
							echo '<h1>Lister les utilisateurs par villle</h1>';
							afficheFormulaireUtilisateurParVille();
							break;
					}
				}
				// traitement du premier formulaire interne de recherche par ville	
				
				if (!empty($_SESSION) && !empty($_POST) && isset($_POST["ville"]) ){
					$ville = formater_saisie($_POST["ville"]);

					afficheTableau(listeUtilisateurParVille($ville));
				}
				
				
			?>
		</article>
		<footer>
			<p>Pied de la page <?php echo $_SERVER['PHP_SELF']; ?></p>
			<a href="javascript:history.back()">Retour à la page précédente</a>
		</footer>
	</body>
</html>


