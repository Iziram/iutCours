function navbar(active){
    const nav = document.createElement('nav')
        nav.className="navbar navbar-expend-lg navbar-dark bg-dark"
        const container = document.createElement('div')
            container.className="container-fluid"
            const a_navbar = document.createElement('a')
                a_navbar.href = "index.html"
                a_navbar.text = "Iziram"
                a_navbar.className = "navbar-brand"
            container.appendChild(a_navbar)
        nav.appendChild(container)
        const collapse = document.createElement('button')
            collapse.outerHTML = `<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>`
        
        nav.appendChild(collapse)


        document.getElementsByTagName('body')[0].appendChild(nav)
}