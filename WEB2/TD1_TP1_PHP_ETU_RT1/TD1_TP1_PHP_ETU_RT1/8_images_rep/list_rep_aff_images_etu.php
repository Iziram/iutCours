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
//On ouvre le dossier "./images"
$dir = opendir("./images");

//Tant qu'on peut lire des fichiers dans le dossier
while(false !== ($fichier = readdir($dir)))	{
	//On vérifie si c'est bien une image
	if(preg_match("/.jpg|.JPG|.png|.PNG/", $fichier)==true){
	//On affiche le nom de l'image
	echo "<p>Nom du fichier : $fichier</p>";
	//On place un lien vers l'image
	echo '<p><a href="'."./images/".$fichier.'">Lien vers l\'image</a></p>';
	//On affiche l'image
	echo '<p><img src="'."./images/".$fichier.'"'." alt=\"$fichier\"/></p>";
	
	}
}
closedir($dir);

?>
</body>
</html>