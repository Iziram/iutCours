//Liste des objets représentant chaque lien à afficher avec un Titre, un petit Texte, une IMaGe, un texte ALTernatif et le lien (LINK)
const liens = [
    {
        titre: "ENT Rennes",
        texte: "L'ensembles des outils pédagogiques",
        img: "images/svgs/menu.svg",
        alt: "logo ENT Rennes",
        trad: "ent-",
        link:"https://ent.univ-rennes1.fr/"
    },
    {
        titre: "Emploi du temps",
        texte: "Meilleur moyen d'être à l'heure",
        img: "images/svgs/calendar.svg",
        alt: "logo Calendrier",
        trad: "schedule-",
        link:"https://planning.univ-rennes1.fr/"
    },
    {
        titre: "Cours en Lignes",
        texte: "L'endroit où retrouver tous ses cours",
        img: "images/svgs/book.svg",
        alt: "logo Livre",
        trad: "class-",
        link:"https://foad.univ-rennes1.fr/"
    },
    {
        titre: "Mail étudiant",
        texte: "Le webmail des étudiants",
        img: "images/svgs/mail.svg",
        alt: "logo mail",
        trad: "mail-",
        link:"https://partage.univ-rennes1.fr/mail#1"
    },
    {
        titre: "Github",
        texte: "Mon github",
        img: "images/svgs/github.svg",
        alt: "logo github",
        trad: "git-",
        link:"https://github.com/Iziram"
    },
    {
        titre: "LinkedIn",
        texte: "Mon Linkedin",
        img: "images/svgs/linkedin.svg",
        alt: "logo linkedin",
        trad: "linke-",
        link:"https://www.linkedin.com/in/matthias-hartmann-iziram/"
    },
    {
        titre: "Trello",
        texte: "Mon bureau Trello",
        img: "images/svgs/trello.svg",
        alt: "logo trello",
        trad: "trello-",
        link:"https://trello.com/espacedetravaildehartmannmatthias/"
    },
    {
        titre: "StackOverflow",
        texte: "Le meilleur site",
        img: "images/svgs/stackoverflow.svg",
        alt: "logo stackoverflow",
        trad: "stack-",
        link:"https://stackoverflow.com/"
    },
    {
        titre: "MDN Web Docs",
        texte: "La docu Du web",
        img: "images/svgs/mozilla.svg",
        alt: "logo mozilla",
        trad: "mdn-",
        link:"https://developer.mozilla.org"
    },
    {
        titre: "CSS Validator",
        texte: "Pour valider son CSS",
        img: "images/svgs/w3c.svg",
        alt: "logo w3",
        trad: "css-",
        link:"https://jigsaw.w3.org/css-validator"
    },
    {
        titre: "HTML Validator",
        texte: "Pour valider son HTML",
        img: "images/svgs/w3c.svg",
        alt: "logo w3",
        trad: "html-",
        link:"https://validator.w3.org/"
    },
    {
        titre: "Code My UI",
        texte: "Idées de web design",
        img: "images/svgs/codemyui.svg",
        alt: "logo codemyui",
        trad: "cmui-",
        link:"https://codemyui.com"
    },
    {
        titre: "Twitter",
        texte: "Mon twitter",
        img: "images/svgs/twitter.svg",
        alt: "logo twitter",
        trad: "twit-",
        link:"https://twitter.com/iziram_"
    },
    {
        titre: "Youtube",
        texte: "Ma chaine youtube",
        img: "images/svgs/youtube.svg",
        alt: "logo youtube",
        trad: "yt-",
        link:"https://www.youtube.com/channel/UCyCn19a5xr8SDdX-qPur1GQ"
    },
    {
        titre: "Twitch",
        texte: "Mon Twitch",
        img: "images/svgs/twitch.svg",
        alt: "logo twitch",
        trad: "tw-",
        link:"https://www.twitch.tv/iziram"
    },
    {
        titre: "Discord",
        texte: "Mon discord",
        img: "images/svgs/discord.svg",
        alt: "logo discord",
        trad: "disc-",
        link:"https://discord.com/users/277501626871447552"
    }
]
/**
 * Cette fonction permet de créer un élément DOM représentant un lien utile à partir de son Object
 * et de directement l'ajouter dans la section "links" de la page liensutiles.html
 * @param {Object} infos Un objet représentant un lien
 */
function createCard(infos){
    //On crée un élément div nomé col 
    const col = document.createElement("div")
        //On lui donne les classes bootstrap pour le Style 
        col.className="col-12 col-sm-6 col-md-4 col-lg-3 flex-centering"
        //On crée un élément figure
        const figure = document.createElement("figure")
            //On lui donne les classes pointer et pcard
            figure.className="pointer pcard"
            //On crée un élément img
            const img = document.createElement("img")
                //On lui donne la classe pcard-img
                img.className="pcard-img"
                //On lui donne comme source la source dans infos.img
                img.src = infos.img
                //Et comme alt infos.alt
                img.alt = infos.alt
            //On crée un élément h2 qui sert de titre à la carte
            const title = document.createElement("h2")
                //On lui donne la classe pcard-title
                title.className = "pcard-title"
                //Et on change le texte de l'élément par le texte dans infos.titre
                title.innerText = infos.titre
                title.setAttribute('trad',infos.trad+"title")
            //On crée un dernier élement : p 
            const text = document.createElement("p")
                //De la même façon que le titre on lui donne la classe "pcard-text" et on change son texte en fonction de infos.texte
                text.className = "pcard-text"
                text.innerText = infos.texte
                text.setAttribute('trad',infos.trad+"text")

            //On finit par ajouter tous les nouveaux éléments (img, title, text) dans l'élément figure en tant qu'enfants
            figure.appendChild(img)
            figure.appendChild(title)
            figure.appendChild(text)
            //On crée un event listener de click pour l'élément figure
            figure.addEventListener('click', ()=>{
                //lorsque l'élément sera cliquer cela ouvrira un nouveau onglet menant vers le lien donné dans infos.link
                window.open(infos.link, '_blank').focus();
            })
        //On ajoute l'élément figure dans l'élément col
        col.appendChild(figure)
    //On récuppère le section links qui contiendra toutes les cartes de liens
    const links = document.getElementById("links")
        //On ajoute l'élément col à la fin de la liste d'enfant de l'élément links
        links.appendChild(col)
}

//On execute la fonction createCard pour chaque objet de la liste d'objets de liens (liens)
liens.forEach((obj)=>{
    createCard(obj)
})