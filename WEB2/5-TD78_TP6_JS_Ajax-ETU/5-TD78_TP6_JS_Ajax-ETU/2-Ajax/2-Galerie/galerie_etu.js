// variables globales
var lien_image =0; // initialiser  au premier chargement du fichier .js

/**********************************/
/* le paramètre sens vaudra + ou - pour charger l'image précédente ou suivante */
function Deplacement(sens){
// créer une requête AJAX
	if(sens == "+")
		lien_image++;
	else
		lien_image--;
	
	let req = null;
        if (window.XMLHttpRequest) {
            req = new XMLHttpRequest();
        } else if (typeof ActiveXObject != "undefined") {
            req = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (req) {
            req.onreadystatechange = function () {TraiteReponse(req)};
			req.open('get', "lireImage.php?image="+lien_image, true);
        	req.send(null);
            }
        
}
/**********************************/
/* le paramètre est l'objet de la requête AJAX */
function TraiteReponse(requete) {
// test si la requête est en cours de chargement et affichage "En cours"
	let state = requete.readyState;
	const p = document.getElementById('chemin_image');
	if(state == 4  && requete.status == 200){
		const data = requete.responseText;
		const img = document.getElementById('image');
			img.src = data;
			const arr = data.split('/');
			img.alt = arr[arr.length - 1];
		p.textContent = data;

		
		
	}else{
			p.textContent = "En cours de chargement";
	}
	

// test si la requête est terminée (état 4) et correcte (code HTTP 200)

} // fin TraiteReponse

/**********************************/
function lancement(){
	setInterval(function(){ Deplacement('+'); }, 3000);
}