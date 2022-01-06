function accordeon(id, titre, contenu){
    acc = document.createElement("div")
        acc.classList.add("accordion","px-4","py-4")
        acc.id = "acc"+id
        item = document.createElement('div')
            item.classList.add("accordion-item")
            h2 = document.createElement("h2")
                h2.classList.add("accordion-header")
                h2.id = "head"+id
                button = HTMLParser(`
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="`+"#coll"+id+`" aria-expanded="true" aria-controls="`+"coll"+id+`" style=""> 
                    `+titre+`
                </button>
                `)
                h2.appendChild(button)
            item.appendChild(h2)

            collapse = HTMLParser(`
            <div id="`+"coll"+id+`" class="accordion-collapse collapse" aria-labelledby="`+"head"+id+`" data-bs-parent="#`+"acc"+id+`" style=""></div>
            `)
                accBody = document.createElement("div")
                    accBody.classList.add("accordion-body")
                    if (typeof(contenu) === "string"){
                        accBody.innerHTML = contenu
                    }else{
                        accBody.appendChild(contenu)
                    }
                collapse.appendChild(accBody)
            item.appendChild(collapse)
        acc.appendChild(item)
    
    return acc
}


function multiAccordeons(objets){

    y = -1
    x = -1

    row = []


    objets.forEach(element => {

        x = (x+1) % 2
        
        if (x == 0){
            y++;
            row.push([])
        }

        o = {
            id : x + y * 2,
            titre : element.titre,
            contenu : element.contenu
        }

        row[y].push(o)

    });
    return row
}


function placeOnDocument(objets){
    row = multiAccordeons(objets)

    body = document.getElementById("body")

        row.forEach((col)=>{
            section = document.createElement('div')
                section.classList.add("row")

                col.forEach((o)=>{
                    column = document.createElement('div')
                    column.classList.add("col-6")
                    column.appendChild(accordeon(o.id, o.titre, o.contenu))
                    section.appendChild(column)
                })
            body.appendChild(section)
        })

}


infos = [
    {
        titre: "Informations",
        contenu: `<section class="row">
        <div class="col-6">
            <p><i class="bi bi-calendar px-2"></i>`+age()+`</p>
            <hr>
            <p><i class="bi bi-flag px-2"></i>Français</p>
            <hr>
            <p><span class="material-icons-outlined px-2">directions_car_filled</span>Vehicule personnel</p>
            <hr>
            <p><span class="material-icons-outlined">
            badge
            </span>Permis B</p>
            
        </div>

        <div class="col-6">
            <p><i class="bi bi-envelope px-2"></i><a href="mailto: hartmann.matthias@iziram.fr">hartmann.matthias@iziram.fr</a></p>
            <hr>
            <p><span class="material-icons-outlined px-2">location_on</span>Kerbrézant, 22300 Ploubezre</p>
            <hr>
            <p><span class="material-icons-outlined px-2">link</span><a href="iziram.fr" target="_blank">iziram.fr</a></p>
            <hr>
        </div>
    </section>`
    },
    {
        titre: "Langue(s)",
        contenu: "test"
    },
    {
        titre: "Diplômes et Formations",
        contenu: "test"
    },
    {
        titre: "Expériences Diverses",
        contenu: "test"
    },
    {
        titre: "Compétences",
        contenu: "test"
    },
    {
        titre: "Centre d'intérets",
        contenu: "test"
    },
]

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

function formations(){

}

placeOnDocument(infos)
