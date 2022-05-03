<?php
	//******************************************************************************
	function afficheFormulaireConnexion(){// fourni
	?>
	<form id="form1" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<fieldset>
			<legend>Formulaire de connexion</legend>	
			<label for="id_mail">Adresse Mail : </label><input type="email" name="login" id="id_mail" placeholder="@mail" required size="20" /><br />
			<label for="id_pass">Mot de passe : </label><input type="password" name="pass" id="id_pass" required size="10" /><br />
			<input type="submit" name="connect" value="Connexion" />
		</fieldset>
	</form>
	<?php
	}
	
	//******************************************************************************
	function afficheMenu($login, $statut = "Etudiant"){	// à compléter
		echo '<p>votre login est '.$login.'</p>';
	?>
	<ul>
		<li><a href="index.php?action=liste_utilisateur" title="Lister les utilisateurs">Lister les utilisateurs</a></li>
		<li><a href="index.php?action=liste_utilisateur_ville" title="Lister les utilisateurs par villle">Lister les utilisateurs par ville</a></li>	
		<?php
		if($statut == "Prof"){
			?>
			<li><a href="insertion.php?action=inserer_utilisateur" title="Insérer un utilisateur">Insérer un utilisateur</a></li>	
		<li><a href="modification.php?action=supprimer_utilisateur" title="Supprimer un utilisateur">Supprimer un utilisateur</a></li>	
		<li><a href="modification.php?action=modifier_utilisateur" title="Modifier un utilisateur">Modifier un utilisateur</a></li>
		<?php
		}
		?>	
	</ul>				
	<p><a href="index.php?action=logout" title="Déconnexion">Se déconnecter</a></p>
	
	<?php
	}
	
	
	//******************************************************************************
	function afficheFormulaireUtilisateurParVille(){
		echo "<br/>";
		// CNX BDD + REQUETE pour obtenir les villes correspondantes à des utilisateurs
		$retour = listeVille();
		
		
		
		
		
	?>
	<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<fieldset> 
			<label for="id_ville">Ville :</label> 
			<select id="id_ville" name="ville" size="1">
				<?php // générer la liste des options à partir de $villes
					
					foreach($retour as $key){
						echo '<option value="'.$key["Insee"].'">'.$key["Commune"].'</option>';
					}
					
					
					
					
				?>
			</select>
			<input type="submit" value="Rechercher Utilisateur par Ville"/>
		</fieldset>
	</form>
	<?php
		echo "<br/>";
	}// fin afficheFormulaireUtilisateurParVille
	
	
	//******************************************************************************
	function afficheFormulaireAjoutUtilisateur(){
		
		$retour = listeVille();
	?>
	<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<fieldset> 
			<label for="id_mail">Adresse Mail : </label><input type="email" name="mail" id="id_mail" placeholder="@mail" required size="20" /><br />
			<label for="id_pass">Mot de passe : </label><input type="password" name="pass" required id="id_pass" size="10" /><br />
			<label for="id_status">Status :</label> 
			<input type="radio" name="status" value="etudiant" checked> Etudiant 
			<input type="radio" name="status" value="prof" > Prof<br/>
			<label for="id_rue">Rue : </label><input type="text" name="rue" id="id_rue" placeholder="adresse" required size="20" /><br />
			<label for="id_ville">Ville :</label> 
			<select id="id_ville" name="ville_etu" size="1">
				<?php // on se sert de value directement pour l'insertion
					
					foreach($retour as $key){
						echo '<option value="'.$key["Insee"].'">'.$key["Commune"].'</option>';
					}
					
					
				?>
			</select>
			<input type="submit" value="Insérer"/>
		</fieldset>
	</form>
	<?php
		echo "<br/>";
	}// fin afficheFormulaireAjoutUtilisateur
	
	
	//******************************************************************************
	function afficheFormulaireChoixUtilisateur($choix){
		
		$retour = array();
		try{
			$bd = new PDO("sqlite:bdd/iut.sqlite");

			$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
			$requete = "SELECT Email FROM utilisateurs";

			$res = $madb->query($requete);
			if($res){
				$tab = $res->fetchAll(PDO::FETCH_ASSOC);
				if($tab){
					$retour = $tab;
				}
			}
		}catch(Exception){

		}
	?>
	<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
		<fieldset> 
			<select id="id_mail" name="mail" size="1">
				<?php // on se sert de value directement 
					
					foreach($retour as $key){
						echo "<option value=\"".$key["Email"]."\">".$key["Email"]	."</option>";
					}
					
					
				?>
			</select>
			
			<input type="submit" value="<?php echo $choix; ?>" name="valider"/>
			
			
		</fieldset>
	</form>
	<?php
		echo "<br/>";
	}// fin afficheFormulaireChoixUtilisateur
	
	
	//*******************************************************************************************
	function afficheFormulaireModificationUtilisateur($mail){
		
		
		
	}// fin afficheFormulaireChoixUtilisateur
?>