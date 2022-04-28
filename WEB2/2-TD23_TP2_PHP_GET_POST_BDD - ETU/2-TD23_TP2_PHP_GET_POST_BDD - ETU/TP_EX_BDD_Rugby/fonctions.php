<?php
	//****EX1************************************************************************************************************
	function afficheTableau($tab){
		echo '<table>';	
		echo '<tr>';// les entetes des colonnes qu'on lit dans le premier tableau par exemple
		foreach($tab[0] as $colonne=>$valeur){		echo "<th>$colonne</th>";		}
		echo "</tr>\n";
		// le corps de la table
		foreach($tab as $ligne){
			echo '<tr>';
			foreach($ligne as $cellule)		{		echo "<td>". utf8_decode($cellule)."</td>";		}
			echo "</tr>\n";
		}
		echo '</table>';
	}
?>

<?php
	//******************Connexion BD*************************************************************************************
	function connexionBD($db = "sqlite:bdd/joueurs.sqlite") {
		return new PDO($db);
	}
?>

<?php
	//****EX1*************************************************************************************************************
	function listerjoueurs() {
		try{
			$res = connexionBD()->query("select nomJoueur as Joueur, nomEquipe as Equipe from joueurs INNER JOIN equipes on equipes.numEquipe = joueurs.numEquipe");
			if($res){
				return $res->fetchAll(PDO::FETCH_ASSOC);
			}
		}catch(Exception){
		}
		return array();

	}
?>

<?php
	//****EX2*************************************************************************************************************
	function listeEquipeSelect(){
		try{
			$res = connexionBD()->query("select nomEquipe, numEquipe from equipes");
			if($res){
				$tab = $res->fetchAll(PDO::FETCH_ASSOC);
				if($tab){
					foreach($tab as $line){
						echo '<option value="'.$line["numEquipe"].'">'.$line["nomEquipe"].'</option>';
					}
				}
			}
		}catch(Exception){
		}
	}

	function afficheFormEquipe() {
	?>
	<h1> Sélectionner une Equipe pour afficher la liste des joueurs</h1>
	<form action="EX2listejoueursParEquipe.php" method="get">
		<fieldset>
			<select name="equipe">
				<option value="toutes">Toutes les Equipes</option>
				<?php
					// à faire : compléter la liste déroulante
					
					
					listeEquipeSelect()
					
				?>
			</select>
			<input type="submit" value="Afficher les joueurs"/>
		</fieldset>
	</form>
	<?php
	}
?>

<?php
	//****EX2*************************************************************************************************************
	function listerjoueursParEquipe($numEquipe) {
		
		try{
			$sql_ = "select nomJoueur as Joueur, nomEquipe as Equipe ";
			$base = " from joueurs INNER JOIN equipes on equipes.numEquipe = joueurs.numEquipe";
			if($numEquipe != "toutes"){
				$sql = $sql_.$base. " where equipes.numEquipe = $numEquipe";
			}else{
				$sql = $sql_.$base;
			}
			$res = connexionBD()->query($sql);
			if($res){
				return $res->fetchAll(PDO::FETCH_ASSOC);
			}
		}catch(Exception){
		}
		return array();
	}

	function nomEquipeParNum($num){
		try{
			$sql = "select nomEquipe from equipes where numEquipe = $num";
			$res = connexionBD()->query($sql);
			if($res){
				$val = $res->fetch(PDO::FETCH_ASSOC);
				return $val["nomEquipe"];
			}
			
		}catch(Exception){

		}
		return "Le numéro $num ne correspond pas à une équipe.";
	}
?>


<?php
	//****EX3 fourni*************************************************************************************************************
	function afficheFormulaireAjoutjoueur(){
	?>
	<h1>Insertion d'un nouveau joueur</h1>	    
	<form action="EX3_InsererJoueurs.php" method="post">
		<fieldset> 
			<label for="id_joueur">Nom joueur : </label>
			<input type="text" name="joueur" id="id_joueur" size="20" /><br />
			<label for="id_equipe">Nom equipe : </label>
			<select name="equipe" id="id_equipe">
				<?php
					// Afficher la liste des équipes
					
					listeEquipeSelect();
					
					
				?>
			</select><br />
			<input type="submit" value="Insérer"/>
		</fieldset>
	</form>
	<?php
	}
?>

<?php
	//****EX3*************************************************************************************************************
	function insererjoueur($joueur,$equipe){
		
		try{
			$db = connexionBD();
			$joueurSTR = $db->quote($joueur);

			$sql = "select nomJoueur from joueurs where nomJoueur = ".$joueurSTR." and numEquipe = ".$equipe;
			$res = $db->query($sql);

			if($res){

				$present = $res->fetch(PDO::FETCH_ASSOC);
				if(!$present){
					$sql = "insert into joueurs (nomJoueur, numEquipe) values ($joueurSTR, $equipe)";
					$res = $db->exec($sql);
					if($res){
						return array($joueur, $equipe);
					}
				}
			}
			
		}catch(Exception){
		}
		return False;
	}
	
?>



<?php


function navbar(){
	?>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container-fluid">
			<a class="navbar-brand" href="#">Menu</a>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
			<div class="navbar-nav">
				<a class="nav-link" href="EX1_ListerJoueurs.php">EX1</a>
				<a class="nav-link" href="EX2listejoueursParEquipe.php">EX2</a>
				<a class="nav-link" href="EX3_InsererJoueurs.php">EX3</a>
			</div>
			</div>
		</div>
	</nav>

<?php 
}
?>

