<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>Formulaire de connexion par la méthode HTTP POST</title>
	</head>
	<body>
		<form id="form1" action="EX4_BDD.php" method="post">
			<fieldset>
				<legend>Formulaire de connexion par la méthode HTTP POST</legend>	
				<label for="id_mail">Adresse Mail : </label><input type="text" name="mail" id="id_mail" size="10" required placeholder="@mail"/><br />
				<label for="id_pass">Mot de passe : </label><input type="password" name="pass" id="id_pass" size="10" required placeholder="@mail" /><br />
				<input type="submit" name="connect" value="Connexion" />
			</fieldset>
		</form>
	</body>
</html>