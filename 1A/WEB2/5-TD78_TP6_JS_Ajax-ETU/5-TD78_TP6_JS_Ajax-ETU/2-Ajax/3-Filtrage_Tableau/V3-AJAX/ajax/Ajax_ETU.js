/*****************************************************************/
function listeFiltreUtilisateurs(ville)	{
	if(ville == 0) return;
	if(window.fetch){
		choix = new FormData();
		choix.append('choix',ville);
		let header = {
            method: "post",
            body: choix
        };
		window.fetch(
			"listeUtilisateurs_ETU.php",
			header
		).then(res => res.text())
		.then(

			res => {
				const el = document.getElementById('tableau');
					el.innerHTML = res;
			}

		).catch( res => {console.error(res)})
	}
}




