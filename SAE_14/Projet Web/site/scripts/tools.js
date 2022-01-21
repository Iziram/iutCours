/**
 * Cette fonction convertie une chaine de caractère (représentant des éléments html) en élément DOM utilisable par JavaScript
 * @param {String} html la chaine de caractère représentant les élémments html
 * @param {String} mode = "text/html" Le mode par défaut est en text/html mais il existe aussi d'autres modes comme le text/XML qui peut être utilisé
 * @returns un élément DOM 
 */
function HTMLParser(html, mode = "text/html"){
    if(mode === "text/html"){
        /** le mode text/html nous renverras un document entier (balise html + balise body + balise éléments)
        * On doit donc ruser un peu pour récuppérer l'élément que l'on souhaite :
        * On prend le premier enfant du document : ( document -> <html/> )
        * Puis le dernier enfant de l'html : ( <html/> -> <body/> )
        * Et enfin le premier enfant du body : ( <body/> -> <element/> )
        */
        return new DOMParser().parseFromString(html, mode).firstChild.lastChild.firstChild
    }else{
        //Dans les autres cas le premier enfant sera directement l'élément
        return new DOMParser().parseFromString(html, mode).firstChild
    }
}
/**
 * 
 */
class Traductor {
    constructor() {
        this.version = 'fr';
        this.constentTrad = {
            "fr":{
                //Navbar
                "nav-index":"CV Numérique",
                    "nav-i-title": "Titre",
                    "nav-i-infos":"Qui suis-je ?",
                    "nav-i-compt":"Mes Compétences",
                    "nav-i-forma":"Mes diplômes et mes formations",
                    "nav-i-exp":"Mes Expériences",
                    "nav-i-inter":"Mes centres d'intérêts",
                "nav-compt":"Mes Compétences",
                "nav-inter":"Mes Intérêts",
                "nav-links":"Les Liens Utiles",
                "nav-prof":"Mon Projet Professionnel",
                "nav-button": "Traduire en Anglais"
            },
            "en":{
                //Navbar
                "nav-index":"Digital Resume",
                    "nav-i-title": "Title",
                    "nav-i-infos":"Who am I?",
                    "nav-i-compt":"My Skills",
                    "nav-i-forma":"My diplomas",
                    "nav-i-exp":"My Experiences",
                    "nav-i-inter":"My interests",
                "nav-compt":"My Skills",
                "nav-inter":"My interests",
                "nav-links":"Useful links",
                "nav-prof":"My Career Plan",
                "nav-button": "Translate to French"
            }
        }
    }

    changeLanguage() {
        if(this.version === "fr"){
            this.version = 'en'
        }else{
            this.version = 'fr'
        }
        this.translate();
    }

    updateTrad(tradObject){
        this.trad =tradObject
    }

    translate() {
        const toTranslate = document.body.getElementsByTagName("*");
        for (let i = 0; i < toTranslate.length; i++) {
            const tr = toTranslate[i];
            if (tr.hasAttribute('data-trad')) {
                const key = tr.getAttribute('data-trad')
                if (this.constentTrad[this.version] && this.constentTrad[this.version][key]) {
                    tr.innerHTML = this.constentTrad[this.version][key]
                }else if (this.trad && this.trad[this.version] && this.trad[this.version][key]) {
                    tr.innerHTML = this.trad[this.version][key]
                }
            }
        }
    }
}


const traductor = new Traductor()