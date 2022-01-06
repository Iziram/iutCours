function HTMLParser(html, mode = "text/html"){
    element = undefined
    if(mode === "text/html"){
        return new DOMParser().parseFromString(html, mode).firstChild.lastChild.firstChild
    }else{
        return new DOMParser().parseFromString(html, mode).firstChild
    }
}