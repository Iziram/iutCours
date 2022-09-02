<?php

function EnteteTitrePage($valeur){
    echo '<!DOCTYPE html>
    <html lang="fr" >
    <head>
    <meta charset="utf-8">
    <title>ETU EXO2 Include</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
    <header>
    <h1> '.$valeur.' </h1>
    </header>';
}

function PiedDePage(){
    echo '<footer>
    <p>Pied de Page</p>
    </footer>
    </body>
    </html> ';
}

?>