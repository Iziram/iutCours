function navbar(active = "index"){
    const body = document.getElementsByTagName('body')[0];
    const pages = [
        "index",
        "competences",
        "interets",
        "liensutiles",
        "projetprofessionnel",
        "english"
    ]
    const titres = [
        "CV Numérique",
        "Mes Compétences",
        "Mes Intérêts",
        "Les Liens utiles",
        "Mon Projet Professionnel",
        "My English Presentation"
    ]

    const nav = document.createElement('nav')
        nav.className = "navbar navbar-dark bg-dark sticky-top"
        const container = document.createElement('div')
            container.className = "container-fluid"
            const brand = document.createElement('a')
                brand.className = "navbar-brand"
                brand.href="index.html"
                brand.text = "Hartmann Matthias"
            container.appendChild(brand)

            const button = new DOMParser().parseFromString(`
            <button class="btn btn-md btn-light" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
                <i class="bi bi-stack"></i>
            </button>
            `,"text/xml")
            container.appendChild(button.firstChild)

            const collapse = document.createElement('div')
                collapse.className = "collapse navbar-collapse"
                collapse.id="navbar"
                const ul = document.createElement('ul')
                    ul.className = "navbar-nav me-auto mb-2"
                    for(let i = 0; i< pages.length; i++){
                        const page = pages[i]
                        const titre = titres[i]
                        const li = document.createElement('li')
                            li.className = "nav-item"
                            const a = document.createElement('a')
                                a.href = page+".html"
                                a.className = "nav-link"
                                if(active === page ){
                                    a.classList.add("active")
                                }
                                a.innerHTML = titre
                            li.appendChild(a)
                        ul.appendChild(li)
                    }

                    
                collapse.appendChild(ul)
            container.appendChild(collapse)
        nav.appendChild(container)
    body.appendChild(nav)
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
            <div class="container">
                <footer class="py-3 my-4 border-top text-center">
                    <span class="border-end px-2">Hartmann Matthias</span>
                    <span class="px-2">2021</span>
                </footer>
            </div>
        `, "text/html").firstChild)
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
