<?php
	session_start();//on enregistre la session, pour le code, pour la vérification du formulaire
	//le fichier se nomme: image.php
	//on indique au header qu'il faut afficher le code en tant qu'image
	header('Content-Type: image/png');
	$largeur=80;//largeur de l'image
	$hauteur=25;//hauteur de l'image
	$lignes=10;//nombre de lignes multicolore qui seront affichées avec le code (10 est bien)
	$caracteres="ABCDEF123456789";//type de caractère du code qui sera affiché dans l'image
	//on crée le rectangle
	$image = imagecreatetruecolor($largeur, $hauteur);
	//on met un fond en blanc (255,255,255)
	imagefilledrectangle($image, 0, 0, $largeur, $hauteur, imagecolorallocate($image, 255, 255, 255));
	//on ajoute les lignes
	function hexargb($hex) {//fonction qui permet de retourner la valeur en RGB d'une couleur hexadécimale
		return array("r"=>hexdec(substr($hex,0,2)),"g"=>hexdec(substr($hex,2,2)),"b"=>hexdec(substr($hex,4,2)));//on retourne la valeur sous forme d'array
	}
	for($i=0;$i<=$lignes;$i++){
		$rgb=hexargb(substr(str_shuffle("ABCDEF0123456789"),0,6));//choisi une couleur aléatoirement (str_shuffle), de 6 caractères (substr(chaine,0,6)) avec la sélection alphanumérique
		imageline($image,rand(1,$largeur-25),rand(1,$hauteur),rand(1,$largeur+25),rand(1,$hauteur),imagecolorallocate($image, $rgb['r'], $rgb['g'], $rgb['b']));
	}
	$code1=substr(str_shuffle($caracteres),0,4);
	$_SESSION['code']=$code1;//on enregistre le code dans une session pour vérifier ensuite se qu'à entré le visiteur est identique
	$code="";//on initialise le code
	for($i=0;$i<=strlen($code1);$i++){
		$code .=substr($code1,$i,1)." ";//on rajoute des espace entre chaque lettre ou chiffre pour faire plus aéré (notez le . devant = qui permettra d'ajouter un caractère après l'autre à $code)
	}
	//on écrit le code dans le rectangle
	imagestring($image, 5, 10, 5, $code, imagecolorallocate($image, 0, 0, 0));
	//on affiche l'image
	imagepng($image);
	//puis on détruit l'image pour libérer de l'espace
	imagedestroy($image);
?>