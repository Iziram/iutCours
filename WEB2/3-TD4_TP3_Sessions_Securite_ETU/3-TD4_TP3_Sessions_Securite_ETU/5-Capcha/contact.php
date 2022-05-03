<?php session_start();//page contact.php
	include('image.php');
?>
<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>Formulaire de contact avec Capcha</title>
	</head>
	<body>
		<h1>Formulaire de contact avec Capcha</h1>
		
		<form action="contact.php" method="post">
			<input type="text" name="captcha"/>
			<input type="submit"/>
			<img src="image.php" onclick="this.src='image.php?	' + Math.random();" alt="captcha" style="cursor:pointer;">
		</form>
		<?php if(isset($_POST['captcha'])){
			if($_POST['captcha']==$_SESSION['code']){
				echo "Code correct";
				//ici vous traitez le formulaire
				} else {
				echo "Code incorrect";
				//ici vous faites un "echo" pour avertir qu'il y a une erreur
			}
		}
		?>
	</body>	