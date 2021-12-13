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

footer()