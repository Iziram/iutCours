function navbar(active = "index"){
    const body = document.getElementsByTagName('body')[0];
    const pages = [
        "index",
        "competences",
        "interets",
        "liensutiles",
        "projetprofessionnel"
    ]
    const titres = [
        "CV Numérique",
        "Mes Compétences",
        "Mes Intérêts",
        "Les Liens utiles",
        "Mon Projet Professionnel"
    ]

    const nav = document.createElement('nav')
        nav.className = "navbar navbar-dark bg-dark sticky-top"
        const container = document.createElement('div')
            container.className = "container-fluid"
            const brand = document.createElement('a')
                brand.className = "navbar-brand"
                brand.href="index.html"
                brand.text = "Iziram"
            container.appendChild(brand)

            const button = new DOMParser().parseFromString(`
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
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
                                if(page === "index") {a.href = page+".html"}
                                else{a.href = "pages/"+page+".html"}
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