<?php include("fonctions.php");?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>EX2 Liste des joueurs Filtre    NOM</title>
		<link href="style.css" rel="stylesheet" type="text/css" />
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

	</head>
	<body>
	<?php navbar();?>
		<h1>EX2 Liste des joueurs Filtre    NOM</h1>
		<?php	
			afficheFormEquipe();
			
			if(!empty($_GET) && isset($_GET["equipe"]) && !empty($_GET["equipe"])){
				$tab = listerjoueursParEquipe($_GET["equipe"]);
				if($tab){
					if($_GET["equipe"] != "toutes"){
						echo "<h2>Composition de l'équipe : ".nomEquipeParNum($_GET["equipe"])."</h2>";
					}
					afficheTableau($tab);
				}
			}
			
		?>
		
	</body>
</html>