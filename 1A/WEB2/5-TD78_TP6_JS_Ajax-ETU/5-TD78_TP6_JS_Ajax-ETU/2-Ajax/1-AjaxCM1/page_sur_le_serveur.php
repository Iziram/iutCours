<?php
header('Content-type: text/plain'); // on retourne du texte brut
sleep(5);// pour montrer les différentes phases
if (!empty($_GET) && isset($_GET) && ($_GET["action"]=="marche")) {// Méthode GET exigée
?>
<form action="page.php" method="get">
 <fieldset><legend>Formulaire HTML5</legend>
	<label for="idnom">Nom (Champ de texte avec placeholder)</label>
	<input type="text" name="nom" id="idnom"  placeholder="Entrer votre nom" required ><br/><br/>  
	<label for="idprenom">Prénom (Champ de texte avec placeholder)</label>
	<input type="text" name="prenom" id="idprenom"  placeholder="Entrer votre prénom" required ><br/>	
	<span>Bouton radio</span>
	<label for="idH">Homme  <input type="radio" name="radioH" id="idH" value="H" checked></label>
	<label for="idF">Femme  <input type="radio" name="radioH" id="idF" value="F"></label><br/>	
	<span>Case à cocher</span>
	<label for="idV">Vélo<input type="checkbox" name="checkboxV" id="idV" value="checkbox" checked ></label>
	<label for="idC">Course à pied<input type="checkbox" name="checkboxC" id="idC" value="checkbox" checked ></label>
	<label for="idN">Natation<input type="checkbox" name="checkboxN" id="idN" value="checkbox" checked ></label><br/><br/>		
	<label for="idemail">Champ Email</label>
	<input type="email" name="email" id="idemail" required ><br/><br/>  
	<label for="idtel">Téléphone</label>
	<input type="tel" name="tel" id="idtel" placeholder="Saisir votre tél" pattern="[0-9]*"><br/><br/>  
 </fieldset>
</form> 
<?php
}
?>