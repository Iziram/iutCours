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
	function connexionBD() {
		
	}
?>

<?php
	//****EX1*************************************************************************************************************
	function listerjoueurs() {
		
	}
?>

<?php
	//****EX2*************************************************************************************************************
	function afficheFormEquipe() {
	?>
	<h1> Sélectionner une Equipe pour afficher la liste des joueurs</h1>
	<form action="" method="get">
		<fieldset>
			<select name="equipe">
				<option value="toutes">Toutes les Equipes</option>
				<?php
					// à faire : compléter la liste déroulante
					
					
					
					
					
					
					
					
					
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
		
		
		
	}
?>
<?php
	//****EX2*************************************************************************************************************
	function getNomEquipeParNum($numEquipe) {
		
		
		
	}
?>


<?php
	//****EX3 fourni*************************************************************************************************************
	function afficheFormulaireAjoutjoueur(){
	?>
	<h1>Insertion d'un nouveau joueur</h1>	    
	<form action="" method="post">
		<fieldset> 
			<label for="id_joueur">Nom joueur : </label><input type="text" name="joueur" id="id_joueur" size="20" /><br />
			<label for="id_equipe">Nom equipe : </label>
			<select name="equipe">
				<?php
					// Afficher la liste des équipes
					
					
					
					
				?>
			</select><br />
			<input type="submit" value="Insérer"/>
		</fieldset>
	</form>
	<?php
	}// fin afficheFormulaireAjoutEtudiant
?>

<?php
	//****EX3*************************************************************************************************************
	function insererjoueur($joueur,$equipe){
		
		
		
	}
	
?>

