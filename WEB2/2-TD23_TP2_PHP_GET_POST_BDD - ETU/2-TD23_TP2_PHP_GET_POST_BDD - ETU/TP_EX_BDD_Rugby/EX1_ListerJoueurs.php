<?php include("fonctions.php");?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>EX1   Liste des joueurs             NOM</title>
		<link href="style.css" rel="stylesheet" type="text/css" />
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

	</head>
	<body>
		<?php navbar();?>
			
			
		<h1>EX1   Liste des joueurs             NOM</h1>
		
		<?php	
			$tab = listerjoueurs();
			if(!empty($tab)){
				afficheTableau($tab);
			}
			
			
		?>
	</body>
</html>