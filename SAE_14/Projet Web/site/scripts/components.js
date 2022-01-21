/**
 * Cette fonction génère une navbar et l'ajoute directement au body de la page courante
 * @param {String} active Chaine de caractère représentant l'id du lien actif (lien reliant à la page courante) dans la navbar
 */
function navbar(active = "index"){
  //On récuppère le body de la page courante 
  const body = document.getElementsByTagName('body')[0];
  // On génère la navbar à partir de sa représentation en html
  const nav = HTMLParser(`
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="index.html#title">Hartmann Matthias</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          
          <li class="nav-item dropdown">
            <a id="index" data-trad="nav-index" class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              CV Numérique
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a data-trad="nav-i-title" class="dropdown-item" href="index.html#title">Titre</a></li>
              <li><a data-trad="nav-i-infos" class="dropdown-item" href="index.html#informations">Qui suis-je ?</a></li>
              <li><a data-trad="nav-i-compt" class="dropdown-item" href="index.html#competences">Mes Compétences</a></li>
              <li><a data-trad="nav-i-forma" class="dropdown-item" href="index.html#formations">Mes diplômes et mes formations</a></li>
              <li><a data-trad="nav-i-exp" class="dropdown-item" href="index.html#experiences">Mes Expériences</a></li>
              <li><a data-trad="nav-i-inter" class="dropdown-item" href="index.html#loisirs">Mes centres d'intérêts</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a data-trad="nav-compt" id="compt" class="nav-link" href="competences.html">Mes Compétences</a>
          </li>
          <li class="nav-item">
            <a data-trad="nav-inter" id="interets" class="nav-link" href="interets.html">Mes Intérêts</a>
          </li>
          <li class="nav-item">
            <a data-trad="nav-links" id="liensutiles" class="nav-link" href="liensutiles.html">Les Liens Utiles</a>
          </li>
          <li class="nav-item">
            <a data-trad="nav-prof" id="projetprofessionnel" class="nav-link" href="projetprofessionnel.html">Mon Projet Professionnel</a>
          </li>
          <li class="nav-item">
            <button id="navbutton" type="button" class="btn btn-outline-light" data-trad="nav-button">Traduire en Anglais</button>
          </li>
          
        </ul>
        
      </div>
    </div>
  </nav>`)
  //On ajoute la navbar en tant qu'enfant du body
  body.appendChild(nav)
  //On ajoute la classe "active" au lien actif pour qu'il soit visible dans la navbar par rapport aux autres liens
  document.getElementById(active).classList.add("active")
  document.getElementById("navbutton").addEventListener('click',()=>{
    traductor.changeLanguage();
  })
}

/**
 * Cette fonction génère le Hero de présentation qu'il y a sur chaque page (sauf index.html) et l'ajoute directement au body de la page courante
 * @param {String} titre Le titre de la page 
 * @param {String} soustitre le paragraphe d'introduction lié à la page
 */
function presentation(titre, soustitre = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod dolore ab debitis deleniti libero reprehenderit aspernatur eligendi repellendus, optio, laborum ex, velit maxime iste fugiat? Autem officiis voluptatibus culpa sint!"){
  //On récuppère le body de la page courante 
  const body = document.getElementsByTagName('body')[0]
    //on crée un div et on le place dans la constante hero
    const hero = document.createElement('div')
      //On lui donne l'id Hero pour le retrouver plus facilement dans le CSS
      hero.id ="hero"
      //On lui donne les classes bootstrap pour les styles
      hero.className="px-4 py-5 my-5 text-center border-top border-bottom"
      //On crée un h1 qui servira de titre
      const h1 = document.createElement('h1')
        //On lui donne les classes bootstrap pour les styles
        h1.className="display-5 fw-bold"
        //On lui donne comme contenu le paramètre titre
        h1.textContent = titre
        //On lui donne l'attribut "trad" et la valeur heroTitle pour pouvoir gérer la traduction automatique
        h1.setAttribute('trad',"heroTitle")
      //On l'ajoute comme enfant de l'élément hero
      hero.appendChild(h1)
      //On fait quasiment la même chose pour le sous-titre
      const sub = document.createElement('div')
          sub.className = "col-lg-6 mx-auto"
          const p = document.createElement('p')
              p.className = "lead mb-4"
              p.setAttribute('trad',"heroText")
              p.textContent = soustitre
          sub.appendChild(p)
      hero.appendChild(sub)
    //On ajoute l'élément hero au body. 
    body.appendChild(hero)
}
/**
 * Cette fonction génère un footer à partir d'une chaine de caractère le représentant en html puis l'ajoute directement dans le body de la page courante
 */
function footer(){
    // On récuppère le body de la page courante 
    const body = document.getElementsByTagName('body')[0]
    //On y insère le footer à partir de sa représentation en html
    body.appendChild(HTMLParser(`
    <div id="footer" class="container bg-dark d-flex justify-content-center align-items-center">
        <footer class="py-3 my-4 border-top text-center">
            <span class="border-end px-2">Hartmann Matthias</span>
            <span class="px-2">2021</span>
        </footer>
    </div>
    `))
}