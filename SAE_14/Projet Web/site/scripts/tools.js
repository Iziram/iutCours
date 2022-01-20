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


class Traductor{
    constructor(traductionObject){
        this.version = 'fr';
        this.trad = traductionObject;
    }

    traduct(key){
        this.trad[this.version][key]
    }

    changeLanguage(lang){
        this.version = lang
    }
}