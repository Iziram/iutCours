<?php

//****************************************************************************************  
function afficheTableauHTML($tab){ 
	echo '<table>
    <thead>
        <tr>
            <th>
                Nom
            </th>
            <th>
                Prénom
            </th>
            <th>
                Club
            </th>
        </tr>
    </thead>
    <tbody>';
    $impair = True;
    foreach($tab as $perso){
        echo '<tr>';
        $class = "impair";
                if(!$impair){
                    $class = "pair";
        }
        foreach($perso as $_ => $val){
            echo '<td class="'.$class.'">'."$val</td>";
        }
        echo '</tr>';
        $impair = !$impair;

    }
    echo '</tbody>
    </table>';
}

//****************************************************************************************  
function afficheTableauFiltreHTML($tab,$club){ 
    echo '<table>
    <thead>
        <tr>
            <th>
                Nom
            </th>
            <th>
                Prénom
            </th>
            <th>
                Club
            </th>
        </tr>
    </thead>
    <tbody>';
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