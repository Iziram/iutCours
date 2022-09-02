<?php
/*
On vérifie que le paramètre GET est bien présent : c'est un chiffre que l'on bornera au nombre maximum d'images dans le dossier
*/
if(!empty($_GET) && isset($_GET['image'])){

//sleep(1);	

$image = $_GET['image']; // on crée une variable $image
$rep = scandir('./img'); // retourne un tableau contenant le nom des fichiers mais aussi . et .. dans les deux premières cases

$tableau=array_slice($rep, 2);//créer un nouveau tableau en enlevant les deux premières cases contenant . et .. 
$nbimage = count ($tableau);
$image = ($image%($nbimage)); 

$this_url = pathinfo($_SERVER['REQUEST_URI']); // on récupère l'url de cette page
echo "http://".$_SERVER['SERVER_NAME'].$this_url['dirname']."/img/".$tableau[$image];
//  on constitue la reponse souhaitée ex: http://129.20.235.109/AJAX/diaporama/img/toto.JPG
}
else
echo "Erreur GET";
?>