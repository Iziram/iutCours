<?php 
include 'fonctions.php';
include 'formulaires.php';
?>
<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<link href="style.css" rel="stylesheet" type="text/css" />
<title>Module WEB2 TD8: Ajax V1 RAPPEL HTML + PHP</title>
</head>
<body>
<header>
<h1>Module WEB2 TD8: Ajax	VERSION 1 </h1>
<h1>Lister les utilisateurs par ville. RAPPEL HTML + PHP</h1>
</header>

<?php		
afficheFormulaireEtudiantParVille();

if (!empty($_GET) && isset($_GET["ville"])){
	//var_dump($_GET);
	$tab=listeEtudiantParVille($_GET["ville"]);
	if ($tab) afficheTableau($tab);	
}
?>
</div>
</body>
</html>


