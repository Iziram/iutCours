function navbar(active = "index"){
    const body = document.getElementsByTagName('body')[0];
    
    const nav = HTMLParser(`<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Hartmann Matthias</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          
          <li class="nav-item dropdown">
            <a id="index" class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              CV Numérique
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="index.html#title">Titre</a></li>
              <li><a class="dropdown-item" href="index.html#informations">Qui suis-je ?</a></li>
              <li><a class="dropdown-item" href="index.html#competences">Mes Compétences</a></li>
              <li><a class="dropdown-item" href="index.html#formations">Mes diplômes et mes formations</a></li>
              <li><a class="dropdown-item" href="index.html#experiences">Mes Expériences</a></li>
              <li><a class="dropdown-item" href="index.html#loisirs">Mes centres d'intérêts</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a id="compt" class="nav-link" href="competences.html">Mes Compétences</a>
          </li>
          <li class="nav-item">
            <a id="interets" class="nav-link" href="interets.html">Mes Intérêts</a>
          </li>
          <li class="nav-item">
            <a id="liensutiles" class="nav-link" href="liensutiles.html">Les Liens Utiles</a>
          </li>
          <li class="nav-item">
            <a id="projetprofessionnel" class="nav-link" href="projetprofessionnel.html">Mon Projet Professionnel</a>
          </li>
          <li class="nav-item">
            <a id="english" class="nav-link" href="english.html">My English Presentation</a>
          </li>
        </ul>
        
      </div>
    </div>
  </nav>`)
  body.appendChild(nav)

  document.getElementById(active).classList.add("active")

}

function presentation(titre, soustitre = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod dolore ab debitis deleniti libero reprehenderit aspernatur eligendi repellendus, optio, laborum ex, velit maxime iste fugiat? Autem officiis voluptatibus culpa sint!"){
    const body = document.getElementsByTagName('body')[0]
        const hero = document.createElement('div')
            hero.id ="hero"
            hero.className="px-4 py-5 my-5 text-center border-top border-bottom"
            const h1 = document.createElement('h1')
                h1.className="display-5 fw-bold"
                h1.textContent = titre
            hero.appendChild(h1)
            const sub = document.createElement('div')
                sub.className = "col-lg-6 mx-auto"
                const p = document.createElement('p')
                    p.className = "lead mb-4"
                    p.textContent = soustitre
                sub.appendChild(p)
            hero.appendChild(sub)
        body.appendChild(hero)
}

function footer(){
    const body = document.getElementsByTagName('body')[0]
    body.appendChild(
        new DOMParser()
        .parseFromString(`
            <div id="footer" class="container bg-dark d-flex justify-content-center align-items-center">
                <footer class="py-3 my-4 border-top text-center">
                    <span class="border-end px-2">Hartmann Matthias</span>
                    <span class="px-2">2021</span>
                </footer>
            </div>
        `, "text/xml").firstChild)
}


function navMenu(){
    const menu = document.getElementById("navCollapse")
    if(menu.classList.contains("show")){
        menu.classList.remove("show")
    }else{
        menu.classList.add("show")
        pushTest()
    }
}

