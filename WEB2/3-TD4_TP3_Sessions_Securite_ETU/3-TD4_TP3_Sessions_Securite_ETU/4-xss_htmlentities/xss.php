<?php
	if (isset($_GET["var"])){
		$var=$_GET["var"];
		//echo "var : ".htmlentities($var);
		echo "PROBLEME: ";
		echo "<br/>";

		echo "var : ".$var;
		echo "<br/>";
		echo "SOLUTION: ";
		echo "<br/>";

		echo "var: ".htmlentities($var);
	}
?>