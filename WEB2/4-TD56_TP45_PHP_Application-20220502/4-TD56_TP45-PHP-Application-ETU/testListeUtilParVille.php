<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<link href="style.css" rel="stylesheet" type="text/css" />
<title>Test testListeUtilisateurParVille ETU</title>
</head>
<body>
<header>
<h1>Test testListeUtilisateurParVille ETU</h1>
</header>

<?php
    include 'fonctions.php';
    include 'formulaires.php';

    afficheFormulaireUtilisateurParVille();
    if (!empty($_POST) && isset($_POST["ville"]) ){
        $ville = formater_saisie($_POST["ville"]);

        afficheTableau(listeUtilisateurParVille($ville));
    }
?>
</body>
</html>	
