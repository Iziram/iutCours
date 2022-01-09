function age(){
    var dob = new Date("01/20/2003"); // ma date de naissance mm/jj/yyyy
    var month_diff = Date.now() - dob.getTime(); // On fait la différence entre maintenant et le jour de naissance
    
    var age_dt = new Date(month_diff);  // On en créer une nouvelle date
    
    //extract year from date    
    var year = age_dt.getUTCFullYear(); // et récuppère l'année
    
    //now calculate the age of the user
    var age_i = Math.abs(year - 1970); // on fait l'année - 1970 pour avoir l'age

    return age_i
}


pointers  = document.getElementsByClassName("responsive py-2 px-1 pointer")






function assignCanva(){
    const icons = [
        {
            title: "HTML 5 / CSS",
            informations: "J'ai commencé l'HTML en 2020, pendant le confinement. Bien que cela ne soit pas mon langage favori, je me débrouille assez pour pouvoir mettre en place des sites web comme celui-ci "
        },
        {
            title: "JavaScript",
            informations: "Tout comme l'HTML, je programme en JavaScript depuis le confinement de 2020. J'apprécie bien ce langage même s'il reste incohérent sur certains points. J'utilise principalement le javascript pour faciliter la création de pages web."
        },
        {
            title: "Typescript",
            informations: "Le TypeScript est un langage dérivé du Javascript. En temps normal le javascript n'est pas un langage dit \"Typé\", mais grace à TypeScript c'est le cas. J'utilise principalement ce langage dans la création d'extensions VSCode."
        },
        {
            title: "Java",
            informations: "Java est le langage que je préfère de loin, la programmation orientée objet est un de mes paradigmes de programmations préféré. J'ai commencé ce langage en Avril 2020 et depuis je programme avec régulièrement."
        },
        {
            title: "PHP",
            informations: "J'ai du apprendre à programmer en PHP lorsque j'ai voulu produire un site web intéractif pour mon club d'escrime. Ce n'est pas un langage que j'aime particulièrement mais il reste néanmoins utile pour la programmation Back-End Web."
        },
        {
            title: "Python",
            informations: "Python est le langage qui m'a été enseigné en cours de programmations durant mon lycée et mon BUT, Il est facile à comprendre et puissant si on s'y connait bien." 
        },
        {
            title: "Github",
            informations: `<p>GitHub est pour moi un outil Indispensable, L'ensemble de mes projets s'y trouvent. Cet outil me permet gérer plusieurs versions d'un même projet et d'accéder aux fichiers depuis n'import quelle machine. De plus la fonction historique permet en cas de problème de revenir à une version plus anciène qui n'avait pas le problème.</p>
            <p>GitHub est une plateforme open source de gestion de versions et de collaboration destinée aux développeurs de logiciels. Livrée en tant que logiciel à la demande (SaaS, Software as a Service), la solution GitHub a été lancée en 2008. Elle repose sur Git, un système de gestion de code open source créé par Linus Torvalds dans le but d'accélérer le développement logiciel.</p>
            `
        },
        {
            title: "Trello",
            informations: `<p>J'utilise Trello dans la plupart de mes projets afin d'organiser mes taches. Il me permet de savoir en temps réel où en est mon projet et de pouvoir respecter mes DeadLines.</p>
            <p>Trello est un outil de gestion de projet en ligne, lancé en septembre 2011 et inspiré par la méthode <a href='https://fr.wikipedia.org/wiki/Kanban_(d%C3%A9veloppement)' target='_blank'>Kanban de Toyota</a>. Il repose sur une organisation des projets en planches listant des cartes, chacune représentant des tâches. Les cartes sont assignables à des utilisateurs et sont mobiles d'une planche à l'autre, traduisant leur avancement.
            La version de base est gratuite, tandis qu'une formule payante permet d'obtenir des services supplémentaires. Le service est disponible en plusieurs langues (23 en juin 2016). </p>
            `
        },
        {
            title: "LinkedIn",
            informations: `
            <p>Je possède un compte LinkedIn qui me permet d'entretenir un réseau professionnel.</p>
            <p>LinkedIn est un service en ligne qui permet de construire et d’agréger son réseau professionnel. Il se définit comme un réseau de connaissances qui facilite le dialogue entre professionnels. Pour ses membres, c'est aussi un outil de gestion de réputation en ligne et de personal branding.</p>
            `
        },
        {
            title: "Linux",
            informations: "Dans le cadre de ma formation BUT Réseaux et Télécommunications, J'ai appris à administrer un système Linux."
        },
        {
            title: "Windows",
            informations: "Dans le cadre de ma formation BUT Réseaux et Télécommunications, J'ai appris à administrer un système Windows."
        },
        {
            title: "Routeurs",
            informations: "Dans le cadre de ma formation BUT Réseaux et Télécommunications, j'ai appris à mettre en place et configurer un Routeur (Cisco). Cette compétence m'est très utile lors de la mise en place de réseaux. Et elle sera approfondie au fil des années sur le terrain."
        },
        {
            title: "Switchs",
            informations: "Dans le cadre de ma formation BUT Réseaux et Télécommunications, j'ai appris à mettre en place et configurer un switch (Aruba ou Cisco). Cette compétence m'est très utile lors de la mise en place de réseaux."
        }
    ]
    for(var i = 0; i< pointers.length; i++){
        const icon = pointers[i]
        const obj = icons[i]
        console.log(obj)
        icon.addEventListener("click", ()=>{
            var myOffcanvas = document.getElementById('myCanvas')
            const label = document.getElementById("offcanvasRightLabel")
                label.innerText = obj.title
            const body = document.getElementById("canvasBody")
                body.innerHTML = obj.informations
            
            var bsOffcanvas = new bootstrap.Offcanvas(myOffcanvas)
            bsOffcanvas.show()
        })
    }
}

assignCanva()

function nextScroll(event){
    anchors = [
        "title",
        "informations",
        "competences",
        "formations",
        "experiences",
        "interets"
    ]

    anchorsId = anchors.indexOf(document.location.href.split("#")[1])
    if (event.deltaY > 0 ){
        anchorsId++
    }else{
        anchorsId--
    }
    if (anchorsId >= anchors.length){
        anchorsId = 0;
    }else if (anchorsId < 0){
        anchorsId = anchors.length - 1
    }

    document.location.href = "#"+anchors[anchorsId]
    return false;
}

window.addEventListener('wheel', nextScroll);