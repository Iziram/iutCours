<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>Lister un répertoire et créer des liens et afficher des images</title>

	</head>
<body>
<!-- <h2>AIDE !!!!!!!! Ce qu'il faut générer en PHP  </h2>
<p> Nom du fichier: IUT-LANNION.jpg </p>
<p><a href="images/IUT-LANNION.jpg">Lien vers l'image</a></p>
<p><img alt="image-1" src="images/IUT-LANNION.jpg" /></p> -->


<?php

$nb=0;
$dir = opendir("./images");

while(false!==($fichier = readdir($dir)))	{
	if(preg_match("/.jpg|.JPG/", $fichier)==true)	{
	// A compléter ici
	echo "<p>Nom du fichier : $fichier</p>";
	echo '<p><a href="'."./images/".$fichier.'">Lien vers l\'image</a></p>';
	echo '<p><img src="'."./images/".$fichier.'"'."alt=\"$fichier\"/></p>";
	
	}
}
closedir($dir);

?>
</body>
</html>