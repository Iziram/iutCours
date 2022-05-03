<?php
session_start();
?>
<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8"/>
		<style>
			.error {color: #FF0000;}
		</style>
	</head>
	<body>
		
		<?php
			//variables affectées à des valeurs vides
			$nomErr = $emailErr = $genreErr = $sitewebErr = "";
			$nom = $email = $genre = $comment = $siteweb = "";
			
			
			
			function formater_saisie($data) {
				$data = trim($data);
				$data = stripslashes($data);
				$data = htmlspecialchars($data);
				return $data;
			}

			if (!empty($_POST)) {
				if(isset($_POST['captcha'])){
					if($_POST['captcha']==$_SESSION['code']){
						echo "Code correct";
						if (empty($_POST["nom"])) { $nomErr = "Il faut saisir un nom";
						} else { $nom = formater_saisie($_POST["nom"]);
							if (!preg_match("/^[a-zA-Z ]*$/",$nom)) {
								$nomErr = "Seules les lettres et les espaces sont autorisées.";
							}
						}
		
						if(empty($_POST["email"])){
							$emailErr = "Il faut mettre une email";
						}
						else{
							$email = formater_saisie($_POST["email"]);
							if(!filter_var($email,FILTER_VALIDATE_EMAIL)){
								$emailErr = "L'email n'est pas valide.";
							}
						}
						if(!empty($_POST["siteweb"])){
							$siteweb = formater_saisie($_POST["siteweb"]);
							if(!filter_var($siteweb,FILTER_VALIDATE_URL)){
								$sitewebErr = "L'url n'est pas valide.";
							}
						}
						if(!empty($_POST["comment"])){
							$comment = formater_saisie($_POST["comment"]);
						}
						if(empty($_POST["genre"])){
							$genreErr = "Il faut indiquer un genre.";	
						}else{
							$genre = formater_saisie($_POST["genre"]);
						}
						} else {
						echo "Code incorrect";
					}
				}
				{
					
				}
				
			}
		?>
		
		<h2>Validation Formulaire en PHP</h2>
		<p><span class="error">* Champs obligatoires</span></p>
		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
			Nom: <input type="text" name="nom">
			<span class="error">* <?php echo $nomErr;?></span>
			<br/><br/>
			E-mail: <input type="text" name="email">
			<span class="error">* <?php echo $emailErr;?></span>
			<br/><br/>
			SiteWeb: <input type="text" name="siteweb">
			<span class="error"><?php echo $sitewebErr;?></span>
			<br/><br/>
			Commentaire: <textarea name="comment" rows="5" cols="40"></textarea>
			<br/><br/>
			Genre:
			<input type="radio" name="genre" value="femme">Féminin
			<input type="radio" name="genre" value="homme">Masculin
			<input type="radio" name="genre" value="autre">Autre
			<span class="error">* <?php echo $genreErr;?></span>
			<br/><br/>
			<input type="submit" name="submit" value="Submit">
			<br>
			<img src="image.php" onclick="this.src='image.php?' + Math.random();" alt="captcha" style="cursor:pointer;">

		</form>
		
		<?php

			
			echo "<h2>Votre saisie</h2>";
			echo $nom;
			echo "<br/>";
			echo $email;
			echo "<br/>";
			echo $siteweb;
			echo "<br/>";
			echo $comment;
			echo "<br/>";
			echo $genre;
		?>
		
	</body>
</html>