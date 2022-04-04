<!DOCTYPE html>
<html lang="fr" >
	<head>
		<meta charset="utf-8">
		<title>Formulaire de connexion par la méthode HTTP POST</title>
	</head>
	<body>
		<form id="form1" action="verif_login_POST.php" method="post">
			<fieldset>
				<legend>Formulaire de connexion par la méthode HTTP POST</legend>	
				<label for="id_mail">Adresse Mail : </label>
				<input type="email" name="mail" id="id_mail" placeholder="@mail" required /><br />
				<label for="id_pass">Mot de passe : </label>
				<input type="password" name="pass" id="id_pass" placeholder="Mot de passe" required /><br />
				<input type="submit" name="connect" value="Connection" />
			</fieldset>
		</form>
	</body>
</html>

<!--

2) verif_login_POST.php
3) "name"
4) $_POST

-->