<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<link href="style.css" rel="stylesheet" type="text/css" />
<title>Test Compte ETU</title>
</head>
<body>
<header>
<h1>Test Compte ETU</h1>
</header>

<?php

include 'fonctions.php';


var_dump(isAdmin('etu@etu.fr'));
var_dump(isAdmin('prof@prof.fr'));



?>
</body>
</html>	
