<?php
function afficheFormulaireEtudiantParVilleAJAX(){
	$madb = new PDO('sqlite:bdd/IUT.sqlite');	
	$requete = 'SELECT DISTINCT (e.insee), commune, cp FROM etudiants e, villes v WHERE e.insee=v.insee';
	$resultat = $madb->query($requete);//var_dump($resultat);echo "<br/>";  
	$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);	//var_dump($tableau_assoc);echo "<br/>"; 

?>
<form id="form1" action="<?php echo $_SERVER['PHP_SELF']; ?>"  method="get">
<fieldset> 
<label for="id_ville">Rechercher Etudiant par Ville</label> 
<select id="id_ville" name="ville" size="1"  >
			<option value="0">Choisir une Ville</option>
			<?php
			foreach ($tableau_assoc as $ligne)	{	
				echo '<option value="'.$ligne["insee"].'">'.$ligne["cp"]." ".$ligne["commune"]."</option>"."\n";			
			}
            ?>
</select>
</fieldset>
</form>
<br/>
<?php
}// fin afficheFormulaireEtudiantParVille


?>