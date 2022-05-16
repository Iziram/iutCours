<?php 
include 'fonctions.php';
include 'formulaires.php';
?>
<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<script src="js/index.js" type="text/javascript"></script>
<link href="style.css" rel="stylesheet" type="text/css" />
<title>Module WEB2 TD8: Ajax V2 JS</title>
</head>
<body>
<header>
<h1>Module WEB2 TD8: Ajax		VERSION 2 	HTML + PHP + JS</h1>
<h1>Lister les utilisateurs par ville. HTML + PHP + JS</h1>
</header>

<?php		
afficheFormulaireEtudiantParVille();


if (!empty($_GET)){
	

	$tab=listeEtudiantParVille($_GET["ville"]);
	if ($tab) afficheTableau($tab);
	
	
}


?>
</div>
</body>
</html>


