<?php include("fonctions.php");?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>EX3   Insertion d'un joueur       HARTMANN</title>
		<link href="style.css" rel="stylesheet" type="text/css" />
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

	</head>
	<body>
	<?php navbar();?>
		<h1>EX3   Insertion d'un joueur       HARTMANN</h1>
		<?php
			$tab = false;
			if(!empty($_POST)){
				if(isset($_POST["joueur"]) && !empty($_POST["joueur"])
				&& isset($_POST["equipe"]) && !empty($_POST["equipe"])){
					$res = insererjoueur($_POST["joueur"], $_POST["equipe"]);
					if($res){
						echo "<p>Le joueur <strong>".$_POST["joueur"]. "</strong> a bien été ajouté à l'équipe <u>".nomEquipeParNum($_POST["equipe"])."</u></p>";
					}else{
						echo "Le joueur n'a pas pu être enregistré. Vérifiez qu'il n'existe pas déjà dans la base puis recommencez.";
					}
					$tab = listerjoueursParEquipe($_POST["equipe"]);
					

				}
			}
			afficheFormulaireAjoutjoueur();
			if($tab) {afficheTableau($tab);}

		?>
	</body>
</html>



