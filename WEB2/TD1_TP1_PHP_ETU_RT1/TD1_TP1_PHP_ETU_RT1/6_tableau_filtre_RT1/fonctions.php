<?php

//****************************************************************************************  
function afficheTableauHTML($tab){ 
?><table>
    <thead>
        <tr>
            <?php
            //On recupère les clés de la première ligne du tableau donné pour créer l'entête
            foreach(array_keys($tab[0]) as $key){
                echo "<th>$key</th>";
            }
            
            ?>
        </tr>
    </thead>
    <tbody>
<?php
    //Définition d'une variable pour déterminer si la ligne est paire ou impaire
    $impair = True;
    foreach($tab as $perso){
        //Pour chaque personne on écrit une ligne du tableau
        echo '<tr>';
        //On met la classe impaire si la ligne est impaire, pair sinon
        $class = "impair";
                if(!$impair){
                    $class = "pair";
        }
        foreach($perso as $_ => $val){
            //Pour chaque valeur de chaque personne on écrit une balise td avec la classe et la valeur
            echo '<td class="'.$class.'">'."$val</td>";
        }
        echo '</tr>';
        //on actualise la variable de parité
        $impair = !$impair;

    }
    //On ferme le tableau
    echo '</tbody>
    </table>';
}

//****************************************************************************************  
function afficheTableauFiltreHTML($tab,$club){ 
    ?><table>
    <thead>
        <tr>
            <?php
            // On affiche les clés en entête
            foreach(array_keys($tab[0]) as $key){
                echo "<th>$key</th>";
            }
            
            ?>
        </tr>
    </thead>
    <tbody>
<?php
    //Exactement la même chose que afficheTableau mais on vérifie si la valeur associé à la clé "club" est $club
    $impair = True;
    foreach($tab as $perso){
        if($perso["club"] == $club){
            echo '<tr>';
            $class = "impair";
                if(!$impair){
                    $class = "pair";
            }
            foreach($perso as $_ => $val){
                echo '<td class="'.$class.'">'.$val.'</td>';
            }
            echo '</tr>';
            $impair = !$impair;
        }

    }
    echo '</tbody>
    </table>';

}

?>