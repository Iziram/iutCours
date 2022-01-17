const liens = [
    {
        titre: "ENT Rennes",
        texte: "L'ensembles des outils pédagogiques",
        img: "images/svgs/menu.svg",
        alt: "logo ENT Rennes",
        link:"https://ent.univ-rennes1.fr/"
    },
    {
        titre: "Emploi du temps",
        texte: "L'ensembles des outils pédagogiques",
        img: "images/svgs/calendar.svg",
        alt: "logo Calendrier",
        link:"https://planning.univ-rennes1.fr/"
    },
    {
        titre: "Cours en Lignes",
        texte: "L'endroit où retrouver tous ses cours",
        img: "images/svgs/book.svg",
        alt: "logo Livre",
        link:"https://foad.univ-rennes1.fr/"
    },
    {
        titre: "Mail étudiant",
        texte: "Le webmail des étutiants",
        img: "images/svgs/mail.svg",
        alt: "logo mail",
        link:"https://partage.univ-rennes1.fr/mail#1"
    },
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
        texte: "Idées de web design",
        img: "images/svgs/codemyui.svg",
        alt: "logo codemyui",
        link:"https://codemyui.com"
    },
    {
        titre: "Twitter",
        texte: "Mon twitter",
        img: "images/svgs/twitter.svg",
        alt: "logo twitter",
        link:"https://twitter.com/iziram_"
    },
    {
        titre: "Youtube",
        texte: "Ma chaine youtube",
        img: "images/svgs/youtube.svg",
        alt: "logo youtube",
        link:"https://www.youtube.com/channel/UCyCn19a5xr8SDdX-qPur1GQ"
    },
    {
        titre: "Twitch",
        texte: "Mon Twitch",
        img: "images/svgs/twitch.svg",
        alt: "logo twitch",
        link:"https://www.twitch.tv/iziram"
    },
    {
        titre: "Discord",
        texte: "Mon discord",
        img: "images/svgs/discord.svg",
        alt: "logo discord",
        link:"https://discord.com/users/277501626871447552"
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