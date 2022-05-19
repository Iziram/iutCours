<?php
header('Content-type: text/plain');
include('fonctions_ETU.php');
if (!empty($_POST) && isset($_POST["choix"])){		

    afficheTableau(listeEtudiantParVille($_POST["choix"]));

}
?>