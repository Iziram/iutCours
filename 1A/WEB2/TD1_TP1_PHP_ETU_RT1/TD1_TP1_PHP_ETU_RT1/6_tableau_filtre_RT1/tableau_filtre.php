<!DOCTYPE html>
<html lang="fr" >
<head>
<meta charset="utf-8">
<link href="style_tableau.css" rel="stylesheet" type="text/css" />
<title>EXO Tableaux filtrés</title>

<style>
table {
border-collapse : collapse ;
}

th,td {
 border : 1px solid black;
 text-align : center;
 }
th{
	background-color : #D48030;}
.impair{
	background-color : #BEA58E;
}
.pair{
	background-color : #EBD9C8;
}
</style>


</head>
<body>
<p>
<?php
include("fonctions.php");
$personnes=array	(	
	array('nom' => 'Bezy', 'prenom' => 'Sébastien'  , 'club'=> 'Clermont'),
	array('nom' => 'Huget', 'prenom' => 'Yoann' , 'club'=> 'Toulouse'),
	array('nom' => 'Vakatawa' , 'prenom' => 'Virimi' ,	'club'=> 'Toulouse'),
	array('nom' => 'Dulin' , 'prenom' => 'Brice'  ,	'club'=> 'La Rochelle')

	);
echo '<hr/>';     
afficheTableauHTML($personnes)  ;
echo '<hr/>';  
//
afficheTableauFiltreHTML($personnes,'La Rochelle')  ;
       



?>

</body>
</html> 