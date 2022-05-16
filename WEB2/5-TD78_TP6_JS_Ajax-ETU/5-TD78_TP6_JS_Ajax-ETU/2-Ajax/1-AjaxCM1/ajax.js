//Envoi d’une requête
function EnvoiRequete() {

        var req_AJAX = null; // Objet qui sera crée
        if (window.XMLHttpRequest) { // Mozilla, Safari
            req_AJAX = new XMLHttpRequest();
        } else
        if (typeof ActiveXObject != "undefined") {
            req_AJAX = new ActiveXObject("Microsoft.XMLHTTP");
            // note: on peut affiner pour utiliser // d’autres versions d’IE
        }

        if (req_AJAX) {
            req_AJAX.onreadystatechange = function() {

                TraiteReponse(req_AJAX); // voir remarque
            };
            req_AJAX.open("GET", "page_sur_le_serveur.php?action=marche", true); // ou .html ou .xml ...
            // on spécifie l'action que l'on demande au serveur
            //req_AJAX.setRequestHeader("Content-Type", "application/x-www-form-url-encoded");  
            // l'envoi de la requête par la méthode GET se fait avec ce Content-Type
            req_AJAX.send(null); // on envoie la requête
            //req_AJAX.send("action=marche"); // si méthode POST	
        } else {
            alert("EnvoiRequete: pas de XMLHTTP !");
        }
    } // fin fonction envoiRequete() 
    /*
    Remarque: L’attribut onreadystatechange spécifie une fonction (callback) appelée automatiquement lorsque la requête change d’état (traitement asynchrone), 
    ici la fonction  (!!! sans de paramètre possible)  appelle une autre se nomme TraiteReponse qui peut prendre des paramètres. */


//Exemple de traitement de la réponse
function TraiteReponse(requete) { // On reçoit en paramètre l'objet XMLHttpRequest
        var READY_STATE_UNINITIALIZED = 0;
        var READY_STATE_LOADING = 1;
        var READY_STATE_LOADED = 2;
        var READY_STATE_INTERACTIVE = 3;
        var READY_STATE_COMPLETE = 4;

        var etat = requete.readyState; // récupère l'état de la requête
        alert(etat);
		console.log(etat);
        var msg_etat = document.getElementById("etat");
        msg_etat.innerHTML = "reponse, etat=" + etat; // on l'affiche pour comprendre
        if (etat == READY_STATE_COMPLETE) { // si c'est fini	
            var vide = document.getElementById("vide");
            // on pointe avec DOM dans notre page initiale
            var status = requete.status; // et le code HTTP associé
            if (status == 200) { // code = 200 réponse HTTP OK
                // insere resultat dans document
                var data = "";
                // version texte
                data = requete.responseText; // on récupère le "travail" du serveur
                vide.innerHTML = data;
            } else {
                vide.innerHTML = "erreur serveur, code " + status;
            }
        }
    } // fin function TraiteReponse(requete)