<?php 

function utilisateurExiste($login,$pass){ 
    $bdd = new PDO("sqlite:bdd/IUT.sqlite");
    $res = $bdd->query("select * from etudiants where mail='$login' and mdp='$pass'");
    if($res){
        $tab = $res->fetch(PDO::FETCH_ASSOC);
        if(!$tab){
            return False;
        }else{
            return True;
        }
    }
}



?>