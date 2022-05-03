<?php
	//****************Fonctions utilisées**************************************
	function compteExiste($mail,$pass){
		$retour = false ;
		$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
		$mail= $madb->quote($mail);
		$pass = $madb->quote($pass);
		$requete = "SELECT Email,Pass FROM utilisateurs WHERE Email = ".$mail." AND Pass = ".$pass ;
		//var_dump($requete);echo "<br/>";  	
		$resultat = $madb->query($requete);
		$tableau_assoc = $resultat->fetchAll(PDO::FETCH_ASSOC);
		if (sizeof($tableau_assoc)!=0) $retour = true;	
		return $retour;
	}
	//********************************************************************************
	function isAdmin($mail){
		$retour = false ;
		try{
			$bd = new PDO("sqlite:bdd/iut.sqlite");

			$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
			$mail= $madb->quote($mail);
			$requete = "SELECT Statut FROM utilisateurs WHERE Email = ".$mail;

			$res = $madb->query($requete);
			if($res){
				$tab = $res->fetch(PDO::FETCH_ASSOC);
				if($tab["Statut"] == "Prof"){
					$retour = true;
				}
			}
		}catch(Exception){

		}
		
		
		
		
		return $retour;		
	}
	//********************************************************************************
	function listeCompte()	{ // A faire
		$retour = array();

		try{
			$bd = new PDO("sqlite:bdd/iut.sqlite");

			$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
			$requete = "SELECT Email,Statut,Adresse,CP,Commune FROM utilisateurs inner join villes on villes.Insee = utilisateurs.Insee ";

			$res = $madb->query($requete);
			if($res){
				$tab = $res->fetchAll(PDO::FETCH_ASSOC);
				if($tab){
					$retour = $tab;
				}
			}
		}catch(Exception){

		}	
		

		
		return $retour;
	}		
	//*******************************************************************************************
	function formater_saisie($data) {
		$data = trim($data);
		$data = stripslashes($data);
		$data = htmlspecialchars($data);
		return $data;
	}
	//*******************************************************************************************
	function afficheTableau($tab){
		echo '<table>';	
		echo '<tr>';// les entetes des colonnes qu'on lit dans le premier tableau par exemple
		foreach($tab[0] as $colonne=>$valeur){		echo "<th>$colonne</th>";		}
		echo "</tr>\n";
		// le corps de la table
		foreach($tab as $ligne){
			echo '<tr>';
			foreach($ligne as $cellule)		{		echo "<td>$cellule</td>";		}
			echo "</tr>\n";
		}
		echo '</table>';
	}
	//*******************************************************************************************
	function listeUtilisateurParVille($insee){
		$retour = array();

		try{
			$bd = new PDO("sqlite:bdd/iut.sqlite");

			$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
			$requete = "SELECT Email,Statut,Adresse,CP,Commune FROM utilisateurs inner join villes on villes.Insee = utilisateurs.Insee where villes.Insee = ".$insee;

			$res = $madb->query($requete);
			if($res){
				$tab = $res->fetchAll(PDO::FETCH_ASSOC);
				if($tab){
					$retour = $tab;
				}
			}
		}catch(Exception){

		}
		
		
		
		
		return $retour;
	}
	//*******************************************************************************************
	function listeVille(){
		$retour = array();
		try{
			$bd = new PDO("sqlite:bdd/iut.sqlite");

			$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
			$requete = "SELECT Commune,villes.Insee FROM utilisateurs inner join villes on villes.Insee = utilisateurs.Insee";

			$res = $madb->query($requete);
			if($res){
				$tab = $res->fetchAll(PDO::FETCH_ASSOC);
				if($tab){
					$retour = $tab;
				}
			}
		}catch(Exception){

		}

		return $retour;
	}
	//*******************************************************************************************
	function ajoutUtilisateur($mail,$pass,$rue,$insee,$status){
		/* on récupère directement le code de la ville qui a été transmis dans l'attribut value de la balise <option> du formulaire
		Il n'est donc pas nécessaire de rechercher le code INSEE de la ville*/
		$madb = new PDO('sqlite:bdd/IUT.sqlite');
		$qmail = $madb->quote($mail);
		$qpass = $madb->quote($pass);
		$qrue = $madb->quote($rue);
		$qstatus = $madb->quote($status);
		// filtrer les paramètres	
		
		$sql = "insert into utilisateurs values ("
		.$qmail.","
		.$qpass.","
		.$qrue.","
		.$insee.","
		.$qstatus.
		")";
		try{
			$res = $madb->exec($sql);
			if($res){
				return true;
			}
		}catch(Exception){
			
		}
		
		
		
		return false;
	}
	//*******************************************************************************************
	function supprimerUtilisateur($mail){
		$retour= false;
		$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
		// filtrer le paramètre	
		
		$sql = "SELECT * from utilisateurs where Email =".$madb->quote($mail);
		$res = $madb->query($sql);
		if($res){
			if($res->fetch(PDO::FETCH_ASSOC)){
				$sql = "DELETE from utilisateurs where Email = ".$madb->quote($mail);
				$res = $madb->exec($sql);
				if($res){
					$retour = true;
				}
			}
		}
		
		
		
		return $retour;
	}
	//*******************************************************************************************
	function modifierUtilisateur($mail,$pass,$rue,$insee,$status){
		$retour=0;
		$madb = new PDO('sqlite:bdd/IUT.sqlite'); 
		// filtrer les paramètres	
		
		
		
		
		
		
		
		
		return $retour;
	}
	//*******************************************************************************************
	//Nom : redirect()
	//Role : Permet une redirection en javascript
	//Parametre : URL de redirection et Délais avant la redirection
	//Retour : Aucun
	//*******************
	function redirect($url,$tps)
	{
		$temps = $tps * 1000;
		
		echo "<script type=\"text/javascript\">\n"
		. "<!--\n"
		. "\n"
		. "function redirect() {\n"
		. "window.location='" . $url . "'\n"
		. "}\n"
		. "setTimeout('redirect()','" . $temps ."');\n"
		. "\n"
		. "// -->\n"
		. "</script>\n";
		
	}
	
?>
