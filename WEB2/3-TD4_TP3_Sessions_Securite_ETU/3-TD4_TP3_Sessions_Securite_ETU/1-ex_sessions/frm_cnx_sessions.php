<?php session_start();?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>TD3 Sessions</title>
	</head>
	<body>
		
		
		<?php // si absence de session on affiche formulaire
		var_dump($_SESSION);
		var_dump($_POST);
		traitementDeconnexion();
		traitementFormulaire();
			if(empty($_SESSION)){
				?>
		
		<form id="conn" method="post" action="">
			<p><label for="login">Login :</label><input type="text" id="login" name="login" /></p>
			<p><label for="pass">Mot de Passe :</label><input type="password" id="pass" name="pass" /></p>
			<p><input type="submit" id="submit" name="submit" value="Connexion" /></p>
		</form>
		<?php
			}else{
				?>
				<h1>Accueil depuis la page initiale</h1>
					<a href="page_session.php">Lien vers la section membre</a>
					<?php
						traitementSession();
					?>		
					<p><a href="frm_cnx_sessions.php?action=logout">Se déconnecter</a></p>
					<?php
			}
		?>
		
		
		
		
		
		<?php

			//traitement de l'affichage des données de la session
			function traitementSession(){
				if(!empty($_SESSION)){
					?>
				<ul>
					<?php
					foreach($_SESSION as $key => $val){
						echo "<li>$key : $val</li>";
					}
					?>
				</ul>
				<?php
				}
				
			}
			//Traitement du formulaire
			function traitementFormulaire(){
				if (!empty($_POST) && isset($_POST['login']) && isset($_POST['pass']))	{		
					if ( utilisateurExiste($_POST["login"],$_POST["pass"]) ){
						$_SESSION["login"] = $_POST["login"];
						$_SESSION["pass"] = $_POST["pass"];
						
						if($_POST["login"] == "admin"){
							$_SESSION["statut"] = "Prof";
	
						}else{
							$_SESSION["statut"] = "Etudiant";
						}
					}
				}
			}
			// traitement de la fermeture de la session
			function traitementDeconnexion(){
				if(!empty($_GET) && isset($_GET["action"]) && $_GET["action"] == "logout"){
					$_SESSION = array();
					session_destroy();
				}
			}
			
			
			
			//****************************************************************************************   
			function utilisateurExiste($login,$pass){ 
				try {
					$retour = false;
					$madb = new PDO('sqlite:bdd/IUT.sqlite');			
					$requete = "SELECT * FROM etudiants WHERE mail = '".$login."' AND mdp = '".$pass."'";
					//var_dump($requete);
					$resultat = $madb->query($requete);
					$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);
					//var_dump($tableau_assoc );	
					if (sizeof($tableau_assoc)!=0) {	// s'il y a une réponse	=> utilisateur éxiste
						$retour = true;
					}// fin if
				}// fin try
				catch (Exception $e) {		
					echo "Erreur BDD" . $e->getMessage();		
				}	// fin catch	
				return $retour;
			}		
		?>
		
		
		</body>
		</html>		