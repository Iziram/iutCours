// variables globales
var lien_image =0; // initialiser  au premier chargement du fichier .js

/**********************************/
/* le paramètre sens vaudra + ou - pour charger l'image précédente ou suivante */
function Deplacement(sens){
// créer une requête AJAX
var req_AJAX = null;

if (req_AJAX) {// le navigateur permet AJAX
	// on incrémente ou décrémente l'image

	// on écrit l'url du script à demander sur le serveur
	// ex : lireImage.php?image=1

	// on définit la méthode TraiteReponse(req_AJAX) qui se sera exécutée lors de chaque cycle de la requête

	// on spécifie l'action que l'on demande au serveur avec la méthode HTTP souhaitée

	//req_AJAX.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");  
	// l'envoi de la requête par la méthode POST se fait avec ce Content-Type
	// on envoie la requête : pas de paramètre avec GET
	} 
else  	
	alert("Le navigateur ne traite pas AJAX");	
}//fin 
/**********************************/
/* le paramètre est l'objet de la requête AJAX */
function TraiteReponse(requete) {
// test si la requête est en cours de chargement et affichage "En cours"


// test si la requête est terminée (état 4) et correcte (code HTTP 200)

} // fin TraiteReponse

/**********************************/
function lancement(){
	 setInterval(function(){ Deplacement('+'); }, 3000);
}