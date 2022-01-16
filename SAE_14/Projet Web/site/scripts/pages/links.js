const liens = [
    {
        titre: "Github",
        texte: "Mon github",
        img: "images/svgs/github.svg",
        alt: "logo github",
        link:"https://github.com/Iziram"
    },
    {
        titre: "LinkedIn",
        texte: "Mon Linkedin",
        img: "images/svgs/linkedin.svg",
        alt: "logo linkedin",
        link:"https://www.linkedin.com/in/matthias-hartmann-iziram/"
    },
    {
        titre: "Trello",
        texte: "Mon bureau Trello",
        img: "images/svgs/trello.svg",
        alt: "logo trello",
        link:"https://trello.com/espacedetravaildehartmannmatthias/"
    },
    {
        titre: "StackOverflow",
        texte: "Le meilleur site",
        img: "images/svgs/stackoverflow.svg",
        alt: "logo stackoverflow",
        link:"https://stackoverflow.com/"
    },
    {
        titre: "MDN Web Docs",
        texte: "La docu Du web",
        img: "images/svgs/mozilla.svg",
        alt: "logo mozilla",
        link:"https://developer.mozilla.org"
    },
    {
        titre: "CSS Validator",
        texte: "Pour valider son CSS",
        img: "images/svgs/w3c.svg",
        alt: "logo w3",
        link:"https://jigsaw.w3.org/css-validator"
    },
    {
        titre: "HTML Validator",
        texte: "Pour valider son HTML",
        img: "images/svgs/w3c.svg",
        alt: "logo w3",
        link:"https://validator.w3.org/"
    },
    {
        titre: "Code My UI",
        texte: "Pour trouver des beaux design web",
        img: "images/svgs/codemyui.svg",
        alt: "logo codemyui",
        link:"https://codemyui.com"
    },
]

function createCard(infos){
    const col = document.createElement("div")
        col.className="col-12 col-sm-6 col-md-4 col-lg-3 flex-centering"
        const figure = document.createElement("figure")
            figure.className="pointer pcard"
            const img = document.createElement("img")
                img.className="pcard-img"
                img.src = infos.img
                img.alt = infos.alt
            const title = document.createElement("h2")
                title.className = "pcard-title"
                title.innerText = infos.titre
            const text = document.createElement("p")
                text.className = "pcard-text"
                text.innerText = infos.texte
            figure.appendChild(img)
            figure.appendChild(title)
            figure.appendChild(text)
            figure.addEventListener('click', ()=>{
                window.open(infos.link, '_blank').focus();
            })
        col.appendChild(figure)
    const links = document.getElementById("links")
            links.appendChild(col)
}

liens.forEach((obj)=>{
    createCard(obj)
})