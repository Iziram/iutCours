<?php
	var_dump($_GET);
	echo "<p>Q1</p>";
	
	if(isset($_GET)){
		foreach($_GET as $key => $value){
			echo "Paramètre : $key Valeur : $value<br/>";
		}
	}
	
	echo "<p>Q2</p>";
	if(isset($_GET) && !empty($_GET)){
		foreach($_GET as $key => $value){
			echo "Paramètre : $key Valeur : $value<br/>";
		}
	}else{
		echo "Aucun paramètre";
	}
	
	echo "<p>Q3</p>";

	if(isset($_GET) && !empty($_GET)){
		if(isset($_GET["action"]) && $_GET["action"] == "marche"){
			echo "Le test est validé";
		}else{
			echo "Le test n'est pas validé";
		}
		echo "<br/>";
		foreach($_GET as $key => $value){
			echo "Paramètre : $key Valeur : $value <br/>";
		}
	}else{
		echo "Aucun paramètre";
	}
	
?>